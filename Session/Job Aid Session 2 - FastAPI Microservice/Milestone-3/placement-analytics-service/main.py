from typing import Any, Dict, List, Optional
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlmodel import Session, select
from sqlalchemy import bindparam, text

from database import engine
from models import CompanyJson, Company, InnovxJson, JobRoleDetailsJson

app = FastAPI(
    title="SRM Placement API",
    description="FastAPI backend for company short/full JSON data from the company_json table.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)


class SkillRoadmapLevel(BaseModel):
    level: int
    name: str
    desc: str


class SkillIntelligenceItem(BaseModel):
    name: str
    bloom: str
    bloomLabel: str
    score: int
    criticality: str
    description: str
    targetLevel: int
    levels: List[SkillRoadmapLevel]


class CompanyShortJsonResponse(BaseModel):
    company_id: int
    short_json: Dict[str, Any] = {}


class CompanyFullJsonResponse(BaseModel):
    company_id: int
    full_json: Dict[str, Any] = {}


PROFICIENCY_TO_BLOOM = {
    1: ("CU", "Conceptual Understanding"),
    2: ("CU", "Conceptual Understanding"),
    3: ("AP", "Application"),
    4: ("AP", "Application"),
    5: ("AS", "Analysis & Synthesis"),
    6: ("AS", "Analysis & Synthesis"),
    7: ("EV", "Evaluate"),
    8: ("EV", "Evaluate"),
    9: ("CR", "Creation"),
    10: ("CR", "Creation"),
}


def score_to_criticality(score: int) -> str:
    if score >= 7:
        return "Critical"
    if score >= 5:
        return "Important"
    return "Baseline"


@app.on_event("startup")
def on_startup():
    from sqlmodel import SQLModel

    SQLModel.metadata.create_all(engine)


@app.get("/health", tags=["Health"])
def health_check() -> dict:
    return {"status": "ok"}


@app.get("/api/v1/skill-intelligence/{company_id}", response_model=List[SkillIntelligenceItem], tags=["Skill Intelligence"])
def get_skill_intelligence(company_id: int) -> List[SkillIntelligenceItem]:
    skill_levels_query = text(
        """
        SELECT
            csl.skill_set_id,
            csl.required_level,
            csl.required_proficiency_level_id,
            ssm.skill_set_name,
            ssm.skill_set_description
        FROM company_skill_levels AS csl
        LEFT JOIN skill_set_master AS ssm
            ON ssm.skill_set_id = csl.skill_set_id
        WHERE csl.company_id = :company_id
        ORDER BY csl.required_level DESC, csl.skill_set_id ASC
        """
    )

    topics_query = (
        text(
            """
            SELECT skill_set_id, level_number, topics
            FROM skill_set_topics
            WHERE skill_set_id IN :skill_set_ids
            ORDER BY skill_set_id ASC, level_number ASC
            """
        ).bindparams(bindparam("skill_set_ids", expanding=True))
    )

    with Session(engine) as session:
        skill_rows = session.execute(skill_levels_query, {"company_id": company_id}).mappings().all()

        if not skill_rows:
            raise HTTPException(status_code=404, detail=f"Skill intelligence not found for company_id={company_id}")

        skill_set_ids = [int(row["skill_set_id"]) for row in skill_rows if row["skill_set_id"] is not None]
        topic_rows = (
            session.execute(topics_query, {"skill_set_ids": skill_set_ids}).mappings().all()
            if skill_set_ids
            else []
        )

    topics_by_skill: dict[int, dict[int, str]] = {}
    for row in topic_rows:
        skill_set_id = int(row["skill_set_id"])
        level_number = int(row["level_number"])
        topics_by_skill.setdefault(skill_set_id, {})[level_number] = row["topics"] or ""

    response: List[SkillIntelligenceItem] = []
    for row in skill_rows:
        required_level = int(row["required_level"] or 0)
        proficiency_id = int(row["required_proficiency_level_id"] or 0)
        bloom, bloom_label = PROFICIENCY_TO_BLOOM.get(proficiency_id, ("AP", "Application"))
        skill_set_id = int(row["skill_set_id"])
        skill_topics = topics_by_skill.get(skill_set_id, {})

        levels = []
        for level in range(1, 11):
            topic = (skill_topics.get(level) or "").strip()
            levels.append(
                SkillRoadmapLevel(
                    level=level,
                    name=topic or ("Beyond scope" if level > required_level else f"Level {level}"),
                    desc="Beyond current requirements" if level > required_level else topic,
                )
            )

        response.append(
            SkillIntelligenceItem(
                name=(row["skill_set_name"] or f"Skill {skill_set_id}").strip(),
                bloom=bloom,
                bloomLabel=bloom_label,
                score=required_level,
                criticality=score_to_criticality(required_level),
                description=(row["skill_set_description"] or "").strip(),
                targetLevel=required_level,
                levels=levels,
            )
        )

    return response


@app.get("/api/v1/companies", response_model=List[CompanyShortJsonResponse], tags=["Companies"])
def list_companies() -> List[CompanyShortJsonResponse]:
    with Session(engine) as session:
        rows = session.exec(
            select(CompanyJson.company_id, CompanyJson.short_json).where(CompanyJson.company_id.is_not(None))
        ).all()
        return [
            CompanyShortJsonResponse(
                company_id=int(company_id),
                short_json=(short_json or {}),
            )
            for company_id, short_json in rows
        ]


@app.get("/api/v1/companies/{company_id}", response_model=CompanyShortJsonResponse, tags=["Companies"])
def get_company(company_id: int) -> CompanyShortJsonResponse:
    with Session(engine) as session:
        row = session.exec(
            select(CompanyJson.company_id, CompanyJson.short_json).where(CompanyJson.company_id == company_id)
        ).first()
        if not row:
            raise HTTPException(status_code=404, detail="Company not found")
        resolved_company_id, short_json = row
        return CompanyShortJsonResponse(
            company_id=int(resolved_company_id),
            short_json=(short_json or {}),
        )


@app.get("/api/v1/companies/{company_id}/full-json", response_model=CompanyFullJsonResponse, tags=["Companies"])
def get_company_full_json(company_id: int) -> CompanyFullJsonResponse:
    with Session(engine) as session:
        row = session.exec(
            select(CompanyJson.company_id, CompanyJson.full_json).where(CompanyJson.company_id == company_id)
        ).first()
        if not row:
            raise HTTPException(status_code=404, detail="Company not found")
        resolved_company_id, full_json = row
        return CompanyFullJsonResponse(
            company_id=int(resolved_company_id),
            full_json=(full_json or {}),
        )


@app.get("/api/v1/company-details", response_model=List[Company], tags=["Company Details"])
def list_company_details() -> List[Company]:
    with Session(engine) as session:
        companies = session.exec(select(Company)).all()
        return companies


@app.get("/api/v1/company-details/{company_id}", response_model=Company, tags=["Company Details"])
def get_company_details(company_id: int) -> Company:
    with Session(engine) as session:
        company = session.exec(select(Company).where(Company.company_id == company_id)).first()
        if not company:
            raise HTTPException(status_code=404, detail="Company not found")
        return company


@app.get("/api/v1/innovx/{company_id}", tags=["InnovX"])
def get_innovx(company_id: int, company_name: Optional[str] = Query(default=None)) -> dict:
    with Session(engine) as session:
        innovx_row = session.exec(
            select(InnovxJson).where(InnovxJson.company_id == company_id)
        ).first()

        if (not innovx_row or not innovx_row.json_data) and company_name:
            all_rows = session.exec(select(InnovxJson)).all()
            normalized_company_name = company_name.strip().casefold()

            for row in all_rows:
                if not row.json_data:
                    continue
                innovx_master = row.json_data.get("innovx_master") or {}
                stored_name = innovx_master.get("company_name")
                if isinstance(stored_name, str) and stored_name.strip().casefold() == normalized_company_name:
                    innovx_row = row
                    break

        if not innovx_row or not innovx_row.json_data:
            raise HTTPException(
                status_code=404,
                detail=f"InnovX data not found for company_id={company_id}"
                + (f" or company_name='{company_name}'" if company_name else ""),
            )

        return innovx_row.json_data


@app.get("/api/v1/hiring-rounds/{company_id}", tags=["Hiring Rounds"])
def get_hiring_rounds(company_id: int, company_name: Optional[str] = Query(default=None)) -> dict:
    with Session(engine) as session:
        hiring_data = session.exec(
            select(JobRoleDetailsJson).where(JobRoleDetailsJson.company_id == company_id)
        ).first()

        if (not hiring_data or not hiring_data.job_role_json) and company_name:
            hiring_data = session.exec(
                select(JobRoleDetailsJson).where(JobRoleDetailsJson.company_name == company_name)
            ).first()

        if not hiring_data or not hiring_data.job_role_json:
            raise HTTPException(
                status_code=404,
                detail=f"Hiring rounds not found for company_id={company_id}"
                + (f" or company_name='{company_name}'" if company_name else ""),
            )
        return hiring_data.job_role_json
