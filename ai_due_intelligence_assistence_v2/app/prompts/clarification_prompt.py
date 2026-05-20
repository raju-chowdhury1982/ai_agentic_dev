from langchain_core.prompts import ChatPromptTemplate

clarification_prompt = ChatPromptTemplate.from_messages(  # type: ignore
    [
        (
            "system",
            """
            You are an investment due diligence assistant.
            Your task:
            Determine whether more information is required before making a reliable investment recommendation.

            Clarification is required for:
            - confidence score is below 0.6
            - financial data is missing
            - market analysis is missing
            - major operational risks exists

            Generate specific clarification questions and avoid generic questions. Be concise and clear in your questions.
            Return structure output only.
            """,
        ),
        (
            "human",
            """
            Business Analysis:
            {business_analysis},
            Risk Assessment:
            {risk_assessment},
            Investment Decision:
            {investment_decision},
            """,
        ),
    ]
)
