# create state change detector for capture the modified fileds value in state

from typing import Any

from app.observability.logger import log_event


def detect_illegal_state_changes(
    before_state: dict[str, Any],
    after_state: dict[str, Any],
    allowed_fields: list[str],
    trace_id: str,
    stage_name: str,
):
    changed_fields: list[str] = []

    for field in after_state:
        if before_state[field] != after_state[field]:
            changed_fields.append(field)

    unauthorized_changes = [fld for fld in changed_fields if fld not in allowed_fields]

    if unauthorized_changes:
        log_event(
            trace_id=trace_id,
            stage="StateGuard",
            level="ERROR",
            message=(
                f"Unauthorized state mutation "
                f"detected in {stage_name}: "
                f"{unauthorized_changes}"
            ),
        )
        raise ValueError(f"Unauthorized state mutation: " f"{unauthorized_changes}")
