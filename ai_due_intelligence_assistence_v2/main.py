from rich import print

from app.pipeline.workflow import workflow_pipeline
from app.schemas.pipeline_state import PipelineState

sample_input = """
A mid-sized real estate developer operates in Kolkata and nearby regions.
The company sells residential flats, leases commercial units, and provides
property maintenance services. It uses offline brokers, Facebook ads, and
local newspaper campaigns for lead generation. The legal team handles land
title verification, customer agreements, RERA documentation, and litigation
tracking manually using shared folders. The finance team maintains project-wise
cash flow in Excel.
"""


def main():
    init_state = PipelineState(raw_input=sample_input)  # type: ignore
    final_state = workflow_pipeline.invoke(init_state)
    return final_state


if __name__ == "__main__":
    print("Hello from ai-due-intelligence-assistence-v2!\n\n")
    print(f"raw_input: {sample_input[:100]}\n\n")

    final_result = main()

    print(f"\n\nFinal Pipeline State: {final_result}")

    # print(f"\n\nModel Dump: {final_result.model_dump(warnings='none')}")
