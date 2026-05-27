from typing import Any

from app.schemas.pipeline_state import PipelineState


# building compact risk schema to reduce latency in risk assessment node
def build_risk_payload(state: PipelineState) -> dict[str, Any]:
    text = state.validated_input or ""

    return {
        "business_input": text,
        "risk_focus_areas": [
            "manual processes",
            "legal/compliance handling",
            "financial tracking",
            "marketing/lead generation",
            "scalability constraints",
        ],
    }
