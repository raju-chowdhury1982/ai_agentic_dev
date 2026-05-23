from rich import print

from app.execution.executor import execute_pipeline
from app.nodes.clarification_node import clarification_node  # type: ignore
from app.pipeline.router import should_route_to_clarification  # type: ignore
from app.pipeline.workflow import workflow_pipeline  # type: ignore
from app.schemas.pipeline_state import PipelineState

# --- version 2.0 ---


sample_input = """
A mid-sized real estate developer operates in Kolkata and nearby regions.
The company sells residential flats, leases commercial units, and provides
property maintenance services. It uses offline brokers, Facebook ads, and
local newspaper campaigns for lead generation. The legal team handles land
title verification, customer agreements, RERA documentation, and litigation
tracking manually using shared folders. The finance team maintains project-wise
cash flow in Excel.
"""

# sample_input = """
# ...
# """


# def main():
#     init_state = PipelineState(raw_input=sample_input)  # type: ignore
#     working_state = workflow_pipeline.invoke(init_state)
#     if should_route_to_clarification(working_state):
#         print("\nRouting to clarification node...\n")
#         working_state.requires_clarification = True
#         working_state.current_stage = "clarification"
#         working_state = clarification_node(working_state)
#     else:
#         print("\nNo clarification needed. Proceeding to final summary...\n")
#         working_state.requires_clarification = False
#         working_state.current_stage = "completed"
#     return working_state


def main() -> PipelineState:
    initial_state = PipelineState(raw_input=sample_input)
    final_state = execute_pipeline(initial_state)  # type: ignore
    return final_state


if __name__ == "__main__":
    print("Hello from ai-due-intelligence-assistence-v2!\n\n")
    print(f"raw_input: {sample_input[:100]}\n\n")

    final_result = main()

    print(f"\n\nFinal Pipeline State: {final_result}")

    # print(f"\n\nModel Dump: {final_result.model_dump(warnings='none')}")
