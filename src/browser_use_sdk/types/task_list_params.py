# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TaskListParams"]


class TaskListParams(TypedDict, total=False):
    filter_by: Annotated[
        Optional[Literal["started", "paused", "stopped", "finished", "successful", "unsuccessful"]],
        PropertyInfo(alias="filterBy"),
    ]
    """Enumeration of possible task filters

    Attributes: STARTED: All started tasks PAUSED: All paused tasks STOPPED: All
    stopped tasks FINISHED: All finished tasks SUCCESSFUL: All successful tasks
    UNSUCCESSFUL: All unsuccessful tasks
    """

    page_number: Annotated[int, PropertyInfo(alias="pageNumber")]

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    session_id: Annotated[Optional[str], PropertyInfo(alias="sessionId")]
