import hashlib
import json
from datetime import datetime
from typing import Any, Generic, TypeVar, Union

from pydantic import BaseModel

from browser_use.types.task_created_response import TaskCreatedResponse
from browser_use.types.task_view import TaskView

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


def _watch(
    self,
    task_id: str,
    interval: float = 1,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
) -> Iterator[TaskView]:
    """Converts a polling loop into a generator loop."""
    hash: str | None = None

    while True:
        res = self.retrieve(
            task_id=task_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )

        res_hash = hash_task_view(res)

        if hash is None or res_hash != hash:
            hash = res_hash
            yield res

        if res.status == "finished":
            break

        time.sleep(interval)


class WrapperTaskCreatedResponse(TaskCreatedResponse):
    """TaskCreatedResponse with utility methods for easier interfacing with Browser Use Cloud."""

    def __init__(self, id: str):
        super().__init__()
        self.id = id
