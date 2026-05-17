from warnings import filterwarnings

filterwarnings(
    "ignore",
    category=UserWarning,
    module="pydantic",
    message=".*Pydantic serializer warnings.*",
)

import json

from app.models.llm import get_model
from app.nodes.validation_node import validate_input_node  # type: ignore
from app.prompts.business_prompt import business_analysis_prompt
from app.schemas.business_schema import BusinessAnalysis
from app.schemas.pipeline_state import PipelineState


def business_analysis_node(state: PipelineState) -> PipelineState:

    # Step 0: Ensure error free state to be propagated to every steps
    if state.errors:
        return state

    # Step 1: Analyze business information using LLM with validated input
    model = get_model(
        temperature=0.1,
        max_tokens=1000,
        top_p=0.9,
    )  # type: ignore
    strc_model = model.with_structured_output(BusinessAnalysis)  # type: ignore
    strc_chain = business_analysis_prompt | strc_model  # type: ignore
    raw_llm_result = strc_chain.invoke({"business_info": state.validated_input})  # type: ignore

    # Step 2: Update state with analysis result
    state.business_analysis = raw_llm_result  # type: ignore
    return state


def analyze_with_retry(business_info: str, retries: int = 2) -> BusinessAnalysis:  # type: ignore
    for attempt in range(retries):
        try:
            return business_analysis_node(business_info)  # type: ignore
        except json.JSONDecodeError as err:
            print(f"Attempt {attempt + 1} failed to decode json: {err}")
            if attempt < retries - 1:
                continue
            else:
                raise ValueError("Failed to parse JSON after multiple attempts.")
