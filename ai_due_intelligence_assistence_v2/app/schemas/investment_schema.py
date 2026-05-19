from typing import List, Literal

from pydantic import BaseModel, Field


class InvestmentDecision(BaseModel):
    """Based on business and risk analysis, then draw inference for investment decision with reason"""

    overall_investment_score: int = Field(..., ge=1, le=10)
    overall_confidence_score: float = Field(..., ge=0.0, le=1.0)
    recommendation: Literal["invest", "further_analysis_needed", "do_not_invest"]
    decision_reason: str
    key_positive_factors: List[str]
    key_risk_factors: List[str]
    required_next_steps: List[str]
