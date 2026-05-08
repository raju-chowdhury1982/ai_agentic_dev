from app.llm import get_chat_model
from app.prompts import business_analysis_prompt
# from langchain_core.chains import LLMChain

def build_business_analysis_chain():    # type: ignore
    model = get_chat_model(temperature=0.01)
    chain = business_analysis_prompt | model    # type: ignore
    return chain    # type: ignore

def analyze_business_info(business_info: str) -> str:
    chain = build_business_analysis_chain() # type: ignore
    result = chain.invoke({"business_info": business_info}) # type: ignore
    return result.content # type: ignore

