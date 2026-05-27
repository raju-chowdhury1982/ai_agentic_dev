from app.models.llm import get_model
from app.observability.timer import trace_execution_time
from app.prompts.risk_prompt import risk_analysis_prompt
from app.schemas.pipeline_state import PipelineState
from app.schemas.risk_schema import RiskAssessment
from app.utils.risk_payload import build_risk_payload

# risk node required to consume both validated_input: raw business facts and business_analysis: compressed interpretation


@trace_execution_time("Risk Assessment Node")
def risk_assessment_node(state: PipelineState) -> PipelineState:
    """Node function to perform risk assessment based on business analysis."""
    # state.trace_id = "hacked"
    risk_payload = build_risk_payload(state)  # type: ignore
    if state.errors:
        return state  # Skip processing if there are existing errors

    # if not state.business_analysis:
    #     state.errors.append("No business analysis available for risk assessment.")
    #     return state

    if not state.validated_input:
        state.errors.append("No business analysis available for risk assessment.")
        return state

    chat_model = get_model()
    structured_chat_model = chat_model.with_structured_output(RiskAssessment)  # type: ignore
    structured_chain = risk_analysis_prompt | structured_chat_model  # type: ignore

    # Generate risk assessment using the defined prompt and the business analysis from the state
    response = structured_chain.invoke(  # type: ignore
        {"risk_payload": risk_payload}  # type: ignore
    )  # type: ignore

    # Parse the response into the RiskAssessment schema
    state.risk_assessment = response  # type: ignore
    return state


# "business_analysis": state.business_analysis.model_dump(),
# "validated_input": state.validated_input,
