from app.decision.materiality import has_material_missing_info
from app.decision.risk_scoring import count_high_risks  # type: ignore
from app.decision.risk_scoring import count_medium_risks  # type: ignore
from app.schemas.pipeline_state import PipelineState


def decide_recommendation(state: PipelineState) -> str:
    if not state.business_analysis:
        return "further_analysis_needed"

    if not state.investment_decision:
        return "further_analysis_needed"

    score = state.investment_decision.overall_investment_score
    confidence = state.investment_decision.overall_confidence_score

    missing_items = state.business_analysis.missing_information
    material_missing = has_material_missing_info(missing_items)

    high_risk_count = count_high_risks(state.risk_assessment)

    if high_risk_count >= 2:
        return "do_not_invest"

    if high_risk_count == 1:
        return "further_analysis_needed"

    if score > 8 and confidence >= 0.8 and not material_missing:
        return "proceed_with_caution"

    if score >= 7 and confidence >= 0.75 and not material_missing:
        return "proceed_with_caution"

    if score <= 4:
        return "further_analysis_needed"

    return "further_analysis_needed"
