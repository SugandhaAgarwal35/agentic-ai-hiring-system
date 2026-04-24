"""Pydantic schema for the Hiring Process agent.

Mirrors the canonical `job_role_details_json` DB structure from Step 9 of the
Database Setup folder.
"""

from typing import Literal, Optional

from pydantic import BaseModel, Field


OpportunityType = Literal["Employment", "Internship"]

RoleCategory = Literal[
    "SDE", "Data_Analyst", "SRE", "DEVOPS",
    "Data_Scientist", "Frontend_Developer", "Others",
]

SkillSetCode = Literal[
    "COD", "DSA", "APTI", "COMM", "OOD",
    "AI", "SQL", "SYSD", "CLOUD", "SWE", "NETW", "OS",
]

RoundCategory = Literal[
    "Aptitude", "Coding Test", "Interview", "Hackathon", "Group Discussion",
]

EvaluationType = Literal["Technical", "Managerial", "HR"]

AssessmentMode = Literal["Online", "On Campus", "Office"]

Compensation = Literal["CTC", "Stipend"]


class RoundSkillSet(BaseModel):
    skill_set_code: SkillSetCode
    typical_questions: str = Field(..., min_length=5)


class HiringRound(BaseModel):
    round_number: int = Field(..., ge=1)
    round_name: Optional[str] = None
    round_category: RoundCategory
    evaluation_type: EvaluationType
    assessment_mode: AssessmentMode
    skill_sets: list[RoundSkillSet] = Field(..., min_length=3)


class JobRoleDetails(BaseModel):
    opportunity_type: OpportunityType
    role_title: str = Field(..., min_length=2)
    role_category: RoleCategory
    job_description: str = Field(..., min_length=20)
    compensation: Compensation
    ctc_or_stipend: float = Field(..., gt=0)
    bonus: Optional[str] = None
    benefits_summary: Optional[str] = None
    hiring_rounds: list[HiringRound] = Field(..., min_length=1)


class HiringResponse(BaseModel):
    company_name: str = Field(..., min_length=1)
    job_role_details: list[JobRoleDetails] = Field(..., min_length=1, max_length=3)
