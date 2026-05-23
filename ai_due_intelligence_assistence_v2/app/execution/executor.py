from app.execution.failure_handler import mark_pipeline_failed
from app.execution.retry_handler import execute_with_retry  # type: ignore
from app.nodes.business_node import business_analysis_node
from app.nodes.clarification_node import clarification_node
from app.nodes.investment_node import investment_node
from app.nodes.risk_node import risk_assessment_node
from app.nodes.validation_node import validate_input_node
from app.pipeline.router import should_route_to_clarification
from app.schemas.pipeline_state import PipelineState


def execute_pipeline(initial_state: PipelineState) -> PipelineState:

    state = initial_state

    # --- Validation ---
    state = execute_with_retry(validate_input_node, state)  # type: ignore

    if state.errors:  # type: ignore
        return mark_pipeline_failed(state, "Validation Failed")  # type: ignore

    # --- Business analysis ---
    state = execute_with_retry(  # type: ignore
        business_analysis_node, state  # type: ignore
    )

    if state.errors:  # type: ignore
        return mark_pipeline_failed(
            state, "Business Analysis Node failed"  # type: ignore
        )

    # --- Risk ---
    state = execute_with_retry(  # type: ignore
        risk_assessment_node, state  # type: ignore
    )

    if state.errors:  # type: ignore
        return mark_pipeline_failed(
            state, "Risk Assessment node failed"  # type: ignore
        )

    # --- Investment ---

    state = execute_with_retry(  # type: ignore
        investment_node, state  # type: ignore
    )

    if state.errors:  # type: ignore
        return mark_pipeline_failed(state, "Investment Node failed")  # type: ignore

    # --- Routing ---
    if should_route_to_clarification(state):  # type: ignore
        state.requires_clarification = True
        state.current_stage = "clarification"
        state = execute_with_retry(clarification_node, state)  # type: ignore
    else:
        state.requires_clarification = False
        state.current_stage = "completed"

    return state  # type: ignore
