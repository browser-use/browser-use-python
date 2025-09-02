#!/usr/bin/env -S rye run python

from typing import Any, Dict, Tuple
from datetime import datetime

from browser_use_sdk.lib.webhooks import (
    Webhook,
    WebhookAgentTaskStatusUpdate,
    WebhookAgentTaskStatusUpdatePayload,
    create_webhook_signature,
    verify_webhook_event_signature,
)

SECRET = "your-webhook-secret-key"


def mock_webhook_event() -> Tuple[Dict[str, Any], str, str]:
    """Mock a webhook event."""

    timestamp = datetime.fromisoformat("2023-01-01T00:00:00").isoformat()

    payload = WebhookAgentTaskStatusUpdatePayload(
        session_id="sess_123",
        task_id="task_123",
        status="started",
        metadata={"progress": 25},
    )

    signature = create_webhook_signature(
        payload=payload.model_dump(),
        timestamp=timestamp,
        secret=SECRET,
    )

    evt: Webhook = WebhookAgentTaskStatusUpdate(
        type="agent.task.status_update",
        timestamp=datetime.fromisoformat("2023-01-01T00:00:00"),
        payload=payload,
    )

    return evt.model_dump(), signature, timestamp


def main() -> None:
    """Demonstrate webhook functionality."""

    # NOTE: You'd get the evt and signature from the webhook request body and headers!
    evt, signature, timestamp = mock_webhook_event()

    verified_webhook = verify_webhook_event_signature(
        body=evt,
        expected_signature=signature,
        timestamp=timestamp,
        secret=SECRET,
    )

    if verified_webhook is None:
        print("✗ Webhook signature verification failed")
    else:
        print("✓ Webhook signature verified successfully")
        print(f"  Event type: {verified_webhook.type}")


if __name__ == "__main__":
    main()
