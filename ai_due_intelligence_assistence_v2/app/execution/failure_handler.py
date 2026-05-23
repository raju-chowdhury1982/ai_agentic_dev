from app.schemas.pipeline_state import PipelineState


def mark_pipeline_failed(
    state: PipelineState,
    reason: str,
) -> PipelineState:
    state.current_stage = "failed"
    state.errors.append(reason)
    return state
