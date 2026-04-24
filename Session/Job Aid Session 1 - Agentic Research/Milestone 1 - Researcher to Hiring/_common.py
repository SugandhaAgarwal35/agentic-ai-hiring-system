"""Shared helpers for every Milestone 1 agent.

- `build_llm(provider)` — returns a LangChain chat model for one of the 4 providers.
- `load_prompt(filename)` — reads a prompt template from the repo-root `Prompts/` folder.
- `run_with_retry(gen, max_attempts)` — bounded self-healing loop.
- `AgentRetryExhausted` — raised when all attempts fail.

The same `_common.py` ships with every step folder so each step is runnable on its own.
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any, Callable

from dotenv import load_dotenv


class AgentRetryExhausted(RuntimeError):
    """Raised when the self-healing loop can't produce a valid payload."""


_THIS_DIR = Path(__file__).resolve().parent
_ENV_FILE = _THIS_DIR / "05 - Setup Accounts and Env" / ".env"
if _ENV_FILE.exists():
    load_dotenv(_ENV_FILE)
else:
    load_dotenv()

_PROMPTS_DIR = _THIS_DIR.parent.parent / "Prompts"


def load_prompt(filename: str) -> str:
    """Read a prompt template from the repo-root Prompts folder."""
    path = _PROMPTS_DIR / filename
    return path.read_text(encoding="utf-8")


def build_llm(provider: str, *, temperature: float = 0.2):
    """Return a LangChain chat model for the named provider.

    Supported: "groq", "google", "cerebras", "openrouter".
    Each provider reads its own API key + model from environment variables.
    """

    provider = provider.lower().strip()

    if provider == "groq":
        from langchain_groq import ChatGroq

        return ChatGroq(
            model=os.environ.get("GROQ_MODEL", "llama-3.3-70b-versatile"),
            api_key=os.environ["GROQ_API_KEY"],
            temperature=temperature,
        )

    if provider == "google":
        from langchain_google_genai import ChatGoogleGenerativeAI

        return ChatGoogleGenerativeAI(
            model=os.environ.get("GOOGLE_MODEL", "gemini-2.5-flash-lite"),
            google_api_key=os.environ["GOOGLE_API_KEY"],
            temperature=temperature,
        )

    if provider == "cerebras":
        from langchain_cerebras import ChatCerebras

        return ChatCerebras(
            model=os.environ.get("CEREBRAS_MODEL", "llama3.1-8b"),
            api_key=os.environ["CEREBRAS_API_KEY"],
            temperature=temperature,
        )

    if provider == "openrouter":
        from langchain_openai import ChatOpenAI

        return ChatOpenAI(
            model=os.environ.get(
                "OPENROUTER_MODEL",
                "meta-llama/llama-3.2-3b-instruct",
            ),
            api_key=os.environ["OPENROUTER_API_KEY"],
            base_url="https://openrouter.ai/api/v1",
            temperature=temperature,
        )

    raise ValueError(
        f"Unknown provider '{provider}'. "
        "Expected one of: groq, google, cerebras, openrouter."
    )


def run_with_retry(
    gen: Callable[[str | None], Any],
    max_attempts: int = 3,
) -> Any:
    """Bounded retry loop.

    `gen(feedback)` is called with the previous error message (or None on the
    first attempt). Returns the first successful payload. Raises
    `AgentRetryExhausted` if every attempt fails.
    """

    last_error: str | None = None
    for attempt in range(1, max_attempts + 1):
        try:
            return gen(last_error)
        except Exception as exc:  # noqa: BLE001 — surface any failure as retry feedback
            last_error = f"{type(exc).__name__}: {exc}"
            if attempt == max_attempts:
                raise AgentRetryExhausted(
                    f"Agent failed after {max_attempts} attempts. "
                    f"Last error: {last_error}"
                ) from exc
    raise AgentRetryExhausted("unreachable")
