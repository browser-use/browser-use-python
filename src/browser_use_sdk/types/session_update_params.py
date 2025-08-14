# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SessionUpdateParams"]


class SessionUpdateParams(TypedDict, total=False):
    action: Required[Literal["stop"]]
    """Available actions that can be performed on a session

    Attributes: STOP: Stop the session and all its associated tasks (cannot be
    undone)
    """
