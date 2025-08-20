import json
import hashlib
from typing import Any, Union, Generic, TypeVar
from datetime import datetime

from pydantic import BaseModel

from browser_use_sdk.types.task_view import TaskView

T = TypeVar("T", bound=BaseModel)


class TaskViewWithOutput(TaskView, Generic[T]):
    """
    TaskView with structured output.
    """

    parsed_output: Union[T, None]


class CustomJSONEncoder(json.JSONEncoder):
    """Custom JSON encoder to handle datetime objects."""

    # NOTE: Python doesn't have the override decorator in 3.8, that's why we ignore it.
    def default(self, o: Any) -> Any:  # type: ignore[override]
        if isinstance(o, datetime):
            return o.isoformat()
        return super().default(o)


def hash_task_view(task_view: TaskView) -> str:
    """Hashes the task view to detect changes."""
    return hashlib.sha256(
        json.dumps(task_view.model_dump(), sort_keys=True, cls=CustomJSONEncoder).encode()
    ).hexdigest()
