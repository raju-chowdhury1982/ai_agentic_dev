from typing import List, Literal

from pydantic import BaseModel


class Risk(BaseModel):
    """Structured output schema for individual risk items."""

    risk_description: str
    is_inferred: bool
    source_reference: str
    risk_category: Literal["operational", "legal", "financial", "market"]
    risk_level: Literal["low", "medium", "high"]


class RiskAssessment(BaseModel):
    """Structured output schema for risk assessment results."""

    risks: List[Risk]
