import time
from functools import wraps

from app.observability.logger import log_event


def trace_execution_time(  # type: ignore
    stage_name: str,
):
    def decorator(func):  # type: ignore

        @wraps(func)  # type: ignore
        def wrapper(state, *args, **kwargs):  # type: ignore
            trace_id = getattr(state, "trace_id", "-")  # type: ignore
            start = time.perf_counter()

            log_event(trace_id=trace_id, stage=stage_name, message="Workflow Pipeline Execution started...")  # type: ignore

            result = func(state, *args, **kwargs)  # type: ignore

            end = time.perf_counter()
            duration = round(end - start, 3)

            if hasattr(result, "execution_metrics"):  # type: ignore
                result.execution_metrics[stage_name] = duration  # type: ignore

            log_event(trace_id=trace_id, stage=stage_name, message=f"Execution completed | duration={duration}sec")  # type: ignore
            return result  # type: ignore

        return wrapper  # type: ignore

    return decorator  # type: ignore
