from typing import List, Literal, Optional  # type: ignore

from pydantic import BaseModel, Field  # type: ignore

from app.schemas.business_schema import BusinessAnalysis
from app.schemas.clarification_schema import \
    ClarificationQuestions  # type: ignore
# user facing final state
from app.schemas.final_report_schema import FinalDecisionReport
from app.schemas.investment_schema import InvestmentDecision  # type: ignore
from app.schemas.risk_schema import RiskAssessment  # type: ignore


class PipelineState(BaseModel):
    """Structured output schema for the overall pipeline state."""

    # --- TRACE ---
    trace_id: Optional[str] = None
    # --- INPUTS ---
    raw_input: str
    validated_input: Optional[str] = None
    # --- NODE OUTPUTS ---
    business_analysis: Optional[BusinessAnalysis] = None
    risk_assessment: Optional[RiskAssessment] = None
    # overall_investment_score: Optional[int] = Field(None, ge=1, le=10)
    # overall_confidence_score: Optional[float] = Field(None, ge=0.0, le=1.0)
    # confidence_reason: Optional[str] = None
    investment_decision: Optional[InvestmentDecision] = None
    clarification_questions: Optional[ClarificationQuestions] = None
    # overall_recommendation: Optional[
    #     Literal["invest", "do_not_invest", "further_analysis_needed"]
    # ] = None
    # --- WORKFLOW CONTROL ---
    current_stage: Optional[str] = None
    requires_clarification: bool = False
    errors: List[str] = []

    # --- USER-READY OUTPUT LAYER ---
    final_report: Optional[FinalDecisionReport] = None
