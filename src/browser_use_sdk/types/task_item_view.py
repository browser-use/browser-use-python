# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .file_view import FileView
from .llm_model import LlmModel
from .task_status import TaskStatus
from .task_step_view import TaskStepView

__all__ = ["TaskItemView"]


class TaskItemView(BaseModel):
    id: str

    is_scheduled: bool = FieldInfo(alias="isScheduled")

    llm: LlmModel

    session_id: str = FieldInfo(alias="sessionId")

    started_at: datetime = FieldInfo(alias="startedAt")

    status: TaskStatus
    """Enumeration of possible task execution states

    Attributes: STARTED: Task has been started and is currently running PAUSED: Task
    execution has been temporarily paused (can be resumed) STOPPED: Task execution
    has been stopped (cannot be resumed) FINISHED: Task has completed successfully
    """

    task: str

    browser_use_version: Optional[str] = FieldInfo(alias="browserUseVersion", default=None)

    done_output: Optional[str] = FieldInfo(alias="doneOutput", default=None)

    finished_at: Optional[datetime] = FieldInfo(alias="finishedAt", default=None)

    is_success: Optional[bool] = FieldInfo(alias="isSuccess", default=None)

    metadata: Optional[Dict[str, object]] = None

    output_files: Optional[List[FileView]] = FieldInfo(alias="outputFiles", default=None)

    session_live_url: Optional[str] = FieldInfo(alias="sessionLiveUrl", default=None)

    steps: Optional[List[TaskStepView]] = None

    user_uploaded_files: Optional[List[FileView]] = FieldInfo(alias="userUploadedFiles", default=None)
