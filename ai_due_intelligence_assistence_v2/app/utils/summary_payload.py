from typing import Any

from app.schemas.pipeline_state import PipelineState


# building compact schema payload for reduce latency
def build_summary_payload(state: PipelineState) -> dict[str, Any]:
    business = state.business_analysis
    risk = state.risk_assessment
    decision = state.investment_decision
    clarification = state.clarification_questions

    return {
        "business_model": business.business_model if business else None,
        "business_model_type": business.business_model_type if business else None,
        "revenue_streams": business.revenue_streams if business else [],
        "missing_information": business.missing_information if business else [],
        "recommendation": decision.recommendation if decision else None,
        "investment_score": decision.overall_investment_score if decision else None,
        "confidence_score": decision.overall_confidence_score if decision else None,
        "decision_reason": decision.decision_reason if decision else None,
        "key_positive_factors": decision.key_positive_factors if decision else [],
        "key_risk_factors": decision.key_risk_factors if decision else [],
        "required_next_steps": decision.required_next_steps if decision else [],
        "risks": [
            {
                "description": r.risk_description,
                "category": r.risk_category,
                "level": r.risk_level,
            }
            for r in (risk.risk if risk else [])
        ],
        "clarification_needed": (
            clarification.clarification_needed if clarification else False
        ),
        "clarification_questions": (
            clarification.clarification_questions if clarification else []
        ),
    }
