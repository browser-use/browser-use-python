# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TaskUpdateParams"]


class TaskUpdateParams(TypedDict, total=False):
    action: Required[Literal["stop", "pause", "resume", "stop_task_and_session"]]
    """Available actions that can be performed on a task

    Attributes: STOP: Stop the current task execution PAUSE: Pause the current task
    execution RESUME: Resume a paused task execution STOP_TASK_AND_SESSION: Stop
    both the task and its parent session
    """
