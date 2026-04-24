"""Cleaning agent — LLM re-write of a broken payload, guided by validator errors."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Literal

from langchain_core.messages import HumanMessage

_M1 = Path(__file__).resolve().parent.parent.parent / "Milestone 1 - Researcher to Hiring"
sys.path.insert(0, str(_M1))
from _common import build_llm, run_with_retry  # noqa: E402


PayloadKind = Literal["company", "skills", "hiring"]


_CLEAN_PROMPT = """You are a Data Cleaning agent. You are given a JSON payload
that FAILED validation, plus the list of errors.

Your job: return a corrected JSON payload that fixes ONLY the failing fields.
Keep every other field exactly as-is. Do NOT invent new keys. Do NOT change
keys that were not flagged as errors.

Return ONLY the corrected JSON object. No commentary, no markdown fences.

# PAYLOAD KIND
{kind}

# VALIDATION ERRORS
{errors}

# ORIGINAL PAYLOAD
{payload}
"""


def _strip_fences(text: str) -> str:
    text = text.strip()
    if text.startswith("```"):
        first_newline = text.find("\n")
        if first_newline != -1:
            text = text[first_newline + 1 :]
        if text.endswith("```"):
            text = text[:-3]
    return text.strip()


def clean(
    kind: PayloadKind,
    payload: dict[str, Any],
    errors: list[str],
    *,
    provider: str = "groq",
) -> dict[str, Any]:
    """Ask the LLM to rewrite only the broken fields."""

    prompt = _CLEAN_PROMPT.format(
        kind=kind,
        errors="\n".join(f"- {e}" for e in errors) or "(none)",
        payload=json.dumps(payload, indent=2, ensure_ascii=False),
    )

    def gen(feedback: str | None) -> dict[str, Any]:
        user_prompt = prompt
        if feedback:
            user_prompt += f"\n\n# RETRY FEEDBACK\n{feedback}\n"
        llm = build_llm(provider)
        response = llm.invoke([HumanMessage(content=user_prompt)])
        raw = _strip_fences(str(response.content))
        return json.loads(raw)

    return run_with_retry(gen, max_attempts=3)
