from typing import Callable

from app.execution.retry_handler import execute_with_retry  # type: ignore
from app.governance.state_guard import detect_illegal_state_changes
from app.governance.state_snapshot import create_state_snapshot  # type: ignore
from app.schemas.pipeline_state import PipelineState


def execute_governed_node(
    node_func: Callable[[PipelineState], PipelineState],
    state: PipelineState,
    allowed_fields: list[str],
    stage_name: str,
) -> PipelineState:
    before_state = create_state_snapshot(state)
    try:
        working_state = execute_with_retry(node_func, state)  # type: ignore
        after_state = create_state_snapshot(working_state)  # type: ignore
        detect_illegal_state_changes(
            before_state=before_state,
            after_state=after_state,  # type: ignore
            allowed_fields=allowed_fields,
            trace_id=before_state.get("trace_id", "-"),  # type: ignore
            stage_name=stage_name,
        )
        return working_state  # type: ignore
    except ValueError as err:
        restore_state = PipelineState(**before_state)
        restore_state.current_stage = "failed"
        restore_state.errors.append(str(err))  # type: ignore
        restore_state.errors.append(f"{stage_name} failed")
        return restore_state  # type: ignore
