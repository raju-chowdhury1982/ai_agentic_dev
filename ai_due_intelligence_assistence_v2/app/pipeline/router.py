from app.schemas.pipeline_state import PipelineState
from app.observability.logger import log_event


def should_route_to_clarification(state: PipelineState) -> bool:
    """Determines if the pipeline should route to the clarification node."""
    # If there are errors, we can skip clarification
    if state.errors:
        return False

    decision = state.investment_decision
    analysis = state.business_analysis

    # for low confidence scores, we want to route to clarification
    if decision and decision.overall_confidence_score < 0.5:
        log_event(
            trace_id=state.trace_id or "-",
            stage="Router",
            message="Routing to clarification"
        )
        return True

    if analysis:
        missing = [item.lower() for item in analysis.missing_information]
        critical_missing = [
            "financial data",
            "market data",
            "financial performance data",
            "market competition analysis",
        ]
        if any(item in missing for item in critical_missing):
            log_event(
            trace_id=state.trace_id or "-",
            stage="Router",
            message="Routing to clarification"
        )
            return True

    # Explicit recommendation for further analysis should route to clarification
    # If the overall recommendation is "further_analysis_needed", we may want to route to clarification
    if decision and decision.recommendation == "further_analysis_needed":
        log_event(
            trace_id=state.trace_id or "-",
            stage="Router",
            message="Routing to clarification"
        )
        return True
    log_event(
            trace_id=state.trace_id or "-",
            stage="Router",
            message="Workflow Pipeline Completed!!!"
        )
    return False
