from app.models.llm import get_model
from app.observability.timer import trace_execution_time
from app.prompts.summary_prompt import summary_prompt
from app.schemas.final_report_schema import FinalDecisionReport
from app.schemas.pipeline_state import PipelineState
from app.utils.summary_payload import build_summary_payload

# payload = build_summary_payload(state)  # type: ignore


@trace_execution_time("Final Summary Node")
def summary_node(state: PipelineState) -> PipelineState:
    payload = build_summary_payload(state)  # type: ignore

    if state.errors:
        return state

    if not state.business_analysis:
        state.errors.append("Business analysis missing")
        return state

    if not state.risk_assessment:
        state.errors.append("Risk assessment missing")
        return state

    if not state.investment_decision:
        state.errors.append("Investment decision missing")
        return state

    model = get_model(temperature=0.0)
    structured_model = model.with_structured_output(FinalDecisionReport)  # type: ignore
    chain = summary_prompt | structured_model  # type: ignore

    result = chain.invoke({"summary_payload": payload})  # type: ignore

    state.final_report = result  # type: ignore
    return state


# "business_analysis": state.business_analysis.model_dump(),
# "risk_assessment": state.risk_assessment.model_dump(),
# "investment_decision": state.investment_decision.model_dump(),
# "clarification_questions": (
#     state.clarification_questions.model_dump()
#     if state.clarification_questions
#     else None
# ),
