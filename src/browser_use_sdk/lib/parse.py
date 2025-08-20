from typing import Union, Generic, TypeVar

from pydantic import BaseModel

from browser_use_sdk.types.task_view import TaskView

T = TypeVar("T", bound=BaseModel)


class TaskViewWithOutput(TaskView, Generic[T]):
    """
    TaskView with structured output.
    """

    parsed_output: Union[T, None]
