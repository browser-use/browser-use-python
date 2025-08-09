# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .._models import BaseModel
from .task_view import TaskView
from .task_status import TaskStatus

__all__ = ["TaskRetrieveResponse", "TaskStatusView"]


class TaskStatusView(BaseModel):
    status: TaskStatus
    """Enumeration of possible task execution states

    Attributes: STARTED: Task has been initiated and is currently running PAUSED:
    Task execution has been temporarily paused STOPPED: Task execution has been
    stopped (not completed) FINISHED: Task has completed successfully
    """


TaskRetrieveResponse: TypeAlias = Union[TaskView, TaskStatusView]
