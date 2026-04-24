"""LangGraph wiring for the end-to-end company-profile flow.

Nodes: researcher → consolidator → validator → (cleaner ↻ validator) → etl
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any, TypedDict

from langgraph.graph import END, StateGraph

_M1 = Path(__file__).resolve().parent.parent.parent / "Milestone 1 - Researcher to Hiring"
_M2 = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_M1))
sys.path.insert(0, str(_M1 / "07 - Researcher Agent"))
sys.path.insert(0, str(_M1 / "08 - Consolidator Agent"))
sys.path.insert(0, str(_M2 / "11 - Data Validation Agent"))
sys.path.insert(0, str(_M2 / "12 - Data Cleaning Agent"))
sys.path.insert(0, str(_M2 / "13 - ETL Agent"))

from researcher_agent import run as researcher_run  # noqa: E402
from consolidator_agent import run as consolidator_run  # noqa: E402
from validator_agent import validate  # noqa: E402
from cleaner_agent import clean  # noqa: E402
from etl_agent import stage  # noqa: E402


MAX_CLEAN_ATTEMPTS = 3


class FlowState(TypedDict, total=False):
    company: str
    candidates: dict[str, Any]
    golden: dict[str, Any]
    errors: list[str]
    clean_attempts: int
    staged_rows: list[dict[str, Any]]


def _researcher_node(state: FlowState) -> FlowState:
    company = state["company"]
    candidates = researcher_run(company)
    return {"candidates": candidates, "clean_attempts": 0}


def _consolidator_node(state: FlowState) -> FlowState:
    company = state["company"]
    model = consolidator_run(company, state["candidates"])
    return {"golden": model.model_dump()}


def _validator_node(state: FlowState) -> FlowState:
    ok, errors = validate("company", state["golden"])
    return {"errors": [] if ok else errors}


def _cleaner_node(state: FlowState) -> FlowState:
    cleaned = clean("company", state["golden"], state["errors"])
    return {
        "golden": cleaned,
        "clean_attempts": state.get("clean_attempts", 0) + 1,
    }


def _etl_node(state: FlowState) -> FlowState:
    rows = stage("company", state["golden"])
    return {"staged_rows": rows}


def _route_after_validate(state: FlowState) -> str:
    if not state.get("errors"):
        return "etl"
    if state.get("clean_attempts", 0) >= MAX_CLEAN_ATTEMPTS:
        raise RuntimeError(
            f"Validator still failing after {MAX_CLEAN_ATTEMPTS} cleanings: "
            f"{state['errors']}"
        )
    return "cleaner"


def build_graph():
    graph = StateGraph(FlowState)
    graph.add_node("researcher", _researcher_node)
    graph.add_node("consolidator", _consolidator_node)
    graph.add_node("validator", _validator_node)
    graph.add_node("cleaner", _cleaner_node)
    graph.add_node("etl", _etl_node)

    graph.set_entry_point("researcher")
    graph.add_edge("researcher", "consolidator")
    graph.add_edge("consolidator", "validator")
    graph.add_conditional_edges(
        "validator",
        _route_after_validate,
        {"cleaner": "cleaner", "etl": "etl"},
    )
    graph.add_edge("cleaner", "validator")
    graph.add_edge("etl", END)

    return graph.compile()


# ---------------------------------------------------------------------------
# Extension: the same pattern works for skill_sets and hiring_process.
# Uncomment and swap the researcher/consolidator nodes for each kind.
# ---------------------------------------------------------------------------
# def build_skill_set_graph(): ...
# def build_hiring_process_graph(): ...
