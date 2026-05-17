from typing import List, Literal, Optional

from pydantic import BaseModel, Field


class BusinessAnalysis(BaseModel):
    """Structured output schema for business analysis results."""

    business_model: str
    business_model_type: Literal[
        "real_estate", "saas", "marketplace", "services", "manufacturing", "unknown"
    ]
    revenue_streams: List[str]
    missing_information: List[str]
    investment_score: int = Field(..., ge=1, le=10)
    investment_reason: str
    confidence_score: float = Field(..., ge=0.0, le=1.0)
    confidence_reason: str
    source_coverage: Optional[float]
    is_inferred: bool
