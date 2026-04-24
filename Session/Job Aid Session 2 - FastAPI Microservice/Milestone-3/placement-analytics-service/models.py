from typing import Optional, Dict, Any
from sqlmodel import SQLModel, Field
from sqlalchemy import Column, JSON


class CompanyJson(SQLModel, table=True):
    __tablename__ = "company_json"  # Explicit table name

    json_id: Optional[int] = Field(default=None, primary_key=True, index=True)
    company_id: Optional[int] = Field(default=None, index=True)
    short_json: Optional[Dict[str, Any]] = Field(sa_column=Column(JSON))
    full_json: Optional[Dict[str, Any]] = Field(sa_column=Column(JSON))


class Company(SQLModel, table=True):
    __tablename__ = "companies"  # Explicit table name

    company_id: Optional[int] = Field(default=None, primary_key=True, index=True)
    name: Optional[str] = Field(default=None)
    short_name: Optional[str] = Field(default=None)
    category: Optional[str] = Field(default=None)
    incorporation_year: Optional[str] = Field(default=None)  # Changed from int to str
    nature_of_company: Optional[str] = Field(default=None)
    headquarters_address: Optional[str] = Field(default=None)
    office_count: Optional[str] = Field(default=None)
    employee_size: Optional[str] = Field(default=None)
    website_url: Optional[str] = Field(default=None)
    linkedin_url: Optional[str] = Field(default=None)
    twitter_handle: Optional[str] = Field(default=None)
    facebook_url: Optional[str] = Field(default=None)
    instagram_url: Optional[str] = Field(default=None)
    primary_contact_email: Optional[str] = Field(default=None)
    primary_phone_number: Optional[str] = Field(default=None)
    overview_text: Optional[str] = Field(default=None)
    vision_statement: Optional[str] = Field(default=None)
    mission_statement: Optional[str] = Field(default=None)
    legal_issues: Optional[str] = Field(default=None)
    carbon_footprint: Optional[str] = Field(default=None)


class JobRoleDetailsJson(SQLModel, table=True):
    __tablename__ = "job_role_details_json"

    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    company_id: Optional[int] = Field(default=None, index=True)
    company_name: Optional[str] = Field(default=None)
    job_role_json: Optional[Dict[str, Any]] = Field(sa_column=Column(JSON))


class InnovxJson(SQLModel, table=True):
    __tablename__ = "innovx_json"

    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    company_id: Optional[int] = Field(default=None, index=True)
    json_data: Optional[Dict[str, Any]] = Field(sa_column=Column(JSON))
