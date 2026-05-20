from langchain_core.runnables import RunnableLambda

from app.nodes.business_node import analyze_with_retry  # type: ignore
from app.nodes.business_node import business_analysis_node
from app.nodes.investment_node import investment_node
from app.nodes.risk_node import risk_assessment_node
# from app.nodes.summary_node import summary_node
from app.nodes.validation_node import validate_input_node
from app.schemas.pipeline_state import PipelineState  # type: ignore

# workflow_pipeline = (
#     RunnableLambda(lambda input_data: PipelineState(input_data=input_data))
#     | validate_input_node
#     | business_analysis_node
#     # | risk_analysis_node
#     # | investment_readiness_node
#     # | summary_node
# )


workflow_pipeline = (
    RunnableLambda(validate_input_node)
    | RunnableLambda(business_analysis_node)
    | RunnableLambda(risk_assessment_node)
    | RunnableLambda(investment_node)
)
