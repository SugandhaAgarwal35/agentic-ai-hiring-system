"""Consolidator agent — reconciles 3 researcher JSONs into 1 Golden Record.

Uses a 4th provider (OpenRouter) to cherry-pick the best value per field.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from langchain_core.messages import HumanMessage

_MILESTONE = Path(__file__).resolve().parent.parent
_RESEARCHER = _MILESTONE / "07 - Researcher Agent"
sys.path.insert(0, str(_MILESTONE))
sys.path.insert(0, str(_RESEARCHER))

from _common import build_llm, load_prompt, run_with_retry  # noqa: E402

from schemas import CompanyCore  # noqa: E402 — loaded from 07/schemas.py


CONSOLIDATOR_PROVIDER = "openrouter"
_PROMPT_FILE = "Consolidator Prompt.md"


def _strip_fences(text: str) -> str:
    text = text.strip()
    if text.startswith("```"):
        first_newline = text.find("\n")
        if first_newline != -1:
            text = text[first_newline + 1 :]
        if text.endswith("```"):
            text = text[:-3]
    return text.strip()


def run(
    company: str,
    candidates_by_provider: dict[str, CompanyCore],
) -> CompanyCore:
    """Run the consolidator and return a single validated CompanyCore."""

    if len(candidates_by_provider) < 2:
        raise ValueError(
            "Consolidator needs >= 2 researcher candidates; "
            f"got {len(candidates_by_provider)}."
        )

    ordered = list(candidates_by_provider.items())
    while len(ordered) < 3:
        # Pad with a copy of the first so the prompt's A/B/C slots always fill.
        ordered.append(ordered[0])

    (_, cand_a), (_, cand_b), (_, cand_c) = ordered[:3]

    template = load_prompt(_PROMPT_FILE)
    prompt = (
        template
        .replace("{{COMPANY_NAME}}", company)
        .replace("{{CANDIDATE_A_JSON}}", json.dumps(cand_a.model_dump(), indent=2))
        .replace("{{CANDIDATE_B_JSON}}", json.dumps(cand_b.model_dump(), indent=2))
        .replace("{{CANDIDATE_C_JSON}}", json.dumps(cand_c.model_dump(), indent=2))
    )

    def gen(feedback: str | None) -> CompanyCore:
        user_prompt = prompt
        if feedback:
            user_prompt += (
                "\n\n# PREVIOUS ATTEMPT FAILED\n"
                f"Fix this error on the next attempt: {feedback}\n"
            )
        llm = build_llm(CONSOLIDATOR_PROVIDER)
        response = llm.invoke([HumanMessage(content=user_prompt)])
        raw = _strip_fences(str(response.content))
        return CompanyCore.model_validate_json(raw)

    return run_with_retry(gen, max_attempts=3)
