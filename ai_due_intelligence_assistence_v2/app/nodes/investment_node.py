from app.models.llm import get_model
from app.prompts.investment_prompt import investment_prompt
from app.schemas.investment_schema import InvestmentDecision
from app.schemas.pipeline_state import PipelineState
from app.observability.timer import trace_execution_time


@trace_execution_time("Investment Node")
def investment_node(state: PipelineState) -> PipelineState:
    if state.errors:
        return state

    if not state.business_analysis:
        state.errors.append("Business Analysis is missing")
        return state

    if not state.risk_assessment:
        state.errors.append("Risk Assessment is missing")
        return state

    model = get_model(temperature=0.0)
    structured_model = model.with_structured_output(InvestmentDecision)  # type: ignore

    structured_investment_chain = investment_prompt | structured_model  # type: ignore

    response = structured_investment_chain.invoke(  # type: ignore
        {
            "business_analysis": state.business_analysis.model_dump(),
            "risk_assessment": state.risk_assessment.model_dump(),
        }
    )

    state.investment_decision = response  # type: ignore
    return state
