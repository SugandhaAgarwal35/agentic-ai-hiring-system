"""Researcher agent — fans the same prompt through 3 LLM providers.

Each provider call goes through the self-healing retry loop:
    generate -> Pydantic gate -> retry (<= 3 attempts).

Returns a dict keyed by provider. Each value is a validated `CompanyCore`.
"""

from __future__ import annotations

import sys
from pathlib import Path

from langchain_core.messages import HumanMessage

# Step folders sit next to the shared _common.py one level up.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from _common import build_llm, load_prompt, run_with_retry  # noqa: E402

from schemas import CompanyCore


PROVIDERS = ("groq", "google", "cerebras")

_PROMPT_FILE = "Researcher Prompt.md"


def _strip_fences(text: str) -> str:
    """Remove ```json ... ``` fences if the model ignored our instruction."""
    text = text.strip()
    if text.startswith("```"):
        first_newline = text.find("\n")
        if first_newline != -1:
            text = text[first_newline + 1 :]
        if text.endswith("```"):
            text = text[:-3]
    return text.strip()


def _run_one(provider: str, company: str) -> CompanyCore:
    prompt = load_prompt(_PROMPT_FILE).replace("{{COMPANY_NAME}}", company)

    def gen(feedback: str | None) -> CompanyCore:
        user_prompt = prompt
        if feedback:
            user_prompt += (
                "\n\n# PREVIOUS ATTEMPT FAILED\n"
                f"Fix this error on the next attempt: {feedback}\n"
            )
        llm = build_llm(provider)
        response = llm.invoke([HumanMessage(content=user_prompt)])
        raw = _strip_fences(str(response.content))
        return CompanyCore.model_validate_json(raw)

    return run_with_retry(gen, max_attempts=3)


def run(company: str) -> dict[str, CompanyCore]:
    """Run the researcher across all 3 providers. Returns provider → model."""
    out: dict[str, CompanyCore] = {}
    for provider in PROVIDERS:
        out[provider] = _run_one(provider, company)
    return out
