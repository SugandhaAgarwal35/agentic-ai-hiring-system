"""Hiring Process agent — single Groq call, nested hiring JSON."""

from __future__ import annotations

import sys
from pathlib import Path

from langchain_core.messages import HumanMessage

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from _common import build_llm, load_prompt, run_with_retry  # noqa: E402

from schemas import HiringResponse


PROVIDER = "groq"
_PROMPT_FILE = "Hiring Process Prompt.md"


def _strip_fences(text: str) -> str:
    text = text.strip()
    if text.startswith("```"):
        first_newline = text.find("\n")
        if first_newline != -1:
            text = text[first_newline + 1 :]
        if text.endswith("```"):
            text = text[:-3]
    return text.strip()


def run(company: str) -> HiringResponse:
    prompt = load_prompt(_PROMPT_FILE).replace("{{COMPANY_NAME}}", company)

    def gen(feedback: str | None) -> HiringResponse:
        user_prompt = prompt
        if feedback:
            user_prompt += f"\n\n# PREVIOUS ATTEMPT FAILED\nFix: {feedback}\n"
        llm = build_llm(PROVIDER)
        response = llm.invoke([HumanMessage(content=user_prompt)])
        raw = _strip_fences(str(response.content))
        return HiringResponse.model_validate_json(raw)

    return run_with_retry(gen, max_attempts=3)
