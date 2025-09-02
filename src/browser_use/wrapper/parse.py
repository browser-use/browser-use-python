import asyncio
import hashlib
import json
import time
import typing
from datetime import datetime
from typing import Any, AsyncIterator, Generic, Iterator, Type, TypeVar, Union

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


def _hash_task_view(task_view: TaskView) -> str:
    """Hashes the task view to detect changes."""
    return hashlib.sha256(
        json.dumps(task_view.model_dump(), sort_keys=True, cls=CustomJSONEncoder).encode()
    ).hexdigest()


def _parse_task_view_with_output(task_view: TaskView, schema: Type[T]) -> TaskViewWithOutput[T]:
    """Parses the task view with output."""
    if task_view.output is None:
        return TaskViewWithOutput[T](**task_view.model_dump(), parsed_output=None)

    return TaskViewWithOutput[T](**task_view.model_dump(), parsed_output=schema.model_validate_json(task_view.output))


# Sync -----------------------------------------------------------------------


def _watch(
    client: TasksClient, task_id: str, interval: float = 1, request_options: typing.Optional[RequestOptions] = None
) -> Iterator[TaskView]:
    """Yields the latest task state on every change."""
    hash: typing.Union[str, None] = None
    while True:
        res = client.get_task(task_id, request_options=request_options)
        res_hash = _hash_task_view(res)

        if hash is None or res_hash != hash:
            hash = res_hash
            yield res

        if res.status == "finished" or res.status == "stopped" or res.status == "paused":
            break

        time.sleep(interval)


def _stream(
    client: TasksClient, task_id: str, interval: float = 1, request_options: typing.Optional[RequestOptions] = None
) -> Iterator[TaskStepView]:
    """Streams the steps of the task and closes when the task is finished."""
    total_steps = 0
    for state in _watch(client, task_id, interval, request_options):
        for i in range(total_steps, len(state.steps)):
            total_steps = i + 1
            yield state.steps[i]


class WrappedTaskCreatedResponse(TaskCreatedResponse):
    """TaskCreatedResponse with utility methods for easier interfacing with Browser Use Cloud."""

    def __init__(self, id: str, client: TasksClient):
        super().__init__(id=id)
        self._client = client

    def complete(self, interval: float = 1, request_options: typing.Optional[RequestOptions] = None) -> TaskView:
        """Waits for the task to finish and return the result."""
        for state in _watch(self._client, self.id, interval, request_options):
            if state.status == "finished" or state.status == "stopped" or state.status == "paused":
                return state

        raise Exception("Iterator ended without finding a finished state!")

    def stream(
        self, interval: float = 1, request_options: typing.Optional[RequestOptions] = None
    ) -> Iterator[TaskStepView]:
        """Streams the steps of the task and closes when the task is finished."""
        return _stream(self._client, self.id, interval, request_options)

    def watch(self, interval: float = 1, request_options: typing.Optional[RequestOptions] = None) -> Iterator[TaskView]:
        """Yields the latest task state on every change."""
        return _watch(self._client, self.id, interval, request_options)


# Structured


class WrappedStructuredTaskCreatedResponse(TaskCreatedResponse, Generic[T]):
    """TaskCreatedResponse with structured output."""

    def __init__(self, id: str, schema: Type[T], client: TasksClient):
        super().__init__(id=id)

        self._client = client
        self._schema = schema

    def complete(
        self, interval: float = 1, request_options: typing.Optional[RequestOptions] = None
    ) -> TaskViewWithOutput[T]:
        """Waits for the task to finish and return the result."""
        for state in _watch(self._client, self.id, interval, request_options):
            if state.status == "finished" or state.status == "stopped" or state.status == "paused":
                return _parse_task_view_with_output(state, self._schema)

        raise Exception("Iterator ended without finding a finished state!")

    def stream(
        self, interval: float = 1, request_options: typing.Optional[RequestOptions] = None
    ) -> Iterator[TaskStepView]:
        """Streams the steps of the task and closes when the task is finished."""
        return _stream(self._client, self.id, interval, request_options)

    def watch(
        self, interval: float = 1, request_options: typing.Optional[RequestOptions] = None
    ) -> Iterator[TaskViewWithOutput[T]]:
        """Yields the latest task state on every change."""
        for state in _watch(self._client, self.id, interval, request_options):
            yield _parse_task_view_with_output(state, self._schema)


# Async ----------------------------------------------------------------------


async def _async_watch(
    client: AsyncTasksClient, task_id: str, interval: float = 1, request_options: typing.Optional[RequestOptions] = None
) -> AsyncIterator[TaskView]:
    """Yields the latest task state on every change."""
    hash: typing.Union[str, None] = None
    while True:
        res = await client.get_task(task_id, request_options=request_options)
        res_hash = _hash_task_view(res)
        if hash is None or res_hash != hash:
            hash = res_hash
            yield res

        if res.status == "finished" or res.status == "stopped" or res.status == "paused":
            break

        await asyncio.sleep(interval)


async def _async_stream(
    client: AsyncTasksClient, task_id: str, interval: float = 1, request_options: typing.Optional[RequestOptions] = None
) -> AsyncIterator[TaskStepView]:
    """Streams the steps of the task and closes when the task is finished."""
    total_steps = 0
    async for state in _async_watch(client, task_id, interval, request_options):
        for i in range(total_steps, len(state.steps)):
            total_steps = i + 1
            yield state.steps[i]


class AsyncWrappedTaskCreatedResponse(TaskCreatedResponse):
    """TaskCreatedResponse with utility methods for easier interfacing with Browser Use Cloud."""

    def __init__(self, id: str, client: AsyncTasksClient):
        super().__init__(id=id)
        self._client = client

    async def complete(self, interval: float = 1, request_options: typing.Optional[RequestOptions] = None) -> TaskView:
        """Waits for the task to finish and return the result."""
        async for state in _async_watch(self._client, self.id, interval, request_options):
            if state.status == "finished" or state.status == "stopped" or state.status == "paused":
                return state

        raise Exception("Iterator ended without finding a finished state!")

    def stream(
        self, interval: float = 1, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncIterator[TaskStepView]:
        """Streams the steps of the task and closes when the task is finished."""
        return _async_stream(self._client, self.id, interval, request_options)

    def watch(
        self, interval: float = 1, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncIterator[TaskView]:
        """Yields the latest task state on every change."""
        return _async_watch(self._client, self.id, interval, request_options)


# Structured


class AsyncWrappedStructuredTaskCreatedResponse(TaskCreatedResponse, Generic[T]):
    """TaskCreatedResponse with structured output."""

    def __init__(self, id: str, schema: Type[T], client: AsyncTasksClient):
        super().__init__(id=id)

        self._client = client
        self._schema = schema

    async def complete(
        self, interval: float = 1, request_options: typing.Optional[RequestOptions] = None
    ) -> TaskViewWithOutput[T]:
        """Waits for the task to finish and return the result."""
        async for state in _async_watch(self._client, self.id, interval, request_options):
            if state.status == "finished" or state.status == "stopped" or state.status == "paused":
                return _parse_task_view_with_output(state, self._schema)

        raise Exception("Iterator ended without finding a finished state!")

    def stream(
        self, interval: float = 1, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncIterator[TaskStepView]:
        """Streams the steps of the task and closes when the task is finished."""
        return _async_stream(self._client, self.id, interval, request_options)

    async def watch(
        self, interval: float = 1, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncIterator[TaskViewWithOutput[T]]:
        """Yields the latest task state on every change."""
        async for state in _async_watch(self._client, self.id, interval, request_options):
            yield _parse_task_view_with_output(state, self._schema)
