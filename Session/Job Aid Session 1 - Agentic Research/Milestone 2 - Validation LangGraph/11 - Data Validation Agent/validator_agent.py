"""Validation agent — pure-Python gate over the 3 Milestone 1 payload types.

Returns (is_valid, errors). `errors` is a list of human-readable strings that
get fed back into the Cleaning agent's prompt.
"""

from __future__ import annotations

import datetime as dt
import sys
from pathlib import Path
from typing import Any, Literal

from pydantic import ValidationError

_M1 = Path(__file__).resolve().parent.parent.parent / "Milestone 1 - Researcher to Hiring"
sys.path.insert(0, str(_M1))
sys.path.insert(0, str(_M1 / "07 - Researcher Agent"))
sys.path.insert(0, str(_M1 / "09 - Skill Set Agent"))
sys.path.insert(0, str(_M1 / "10 - Hiring Process Agent"))

# Separate imports so each schema loads from its own step folder.
# CompanyCore will be imported dynamically in validate_company_core()


PayloadKind = Literal["company", "skills", "hiring"]

_PLACEHOLDERS = ("tbd", "todo", "lorem", "placeholder", "not found", "n/a", "unknown")


def _contains_placeholder(value: str) -> bool:
    low = value.lower()
    return any(token in low for token in _PLACEHOLDERS)


def validate_company_core(payload: dict[str, Any]) -> tuple[bool, list[str]]:
    errors: list[str] = []

    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "company_schemas",
        _M1 / "07 - Researcher Agent" / "schemas.py",
    )
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    CompanyCore = module.CompanyCore

    try:
        model = CompanyCore.model_validate(payload)
    except ValidationError as exc:
        return False, [f"Pydantic: {err['loc']} -> {err['msg']}" for err in exc.errors()]

    current_year = dt.datetime.now().year
    try:
        year = int(model.incorporation_year)
        if not 1800 <= year <= current_year:
            errors.append(
                f"incorporation_year={year} outside 1800..{current_year}."
            )
    except ValueError:
        errors.append(f"incorporation_year={model.incorporation_year!r} is not a 4-digit integer.")

    for field in ("vision_statement", "mission_statement", "overview_text"):
        val = getattr(model, field)
        if _contains_placeholder(val):
            errors.append(f"{field} contains placeholder text: {val[:60]!r}")

    if ";" not in model.operating_countries and "," not in model.operating_countries:
        if len(model.operating_countries.split()) < 1:
            errors.append("operating_countries looks empty.")

    return (not errors), errors


def validate_skill_sets(payload: dict[str, Any]) -> tuple[bool, list[str]]:
    errors: list[str] = []

    # Lazy import so this step works even if only 'company' is being validated.
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "skill_set_schemas",
        _M1 / "09 - Skill Set Agent" / "schemas.py",
    )
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    SkillSetsResponse = module.SkillSetsResponse

    try:
        model = SkillSetsResponse.model_validate(payload)
    except ValidationError as exc:
        return False, [f"Pydantic: {err['loc']} -> {err['msg']}" for err in exc.errors()]

    seen_areas = [row.skill_area for row in model.skill_sets]
    if len(set(seen_areas)) != 12:
        errors.append(f"Expected 12 unique skill_area values, got {len(set(seen_areas))}.")

    if len({row.level for row in model.skill_sets}) == 1:
        errors.append("All 12 skill_area rows share the same level — likely a hallucination.")

    return (not errors), errors


def validate_hiring_process(payload: dict[str, Any]) -> tuple[bool, list[str]]:
    errors: list[str] = []

    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "hiring_schemas",
        _M1 / "10 - Hiring Process Agent" / "schemas.py",
    )
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    HiringResponse = module.HiringResponse

    try:
        model = HiringResponse.model_validate(payload)
    except ValidationError as exc:
        return False, [f"Pydantic: {err['loc']} -> {err['msg']}" for err in exc.errors()]

    for role in model.job_role_details:
        numbers = [r.round_number for r in role.hiring_rounds]
        if numbers != sorted(numbers):
            errors.append(f"Role '{role.role_title}': hiring_rounds not in chronological order.")
        if role.opportunity_type == "Employment" and role.compensation != "CTC":
            errors.append(f"Role '{role.role_title}': Employment must use CTC, got {role.compensation}.")
        if role.opportunity_type == "Internship" and role.compensation != "Stipend":
            errors.append(f"Role '{role.role_title}': Internship must use Stipend.")

    return (not errors), errors


def validate(kind: PayloadKind, payload: dict[str, Any]) -> tuple[bool, list[str]]:
    if kind == "company":
        return validate_company_core(payload)
    if kind == "skills":
        return validate_skill_sets(payload)
    if kind == "hiring":
        return validate_hiring_process(payload)
    raise ValueError(f"Unknown payload kind: {kind!r}")
