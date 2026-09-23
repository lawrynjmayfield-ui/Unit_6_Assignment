import json
from datetime import datetime, timezone

def lambda_handler(event, context):

    # Receive prediction results from the ML workflow
    current_cpu = float(event.get("current_cpu", 0))
    probability = float(event.get("high_cpu_probability", 0))

    # AI-driven automation decision
    if probability >= 0.70:
        status = "HIGH CPU RISK"
        action = "PREVENTIVE MAINTENANCE ALERT"
        message = (
            f"AI model predicts high CPU utilization. "
            f"Current CPU is {current_cpu:.1f}% and "
            f"predicted high-CPU probability is {probability:.1%}. "
            f"Administrator review recommended."
        )
    else:
        status = "NORMAL"
        action = "CONTINUE MONITORING"
        message = (
            f"No preventive action required. "
            f"Current CPU is {current_cpu:.1f}% and "
            f"predicted high-CPU probability is {probability:.1%}."
        )

    result = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "status": status,
        "action": action,
        "message": message
    }

    print(json.dumps(result))

    return {
        "statusCode": 200,
        "body": json.dumps(result)
    }
