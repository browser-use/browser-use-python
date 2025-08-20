# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import json
import time
import asyncio
from typing import Dict, List, Union, TypeVar, Iterator, Optional, AsyncIterator, overload
from datetime import datetime
from typing_extensions import Literal

import httpx
from pydantic import BaseModel

from ..types import TaskStatus, task_list_params, task_create_params, task_update_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..lib.parse import TaskViewWithOutput, hash_task_view
from .._base_client import make_request_options
from ..types.task_view import TaskView
from ..types.task_status import TaskStatus
from ..types.task_list_response import TaskListResponse
from ..types.task_create_response import TaskCreateResponse
from ..types.task_get_logs_response import TaskGetLogsResponse
from ..types.task_get_output_file_response import TaskGetOutputFileResponse
from ..types.task_get_user_uploaded_file_response import TaskGetUserUploadedFileResponse

__all__ = ["TasksResource", "AsyncTasksResource"]

T = TypeVar("T", bound=BaseModel)


class TasksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TasksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/browser-use/browser-use-python#accessing-raw-response-data-eg-headers
        """
        return TasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TasksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/browser-use/browser-use-python#with_streaming_response
        """
        return TasksResourceWithStreamingResponse(self)

    @overload
    def run(
        self,
        *,
        task: str,
        agent_settings: task_create_params.AgentSettings | NotGiven = NOT_GIVEN,
        browser_settings: task_create_params.BrowserSettings | NotGiven = NOT_GIVEN,
        included_file_names: Optional[List[str]] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        secrets: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        structured_output_json: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskView: ...

    @overload
    def run(
        self,
        *,
        task: str,
        agent_settings: task_create_params.AgentSettings | NotGiven = NOT_GIVEN,
        browser_settings: task_create_params.BrowserSettings | NotGiven = NOT_GIVEN,
        included_file_names: Optional[List[str]] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        secrets: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        structured_output_json: type[T],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskViewWithOutput[T]: ...

    def run(
        self,
        *,
        task: str,
        agent_settings: task_create_params.AgentSettings | NotGiven = NOT_GIVEN,
        browser_settings: task_create_params.BrowserSettings | NotGiven = NOT_GIVEN,
        included_file_names: Optional[List[str]] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        secrets: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        structured_output_json: Optional[Union[type[BaseModel], str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Union[TaskView, TaskViewWithOutput[BaseModel]]:
        """
        Run a new task and return the task view.
        """
        if structured_output_json is not None and isinstance(structured_output_json, type):
            create_task_res = self.create(
                task=task,
                agent_settings=agent_settings,
                browser_settings=browser_settings,
                included_file_names=included_file_names,
                metadata=metadata,
                secrets=secrets,
                structured_output_json=structured_output_json,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            )

            for structured_msg in self.stream(create_task_res.id, structured_output_json=structured_output_json):
                if structured_msg.status == "finished":
                    return structured_msg

            raise ValueError("Task did not finish")

        else:
            create_task_res = self.create(
                task=task,
                agent_settings=agent_settings,
                browser_settings=browser_settings,
                included_file_names=included_file_names,
                metadata=metadata,
                secrets=secrets,
                structured_output_json=structured_output_json,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            )

            for msg in self.stream(create_task_res.id):
                if msg.status == "finished":
                    return msg

            raise ValueError("Task did not finish")

    @overload
    def create(
        self,
        *,
        task: str,
        agent_settings: task_create_params.AgentSettings | NotGiven = NOT_GIVEN,
        browser_settings: task_create_params.BrowserSettings | NotGiven = NOT_GIVEN,
        included_file_names: Optional[List[str]] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        secrets: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        structured_output_json: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskCreateResponse: ...

    @overload
    def create(
        self,
        *,
        task: str,
        agent_settings: task_create_params.AgentSettings | NotGiven = NOT_GIVEN,
        browser_settings: task_create_params.BrowserSettings | NotGiven = NOT_GIVEN,
        included_file_names: Optional[List[str]] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        secrets: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        structured_output_json: type[BaseModel],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskCreateResponse: ...

    def create(
        self,
        *,
        task: str,
        agent_settings: task_create_params.AgentSettings | NotGiven = NOT_GIVEN,
        browser_settings: task_create_params.BrowserSettings | NotGiven = NOT_GIVEN,
        included_file_names: Optional[List[str]] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        secrets: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        structured_output_json: Optional[Union[type[BaseModel], str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskCreateResponse:
        """
        Create and start a new Browser Use Agent task.

        This is the main endpoint for running AI agents. You can either:

        1. Start a new session with a new task.
        2. Add a follow-up task to an existing session.

        When starting a new session:

        - A new browser session is created
        - Credits are deducted from your account
        - The agent begins executing your task immediately

        When adding to an existing session:

        - The agent continues in the same browser context
        - No additional browser start up costs are charged (browser session is already
          active)
        - The agent can build on previous work

        Key features:

        - Agent profiles: Define agent behavior and capabilities
        - Browser profiles: Control browser settings and environment (only used for new
          sessions)
        - File uploads: Include documents for the agent to work with
        - Structured output: Define the format of the task result
        - Task metadata: Add custom data for tracking and organization

        Args:

        - request: Complete task configuration including agent settings, browser
          settings, and task description

        Returns:

        - The created task ID together with the task's session ID

        Raises:

        - 402: If user has insufficient credits for a new session
        - 404: If referenced agent/browser profiles don't exist
        - 400: If session is stopped or already has a running task

        Args:
          agent_settings: Configuration settings for the agent

              Attributes: llm: The LLM model to use for the agent start_url: Optional URL to
              start the agent on (will not be changed as a step) profile_id: Unique identifier
              of the agent profile to use for the task

          browser_settings: Configuration settings for the browser session

              Attributes: session_id: Unique identifier of existing session to continue
              profile_id: Unique identifier of browser profile to use (use if you want to
              start a new session)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if (
            structured_output_json is not None
            and not isinstance(structured_output_json, str)
            and isinstance(structured_output_json, type)
        ):
            structured_output_json = json.dumps(structured_output_json.model_json_schema())

        return self._post(
            "/tasks",
            body=maybe_transform(
                {
                    "task": task,
                    "agent_settings": agent_settings,
                    "browser_settings": browser_settings,
                    "included_file_names": included_file_names,
                    "metadata": metadata,
                    "secrets": secrets,
                    "structured_output_json": structured_output_json,
                },
                task_create_params.TaskCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskCreateResponse,
        )

    @overload
    def retrieve(
        self,
        task_id: str,
        structured_output_json: type[T],
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskViewWithOutput[T]: ...

    @overload
    def retrieve(
        self,
        task_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskView: ...

    def retrieve(
        self,
        task_id: str,
        structured_output_json: Optional[type[BaseModel]] | NotGiven = NOT_GIVEN,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Union[TaskView, TaskViewWithOutput[BaseModel]]:
        """
        Get detailed information about a specific AI agent task.

        Retrieves comprehensive information about a task, including its current status,
        progress, and detailed execution data. You can choose to get just the status
        (for quick polling) or full details including steps and file information.

        Use this endpoint to:

        - Monitor task progress in real-time
        - Review completed task results
        - Debug failed tasks by examining steps
        - Download output files and logs

        Args:

        - task_id: The unique identifier of the agent task

        Returns:

        - Complete task information

        Raises:

        - 404: If the user agent task doesn't exist

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")

        if structured_output_json is not None and isinstance(structured_output_json, type):
            res = self._get(
                f"/tasks/{task_id}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=TaskView,
            )

            if res.done_output is None:
                return TaskViewWithOutput[BaseModel](
                    **res.model_dump(),
                    parsed_output=None,
                )

            parsed_output = structured_output_json.model_validate_json(res.done_output)

            return TaskViewWithOutput[BaseModel](
                **res.model_dump(),
                parsed_output=parsed_output,
            )

        return self._get(
            f"/tasks/{task_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskView,
        )

    @overload
    def stream(
        self,
        task_id: str,
        structured_output_json: type[T],
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Iterator[TaskViewWithOutput[T]]: ...

    @overload
    def stream(
        self,
        task_id: str,
        structured_output_json: None | NotGiven = NOT_GIVEN,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Iterator[TaskView]: ...

    def stream(
        self,
        task_id: str,
        structured_output_json: type[T] | None | NotGiven = NOT_GIVEN,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Iterator[TaskView | TaskViewWithOutput[T]]:
        """
        Stream the task view as it is updated until the task is finished.
        """

        for res in self._watch(
            task_id=task_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        ):
            if structured_output_json is not None and isinstance(structured_output_json, type):
                if res.done_output is None:
                    yield TaskViewWithOutput[T](
                        **res.model_dump(),
                        parsed_output=None,
                    )
                else:
                    schema: type[T] = structured_output_json
                    parsed_output: T = schema.model_validate_json(res.done_output)

                    yield TaskViewWithOutput[T](
                        **res.model_dump(),
                        parsed_output=parsed_output,
                    )

            else:
                yield res

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

    def update(
        self,
        task_id: str,
        *,
        action: Literal["stop", "pause", "resume", "stop_task_and_session"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskView:
        """
        Control the execution of an AI agent task.

        Allows you to pause, resume, or stop tasks, and optionally stop the entire
        session. This is useful for:

        - Pausing long-running tasks to review progress
        - Stopping tasks that are taking too long
        - Ending sessions when you're done with all tasks

        Available actions:

        - STOP: Stop the current task
        - PAUSE: Pause the task (can be resumed later)
        - RESUME: Resume a paused task
        - STOP_TASK_AND_SESSION: Stop the task and end the entire session

        Args:

        - task_id: The unique identifier of the agent task to control
        - request: The action to perform on the task

        Returns:

        - The updated task information

        Raises:

        - 404: If the user agent task doesn't exist

        Args:
          action: Available actions that can be performed on a task

              Attributes: STOP: Stop the current task execution PAUSE: Pause the current task
              execution RESUME: Resume a paused task execution STOP_TASK_AND_SESSION: Stop
              both the task and its parent session

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return self._patch(
            f"/tasks/{task_id}",
            body=maybe_transform({"action": action}, task_update_params.TaskUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskView,
        )

    def list(
        self,
        *,
        after: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        before: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        filter_by: Optional[TaskStatus] | NotGiven = NOT_GIVEN,
        page_number: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        session_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskListResponse:
        """
        Get a paginated list of all Browser Use Agent tasks for the authenticated user.

        Browser Use Agent tasks are the individual jobs that your agents perform within
        a session. Each task represents a specific instruction or goal that the agent
        works on, such as filling out a form, extracting data, or navigating to specific
        pages.

        Returns:

        - A paginated list of Browser Use Agent tasks
        - Total count of Browser Use Agent tasks
        - Page information for navigation

        Args:
          filter_by: Enumeration of possible task execution states

              Attributes: STARTED: Task has been started and is currently running. PAUSED:
              Task execution has been temporarily paused (can be resumed) FINISHED: Task has
              finished and the agent has completed the task. STOPPED: Task execution has been
              manually stopped (cannot be resumed).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/tasks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "filter_by": filter_by,
                        "page_number": page_number,
                        "page_size": page_size,
                        "session_id": session_id,
                    },
                    task_list_params.TaskListParams,
                ),
            ),
            cast_to=TaskListResponse,
        )

    def get_logs(
        self,
        task_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskGetLogsResponse:
        """
        Get a download URL for the execution logs of an AI agent task.

        Task logs contain detailed information about how the AI agent executed the task,
        including:

        - Step-by-step reasoning and decisions
        - Actions taken on web pages
        - Error messages and debugging information
        - Performance metrics and timing data

        This is useful for:

        - Understanding how the agent solved the task
        - Debugging failed or unexpected results
        - Optimizing agent behavior and prompts
        - Auditing agent actions for compliance

        Args:

        - task_id: The unique identifier of the agent task

        Returns:

        - A presigned download URL for the task log file

        Raises:

        - 404: If the user agent task doesn't exist
        - 500: If the download URL cannot be generated (should not happen)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return self._get(
            f"/tasks/{task_id}/logs",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskGetLogsResponse,
        )

    def get_output_file(
        self,
        file_id: str,
        *,
        task_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskGetOutputFileResponse:
        """
        Get a download URL for a specific output file generated by an AI agent task.

        AI agents can generate various output files during task execution, such as:

        - Screenshots of web pages
        - Extracted data in CSV/JSON format
        - Generated reports or documents
        - Downloaded files from websites

        This endpoint provides a secure, time-limited download URL for accessing these
        files. The URL expires after a short time for security.

        Args:

        - task_id: The unique identifier of the agent task
        - file_id: The unique identifier of the output file

        Returns:

        - A presigned download URL for the requested file

        Raises:

        - 404: If the user agent task or output file doesn't exist
        - 500: If the download URL cannot be generated (should not happen)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return self._get(
            f"/tasks/{task_id}/output-files/{file_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskGetOutputFileResponse,
        )

    def get_user_uploaded_file(
        self,
        file_id: str,
        *,
        task_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskGetUserUploadedFileResponse:
        """
        Get a download URL for a specific user uploaded file that was used in the task.

        A user can upload files to their account file bucket and reference the name of
        the file in a task. These files are then made available for the agent to use
        during the agent task run.

        This endpoint provides a secure, time-limited download URL for accessing these
        files. The URL expires after a short time for security.

        Args:

        - task_id: The unique identifier of the agent task
        - file_id: The unique identifier of the user uploaded file

        Returns:

        - A presigned download URL for the requested file

        Raises:

        - 404: If the user agent task or user uploaded file doesn't exist
        - 500: If the download URL cannot be generated (should not happen)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return self._get(
            f"/tasks/{task_id}/user-uploaded-files/{file_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskGetUserUploadedFileResponse,
        )


class AsyncTasksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTasksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/browser-use/browser-use-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTasksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/browser-use/browser-use-python#with_streaming_response
        """
        return AsyncTasksResourceWithStreamingResponse(self)

    @overload
    async def run(
        self,
        *,
        task: str,
        agent_settings: task_create_params.AgentSettings | NotGiven = NOT_GIVEN,
        browser_settings: task_create_params.BrowserSettings | NotGiven = NOT_GIVEN,
        included_file_names: Optional[List[str]] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        secrets: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        structured_output_json: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskView: ...

    @overload
    async def run(
        self,
        *,
        task: str,
        agent_settings: task_create_params.AgentSettings | NotGiven = NOT_GIVEN,
        browser_settings: task_create_params.BrowserSettings | NotGiven = NOT_GIVEN,
        included_file_names: Optional[List[str]] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        secrets: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        structured_output_json: type[T],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskViewWithOutput[T]: ...

    async def run(
        self,
        *,
        task: str,
        agent_settings: task_create_params.AgentSettings | NotGiven = NOT_GIVEN,
        browser_settings: task_create_params.BrowserSettings | NotGiven = NOT_GIVEN,
        included_file_names: Optional[List[str]] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        secrets: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        structured_output_json: Optional[Union[type[BaseModel], str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Union[TaskView, TaskViewWithOutput[BaseModel]]:
        """
        Run a new Browser Use Agent task.
        """
        if structured_output_json is not None and isinstance(structured_output_json, type):
            create_task_res = await self.create(
                task=task,
                agent_settings=agent_settings,
                browser_settings=browser_settings,
                included_file_names=included_file_names,
                metadata=metadata,
                secrets=secrets,
                structured_output_json=structured_output_json,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            )

            async for structured_msg in self.stream(create_task_res.id, structured_output_json=structured_output_json):
                if structured_msg.status == "finished":
                    return structured_msg

            raise ValueError("Task did not finish")

        else:
            create_task_res = await self.create(
                task=task,
                agent_settings=agent_settings,
                browser_settings=browser_settings,
                included_file_names=included_file_names,
                metadata=metadata,
                secrets=secrets,
                structured_output_json=structured_output_json,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            )

            async for msg in self.stream(create_task_res.id):
                if msg.status == "finished":
                    return msg

            raise ValueError("Task did not finish")

    @overload
    async def create(
        self,
        *,
        task: str,
        agent_settings: task_create_params.AgentSettings | NotGiven = NOT_GIVEN,
        browser_settings: task_create_params.BrowserSettings | NotGiven = NOT_GIVEN,
        included_file_names: Optional[List[str]] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        secrets: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        structured_output_json: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskCreateResponse: ...

    @overload
    async def create(
        self,
        *,
        task: str,
        agent_settings: task_create_params.AgentSettings | NotGiven = NOT_GIVEN,
        browser_settings: task_create_params.BrowserSettings | NotGiven = NOT_GIVEN,
        included_file_names: Optional[List[str]] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        secrets: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        structured_output_json: type[BaseModel],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskCreateResponse: ...

    async def create(
        self,
        *,
        task: str,
        agent_settings: task_create_params.AgentSettings | NotGiven = NOT_GIVEN,
        browser_settings: task_create_params.BrowserSettings | NotGiven = NOT_GIVEN,
        included_file_names: Optional[List[str]] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        secrets: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        structured_output_json: Optional[Union[type[BaseModel], str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskCreateResponse:
        """
        Create and start a new Browser Use Agent task.

        This is the main endpoint for running AI agents. You can either:

        1. Start a new session with a new task.
        2. Add a follow-up task to an existing session.

        When starting a new session:

        - A new browser session is created
        - Credits are deducted from your account
        - The agent begins executing your task immediately

        When adding to an existing session:

        - The agent continues in the same browser context
        - No additional browser start up costs are charged (browser session is already
          active)
        - The agent can build on previous work

        Key features:

        - Agent profiles: Define agent behavior and capabilities
        - Browser profiles: Control browser settings and environment (only used for new
          sessions)
        - File uploads: Include documents for the agent to work with
        - Structured output: Define the format of the task result
        - Task metadata: Add custom data for tracking and organization

        Args:

        - request: Complete task configuration including agent settings, browser
          settings, and task description

        Returns:

        - The created task ID together with the task's session ID

        Raises:

        - 402: If user has insufficient credits for a new session
        - 404: If referenced agent/browser profiles don't exist
        - 400: If session is stopped or already has a running task

        Args:
          agent_settings: Configuration settings for the agent

              Attributes: llm: The LLM model to use for the agent start_url: Optional URL to
              start the agent on (will not be changed as a step) profile_id: Unique identifier
              of the agent profile to use for the task

          browser_settings: Configuration settings for the browser session

              Attributes: session_id: Unique identifier of existing session to continue
              profile_id: Unique identifier of browser profile to use (use if you want to
              start a new session)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """

        if (
            structured_output_json is not None
            and not isinstance(structured_output_json, str)
            and isinstance(structured_output_json, type)
        ):
            structured_output_json = json.dumps(structured_output_json.model_json_schema())

        return await self._post(
            "/tasks",
            body=await async_maybe_transform(
                {
                    "task": task,
                    "agent_settings": agent_settings,
                    "browser_settings": browser_settings,
                    "included_file_names": included_file_names,
                    "metadata": metadata,
                    "secrets": secrets,
                    "structured_output_json": structured_output_json,
                },
                task_create_params.TaskCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskCreateResponse,
        )

    @overload
    async def retrieve(
        self,
        task_id: str,
        structured_output_json: type[T],
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskViewWithOutput[T]: ...

    @overload
    async def retrieve(
        self,
        task_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskView: ...

    async def retrieve(
        self,
        task_id: str,
        structured_output_json: Optional[type[BaseModel]] | NotGiven = NOT_GIVEN,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Union[TaskView, TaskViewWithOutput[BaseModel]]:
        """
        Get detailed information about a specific AI agent task.

        Retrieves comprehensive information about a task, including its current status,
        progress, and detailed execution data. You can choose to get just the status
        (for quick polling) or full details including steps and file information.

        Use this endpoint to:

        - Monitor task progress in real-time
        - Review completed task results
        - Debug failed tasks by examining steps
        - Download output files and logs

        Args:

        - task_id: The unique identifier of the agent task

        Returns:

        - Complete task information

        Raises:

        - 404: If the user agent task doesn't exist

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")

        if structured_output_json is not None and isinstance(structured_output_json, type):
            res = await self._get(
                f"/tasks/{task_id}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=TaskView,
            )

            if res.done_output is None:
                return TaskViewWithOutput[BaseModel](
                    **res.model_dump(),
                    parsed_output=None,
                )

            parsed_output = structured_output_json.model_validate_json(res.done_output)

            return TaskViewWithOutput[BaseModel](
                **res.model_dump(),
                parsed_output=parsed_output,
            )

        return await self._get(
            f"/tasks/{task_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskView,
        )

    @overload
    def stream(
        self,
        task_id: str,
        structured_output_json: type[T],
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncIterator[TaskViewWithOutput[T]]: ...

    @overload
    def stream(
        self,
        task_id: str,
        structured_output_json: None | NotGiven = NOT_GIVEN,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncIterator[TaskView]: ...

    async def stream(
        self,
        task_id: str,
        structured_output_json: type[T] | None | NotGiven = NOT_GIVEN,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncIterator[TaskView | TaskViewWithOutput[T]]:
        """
        Stream the task view as it is updated until the task is finished.
        """

        async for res in self._watch(
            task_id=task_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        ):
            if structured_output_json is not None and isinstance(structured_output_json, type):
                if res.done_output is None:
                    yield TaskViewWithOutput[T](
                        **res.model_dump(),
                        parsed_output=None,
                    )
                else:
                    schema: type[T] = structured_output_json
                    # pydantic returns the model instance, but the type checker can’t infer it.
                    parsed_output: T = schema.model_validate_json(res.done_output)
                    yield TaskViewWithOutput[T](
                        **res.model_dump(),
                        parsed_output=parsed_output,
                    )
            else:
                yield res

    async def _watch(
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
    ) -> AsyncIterator[TaskView]:
        """Converts a polling loop into a generator loop."""
        prev_hash: str | None = None

        while True:
            res = await self.retrieve(
                task_id=task_id,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            )

            res_hash = hash_task_view(res)
            if prev_hash is None or res_hash != prev_hash:
                prev_hash = res_hash
                yield res

            if res.status == "finished":
                break
            if res.status == "paused":
                break
            if res.status == "stopped":
                break
            if res.status == "started":
                await asyncio.sleep(interval)
            else:
                raise ValueError(
                    f"Expected one of 'finished', 'paused', 'stopped', or 'started' but received {res.status!r}"
                )

    async def update(
        self,
        task_id: str,
        *,
        action: Literal["stop", "pause", "resume", "stop_task_and_session"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskView:
        """
        Control the execution of an AI agent task.

        Allows you to pause, resume, or stop tasks, and optionally stop the entire
        session. This is useful for:

        - Pausing long-running tasks to review progress
        - Stopping tasks that are taking too long
        - Ending sessions when you're done with all tasks

        Available actions:

        - STOP: Stop the current task
        - PAUSE: Pause the task (can be resumed later)
        - RESUME: Resume a paused task
        - STOP_TASK_AND_SESSION: Stop the task and end the entire session

        Args:

        - task_id: The unique identifier of the agent task to control
        - request: The action to perform on the task

        Returns:

        - The updated task information

        Raises:

        - 404: If the user agent task doesn't exist

        Args:
          action: Available actions that can be performed on a task

              Attributes: STOP: Stop the current task execution PAUSE: Pause the current task
              execution RESUME: Resume a paused task execution STOP_TASK_AND_SESSION: Stop
              both the task and its parent session

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return await self._patch(
            f"/tasks/{task_id}",
            body=await async_maybe_transform({"action": action}, task_update_params.TaskUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskView,
        )

    async def list(
        self,
        *,
        after: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        before: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        filter_by: Optional[TaskStatus] | NotGiven = NOT_GIVEN,
        page_number: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        session_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskListResponse:
        """
        Get a paginated list of all Browser Use Agent tasks for the authenticated user.

        Browser Use Agent tasks are the individual jobs that your agents perform within
        a session. Each task represents a specific instruction or goal that the agent
        works on, such as filling out a form, extracting data, or navigating to specific
        pages.

        Returns:

        - A paginated list of Browser Use Agent tasks
        - Total count of Browser Use Agent tasks
        - Page information for navigation

        Args:
          filter_by: Enumeration of possible task execution states

              Attributes: STARTED: Task has been started and is currently running. PAUSED:
              Task execution has been temporarily paused (can be resumed) FINISHED: Task has
              finished and the agent has completed the task. STOPPED: Task execution has been
              manually stopped (cannot be resumed).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/tasks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "filter_by": filter_by,
                        "page_number": page_number,
                        "page_size": page_size,
                        "session_id": session_id,
                    },
                    task_list_params.TaskListParams,
                ),
            ),
            cast_to=TaskListResponse,
        )

    async def get_logs(
        self,
        task_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskGetLogsResponse:
        """
        Get a download URL for the execution logs of an AI agent task.

        Task logs contain detailed information about how the AI agent executed the task,
        including:

        - Step-by-step reasoning and decisions
        - Actions taken on web pages
        - Error messages and debugging information
        - Performance metrics and timing data

        This is useful for:

        - Understanding how the agent solved the task
        - Debugging failed or unexpected results
        - Optimizing agent behavior and prompts
        - Auditing agent actions for compliance

        Args:

        - task_id: The unique identifier of the agent task

        Returns:

        - A presigned download URL for the task log file

        Raises:

        - 404: If the user agent task doesn't exist
        - 500: If the download URL cannot be generated (should not happen)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return await self._get(
            f"/tasks/{task_id}/logs",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskGetLogsResponse,
        )

    async def get_output_file(
        self,
        file_id: str,
        *,
        task_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskGetOutputFileResponse:
        """
        Get a download URL for a specific output file generated by an AI agent task.

        AI agents can generate various output files during task execution, such as:

        - Screenshots of web pages
        - Extracted data in CSV/JSON format
        - Generated reports or documents
        - Downloaded files from websites

        This endpoint provides a secure, time-limited download URL for accessing these
        files. The URL expires after a short time for security.

        Args:

        - task_id: The unique identifier of the agent task
        - file_id: The unique identifier of the output file

        Returns:

        - A presigned download URL for the requested file

        Raises:

        - 404: If the user agent task or output file doesn't exist
        - 500: If the download URL cannot be generated (should not happen)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return await self._get(
            f"/tasks/{task_id}/output-files/{file_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskGetOutputFileResponse,
        )

    async def get_user_uploaded_file(
        self,
        file_id: str,
        *,
        task_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskGetUserUploadedFileResponse:
        """
        Get a download URL for a specific user uploaded file that was used in the task.

        A user can upload files to their account file bucket and reference the name of
        the file in a task. These files are then made available for the agent to use
        during the agent task run.

        This endpoint provides a secure, time-limited download URL for accessing these
        files. The URL expires after a short time for security.

        Args:

        - task_id: The unique identifier of the agent task
        - file_id: The unique identifier of the user uploaded file

        Returns:

        - A presigned download URL for the requested file

        Raises:

        - 404: If the user agent task or user uploaded file doesn't exist
        - 500: If the download URL cannot be generated (should not happen)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return await self._get(
            f"/tasks/{task_id}/user-uploaded-files/{file_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskGetUserUploadedFileResponse,
        )


class TasksResourceWithRawResponse:
    def __init__(self, tasks: TasksResource) -> None:
        self._tasks = tasks

        self.create = to_raw_response_wrapper(
            tasks.create,
        )
        self.retrieve = to_raw_response_wrapper(
            tasks.retrieve,
        )
        self.update = to_raw_response_wrapper(
            tasks.update,
        )
        self.list = to_raw_response_wrapper(
            tasks.list,
        )
        self.get_logs = to_raw_response_wrapper(
            tasks.get_logs,
        )
        self.get_output_file = to_raw_response_wrapper(
            tasks.get_output_file,
        )
        self.get_user_uploaded_file = to_raw_response_wrapper(
            tasks.get_user_uploaded_file,
        )


class AsyncTasksResourceWithRawResponse:
    def __init__(self, tasks: AsyncTasksResource) -> None:
        self._tasks = tasks

        self.create = async_to_raw_response_wrapper(
            tasks.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            tasks.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            tasks.update,
        )
        self.list = async_to_raw_response_wrapper(
            tasks.list,
        )
        self.get_logs = async_to_raw_response_wrapper(
            tasks.get_logs,
        )
        self.get_output_file = async_to_raw_response_wrapper(
            tasks.get_output_file,
        )
        self.get_user_uploaded_file = async_to_raw_response_wrapper(
            tasks.get_user_uploaded_file,
        )


class TasksResourceWithStreamingResponse:
    def __init__(self, tasks: TasksResource) -> None:
        self._tasks = tasks

        self.create = to_streamed_response_wrapper(
            tasks.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            tasks.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            tasks.update,
        )
        self.list = to_streamed_response_wrapper(
            tasks.list,
        )
        self.get_logs = to_streamed_response_wrapper(
            tasks.get_logs,
        )
        self.get_output_file = to_streamed_response_wrapper(
            tasks.get_output_file,
        )
        self.get_user_uploaded_file = to_streamed_response_wrapper(
            tasks.get_user_uploaded_file,
        )


class AsyncTasksResourceWithStreamingResponse:
    def __init__(self, tasks: AsyncTasksResource) -> None:
        self._tasks = tasks

        self.create = async_to_streamed_response_wrapper(
            tasks.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            tasks.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            tasks.update,
        )
        self.list = async_to_streamed_response_wrapper(
            tasks.list,
        )
        self.get_logs = async_to_streamed_response_wrapper(
            tasks.get_logs,
        )
        self.get_output_file = async_to_streamed_response_wrapper(
            tasks.get_output_file,
        )
        self.get_user_uploaded_file = async_to_streamed_response_wrapper(
            tasks.get_user_uploaded_file,
        )
