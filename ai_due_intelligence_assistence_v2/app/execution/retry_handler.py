import time
from typing import Callable

from app.schemas.pipeline_state import PipelineState
from app.observability.logger import log_event


def execute_with_retry(  # type: ignore
    node_func: Callable,  # type: ignore
    state: PipelineState,
    retries: int = 2,
    delay: int = 3,
):
    last_error = None  # type: ignore

    for attempt in range(retries + 1):
        try:
            log_event(
                trace_id=state.trace_id or "-",  # type: ignore
                stage="RetryHandler",
                message=f"{node_func.__name__} "
                f"attempt: {attempt+1}"
            )
            return node_func(state)  # type: ignore
        except Exception as err:
            last_error = err  # type: ignore
            log_event(
                trace_id=state.trace_id or "-",  # type: ignore
                stage="RetryHandler",
                message=f"{node_func.__name__} "
                f"failed: {err}",
                level="ERROR"
            )
            # print(f"[RetryHandler] " f"Attemp {attempt+1} failed: {err}")
            time.sleep(delay)  # retry after delay sec
    state.errors.append(f"{node_func.__name__} failed after retries...")
    return state
