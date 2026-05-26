from langchain_core.prompts import ChatPromptTemplate

summary_prompt: ChatPromptTemplate = ChatPromptTemplate.from_messages(  # type: ignore
    [
        (
            "system",
            """
            You are a senior investment due diligence analyst.
            Create a concise, client-ready final decision report.
            Use ONLY the provided:
            - business_analysis
            - risk_assessment
            - investment_decision
            - clarification_questions

            DO NOT invent facts AND avoid generalized response
            Return structured output only.
            """,
        ),
        (
            "human",
            """
            Business Analysis: {business_analysis}
            Risk Assessment: {risk_assessment}
            Investment Decision: {investment_decision}
            Clarification Questions: {clarification_questions}
            """,
        ),
    ]
)
