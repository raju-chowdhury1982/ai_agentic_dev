from typing import List, Literal

from pydantic import BaseModel


class FinalDecisionReport(BaseModel):
    report_title: str
    executive_summary: str
    recommendations: Literal["invest", "do_not_invest", "further_analysis_needed"]
    investment_score: int
    confidence_score: float

    key_positive_factors: List[str]
    key_risk_factors: List[str]

    clarification_needed: bool
    clarification_questions: List[str]

    next_steps: List[str]
