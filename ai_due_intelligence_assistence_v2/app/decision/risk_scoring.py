from app.schemas.risk_schema import RiskAssessment


def count_high_risks(risk_assessment: RiskAssessment | None) -> int:
    if not risk_assessment:
        return 0

    return sum(1 for risk in risk_assessment.risk if risk.risk_level == "high")


def count_medium_risks(risk_assessment: RiskAssessment | None) -> int:
    if not risk_assessment:
        return 0

    return sum(1 for risk in risk_assessment.risk if risk.risk_level == "medium")
