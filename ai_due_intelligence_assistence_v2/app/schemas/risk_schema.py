from typing import List, Literal, Optional

from pydantic import BaseModel


class Risk(BaseModel):
    """Structured output schema for individual risk items."""

    risk_description: str
    risk_source_fact: str
    risk_reasoning: str
    source_reference: Optional[str] = None
    risk_category: Literal["financial", "operational", "legal", "market", "strategic"]
    risk_level: Literal["low", "medium", "high"]
    risk_is_inferred: bool


class RiskAssessment(BaseModel):
    """Structured output schema for risk assessment results."""

    risk: List[Risk]
