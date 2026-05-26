from app.observability.timer import trace_execution_time
from app.schemas.pipeline_state import PipelineState


@trace_execution_time("Input Validation Node")
def validate_input_node(state: PipelineState) -> PipelineState:
    text = state.raw_input.strip()

    if len(text.split()) < 15:
        state.errors.append(
            "Insufficient business information. Please provide more details."
        )
        return state
    state.validated_input = text
    print(f"[Validation_Node] Validated Input: {state.validated_input[:200]}...\n")
    return state
