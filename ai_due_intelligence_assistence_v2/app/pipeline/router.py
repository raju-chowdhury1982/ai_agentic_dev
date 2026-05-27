from app.observability.logger import log_event
from app.schemas.pipeline_state import PipelineState

CRITICAL_MISSING_TERMS: list[str] = [
    "financial data",
    "financial performance data",
    "market data",
    "competitor analysis",
    "customer demographics",
]


def has_ciritical_missing_info(state: PipelineState) -> bool:
    """check input text to find out any critical missing"""
    if not state.business_analysis:
        return False

    missing_items = [
        item.lower() for item in state.business_analysis.missing_information
    ]

    return any(
        critical_term == item
        for item in missing_items
        for critical_term in CRITICAL_MISSING_TERMS
    )


def has_high_risk(state: PipelineState) -> bool:
    """Find risk levels"""
    if not state.risk_assessment:
        return False

    return any(risk.risk_level == "high" for risk in state.risk_assessment.risk)


def should_route_to_clarification(state: PipelineState) -> bool:
    """Determines if the pipeline should route to the clarification node."""

    trace_id = state.trace_id or "-"

    if not state.investment_decision:
        log_event(
            trace_id=trace_id,
            stage="Router",
            message="No Investment decision found; skipping clarification route",
            level="WARNING",
        )
        return False

    confidence = state.investment_decision.overall_confidence_score
    critical_missing = has_ciritical_missing_info(state)
    high_risk = has_high_risk(state)
    recommendation = state.investment_decision.recommendation

    # PRIMARY ROUTING AUTHORITY = FINAL INVESTMENT RECOMMENDATION
    if recommendation == "do_not_invest":
        log_event(
            trace_id=trace_id,
            stage="Router",
            message="Routing to clarification | reason=do_not_invest",
        )
        return True

    if recommendation == "further_analysis_needed":
        log_event(
            trace_id=trace_id,
            stage="Router",
            message="Routing to clarification | reason=further_analysis_needed",
        )
        return True

    # PROCEEDABLE BUSINESS CASES
    if recommendation in ["invest", "proceed_with_caution"]:
        log_event(
            trace_id=trace_id,
            stage="Router",
            message="Routing to clarification | reason=sufficient_information",
        )
        return False

    # SAFETY FALLBACKS
    if confidence < 0.5:
        log_event(
            trace_id=trace_id,
            stage="Router",
            message="Routing to clarification | reason=low_confidence",
        )
        return True

    if (
        critical_missing
        and state.investment_decision.recommendation == "further_analysis_needed"
    ):
        log_event(
            trace_id=trace_id,
            stage="Router",
            message="Routing to clarification | reason=critical_missing_information",
        )
        return True

    if high_risk:
        log_event(
            trace_id=trace_id,
            stage="Router",
            message="Routing to clarification | reason=high_risk_detected",
        )
        return True

    # DEFAULT SAFE PATH
    log_event(
        trace_id=trace_id,
        stage="Router",
        message="Skipping clarification | reason=sufficient_information",
    )
    return False

    # # If there are errors, we can skip clarification
    # if state.errors:
    #     return False

    # decision = state.investment_decision
    # analysis = state.business_analysis

    # # for low confidence scores, we want to route to clarification
    # if decision and decision.overall_confidence_score < 0.5:
    #     log_event(
    #         trace_id=state.trace_id or "-",
    #         stage="Router",
    #         message="Routing to clarification",
    #     )
    #     return True

    # if analysis:
    #     missing = [item.lower() for item in analysis.missing_information]
    #     critical_missing = [
    #         "financial data",
    #         "market data",
    #         "financial performance data",
    #         "market competition analysis",
    #     ]
    #     if any(item in missing for item in critical_missing):
    #         log_event(
    #             trace_id=state.trace_id or "-",
    #             stage="Router",
    #             message="Routing to clarification",
    #         )
    #         return True

    # # Explicit recommendation for further analysis should route to clarification
    # # If the overall recommendation is "further_analysis_needed", we may want to route to clarification
    # if decision and decision.recommendation == "further_analysis_needed":
    #     log_event(
    #         trace_id=state.trace_id or "-",
    #         stage="Router",
    #         message="Routing to clarification",
    #     )
    #     return True
    # log_event(
    #     trace_id=state.trace_id or "-",
    #     stage="Router",
    #     message="Workflow Pipeline Completed!!!",
    # )
    # return False
