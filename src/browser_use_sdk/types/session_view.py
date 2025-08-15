# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .session_status import SessionStatus
from .task_item_view import TaskItemView

__all__ = ["SessionView"]


class SessionView(BaseModel):
    id: str

    started_at: datetime = FieldInfo(alias="startedAt")

    status: SessionStatus
    """Enumeration of possible (browser) session states

    Attributes: ACTIVE: Session is currently active and running (browser is running)
    STOPPED: Session has been stopped and is no longer active (browser is stopped)
    """

    finished_at: Optional[datetime] = FieldInfo(alias="finishedAt", default=None)

    live_url: Optional[str] = FieldInfo(alias="liveUrl", default=None)

    public_share_url: Optional[str] = FieldInfo(alias="publicShareUrl", default=None)

    record_url: Optional[str] = FieldInfo(alias="recordUrl", default=None)

    tasks: Optional[List[TaskItemView]] = None
