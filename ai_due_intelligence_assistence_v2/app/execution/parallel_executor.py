from concurrent.futures import ThreadPoolExecutor

from app.execution.governed_executor import execute_governed_node
from app.governance.state_merger import merge_parallel_states
from app.nodes.business_node import business_analysis_node
from app.nodes.risk_node import risk_assessment_node
from app.schemas.pipeline_state import PipelineState


def execute_business_and_risk_parallel(
    state: PipelineState,
) -> PipelineState:
    business_state = PipelineState(**state.model_dump())
    risk_state = PipelineState(**state.model_dump())

    with ThreadPoolExecutor(max_workers=2) as executor:
        business_future = executor.submit(
            execute_governed_node,
            business_analysis_node,
            business_state,
            ["business_analysis", "errors", "execution_metrics"],
            "Business Analysis Node",
        )

        risk_future = executor.submit(
            execute_governed_node,
            risk_assessment_node,
            risk_state,
            ["risk_assessment", "errors", "execution_metrics"],
            "Risk Assessment Node",
        )

        completed_business_state = business_future.result()
        completed_risk_state = risk_future.result()

        return merge_parallel_states(
            base_state=state,
            business_state=completed_business_state,
            risk_state=completed_risk_state,
        )
