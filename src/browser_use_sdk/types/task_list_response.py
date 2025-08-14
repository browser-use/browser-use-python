# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .llm_model import LlmModel
from .task_status import TaskStatus

__all__ = ["TaskListResponse", "Item", "ItemOutputFile", "ItemStep", "ItemUserUploadedFile"]


class ItemOutputFile(BaseModel):
    id: str

    file_name: str = FieldInfo(alias="fileName")


class ItemStep(BaseModel):
    actions: List[str]

    evaluation_previous_goal: str = FieldInfo(alias="evaluationPreviousGoal")

    memory: str

    next_goal: str = FieldInfo(alias="nextGoal")

    number: int

    url: str

    screenshot_url: Optional[str] = FieldInfo(alias="screenshotUrl", default=None)


class ItemUserUploadedFile(BaseModel):
    id: str

    file_name: str = FieldInfo(alias="fileName")


class Item(BaseModel):
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

    output_files: Optional[List[ItemOutputFile]] = FieldInfo(alias="outputFiles", default=None)

    session_live_url: Optional[str] = FieldInfo(alias="sessionLiveUrl", default=None)

    steps: Optional[List[ItemStep]] = None

    user_uploaded_files: Optional[List[ItemUserUploadedFile]] = FieldInfo(alias="userUploadedFiles", default=None)


class TaskListResponse(BaseModel):
    items: List[Item]

    page_number: int = FieldInfo(alias="pageNumber")

    page_size: int = FieldInfo(alias="pageSize")

    total_items: int = FieldInfo(alias="totalItems")
