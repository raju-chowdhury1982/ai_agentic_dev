from app.schemas.pipeline_state import PipelineState


def merge_parallel_states(
    base_state: PipelineState, business_state: PipelineState, risk_state: PipelineState
) -> PipelineState:
    base_state.business_analysis = business_state.business_analysis
    base_state.risk_assessment = risk_state.risk_assessment

    base_state.errors.extend(business_state.errors)
    base_state.errors.extend(risk_state.errors)

    base_state.execution_metrics.update(business_state.execution_metrics)
    base_state.execution_metrics.update(risk_state.execution_metrics)

    return base_state
