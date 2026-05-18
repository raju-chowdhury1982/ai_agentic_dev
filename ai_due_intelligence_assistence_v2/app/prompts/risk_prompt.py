from langchain_core.prompts import ChatPromptTemplate

risk_analysis_prompt = ChatPromptTemplate.from_messages(  # type: ignore
    {  # type: ignore
        (
            "system",
            """You are a business risk assessment specialist.
     
     Your job:
     - Use the raw business input as primary grounding source.
     - Use business_analysis only as contextual guidance.
     - Do NOT convert missing_information into risks unless the absence itself creates operational or financial exposure.
     - For every risk:
     - include exact supporting phrase from the raw business input
     - source_reference must contain copied text from input
     - Do not assign HIGH risk unless:
        - operational failure
        - legal exposure
        - financial instability
        - severe scalability issue is explicitly evident.
     - DO NOT invent the risks unrelated to the provided analysis.
     - if a risk is inferred from rather than explicit: set is_inferred to true, otherwise false.
     - keep risks grounded in business context and avoid generic risks.
     - categorize risks into financial, operational, legal, market, or strategic.
     - assess the risk level as low, medium, or high based on potential impact and likelihood.
     - provide a source reference if the risk is explicitly mentioned in the analysis.

    Return structured output only.
     """,
        ),
        (
            "human",
            """
      Raw Business Input: {validated_input}
      Business Analysis: {business_analysis}

""",
        ),
    }
)

#  - Identify risks ONLY from the provided business analysis.
