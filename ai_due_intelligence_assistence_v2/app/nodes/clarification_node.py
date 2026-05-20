from app.models.llm import get_model
from app.prompts.clarification_prompt import clarification_prompt
from app.schemas.clarification_schema import ClarificationQuestions
from app.schemas.pipeline_state import PipelineState


def clarification_node(state: PipelineState) -> PipelineState:
    """Node to determine if clarification is needed and generate specific questions."""
    if state.errors:
        # If there are errors, we can skip clarification and return the state as is
        return state

    if not state.investment_decision:
        # If there is no investment decision, we can skip clarification and return the state as is
        return state

    llm = get_model(temperature=0.1)
    structured_llm = llm.with_structured_output(ClarificationQuestions)  # type: ignore

    clarification_chain = clarification_prompt | structured_llm  # type: ignore

    response = clarification_chain.invoke(
        {  # type: ignore
            "business_analysis": state.business_analysis.model_dump(),  # type: ignore
            "risk_assessment": state.risk_assessment.model_dump(),  # type: ignore
            "investment_decision": state.investment_decision.model_dump(),
        }
    )

    state.clarification_questions = response  # type: ignore
    # Assuming the response is in a structured format that can be directly parsed
    return state
