"""ETL agent — writes validated payloads into staging tables.

Default mode is `dry` (just prints the row). Set ETL_WRITE_MODE=db + DATABASE_URL
to perform a real insert. The DB trigger from `Database Setup/Step 4` migrates
the staged row into normalized tables.
"""

from __future__ import annotations

import json
import os
from typing import Any, Literal

from models import (
    STAGING_COMPANY_DATA_COLUMNS,
    JobRoleDetailsJson,
    StagingCompany,
    StagingCompanySkillLevels,
)


PayloadKind = Literal["company", "skills", "hiring"]


def _stable_company_id(company: str) -> int:
    return abs(hash(company)) % 10_000_000


def _build_company_rows(payload: dict[str, Any]) -> list[dict[str, Any]]:
    return [{
        "company_id": _stable_company_id(payload["name"]),
        **{k: payload.get(k) for k in STAGING_COMPANY_DATA_COLUMNS},
        "processing_status": "pending",
    }]


def _build_skill_rows(payload: dict[str, Any]) -> list[dict[str, Any]]:
    company = payload["company_name"]
    return [
        {
            "company_name": company,
            "skill_area": row["skill_area"],
            "level": int(row["level"]),
            "proficiency_code": row["proficiency_code"],
            "rationale": row.get("rationale"),
            "processing_status": "pending",
        }
        for row in payload["skill_sets"]
    ]


def _build_hiring_rows(payload: dict[str, Any]) -> list[dict[str, Any]]:
    return [{
        "company_name": payload["company_name"],
        "payload_json": json.dumps(payload, ensure_ascii=False),
        "processing_status": "pending",
    }]


def stage(kind: PayloadKind, payload: dict[str, Any]) -> list[dict[str, Any]]:
    """Write the payload to the correct staging table and return the inserted rows."""

    if kind == "company":
        rows = _build_company_rows(payload)
        model_cls = StagingCompany
    elif kind == "skills":
        rows = _build_skill_rows(payload)
        model_cls = StagingCompanySkillLevels
    elif kind == "hiring":
        rows = _build_hiring_rows(payload)
        model_cls = JobRoleDetailsJson
    else:
        raise ValueError(f"Unknown kind: {kind!r}")

    if os.environ.get("ETL_WRITE_MODE") != "db":
        print(f"[ETL][dry-run] would insert {len(rows)} row(s) into {model_cls.__tablename__}")
        for row in rows:
            print(json.dumps(row, indent=2, ensure_ascii=False))
        return rows

    from sqlmodel import Session, create_engine  # noqa: WPS433

    engine = create_engine(os.environ["DATABASE_URL"])
    with Session(engine) as session:
        for row in rows:
            session.add(model_cls(**row))
        session.commit()

    print(f"[ETL][db] inserted {len(rows)} row(s) into {model_cls.__tablename__}")
    return rows
