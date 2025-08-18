# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .session_status import SessionStatus

__all__ = ["SessionListParams"]


class SessionListParams(TypedDict, total=False):
    filter_by: Annotated[Optional[SessionStatus], PropertyInfo(alias="filterBy")]
    """Enumeration of possible (browser) session states

    Attributes: ACTIVE: Session is currently active and running (browser is running)
    STOPPED: Session has been stopped and is no longer active (browser is stopped)
    """

    page_number: Annotated[int, PropertyInfo(alias="pageNumber")]

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]
