from langchain_core.prompts import ChatPromptTemplate

# from app.schema import BusinessAnalysis

######################## day: 1

# business_analysis_prompt = ChatPromptTemplate.from_messages(  # type: ignore
#     [
#         (
#             "system",
#             """You are a helpful assistant for business due diligence analyst.
#      Your job:
#      1. Identify the business model.
#      2. Extract the revenue streams.
#      3. Identify the operational risks.
#      4. Identify legal/compliane risks.
#      5. Identify missing informations.
#      6. Give a final investment-readiness score from 1 to 10.

#      Rule:
#      - Do not invents any fact.
#      - If any information is missing, just say "No information found in given data".)
#      - Be concise, specific and use acute profesional tune and nature.
#     """,
#         ),
#         (
#             "human",
#             "Analyze the following business information and descriptions:{business_info}",
#         ),
#     ]
# )


######################## day: 2

business_analysis_prompt = ChatPromptTemplate.from_messages(  # type: ignore
    [
        (
            "system",
            """You are a helpfull assistant for business due intelligence analyst.
                  Your job:
     1. Identify the business model.
     2. Extract the revenue streams.
     3. Identify the operational risks.
     4. Identify legal/compliane risks.
     5. Identify missing informations.
     6. Give a final investment-readiness score from 1 to 10.
     7. Return confidence score between 0 and 1 based ONLY on input completeness.
     8. If financial AND market data missing → confidence_score MUST be ≤ 0.4
     9. If not explicitly mentioned → mark as inferred = true else false.
     10. Provide reason for confidence score.
     11. source_reference must be EXACT substring from input (copy-paste) if any risk is identified, else "No information found in given data".
     12. Return a JSON object matching the UnifiedAnalysisOutput schema.
     
     Rule:
     - Do not invents any fact.
     - If any information is missing, just say "No information found in given data".)
     - Be concise, specific and use acute profesional tune and nature.

     Critical Rule:
     Only extract information EXPLICITLY present in the input text.
     if any field is not clearly mentioned:
     -> return "Not Available"
     - DO NOT infer from general knowledge or assumptions.
     - DO NOT assume industry patterns.
     - DO NOT complete missing information.

    Think step by step internally, but output only JSON.
    """,
        ),
        (
            "human",
            "Analyze the following business information and descriptions:{business_info}",
        ),
    ]
)
