# import json
# from typing import Union
import warnings

from app.llm import get_chat_model
from app.prompts import business_analysis_prompt
from app.schema import UnifiedAnalysisOutput

warnings.filterwarnings(
    "ignore",
    message="Pydantic serializer warnings. *field_name='parsed'",
    category=UserWarning,
    module="pydantic",
)


# from langchain_core.chains import LLMChain

######################## day: 1


def build_business_analysis_chain():  # type: ignore
    model = get_chat_model(temperature=0.01)
    chain = business_analysis_prompt | model  # type: ignore
    return chain  # type: ignore


def analyze_business_info(business_info: str) -> str:
    chain = build_business_analysis_chain()  # type: ignore
    result = chain.invoke({"business_info": business_info})  # type: ignore
    return result.content  # type: ignore


######################## day: 2


def analyze_business_text_structured(business_info: str) -> UnifiedAnalysisOutput:
    model = get_chat_model(temperature=0.01)
    structured_risk_model = model.with_structured_output(UnifiedAnalysisOutput)  # type: ignore
    structured_risk_chain = business_analysis_prompt | structured_risk_model  # type: ignore
    # result = structured_chain.invoke({"business_info": business_info})  # type: ignore
    result = structured_risk_chain.invoke({"business_info": business_info})  # type: ignore
    print(f"\nRaw LLM Output:\n{result.model_dump()}\n\n")  # type: ignore Debugging line to see the raw output
    # parsed = json.loads(result)  # type: ignore
    # return BusinessAnalysis(**parsed)  # type: ignore
    # return BusinessAnalysis(result)  # type: ignore
    return result  # type: ignore


def analyze_with_retry(business_info: str, retries: int = 2) -> UnifiedAnalysisOutput:  # type: ignore
    for attempt in range(retries):
        try:
            return analyze_business_text_structured(business_info)
        # except json.JSONDecodeError:
        except Exception as err:
            print(f"Attempt {attempt + 1} failed with error: {err}")
            if attempt < retries - 1:
                continue
            else:
                raise ValueError("Failed to parse JSON after multiple attempts.")
