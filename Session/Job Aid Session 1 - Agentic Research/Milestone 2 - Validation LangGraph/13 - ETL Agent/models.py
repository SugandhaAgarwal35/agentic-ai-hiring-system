"""SQLModel mirrors of the 3 staging tables we write to.

`StagingCompany` models all 163 researchable columns from `staging_company`,
matching the expanded Milestone 1 `CompanyCore` schema. The skills and
hiring-process tables still use their original narrow shape.
"""

from typing import Optional

from sqlmodel import Field, SQLModel


# Full list of researchable columns on staging_company (matches CSV header,
# minus the `company_id` primary key and the `processing_status` state column).
STAGING_COMPANY_DATA_COLUMNS: tuple[str, ...] = (
    "name", "short_name", "logo_url", "category", "incorporation_year",
    "overview_text", "nature_of_company", "headquarters_address",
    "operating_countries", "office_count", "office_locations", "employee_size",
    "hiring_velocity", "employee_turnover", "avg_retention_tenure",
    "pain_points_addressed", "focus_sectors", "offerings_description",
    "top_customers", "core_value_proposition", "vision_statement",
    "mission_statement", "core_values", "unique_differentiators",
    "competitive_advantages", "weaknesses_gaps", "key_challenges_needs",
    "key_competitors", "technology_partners", "history_timeline", "recent_news",
    "website_url", "website_quality", "website_rating", "website_traffic_rank",
    "social_media_followers", "glassdoor_rating", "indeed_rating",
    "google_rating", "linkedin_url", "twitter_handle", "facebook_url",
    "instagram_url", "ceo_name", "ceo_linkedin_url", "key_leaders",
    "warm_intro_pathways", "decision_maker_access", "primary_contact_email",
    "primary_phone_number", "contact_person_name", "contact_person_title",
    "contact_person_email", "contact_person_phone", "awards_recognitions",
    "brand_sentiment_score", "event_participation", "regulatory_status",
    "legal_issues", "annual_revenue", "annual_profit", "revenue_mix",
    "valuation", "yoy_growth_rate", "profitability_status",
    "market_share_percentage", "key_investors", "recent_funding_rounds",
    "total_capital_raised", "esg_ratings", "sales_motion",
    "customer_acquisition_cost", "customer_lifetime_value", "cac_ltv_ratio",
    "churn_rate", "net_promoter_score", "customer_concentration_risk",
    "burn_rate", "runway_months", "burn_multiplier", "intellectual_property",
    "r_and_d_investment", "ai_ml_adoption_level", "tech_stack",
    "cybersecurity_posture", "supply_chain_dependencies", "geopolitical_risks",
    "macro_risks", "diversity_metrics", "remote_policy_details",
    "training_spend", "partnership_ecosystem", "exit_strategy_history",
    "carbon_footprint", "ethical_sourcing", "benchmark_vs_peers",
    "future_projections", "strategic_priorities", "industry_associations",
    "case_studies", "go_to_market_strategy", "innovation_roadmap",
    "product_pipeline", "board_members", "marketing_video_url",
    "customer_testimonials", "tech_adoption_rating", "tam", "sam", "som",
    "work_culture_summary", "manager_quality", "psychological_safety",
    "feedback_culture", "diversity_inclusion_score", "ethical_standards",
    "typical_hours", "overtime_expectations", "weekend_work",
    "flexibility_level", "leave_policy", "burnout_risk", "location_centrality",
    "public_transport_access", "cab_policy", "airport_commute_time",
    "office_zone_type", "area_safety", "safety_policies",
    "infrastructure_safety", "emergency_preparedness", "health_support",
    "onboarding_quality", "learning_culture", "exposure_quality",
    "mentorship_availability", "internal_mobility", "promotion_clarity",
    "tools_access", "role_clarity", "early_ownership", "work_impact",
    "execution_thinking_balance", "automation_level", "cross_functional_exposure",
    "company_maturity", "brand_value", "client_quality", "layoff_history",
    "fixed_vs_variable_pay", "bonus_predictability", "esops_incentives",
    "family_health_insurance", "relocation_support", "lifestyle_benefits",
    "exit_opportunities", "skill_relevance", "external_recognition",
    "network_strength", "global_exposure", "mission_clarity",
    "sustainability_csr", "crisis_behavior",
)


class StagingCompany(SQLModel, table=True):
    __tablename__ = "staging_company"

    company_id: Optional[int] = Field(default=None, primary_key=True)
    # Core identity
    name: str = Field(index=True)
    short_name: Optional[str] = None
    logo_url: Optional[str] = None
    category: Optional[str] = None
    incorporation_year: Optional[str] = None
    overview_text: Optional[str] = None
    nature_of_company: Optional[str] = None
    headquarters_address: Optional[str] = None
    operating_countries: Optional[str] = None
    office_count: Optional[str] = None
    office_locations: Optional[str] = None
    employee_size: Optional[str] = None
    # Hiring
    hiring_velocity: Optional[str] = None
    employee_turnover: Optional[str] = None
    avg_retention_tenure: Optional[str] = None
    # Business
    pain_points_addressed: Optional[str] = None
    focus_sectors: Optional[str] = None
    offerings_description: Optional[str] = None
    top_customers: Optional[str] = None
    # Strategy / vision
    core_value_proposition: Optional[str] = None
    vision_statement: Optional[str] = None
    mission_statement: Optional[str] = None
    core_values: Optional[str] = None
    unique_differentiators: Optional[str] = None
    # Competitive
    competitive_advantages: Optional[str] = None
    weaknesses_gaps: Optional[str] = None
    key_challenges_needs: Optional[str] = None
    key_competitors: Optional[str] = None
    technology_partners: Optional[str] = None
    # History / news
    history_timeline: Optional[str] = None
    recent_news: Optional[str] = None
    # Web presence / ratings
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
    # Leadership / contacts
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
    # Reputation / legal
    awards_recognitions: Optional[str] = None
    brand_sentiment_score: Optional[str] = None
    event_participation: Optional[str] = None
    regulatory_status: Optional[str] = None
    legal_issues: Optional[str] = None
    # Financials
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
    # ESG / sales
    esg_ratings: Optional[str] = None
    sales_motion: Optional[str] = None
    customer_acquisition_cost: Optional[str] = None
    customer_lifetime_value: Optional[str] = None
    cac_ltv_ratio: Optional[str] = None
    churn_rate: Optional[str] = None
    net_promoter_score: Optional[str] = None
    customer_concentration_risk: Optional[str] = None
    # Cash
    burn_rate: Optional[str] = None
    runway_months: Optional[str] = None
    burn_multiplier: Optional[str] = None
    # Tech / IP
    intellectual_property: Optional[str] = None
    r_and_d_investment: Optional[str] = None
    ai_ml_adoption_level: Optional[str] = None
    tech_stack: Optional[str] = None
    cybersecurity_posture: Optional[str] = None
    supply_chain_dependencies: Optional[str] = None
    # Risk
    geopolitical_risks: Optional[str] = None
    macro_risks: Optional[str] = None
    # People ops
    diversity_metrics: Optional[str] = None
    remote_policy_details: Optional[str] = None
    training_spend: Optional[str] = None
    partnership_ecosystem: Optional[str] = None
    # Outlook
    exit_strategy_history: Optional[str] = None
    carbon_footprint: Optional[str] = None
    ethical_sourcing: Optional[str] = None
    benchmark_vs_peers: Optional[str] = None
    future_projections: Optional[str] = None
    strategic_priorities: Optional[str] = None
    industry_associations: Optional[str] = None
    # Marketing / product
    case_studies: Optional[str] = None
    go_to_market_strategy: Optional[str] = None
    innovation_roadmap: Optional[str] = None
    product_pipeline: Optional[str] = None
    board_members: Optional[str] = None
    marketing_video_url: Optional[str] = None
    customer_testimonials: Optional[str] = None
    # Market sizing
    tech_adoption_rating: Optional[str] = None
    tam: Optional[str] = None
    sam: Optional[str] = None
    som: Optional[str] = None
    # Work culture
    work_culture_summary: Optional[str] = None
    manager_quality: Optional[str] = None
    psychological_safety: Optional[str] = None
    feedback_culture: Optional[str] = None
    diversity_inclusion_score: Optional[str] = None
    ethical_standards: Optional[str] = None
    # Hours / flexibility
    typical_hours: Optional[str] = None
    overtime_expectations: Optional[str] = None
    weekend_work: Optional[str] = None
    flexibility_level: Optional[str] = None
    leave_policy: Optional[str] = None
    burnout_risk: Optional[str] = None
    # Office / location
    location_centrality: Optional[str] = None
    public_transport_access: Optional[str] = None
    cab_policy: Optional[str] = None
    airport_commute_time: Optional[str] = None
    office_zone_type: Optional[str] = None
    # Safety / health
    area_safety: Optional[str] = None
    safety_policies: Optional[str] = None
    infrastructure_safety: Optional[str] = None
    emergency_preparedness: Optional[str] = None
    health_support: Optional[str] = None
    # Learning & growth
    onboarding_quality: Optional[str] = None
    learning_culture: Optional[str] = None
    exposure_quality: Optional[str] = None
    mentorship_availability: Optional[str] = None
    internal_mobility: Optional[str] = None
    promotion_clarity: Optional[str] = None
    tools_access: Optional[str] = None
    # Role & impact
    role_clarity: Optional[str] = None
    early_ownership: Optional[str] = None
    work_impact: Optional[str] = None
    execution_thinking_balance: Optional[str] = None
    automation_level: Optional[str] = None
    cross_functional_exposure: Optional[str] = None
    # Company position
    company_maturity: Optional[str] = None
    brand_value: Optional[str] = None
    client_quality: Optional[str] = None
    layoff_history: Optional[str] = None
    # Compensation & benefits
    fixed_vs_variable_pay: Optional[str] = None
    bonus_predictability: Optional[str] = None
    esops_incentives: Optional[str] = None
    family_health_insurance: Optional[str] = None
    relocation_support: Optional[str] = None
    lifestyle_benefits: Optional[str] = None
    # Career outcomes
    exit_opportunities: Optional[str] = None
    skill_relevance: Optional[str] = None
    external_recognition: Optional[str] = None
    network_strength: Optional[str] = None
    global_exposure: Optional[str] = None
    mission_clarity: Optional[str] = None
    sustainability_csr: Optional[str] = None
    crisis_behavior: Optional[str] = None

    processing_status: str = Field(default="pending")


class StagingCompanySkillLevels(SQLModel, table=True):
    __tablename__ = "staging_company_skill_levels"

    id: Optional[int] = Field(default=None, primary_key=True)
    company_name: str = Field(index=True)
    skill_area: str
    level: int
    proficiency_code: str
    rationale: Optional[str] = None
    processing_status: str = Field(default="pending")


class JobRoleDetailsJson(SQLModel, table=True):
    __tablename__ = "job_role_details_json"

    id: Optional[int] = Field(default=None, primary_key=True)
    company_name: str = Field(index=True)
    payload_json: str  # raw JSON payload — trigger parses it downstream
    processing_status: str = Field(default="pending")
