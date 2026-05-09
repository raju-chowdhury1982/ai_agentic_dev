from typing import List, Literal

from pydantic import BaseModel, Field


class BusinessAnalysis(BaseModel):
    """Structured output schema for business analysis results."""

    business_model: str
    business_model_type: Literal[
        "real_estate", "saas", "marketplace", "services", "manufacturing", "unknown"
    ]
    revenue_streams: List[str]
    # operational_risks: List[str]
    # legal_risks: List[str]
    missing_information: List[str]
    investment_score: int = Field(..., ge=1, le=10)
    investment_reason: str
    confidence_score: float = Field(..., ge=0.0, le=1.0)
    confidence_reason: str
    source_coverage: float
    is_inferred: bool


class Risk(BaseModel):
    """Structured output schema for individual risk items."""

    risk_description: str
    is_inferred: bool
    source_reference: str
    risk_category: Literal["operational", "legal", "financial", "market"]
    risk_level: Literal["low", "medium", "high"]


class RiskAssessment(BaseModel):
    """Structured output schema for risk assessment results."""

    risks: List[Risk]


class UnifiedAnalysisOutput(BaseModel):
    """Unified schema to combine business analysis and risk assessment."""

    # business_analysis: Optional[BusinessAnalysis] = None
    # risk_assessment: Optional[RiskAssessment] = None
    business_analysis: BusinessAnalysis
    risk_assessment: RiskAssessment
