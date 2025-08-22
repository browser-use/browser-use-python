"""Tests for webhook functionality."""

from __future__ import annotations

from typing import Any, Dict
from datetime import datetime, timezone

from browser_use_sdk.lib.webhooks import (
    WebhookTest,
    WebhookTestPayload,
    WebhookAgentTaskStatusUpdate,
    WebhookAgentTaskStatusUpdatePayload,
    create_webhook_signature,
    verify_webhook_event_signature,
)


def test_create_webhook_signature() -> None:
    """Test webhook signature creation."""
    secret = "test-secret-key"
    timestamp = "2023-01-01T00:00:00Z"
    payload = {"test": "ok"}

    signature = create_webhook_signature(payload, timestamp, secret)

    # Signature should be a hex string
    assert isinstance(signature, str)
    assert len(signature) == 64  # SHA256 hex length

    # Same inputs should produce same signature
    signature2 = create_webhook_signature(payload, timestamp, secret)
    assert signature == signature2

    # Different payload should produce different signature
    different_payload = {"test": "different"}
    different_signature = create_webhook_signature(different_payload, timestamp, secret)
    assert signature != different_signature


def test_verify_webhook_event_signature_valid() -> None:
    """Test webhook signature verification with valid signature."""
    secret = "test-secret-key"
    timestamp = "2023-01-01T00:00:00Z"

    # Create test webhook
    payload = WebhookTestPayload(test="ok")
    webhook = WebhookTest(type="test", timestamp=datetime.now(timezone.utc), payload=payload)

    # Create signature
    signature = create_webhook_signature(webhook.payload.model_dump(), timestamp, secret)

    # Verify signature
    verified_webhook = verify_webhook_event_signature(
        body=webhook.model_dump(), secret=secret, signature=signature, timestamp=timestamp
    )

    assert verified_webhook is not None
    assert isinstance(verified_webhook, WebhookTest)
    assert verified_webhook.payload.test == "ok"


def test_verify_webhook_event_signature_invalid_signature() -> None:
    """Test webhook signature verification with invalid signature."""
    secret = "test-secret-key"
    timestamp = "2023-01-01T00:00:00Z"

    # Create test webhook
    payload = WebhookTestPayload(test="ok")
    webhook = WebhookTest(type="test", timestamp=datetime.now(timezone.utc), payload=payload)

    # Use invalid signature
    invalid_signature = "invalid_signature_123"

    verified_webhook = verify_webhook_event_signature(
        body=webhook.model_dump(), secret=secret, signature=invalid_signature, timestamp=timestamp
    )

    assert verified_webhook is None


def test_verify_webhook_event_signature_wrong_secret() -> None:
    """Test webhook signature verification with wrong secret."""
    secret = "test-secret-key"
    wrong_secret = "wrong-secret-key"
    timestamp = "2023-01-01T00:00:00Z"

    # Create test webhook
    payload = WebhookTestPayload(test="ok")
    webhook = WebhookTest(type="test", timestamp=datetime.now(timezone.utc), payload=payload)

    # Create signature with correct secret
    signature = create_webhook_signature(webhook.payload.model_dump(), timestamp, secret)

    # Verify with wrong secret
    verified_webhook = verify_webhook_event_signature(
        body=webhook.model_dump(), secret=wrong_secret, signature=signature, timestamp=timestamp
    )

    assert verified_webhook is None


def test_verify_webhook_event_signature_agent_task_status_update() -> None:
    """Test webhook signature verification for agent task status update."""
    secret = "test-secret-key"
    timestamp = "2023-01-01T00:00:00Z"

    # Create agent task status update webhook
    payload = WebhookAgentTaskStatusUpdatePayload(
        session_id="sess_123", task_id="task_456", status="started", metadata={"progress": 25}
    )

    webhook = WebhookAgentTaskStatusUpdate(
        type="agent.task.status_update", timestamp=datetime.now(timezone.utc), payload=payload
    )

    # Create signature
    signature = create_webhook_signature(webhook.payload.model_dump(), timestamp, secret)

    # Verify signature
    verified_webhook = verify_webhook_event_signature(
        body=webhook.model_dump(), secret=secret, signature=signature, timestamp=timestamp
    )

    assert verified_webhook is not None
    assert isinstance(verified_webhook, WebhookAgentTaskStatusUpdate)
    assert verified_webhook.payload.session_id == "sess_123"
    assert verified_webhook.payload.status == "started"
    assert verified_webhook.payload.metadata is not None
    assert verified_webhook.payload.metadata["progress"] == 25


def test_verify_webhook_event_signature_string_body() -> None:
    """Test webhook signature verification with string body."""
    secret = "test-secret-key"
    timestamp = "2023-01-01T00:00:00Z"

    # Create test webhook
    payload = WebhookTestPayload(test="ok")
    webhook = WebhookTest(type="test", timestamp=datetime.now(timezone.utc), payload=payload)

    # Create signature
    signature = create_webhook_signature(webhook.payload.model_dump(), timestamp, secret)

    # Verify with string body
    verified_webhook = verify_webhook_event_signature(
        body=webhook.model_dump(), secret=secret, signature=signature, timestamp=timestamp
    )

    assert verified_webhook is not None
    assert isinstance(verified_webhook, WebhookTest)


def test_verify_webhook_event_signature_invalid_body() -> None:
    """Test webhook signature verification with invalid body."""
    secret = "test-secret-key"
    timestamp = "2023-01-01T00:00:00Z"

    # Invalid webhook data
    invalid_body: Dict[str, Any] = {"type": "invalid_type", "timestamp": "invalid", "payload": {}}

    verified_webhook = verify_webhook_event_signature(
        body=invalid_body, secret=secret, signature="some_signature", timestamp=timestamp
    )

    assert verified_webhook is None
