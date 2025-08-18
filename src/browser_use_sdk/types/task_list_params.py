# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .task_status import TaskStatus

__all__ = ["TaskListParams"]


class TaskListParams(TypedDict, total=False):
    after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    filter_by: Annotated[Optional[TaskStatus], PropertyInfo(alias="filterBy")]
    """Enumeration of possible task execution states

    Attributes: STARTED: Task has been started and is currently running. PAUSED:
    Task execution has been temporarily paused (can be resumed) FINISHED: Task has
    finished and the agent has completed the task. STOPPED: Task execution has been
    manually stopped (cannot be resumed).
    """

    page_number: Annotated[int, PropertyInfo(alias="pageNumber")]

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    session_id: Annotated[Optional[str], PropertyInfo(alias="sessionId")]
