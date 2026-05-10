from typing import List, Literal, Optional

from pydantic import BaseModel, Field

from app.schemas.business_schema import BusinessAnalysis
from app.schemas.risk_schema import RiskAssessment  # type: ignore


class PipelineState(BaseModel):
    """Structured output schema for the overall pipeline state."""

    raw_input: str
    validated_input: Optional[str] = None
    business_analysis: Optional[BusinessAnalysis] = None
    risk_assessment: Optional[RiskAssessment] = None
    overall_investment_score: Optional[int] = Field(None, ge=1, le=10)
    overall_confidence_score: Optional[float] = Field(None, ge=0.0, le=1.0)
    confidence_reason: Optional[str] = None
    overall_recommendation: Optional[
        Literal["invest", "do_not_invest", "further_analysis_needed"]
    ] = None
    final_summary: Optional[str] = None
    errors: List[str] = []
