"""Tests for webhook functionality."""

from __future__ import annotations

from typing import Any, Dict
from datetime import datetime, timezone

import pytest

from browser_use_sdk._compat import PYDANTIC_V2
from browser_use_sdk.lib.webhooks import (
    WebhookTest,
    WebhookTestPayload,
    create_webhook_signature,
    verify_webhook_event_signature,
)

# Signature Creation ---------------------------------------------------------


@pytest.mark.skipif(not PYDANTIC_V2, reason="Webhook tests only run in Pydantic V2")
def test_create_webhook_signature() -> None:
    """Test webhook signature creation."""
    secret = "test-secret-key"
    timestamp = "2023-01-01T00:00:00Z"
    payload = {"test": "ok"}

    signature = create_webhook_signature(payload, timestamp, secret)

    assert isinstance(signature, str)
    assert len(signature) == 64

    signature2 = create_webhook_signature(payload, timestamp, secret)
    assert signature == signature2

    different_payload = {"test": "different"}
    different_signature = create_webhook_signature(different_payload, timestamp, secret)

    assert signature != different_signature


# Webhook Verification --------------------------------------------------------


@pytest.mark.skipif(not PYDANTIC_V2, reason="Webhook tests only run in Pydantic V2")
def test_verify_webhook_event_signature_valid() -> None:
    """Test webhook signature verification with valid signature."""
    secret = "test-secret-key"
    timestamp = "2023-01-01T00:00:00Z"

    payload = WebhookTestPayload(test="ok")
    webhook = WebhookTest(type="test", timestamp=datetime.now(timezone.utc), payload=payload)
    signature = create_webhook_signature(webhook.payload.model_dump(), timestamp, secret)

    # Verify signature
    verified_webhook = verify_webhook_event_signature(
        body=webhook.model_dump(),
        secret=secret,
        timestamp=timestamp,
        expected_signature=signature,
    )

    assert verified_webhook is not None
    assert isinstance(verified_webhook, WebhookTest)
    assert verified_webhook.payload.test == "ok"


@pytest.mark.skipif(not PYDANTIC_V2, reason="Webhook tests only run in Pydantic V2")
def test_verify_webhook_event_signature_invalid_signature() -> None:
    """Test webhook signature verification with invalid signature."""
    secret = "test-secret-key"
    timestamp = "2023-01-01T00:00:00Z"

    # Create test webhook
    payload = WebhookTestPayload(test="ok")
    webhook = WebhookTest(type="test", timestamp=datetime.now(timezone.utc), payload=payload)

    verified_webhook = verify_webhook_event_signature(
        body=webhook.model_dump(),
        secret=secret,
        timestamp=timestamp,
        expected_signature="random_invalid_signature",
    )

    assert verified_webhook is None


@pytest.mark.skipif(not PYDANTIC_V2, reason="Webhook tests only run in Pydantic V2")
def test_verify_webhook_event_signature_wrong_secret() -> None:
    """Test webhook signature verification with wrong secret."""

    timestamp = "2023-01-01T00:00:00Z"

    # Create test webhook
    payload = WebhookTestPayload(test="ok")
    webhook = WebhookTest(type="test", timestamp=datetime.now(timezone.utc), payload=payload)

    # Create signature with correct secret
    signature = create_webhook_signature(
        payload=payload.model_dump(),
        timestamp=timestamp,
        secret="test-secret-key",
    )

    # Verify with wrong secret
    verified_webhook = verify_webhook_event_signature(
        body=webhook.model_dump(),
        secret="wrong-secret-key",
        timestamp=timestamp,
        expected_signature=signature,
    )

    assert verified_webhook is None


@pytest.mark.skipif(not PYDANTIC_V2, reason="Webhook tests only run in Pydantic V2")
def test_verify_webhook_event_signature_string_body() -> None:
    """Test webhook signature verification with string body."""
    secret = "test-secret-key"
    timestamp = "2023-01-01T00:00:00Z"

    # Create test webhook
    payload = WebhookTestPayload(test="ok")
    webhook = WebhookTest(type="test", timestamp=datetime.now(timezone.utc), payload=payload)
    signature = create_webhook_signature(webhook.payload.model_dump(), timestamp, secret)

    verified_webhook = verify_webhook_event_signature(
        body=webhook.model_dump_json(),
        secret=secret,
        timestamp=timestamp,
        expected_signature=signature,
    )

    assert verified_webhook is not None
    assert isinstance(verified_webhook, WebhookTest)


@pytest.mark.skipif(not PYDANTIC_V2, reason="Webhook tests only run in Pydantic V2")
def test_verify_webhook_event_signature_invalid_body() -> None:
    """Test webhook signature verification with invalid body."""
    secret = "test-secret-key"
    timestamp = "2023-01-01T00:00:00Z"

    # Invalid webhook data
    invalid_body: Dict[str, Any] = {"type": "invalid_type", "timestamp": "invalid", "payload": {}}

    verified_webhook = verify_webhook_event_signature(
        body=invalid_body, secret=secret, expected_signature="some_signature", timestamp=timestamp
    )

    assert verified_webhook is None
