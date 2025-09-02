import hashlib
import hmac
import json
from datetime import datetime
from typing import Any, Dict, Literal, Optional, Union

from pydantic import BaseModel

# https://docs.browser-use.com/cloud/webhooks

# Models ---------------------------------------------------------------------

# test


class WebhookTestPayload(BaseModel):
    """Test webhook payload."""

    test: Literal["ok"]


class WebhookTest(BaseModel):
    """Test webhook event."""

    type: Literal["test"]
    timestamp: datetime
    payload: WebhookTestPayload


# agent.task.status_update


class WebhookAgentTaskStatusUpdatePayload(BaseModel):
    """Agent task status update webhook payload."""

    session_id: str
    task_id: str
    status: Literal["initializing", "started", "paused", "stopped", "finished"]
    metadata: Optional[Dict[str, Any]] = None


class WebhookAgentTaskStatusUpdate(BaseModel):
    """Agent task status update webhook event."""

    type: Literal["agent.task.status_update"]
    timestamp: datetime
    payload: WebhookAgentTaskStatusUpdatePayload


# Union of all webhook types
Webhook = Union[WebhookTest, WebhookAgentTaskStatusUpdate]

# Methods --------------------------------------------------------------------


def create_webhook_signature(payload: Any, timestamp: str, secret: str) -> str:
    """
    Creates a webhook signature for the given payload, timestamp, and secret.

    Args:
        payload: The webhook payload to sign
        timestamp: The timestamp string
        secret: The secret key for signing

    Returns:
        The HMAC-SHA256 signature as a hex string
    """

    dump = json.dumps(payload, separators=(",", ":"), sort_keys=True)
    message = f"{timestamp}.{dump}"

    # Create HMAC-SHA256 signature
    hmac_obj = hmac.new(secret.encode(), message.encode(), hashlib.sha256)
    signature = hmac_obj.hexdigest()

    return signature


def verify_webhook_event_signature(
    body: Union[Dict[str, Any], str],
    expected_signature: str,
    timestamp: str,
    #
    secret: str,
) -> Union["Webhook", None]:
    """
    Utility function that validates the received webhook event signature.

    Args:
        body: Dictionary containing 'body', 'signature', and 'timestamp'
        signature: The signature of the webhook event
        timestamp: The timestamp of the webhook event
        secret: The secret key for signing

    Returns:
        None if the signature is invalid, otherwise the parsed webhook event.
    """
    try:
        if isinstance(body, str):
            json_data = json.loads(body)
        else:
            json_data = body

        # PARSE

        webhook_event: Optional[Webhook] = None

        if webhook_event is None:
            try:
                webhook_event = WebhookTest(**json_data)
            except Exception:
                pass

        # Try agent task status update webhook
        if webhook_event is None:
            try:
                webhook_event = WebhookAgentTaskStatusUpdate(**json_data)
            except Exception:
                pass

        if webhook_event is None:
            return None

        # Verify

        calculated_signature = create_webhook_signature(
            payload=webhook_event.payload.model_dump(), timestamp=timestamp, secret=secret
        )

        if not hmac.compare_digest(expected_signature, calculated_signature):
            return None

        return webhook_event

    except Exception:
        return None
