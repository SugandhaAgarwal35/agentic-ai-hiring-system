"""Pydantic schema for the Researcher agent — all 163 staging_company fields.

All 163 researchable columns from the `staging_company` table are now modeled.

- 10 CORE fields are strictly validated (required; enum / min_length rules).
- 153 EXTENDED fields are `Optional[str] = None` so the agent can omit them,
  or return the sentinel string "Not Found" without breaking validation.

NOTE: every field is a `str` to mirror the wide staging table (TEXT columns).
Type precision (numerics, dates, URLs) is enforced by the Milestone 2 validators,
not by the Pydantic column type itself.
"""

from typing import Literal, Optional

from pydantic import BaseModel, Field


Category = Literal[
    "Startup", "MSME", "SMB", "Enterprise", "Investor", "VC", "Conglomerate",
]


class CompanyCore(BaseModel):
    """All 163 `staging_company` fields. 10 required, 153 optional."""

    model_config = {"extra": "ignore"}

    # ---- CORE IDENTITY (4) ------------------------------------------------
    name: str = Field(..., min_length=1, description="Legal or commonly used company name.")
    short_name: Optional[str] = None
    logo_url: Optional[str] = None
    category: Category = Field(..., description="One of the 7 enum categories.")
    incorporation_year: str = Field(..., description="4-digit founding year, as string.")
    overview_text: str = Field(..., min_length=40, description="1-3 sentence summary.")
    nature_of_company: str = Field(..., description="Public, Private, Subsidiary, Non-profit, etc.")
    headquarters_address: str = Field(..., description="City, State/Region, Country.")
    operating_countries: str = Field(..., description="Semicolon-separated list of countries.")
    office_count: Optional[str] = None
    office_locations: Optional[str] = None
    employee_size: str = Field(..., description="Headcount bucket, e.g. '1001-5000'.")

    # ---- HIRING / RETENTION (3) -------------------------------------------
    hiring_velocity: Optional[str] = None
    employee_turnover: Optional[str] = None
    avg_retention_tenure: Optional[str] = None

    # ---- BUSINESS / MARKET (4) --------------------------------------------
    pain_points_addressed: Optional[str] = None
    focus_sectors: Optional[str] = None
    offerings_description: Optional[str] = None
    top_customers: Optional[str] = None

    # ---- STRATEGY / VISION (3 core + 2 opt) -------------------------------
    core_value_proposition: Optional[str] = None
    vision_statement: str = Field(..., min_length=10)
    mission_statement: str = Field(..., min_length=10)
    core_values: Optional[str] = None
    unique_differentiators: Optional[str] = None

    # ---- COMPETITIVE POSITION (5) -----------------------------------------
    competitive_advantages: Optional[str] = None
    weaknesses_gaps: Optional[str] = None
    key_challenges_needs: Optional[str] = None
    key_competitors: Optional[str] = None
    technology_partners: Optional[str] = None

    # ---- HISTORY / NEWS (2) -----------------------------------------------
    history_timeline: Optional[str] = None
    recent_news: Optional[str] = None

    # ---- WEB PRESENCE / RATINGS (11) --------------------------------------
    website_url: Optional[str] = None
    website_quality: Optional[str] = None
    website_rating: Optional[str] = None
    website_traffic_rank: Optional[str] = None
    social_media_followers: Optional[str] = None
    glassdoor_rating: Optional[str] = None
    indeed_rating: Optional[str] = None
    google_rating: Optional[str] = None
    linkedin_url: Optional[str] = None
    twitter_handle: Optional[str] = None
    facebook_url: Optional[str] = None
    instagram_url: Optional[str] = None

    # ---- LEADERSHIP / CONTACTS (11) ---------------------------------------
    ceo_name: Optional[str] = None
    ceo_linkedin_url: Optional[str] = None
    key_leaders: Optional[str] = None
    warm_intro_pathways: Optional[str] = None
    decision_maker_access: Optional[str] = None
    primary_contact_email: Optional[str] = None
    primary_phone_number: Optional[str] = None
    contact_person_name: Optional[str] = None
    contact_person_title: Optional[str] = None
    contact_person_email: Optional[str] = None
    contact_person_phone: Optional[str] = None

    # ---- REPUTATION / LEGAL (5) -------------------------------------------
    awards_recognitions: Optional[str] = None
    brand_sentiment_score: Optional[str] = None
    event_participation: Optional[str] = None
    regulatory_status: Optional[str] = None
    legal_issues: Optional[str] = None

    # ---- FINANCIALS (10) --------------------------------------------------
    annual_revenue: Optional[str] = None
    annual_profit: Optional[str] = None
    revenue_mix: Optional[str] = None
    valuation: Optional[str] = None
    yoy_growth_rate: Optional[str] = None
    profitability_status: Optional[str] = None
    market_share_percentage: Optional[str] = None
    key_investors: Optional[str] = None
    recent_funding_rounds: Optional[str] = None
    total_capital_raised: Optional[str] = None

    # ---- ESG / SALES METRICS (8) ------------------------------------------
    esg_ratings: Optional[str] = None
    sales_motion: Optional[str] = None
    customer_acquisition_cost: Optional[str] = None
    customer_lifetime_value: Optional[str] = None
    cac_ltv_ratio: Optional[str] = None
    churn_rate: Optional[str] = None
    net_promoter_score: Optional[str] = None
    customer_concentration_risk: Optional[str] = None

    # ---- CASH / BURN (3) --------------------------------------------------
    burn_rate: Optional[str] = None
    runway_months: Optional[str] = None
    burn_multiplier: Optional[str] = None

    # ---- TECH / IP (6) ----------------------------------------------------
    intellectual_property: Optional[str] = None
    r_and_d_investment: Optional[str] = None
    ai_ml_adoption_level: Optional[str] = None
    tech_stack: Optional[str] = None
    cybersecurity_posture: Optional[str] = None
    supply_chain_dependencies: Optional[str] = None

    # ---- RISK (2) ---------------------------------------------------------
    geopolitical_risks: Optional[str] = None
    macro_risks: Optional[str] = None

    # ---- PEOPLE / CULTURE LEVEL-1 (4) -------------------------------------
    diversity_metrics: Optional[str] = None
    remote_policy_details: Optional[str] = None
    training_spend: Optional[str] = None
    partnership_ecosystem: Optional[str] = None

    # ---- OUTLOOK / STRATEGY (7) -------------------------------------------
    exit_strategy_history: Optional[str] = None
    carbon_footprint: Optional[str] = None
    ethical_sourcing: Optional[str] = None
    benchmark_vs_peers: Optional[str] = None
    future_projections: Optional[str] = None
    strategic_priorities: Optional[str] = None
    industry_associations: Optional[str] = None

    # ---- MARKETING / PRODUCT (7) ------------------------------------------
    case_studies: Optional[str] = None
    go_to_market_strategy: Optional[str] = None
    innovation_roadmap: Optional[str] = None
    product_pipeline: Optional[str] = None
    board_members: Optional[str] = None
    marketing_video_url: Optional[str] = None
    customer_testimonials: Optional[str] = None

    # ---- MARKET SIZING (4) ------------------------------------------------
    tech_adoption_rating: Optional[str] = None
    tam: Optional[str] = None
    sam: Optional[str] = None
    som: Optional[str] = None

    # ---- WORK CULTURE (6) -------------------------------------------------
    work_culture_summary: Optional[str] = None
    manager_quality: Optional[str] = None
    psychological_safety: Optional[str] = None
    feedback_culture: Optional[str] = None
    diversity_inclusion_score: Optional[str] = None
    ethical_standards: Optional[str] = None

    # ---- HOURS / FLEXIBILITY (6) ------------------------------------------
    typical_hours: Optional[str] = None
    overtime_expectations: Optional[str] = None
    weekend_work: Optional[str] = None
    flexibility_level: Optional[str] = None
    leave_policy: Optional[str] = None
    burnout_risk: Optional[str] = None

    # ---- OFFICE / LOCATION (5) --------------------------------------------
    location_centrality: Optional[str] = None
    public_transport_access: Optional[str] = None
    cab_policy: Optional[str] = None
    airport_commute_time: Optional[str] = None
    office_zone_type: Optional[str] = None

    # ---- SAFETY / HEALTH (5) ----------------------------------------------
    area_safety: Optional[str] = None
    safety_policies: Optional[str] = None
    infrastructure_safety: Optional[str] = None
    emergency_preparedness: Optional[str] = None
    health_support: Optional[str] = None

    # ---- LEARNING / GROWTH (7) --------------------------------------------
    onboarding_quality: Optional[str] = None
    learning_culture: Optional[str] = None
    exposure_quality: Optional[str] = None
    mentorship_availability: Optional[str] = None
    internal_mobility: Optional[str] = None
    promotion_clarity: Optional[str] = None
    tools_access: Optional[str] = None

    # ---- ROLE / IMPACT (6) ------------------------------------------------
    role_clarity: Optional[str] = None
    early_ownership: Optional[str] = None
    work_impact: Optional[str] = None
    execution_thinking_balance: Optional[str] = None
    automation_level: Optional[str] = None
    cross_functional_exposure: Optional[str] = None

    # ---- COMPANY POSITION (4) ---------------------------------------------
    company_maturity: Optional[str] = None
    brand_value: Optional[str] = None
    client_quality: Optional[str] = None
    layoff_history: Optional[str] = None

    # ---- COMPENSATION / BENEFITS (6) --------------------------------------
    fixed_vs_variable_pay: Optional[str] = None
    bonus_predictability: Optional[str] = None
    esops_incentives: Optional[str] = None
    family_health_insurance: Optional[str] = None
    relocation_support: Optional[str] = None
    lifestyle_benefits: Optional[str] = None

    # ---- CAREER OUTCOMES (7) ----------------------------------------------
    exit_opportunities: Optional[str] = None
    skill_relevance: Optional[str] = None
    external_recognition: Optional[str] = None
    network_strength: Optional[str] = None
    global_exposure: Optional[str] = None
    mission_clarity: Optional[str] = None
    sustainability_csr: Optional[str] = None
    crisis_behavior: Optional[str] = None
