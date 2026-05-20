from typing import List

from pydantic import BaseModel


class ClarificationQuestions(BaseModel):
    """Schema for a list of clarification questions."""

    clarification_needed: bool
    clarification_reasons: List[str]

    clarification_questions: List[str]
