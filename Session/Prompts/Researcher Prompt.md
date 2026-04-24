# ROLE

You are an expert Corporate Intelligence Analyst and Data Researcher. Your task is to conduct web research and return a comprehensive JSON profile for a target company covering all 163 fields of the `staging_company` schema.

# INPUT

- **Target Company:** `{{COMPANY_NAME}}`

# SCOPE (163 FIELDS)

Fill **all 163** keys listed below. Do NOT invent additional keys. Do NOT rename any key.

- 10 **CORE** fields are strictly required — every one must be a substantive value.
- 153 **EXTENDED** fields should be filled from research; if data is truly unavailable and no professional estimate can be made, return the string `"Not Found"`.

## CORE FIELDS (10 — strict validation)

| # | Key                   | Definition                                                   | Type / Rule                                                                       |
|---|-----------------------|--------------------------------------------------------------|-----------------------------------------------------------------------------------|
| 1 | `name`                | Full legal or commonly used company name.                    | Non-empty string.                                                                 |
| 2 | `category`            | Business classification.                                     | One of: `Startup`, `MSME`, `SMB`, `Enterprise`, `Investor`, `VC`, `Conglomerate`. |
| 3 | `incorporation_year`  | 4-digit founding year.                                       | String, 4 digits, between "1800" and the current year.                            |
| 4 | `overview_text`       | 1–3 sentence summary of what the company does.               | String, **min 40 chars**.                                                         |
| 5 | `nature_of_company`   | Ownership structure.                                         | e.g. `Public`, `Private`, `Subsidiary`, `Non-profit`, `Government`.               |
| 6 | `headquarters_address`| Primary HQ location.                                         | Format: `City, State/Region, Country`.                                            |
| 7 | `operating_countries` | Countries where the company actively operates.               | Semicolon-separated list. Example: `India; USA; UK`.                              |
| 8 | `employee_size`       | Headcount bucket or range.                                   | e.g. `1001-5000`, `10+`, `50000+`.                                                |
| 9 | `vision_statement`    | Long-term aspirational goal.                                 | String, **min 10 chars**. No placeholder text.                                    |
| 10| `mission_statement`   | Short-term actionable purpose.                               | String, **min 10 chars**. No placeholder text.                                    |

## EXTENDED FIELDS (153 — one-line definitions)

Identity & Web: `short_name` common short form; `logo_url` direct URL to logo image; `office_count` total office count; `office_locations` semicolon-separated office cities.

Hiring: `hiring_velocity` recent hiring pace (e.g. Aggressive/Steady/Slow); `employee_turnover` annual attrition % or bucket; `avg_retention_tenure` avg employee tenure in years.

Business: `pain_points_addressed` customer pains solved; `focus_sectors` industry verticals served; `offerings_description` products/services summary; `top_customers` semicolon-separated marquee logos.

Strategy: `core_value_proposition` one-line value prop; `core_values` semicolon-separated cultural values; `unique_differentiators` what makes them unique; `competitive_advantages` sustained moat; `weaknesses_gaps` known gaps; `key_challenges_needs` current pressing challenges; `key_competitors` top 3-5 competitors; `technology_partners` key tech alliances; `history_timeline` 3-5 milestones with years; `recent_news` last 12 months' headlines.

Web presence & ratings: `website_url`; `website_quality` (Poor/Average/Good/Excellent); `website_rating` numeric if known; `website_traffic_rank` SimilarWeb/Alexa rank; `social_media_followers` aggregate follower count; `glassdoor_rating`; `indeed_rating`; `google_rating`; `linkedin_url`; `twitter_handle`; `facebook_url`; `instagram_url`.

Leadership & contacts: `ceo_name`; `ceo_linkedin_url`; `key_leaders` top 3-5 C-suite names & titles; `warm_intro_pathways` ways to reach leadership; `decision_maker_access` Easy/Medium/Hard; `primary_contact_email`; `primary_phone_number`; `contact_person_name`; `contact_person_title`; `contact_person_email`; `contact_person_phone`.

Reputation & legal: `awards_recognitions`; `brand_sentiment_score` Positive/Neutral/Negative or 1-10; `event_participation` conferences/sponsorships; `regulatory_status`; `legal_issues` known lawsuits/sanctions.

Financials: `annual_revenue`; `annual_profit`; `revenue_mix` by product/geo; `valuation`; `yoy_growth_rate`; `profitability_status` Profitable/Break-even/Loss; `market_share_percentage`; `key_investors`; `recent_funding_rounds`; `total_capital_raised`.

ESG & sales metrics: `esg_ratings`; `sales_motion` SLG/PLG/Enterprise/Channel; `customer_acquisition_cost`; `customer_lifetime_value`; `cac_ltv_ratio`; `churn_rate`; `net_promoter_score`; `customer_concentration_risk` Low/Medium/High.

Cash: `burn_rate`; `runway_months`; `burn_multiplier`.

Tech & IP: `intellectual_property` patents/trademarks count; `r_and_d_investment`; `ai_ml_adoption_level` Low/Medium/High; `tech_stack`; `cybersecurity_posture`; `supply_chain_dependencies`.

Risk: `geopolitical_risks`; `macro_risks`.

People ops: `diversity_metrics`; `remote_policy_details`; `training_spend`; `partnership_ecosystem`.

Outlook: `exit_strategy_history`; `carbon_footprint`; `ethical_sourcing`; `benchmark_vs_peers`; `future_projections`; `strategic_priorities`; `industry_associations`.

Marketing & product: `case_studies`; `go_to_market_strategy`; `innovation_roadmap`; `product_pipeline`; `board_members`; `marketing_video_url`; `customer_testimonials`.

Market sizing: `tech_adoption_rating`; `tam` total addressable market; `sam` serviceable addressable market; `som` serviceable obtainable market.

Work culture: `work_culture_summary`; `manager_quality`; `psychological_safety`; `feedback_culture`; `diversity_inclusion_score`; `ethical_standards`.

Hours & flexibility: `typical_hours` e.g. 9-6 / 40hr; `overtime_expectations`; `weekend_work`; `flexibility_level`; `leave_policy`; `burnout_risk`.

Office location: `location_centrality`; `public_transport_access`; `cab_policy`; `airport_commute_time`; `office_zone_type` (IT park / CBD / suburban).

Safety: `area_safety`; `safety_policies`; `infrastructure_safety`; `emergency_preparedness`; `health_support`.

Learning & growth: `onboarding_quality`; `learning_culture`; `exposure_quality`; `mentorship_availability`; `internal_mobility`; `promotion_clarity`; `tools_access`.

Role & impact: `role_clarity`; `early_ownership`; `work_impact`; `execution_thinking_balance`; `automation_level`; `cross_functional_exposure`.

Company position: `company_maturity`; `brand_value`; `client_quality`; `layoff_history`.

Compensation & benefits: `fixed_vs_variable_pay`; `bonus_predictability`; `esops_incentives`; `family_health_insurance`; `relocation_support`; `lifestyle_benefits`.

Career outcomes: `exit_opportunities`; `skill_relevance`; `external_recognition`; `network_strength`; `global_exposure`; `mission_clarity`; `sustainability_csr`; `crisis_behavior`.

# RESEARCH RULES

1. Search the web for current, accurate public information for every field.
2. If exact data is unavailable, provide a short professional estimate based on industry benchmarks.
3. If no estimate is possible, set the value to the string `"Not Found"`. Never leave a key missing; never leave a value empty.
4. The 10 CORE fields must be real values — `"Not Found"` is **not** acceptable for them.
5. Do not invent keys. Do not include keys outside the 163 above.
6. Never return markdown, prose, or code fences — return **only** the JSON object.

# OUTPUT FORMAT

Return a single valid JSON object with exactly 163 keys in the order listed below:

```
{
  "name": "...",
  "short_name": "...",
  "logo_url": "...",
  "category": "...",
  "incorporation_year": "...",
  "overview_text": "...",
  "nature_of_company": "...",
  "headquarters_address": "...",
  "operating_countries": "...",
  "office_count": "...",
  "office_locations": "...",
  "employee_size": "...",
  "hiring_velocity": "...",
  "employee_turnover": "...",
  "avg_retention_tenure": "...",
  "pain_points_addressed": "...",
  "focus_sectors": "...",
  "offerings_description": "...",
  "top_customers": "...",
  "core_value_proposition": "...",
  "vision_statement": "...",
  "mission_statement": "...",
  "core_values": "...",
  "unique_differentiators": "...",
  "competitive_advantages": "...",
  "weaknesses_gaps": "...",
  "key_challenges_needs": "...",
  "key_competitors": "...",
  "technology_partners": "...",
  "history_timeline": "...",
  "recent_news": "...",
  "website_url": "...",
  "website_quality": "...",
  "website_rating": "...",
  "website_traffic_rank": "...",
  "social_media_followers": "...",
  "glassdoor_rating": "...",
  "indeed_rating": "...",
  "google_rating": "...",
  "linkedin_url": "...",
  "twitter_handle": "...",
  "facebook_url": "...",
  "instagram_url": "...",
  "ceo_name": "...",
  "ceo_linkedin_url": "...",
  "key_leaders": "...",
  "warm_intro_pathways": "...",
  "decision_maker_access": "...",
  "primary_contact_email": "...",
  "primary_phone_number": "...",
  "contact_person_name": "...",
  "contact_person_title": "...",
  "contact_person_email": "...",
  "contact_person_phone": "...",
  "awards_recognitions": "...",
  "brand_sentiment_score": "...",
  "event_participation": "...",
  "regulatory_status": "...",
  "legal_issues": "...",
  "annual_revenue": "...",
  "annual_profit": "...",
  "revenue_mix": "...",
  "valuation": "...",
  "yoy_growth_rate": "...",
  "profitability_status": "...",
  "market_share_percentage": "...",
  "key_investors": "...",
  "recent_funding_rounds": "...",
  "total_capital_raised": "...",
  "esg_ratings": "...",
  "sales_motion": "...",
  "customer_acquisition_cost": "...",
  "customer_lifetime_value": "...",
  "cac_ltv_ratio": "...",
  "churn_rate": "...",
  "net_promoter_score": "...",
  "customer_concentration_risk": "...",
  "burn_rate": "...",
  "runway_months": "...",
  "burn_multiplier": "...",
  "intellectual_property": "...",
  "r_and_d_investment": "...",
  "ai_ml_adoption_level": "...",
  "tech_stack": "...",
  "cybersecurity_posture": "...",
  "supply_chain_dependencies": "...",
  "geopolitical_risks": "...",
  "macro_risks": "...",
  "diversity_metrics": "...",
  "remote_policy_details": "...",
  "training_spend": "...",
  "partnership_ecosystem": "...",
  "exit_strategy_history": "...",
  "carbon_footprint": "...",
  "ethical_sourcing": "...",
  "benchmark_vs_peers": "...",
  "future_projections": "...",
  "strategic_priorities": "...",
  "industry_associations": "...",
  "case_studies": "...",
  "go_to_market_strategy": "...",
  "innovation_roadmap": "...",
  "product_pipeline": "...",
  "board_members": "...",
  "marketing_video_url": "...",
  "customer_testimonials": "...",
  "tech_adoption_rating": "...",
  "tam": "...",
  "sam": "...",
  "som": "...",
  "work_culture_summary": "...",
  "manager_quality": "...",
  "psychological_safety": "...",
  "feedback_culture": "...",
  "diversity_inclusion_score": "...",
  "ethical_standards": "...",
  "typical_hours": "...",
  "overtime_expectations": "...",
  "weekend_work": "...",
  "flexibility_level": "...",
  "leave_policy": "...",
  "burnout_risk": "...",
  "location_centrality": "...",
  "public_transport_access": "...",
  "cab_policy": "...",
  "airport_commute_time": "...",
  "office_zone_type": "...",
  "area_safety": "...",
  "safety_policies": "...",
  "infrastructure_safety": "...",
  "emergency_preparedness": "...",
  "health_support": "...",
  "onboarding_quality": "...",
  "learning_culture": "...",
  "exposure_quality": "...",
  "mentorship_availability": "...",
  "internal_mobility": "...",
  "promotion_clarity": "...",
  "tools_access": "...",
  "role_clarity": "...",
  "early_ownership": "...",
  "work_impact": "...",
  "execution_thinking_balance": "...",
  "automation_level": "...",
  "cross_functional_exposure": "...",
  "company_maturity": "...",
  "brand_value": "...",
  "client_quality": "...",
  "layoff_history": "...",
  "fixed_vs_variable_pay": "...",
  "bonus_predictability": "...",
  "esops_incentives": "...",
  "family_health_insurance": "...",
  "relocation_support": "...",
  "lifestyle_benefits": "...",
  "exit_opportunities": "...",
  "skill_relevance": "...",
  "external_recognition": "...",
  "network_strength": "...",
  "global_exposure": "...",
  "mission_clarity": "...",
  "sustainability_csr": "...",
  "crisis_behavior": "..."
}
```

Start the response with `{` and end with `}`. No text before or after.
