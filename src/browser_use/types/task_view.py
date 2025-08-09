# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .llm_model import LlmModel
from .task_status import TaskStatus

__all__ = ["TaskView", "Step"]


class Step(BaseModel):
    actions: List[str]

    evaluation_previous_goal: str = FieldInfo(alias="evaluationPreviousGoal")

    memory: str

    next_goal: str = FieldInfo(alias="nextGoal")

    number: int

    url: str

    screenshot_url: Optional[str] = FieldInfo(alias="screenshotUrl", default=None)


class TaskView(BaseModel):
    id: str

    done_output: str = FieldInfo(alias="doneOutput")

    is_scheduled: bool = FieldInfo(alias="isScheduled")

    llm: LlmModel

    session_id: str = FieldInfo(alias="sessionId")

    started_at: datetime = FieldInfo(alias="startedAt")

    status: TaskStatus
    """Enumeration of possible task execution states

    Attributes: STARTED: Task has been initiated and is currently running PAUSED:
    Task execution has been temporarily paused STOPPED: Task execution has been
    stopped (not completed) FINISHED: Task has completed successfully
    """

    task: str

    browser_use_version: Optional[str] = FieldInfo(alias="browserUseVersion", default=None)

    finished_at: Optional[datetime] = FieldInfo(alias="finishedAt", default=None)

    metadata: Optional[Dict[str, object]] = None

    output_files: Optional[List[str]] = FieldInfo(alias="outputFiles", default=None)

    session_live_url: Optional[str] = FieldInfo(alias="sessionLiveUrl", default=None)

    steps: Optional[List[Step]] = None

    user_uploaded_files: Optional[List[str]] = FieldInfo(alias="userUploadedFiles", default=None)
