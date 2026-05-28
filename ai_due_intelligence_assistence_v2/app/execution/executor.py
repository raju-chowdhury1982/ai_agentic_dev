from app.decision.decision_engine import decide_recommendation
from app.execution.failure_handler import mark_pipeline_failed  # type: ignore
from app.execution.governed_executor import execute_governed_node
from app.execution.parallel_executor import execute_business_and_risk_parallel
# from app.governance.state_guard import detect_illegal_state_changes
from app.governance.state_snapshot import create_state_snapshot  # type: ignore
# from app.nodes.business_node import business_analysis_node
from app.nodes.clarification_node import clarification_node
from app.nodes.investment_node import investment_node
# from app.nodes.risk_node import risk_assessment_node
from app.nodes.summary_node import summary_node
from app.nodes.validation_node import validate_input_node
from app.pipeline.router import should_route_to_clarification
from app.schemas.pipeline_state import PipelineState


def execute_pipeline(initial_state: PipelineState) -> PipelineState:

    state = initial_state

    # --- Validation ---
    # state = execute_with_retry(validate_input_node, state)  # type: ignore
    state = execute_governed_node(
        node_func=validate_input_node,
        state=state,
        allowed_fields=[
            "validated_input",
            "execution_metrics",
            "error",
            "current_stage",
        ],
        stage_name="Validation Node",
    )

    # if state.errors:  # type: ignore
    #     return mark_pipeline_failed(state, "Validation Failed")  # type: ignore
    # --------------------------------------------------------------------
    # # --- Business analysis ---
    # # state = execute_with_retry(business_analysis_node, state)
    # state = execute_governed_node(
    #     node_func=business_analysis_node,
    #     state=state,
    #     allowed_fields=[
    #         "business_analysis",
    #         "execution_metrics",
    #         "error",
    #     ],
    #     stage_name="Business Analysis Node",
    # )

    # # if state.errors:  # type: ignore
    # #     return mark_pipeline_failed(state, "Business Analysis Node failed")

    # # --- Risk ---
    # # state = execute_with_retry(risk_assessment_node, state)
    # state = execute_governed_node(
    #     node_func=risk_assessment_node,
    #     state=state,
    #     allowed_fields=["risk_assessment", "execution_metrics", "error"],
    #     stage_name="Risk Assessment Node",
    # )

    # # if state.errors:  # type: ignore
    # #     return mark_pipeline_failed(state, "Risk Assessment node failed")
    # --------------------------------------------------------------------
    # parallel business and risk node execution
    state = execute_business_and_risk_parallel(state)

    if state.errors:
        return mark_pipeline_failed(state, "Parallel business/risk Execution Failed")

    # --- Investment ---
    # state = execute_with_retry(investment_node, state)
    state = execute_governed_node(
        node_func=investment_node,
        state=state,
        allowed_fields=["investment_decision", "execution_metrics", "error"],
        stage_name="Investment Node",
    )

    # if state.errors:  # type: ignore
    #     return mark_pipeline_failed(state, "Investment Node failed")  # type: ignore
    # --- DECISION ENGINE ---
    if state.investment_decision:
        state.investment_decision.recommendation = decide_recommendation(state)  # type: ignore

    # --- Routing ---
    if should_route_to_clarification(state):  # type: ignore
        state.requires_clarification = True
        state.current_stage = "clarification"
        state = execute_governed_node(
            node_func=clarification_node,
            state=state,
            allowed_fields=["clarification_questions", "execution_metrics", "errors"],
            stage_name="Clarification Node",
        )  # type: ignore
    else:
        state.requires_clarification = False
        state.current_stage = "completed"

    # --- Final summary ---
    state = execute_governed_node(
        node_func=summary_node,
        state=state,
        allowed_fields=["final_report", "execution_metrics", "errors"],
        stage_name="Final Summary Node",
    )

    return state  # type: ignore
