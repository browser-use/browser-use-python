# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .file_view import FileView
from .llm_model import LlmModel
from .task_status import TaskStatus
from .task_step_view import TaskStepView

__all__ = ["TaskView", "Session"]


class Session(BaseModel):
    id: str

    started_at: datetime = FieldInfo(alias="startedAt")

    status: Literal["active", "stopped"]
    """Enumeration of possible (browser) session states

    Attributes: ACTIVE: Session is currently active and running (browser is running)
    STOPPED: Session has been stopped and is no longer active (browser is stopped)
    """

    finished_at: Optional[datetime] = FieldInfo(alias="finishedAt", default=None)

    live_url: Optional[str] = FieldInfo(alias="liveUrl", default=None)


class TaskView(BaseModel):
    id: str

    is_scheduled: bool = FieldInfo(alias="isScheduled")

    llm: LlmModel

    output_files: List[FileView] = FieldInfo(alias="outputFiles")

    session: Session
    """View model for representing a session that a task belongs to

    Attributes: id: Unique identifier for the session status: Current status of the
    session (active/stopped) live_url: URL where the browser can be viewed live in
    real-time. started_at: Timestamp when the session was created and started.
    finished_at: Timestamp when the session was stopped (None if still active).
    """

    session_id: str = FieldInfo(alias="sessionId")

    started_at: datetime = FieldInfo(alias="startedAt")

    status: TaskStatus
    """Enumeration of possible task execution states

    Attributes: STARTED: Task has been started and is currently running. PAUSED:
    Task execution has been temporarily paused (can be resumed) FINISHED: Task has
    finished and the agent has completed the task. STOPPED: Task execution has been
    manually stopped (cannot be resumed).
    """

    steps: List[TaskStepView]

    task: str

    user_uploaded_files: List[FileView] = FieldInfo(alias="userUploadedFiles")

    browser_use_version: Optional[str] = FieldInfo(alias="browserUseVersion", default=None)

    done_output: Optional[str] = FieldInfo(alias="doneOutput", default=None)

    finished_at: Optional[datetime] = FieldInfo(alias="finishedAt", default=None)

    is_success: Optional[bool] = FieldInfo(alias="isSuccess", default=None)

    metadata: Optional[Dict[str, object]] = None
