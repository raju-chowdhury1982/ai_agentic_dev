from datetime import datetime


def log_event(trace_id: str, stage: str, message: str, level: str = "INFO"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(
        f"timestamp: {timestamp} "
        f"level: {level} "
        f"trace: <{trace_id}> "
        f"stage:{stage} "
        f"log_message:{message}"
    )
