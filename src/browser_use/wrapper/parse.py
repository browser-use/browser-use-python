import hashlib
import json
import typing
from datetime import datetime
from typing import Any, AsyncIterator, Generic, Iterator, TypeVar, Union

from pydantic import BaseModel

from browser_use.core.request_options import RequestOptions
from browser_use.tasks.client import AsyncTasksClient, TasksClient
from browser_use.types.task_created_response import TaskCreatedResponse
from browser_use.types.task_step_view import TaskStepView
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


# def _watch(
#     self,
#     task_id: str,
#     interval: float = 1, request_options:typing.Optional[RequestOptions] = None,
#     *,
#     # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
#     # The extra values given here take precedence over values defined on the client or passed to this method.
#     request_options: typing.Optional[RequestOptions] = None,
# ) -> Iterator[TaskView]:
#     """Converts a polling loop into a generator loop."""
#     hash: str | None = None

#     while True:
#         res = self.retrieve(
#             task_id=task_id,
#             extra_headers=extra_headers,
#             extra_query=extra_query,
#             extra_body=extra_body,
#             timeout=timeout,
#         )

#         res_hash = hash_task_view(res)

#         if hash is None or res_hash != hash:
#             hash = res_hash
#             yield res

#         if res.status == "finished":
#             break

#         time.sleep(interval)


# Sync -----------------------------------------------------------------------


class WrappedTaskCreatedResponse(TaskCreatedResponse):
    """TaskCreatedResponse with utility methods for easier interfacing with Browser Use Cloud."""

    def __init__(self, id: str, client: TasksClient):
        super().__init__(id=id)
        self._client = client

    def complete(
        self, interval: float = 1, request_options: typing.Optional[RequestOptions] = None
    ) -> TaskViewWithOutput[T]:
        """Waits for the task to finish and return the result."""
        pass

    def stream(
        self, interval: float = 1, request_options: typing.Optional[RequestOptions] = None
    ) -> Iterator[TaskStepView]:
        """Streams the steps of the task and closes when the task is finished."""
        for i in range(10):
            yield TaskStepView(number=i, status="finished")

    def watch(
        self, interval: float = 1, request_options: typing.Optional[RequestOptions] = None
    ) -> Iterator[TaskViewWithOutput[T]]:
        """Yields the latest task state on every change."""
        for i in range(10):
            yield TaskViewWithOutput[T](status="finished")


# Structured


class WrappedStructuredTaskCreatedResponse(TaskCreatedResponse, Generic[T]):
    """TaskCreatedResponse with structured output."""

    def __init__(self, id: str, schema: type[T], client: TasksClient):
        super().__init__(id=id)

        self._client = client
        self._schema = schema

    def complete(
        self, interval: float = 1, request_options: typing.Optional[RequestOptions] = None
    ) -> TaskViewWithOutput[T]:
        """Waits for the task to finish and return the result."""
        pass

    def stream(
        self, interval: float = 1, request_options: typing.Optional[RequestOptions] = None
    ) -> Iterator[TaskStepView]:
        """Streams the steps of the task and closes when the task is finished."""
        for i in range(10):
            yield TaskStepView(number=i, status="finished")

    def watch(
        self, interval: float = 1, request_options: typing.Optional[RequestOptions] = None
    ) -> Iterator[TaskViewWithOutput[T]]:
        """Yields the latest task state on every change."""
        for i in range(10):
            yield TaskViewWithOutput[T](status="finished")


# Async ----------------------------------------------------------------------


class AsyncWrappedTaskCreatedResponse(TaskCreatedResponse):
    """TaskCreatedResponse with utility methods for easier interfacing with Browser Use Cloud."""

    def __init__(self, id: str, client: AsyncTasksClient):
        super().__init__(id=id)
        self._client = client

    async def complete(self, interval: float = 1, request_options: typing.Optional[RequestOptions] = None) -> TaskView:
        """Waits for the task to finish and return the result."""
        pass

    async def stream(
        self, interval: float = 1, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncIterator[TaskStepView]:
        """Streams the steps of the task and closes when the task is finished."""
        for i in range(10):
            yield TaskStepView(number=i, status="finished")

    async def watch(
        self, interval: float = 1, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncIterator[TaskView]:
        """Yields the latest task state on every change."""
        for i in range(10):
            yield TaskView(status="finished")


# Structured


class AsyncWrappedStructuredTaskCreatedResponse(TaskCreatedResponse, Generic[T]):
    """TaskCreatedResponse with structured output."""

    def __init__(self, id: str, schema: type[T], client: AsyncTasksClient):
        super().__init__(id=id)

        self._client = client
        self._schema = schema

    async def complete(
        self, interval: float = 1, request_options: typing.Optional[RequestOptions] = None
    ) -> TaskViewWithOutput[T]:
        """Waits for the task to finish and return the result."""
        pass

    async def stream(
        self, interval: float = 1, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncIterator[TaskStepView]:
        """Streams the steps of the task and closes when the task is finished."""
        for i in range(10):
            yield TaskStepView(number=i, status="finished")

    async def watch(
        self, interval: float = 1, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncIterator[TaskViewWithOutput[T]]:
        """Yields the latest task state on every change."""
        for i in range(10):
            yield TaskViewWithOutput[T](status="finished")
