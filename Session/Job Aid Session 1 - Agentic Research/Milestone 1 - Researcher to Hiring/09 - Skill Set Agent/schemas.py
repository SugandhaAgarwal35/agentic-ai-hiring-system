"""Pydantic schema for the Skill Set agent.

12 fixed skill areas, levels 1–10 (Bloom's depth mapped to a code).
"""

from typing import Literal

from pydantic import BaseModel, Field


SkillArea = Literal[
    "coding",
    "data_structures_and_algorithms",
    "object_oriented_programming_and_design",
    "aptitude_and_problem_solving",
    "communication_skills",
    "ai_native_engineering",
    "devops_and_cloud",
    "sql_and_design",
    "software_engineering",
    "system_design_and_architecture",
    "computer_networking",
    "operating_system",
]

ProficiencyCode = Literal["CU", "AP", "AS", "EV", "CR"]


class SkillSetEntry(BaseModel):
    skill_area: SkillArea
    level: int = Field(..., ge=1, le=10, description="Bloom's scope (1-10).")
    proficiency_code: ProficiencyCode = Field(..., description="Bloom's depth code.")
    rationale: str = Field(..., min_length=5, description="Why this pairing.")


class SkillSetsResponse(BaseModel):
    company_name: str = Field(..., min_length=1)
    skill_sets: list[SkillSetEntry] = Field(..., min_length=12, max_length=12)
