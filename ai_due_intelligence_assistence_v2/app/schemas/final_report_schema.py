from typing import List, Literal

from pydantic import BaseModel


class FinalDecisionReport(BaseModel):
    report_title: str
    executive_summary: str
    recommendations: Literal[
        "invest", "proceed_with_caution", "further_analysis_needed", "do_not_invest"
    ]
    investment_score: int
    confidence_score: float

    key_positive_factors: List[str]
    key_risk_factors: List[str]

    clarification_needed: bool
    clarification_questions: List[str]

    next_steps: List[str]
