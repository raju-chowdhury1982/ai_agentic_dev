from rich import print

from app.execution.executor import execute_pipeline
from app.nodes.clarification_node import clarification_node  # type: ignore
from app.observability.tracer import generate_trace_id
from app.pipeline.router import should_route_to_clarification  # type: ignore
from app.pipeline.workflow import workflow_pipeline  # type: ignore
from app.schemas.pipeline_state import PipelineState

# --- version 2.0 ---

# test-case: 0 or default
sample_input = """
A mid-sized real estate developer operates in Kolkata and nearby regions.
The company sells residential flats, leases commercial units, and provides
property maintenance services.
It uses offline brokers, Facebook ads, and
local newspaper campaigns for lead generation.
The legal team handles land title verification, customer agreements, RERA documentation, and litigation
tracking manually using shared folders.
The finance team maintains project-wise cash flow in Excel.
"""

# test-case: 1
weak_input = """
A mid-sized real estate developer operates in Kolkata and nearby regions.
The company sells residential flats, leases commercial units, and provides
property maintenance services.
It uses offline brokers, Facebook ads, and
local newspaper campaigns for lead generation.
The legal team handles land title verification, customer agreements, RERA documentation, and litigation
tracking manually using shared folders.
The finance team maintains project-wise cash flow in Excel.
"""

# test-case: 2
rich_input = """
A real estate developer based in Kolkata operates across residential,
commercial, and maintenance services.

The company generated INR 145 crore revenue in FY2025 with a
net profit margin of 18 percent and year-over-year growth of 14 percent.
Its primary customers are upper-middle-income families and small
commercial retailers in Eastern India.

The company operates through digital marketing campaigns,
broker partnerships, SEO-driven lead generation, and CRM-based
sales tracking systems.

The legal department uses a centralized document management platform
for land verification, litigation tracking, and RERA compliance.

The finance team uses SAP for project-wise budgeting,
cash flow forecasting, and audit management.

The company currently holds 11 active residential projects and
2 commercial projects with occupancy rates above 87 percent.

Major competitors include regional developers operating in
Kolkata and Bhubaneswar markets.
"""


# test-case: 3
high_risk_input = """
A real estate developer operates in Kolkata and nearby regions,
focusing on residential and commercial projects.

The company generated INR 110 crore revenue in FY2025,
but operating cash flow declined by 28 percent over the last year.

The company currently faces multiple unresolved land disputes
and ongoing litigation related to project delivery delays.

Several projects are under regulatory review due to delayed
RERA compliance submissions.

The finance team reported increasing debt obligations and
difficulty maintaining vendor payments.

Customer complaints regarding delayed handovers have increased
during the last two quarters.

The company uses Excel-based financial tracking and
manual legal document workflows.

Lead generation depends heavily on brokers and local advertising channels.         
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

TEST_CASE = "rich"
SAMPLES = {"weak": weak_input, "rich": rich_input, "high": high_risk_input}

sample_input = SAMPLES[TEST_CASE]


def main() -> PipelineState:
    initial_state = PipelineState(raw_input=sample_input, trace_id=generate_trace_id())
    final_state = execute_pipeline(initial_state)  # type: ignore
    return final_state


if __name__ == "__main__":
    print("Hello from ai-due-intelligence-assistence-v2!\n\n")
    print(f"raw_input: {sample_input[:250]}\n\n")

    final_result = main()

    print(f"\n\nFinal Pipeline State: {final_result}")
    if final_result.final_report:
        print("\nFinal Client Report: ")
        print(final_result.final_report.model_dump())  # type: ignore
    else:
        print("\nPipeline Failed:")
        print(final_result.errors)

    print("\nExecution_metrics:")
    print(final_result.execution_metrics)

    # print(f"\n\nModel Dump: {final_result.model_dump(warnings='none')}")
