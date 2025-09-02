import json
import typing

from browser_use.core.request_options import RequestOptions
from browser_use.tasks.client import OMIT, AsyncClientWrapper, AsyncTasksClient, SyncClientWrapper, TasksClient
from browser_use.types.supported_ll_ms import SupportedLlMs
from browser_use.types.task_view import TaskView
from browser_use.wrapper.parse import (
    AsyncWrappedStructuredTaskCreatedResponse,
    AsyncWrappedTaskCreatedResponse,
    T,
    TaskViewWithOutput,
    WrappedStructuredTaskCreatedResponse,
    WrappedTaskCreatedResponse,
    _parse_task_view_with_output,
)


class BrowserUseTasksClient(TasksClient):
    """TasksClient with utility method overrides."""

    def __init__(self, *, client_wrapper: SyncClientWrapper):
        super().__init__(client_wrapper=client_wrapper)

    @typing.overload
    def create_task(
        self,
        *,
        task: str,
        llm: typing.Optional[SupportedLlMs] = OMIT,
        start_url: typing.Optional[str] = OMIT,
        max_steps: typing.Optional[int] = OMIT,
        schema: typing.Type[T],
        session_id: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        secrets: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        allowed_domains: typing.Optional[typing.Sequence[str]] = OMIT,
        highlight_elements: typing.Optional[bool] = OMIT,
        flash_mode: typing.Optional[bool] = OMIT,
        thinking: typing.Optional[bool] = OMIT,
        vision: typing.Optional[bool] = OMIT,
        system_prompt_extension: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WrappedStructuredTaskCreatedResponse[T]: ...

    @typing.overload
    def create_task(
        self,
        *,
        task: str,
        llm: typing.Optional[SupportedLlMs] = OMIT,
        start_url: typing.Optional[str] = OMIT,
        max_steps: typing.Optional[int] = OMIT,
        structured_output: typing.Optional[str] = OMIT,
        session_id: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        secrets: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        allowed_domains: typing.Optional[typing.Sequence[str]] = OMIT,
        highlight_elements: typing.Optional[bool] = OMIT,
        flash_mode: typing.Optional[bool] = OMIT,
        thinking: typing.Optional[bool] = OMIT,
        vision: typing.Optional[bool] = OMIT,
        system_prompt_extension: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WrappedTaskCreatedResponse: ...

    def create_task(
        self,
        *,
        task: str,
        llm: typing.Optional[SupportedLlMs] = OMIT,
        start_url: typing.Optional[str] = OMIT,
        max_steps: typing.Optional[int] = OMIT,
        structured_output: typing.Optional[str] = OMIT,
        schema: typing.Optional[typing.Type[T]] = OMIT,
        session_id: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        secrets: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        allowed_domains: typing.Optional[typing.Sequence[str]] = OMIT,
        highlight_elements: typing.Optional[bool] = OMIT,
        flash_mode: typing.Optional[bool] = OMIT,
        thinking: typing.Optional[bool] = OMIT,
        vision: typing.Optional[bool] = OMIT,
        system_prompt_extension: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[WrappedStructuredTaskCreatedResponse[T], WrappedTaskCreatedResponse]:
        if schema is not None and schema is not OMIT:
            structured_output = json.dumps(schema.model_json_schema())

            res = super().create_task(
                task=task,
                llm=llm,
                start_url=start_url,
                max_steps=max_steps,
                structured_output=structured_output,
                session_id=session_id,
                metadata=metadata,
                secrets=secrets,
                allowed_domains=allowed_domains,
                highlight_elements=highlight_elements,
                flash_mode=flash_mode,
                thinking=thinking,
                vision=vision,
                system_prompt_extension=system_prompt_extension,
                request_options=request_options,
            )

            return WrappedStructuredTaskCreatedResponse[T](id=res.id, schema=schema, client=self)

        else:
            res = super().create_task(
                task=task,
                llm=llm,
                start_url=start_url,
                max_steps=max_steps,
                structured_output=structured_output,
                session_id=session_id,
                metadata=metadata,
                secrets=secrets,
                allowed_domains=allowed_domains,
                highlight_elements=highlight_elements,
                flash_mode=flash_mode,
                thinking=thinking,
                vision=vision,
                system_prompt_extension=system_prompt_extension,
                request_options=request_options,
            )

            return WrappedTaskCreatedResponse(id=res.id, client=self)

    @typing.overload
    def get_task(
        self, task_id: str, schema: typing.Type[T], *, request_options: typing.Optional[RequestOptions] = None
    ) -> TaskViewWithOutput[T]: ...

    @typing.overload
    def get_task(self, task_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> TaskView: ...

    def get_task(
        self,
        task_id: str,
        schema: typing.Optional[typing.Type[T]] = OMIT,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[TaskViewWithOutput[T], TaskView]:
        res = super().get_task(task_id, request_options=request_options)

        if schema is not None and schema is not OMIT:
            return _parse_task_view_with_output(res, schema)
        else:
            return res


class AsyncBrowserUseTasksClient(AsyncTasksClient):
    """AsyncTaskClient with utility method overrides."""

    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        super().__init__(client_wrapper=client_wrapper)

    @typing.overload
    async def create_task(
        self,
        *,
        task: str,
        llm: typing.Optional[SupportedLlMs] = OMIT,
        start_url: typing.Optional[str] = OMIT,
        max_steps: typing.Optional[int] = OMIT,
        schema: typing.Type[T],
        session_id: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        secrets: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        allowed_domains: typing.Optional[typing.Sequence[str]] = OMIT,
        highlight_elements: typing.Optional[bool] = OMIT,
        flash_mode: typing.Optional[bool] = OMIT,
        thinking: typing.Optional[bool] = OMIT,
        vision: typing.Optional[bool] = OMIT,
        system_prompt_extension: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncWrappedStructuredTaskCreatedResponse[T]: ...

    @typing.overload
    async def create_task(
        self,
        *,
        task: str,
        llm: typing.Optional[SupportedLlMs] = OMIT,
        start_url: typing.Optional[str] = OMIT,
        max_steps: typing.Optional[int] = OMIT,
        structured_output: typing.Optional[str] = OMIT,
        session_id: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        secrets: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        allowed_domains: typing.Optional[typing.Sequence[str]] = OMIT,
        highlight_elements: typing.Optional[bool] = OMIT,
        flash_mode: typing.Optional[bool] = OMIT,
        thinking: typing.Optional[bool] = OMIT,
        vision: typing.Optional[bool] = OMIT,
        system_prompt_extension: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncWrappedTaskCreatedResponse: ...

    async def create_task(
        self,
        *,
        task: str,
        llm: typing.Optional[SupportedLlMs] = OMIT,
        start_url: typing.Optional[str] = OMIT,
        max_steps: typing.Optional[int] = OMIT,
        structured_output: typing.Optional[str] = OMIT,
        schema: typing.Optional[typing.Type[T]] = OMIT,
        session_id: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        secrets: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        allowed_domains: typing.Optional[typing.Sequence[str]] = OMIT,
        highlight_elements: typing.Optional[bool] = OMIT,
        flash_mode: typing.Optional[bool] = OMIT,
        thinking: typing.Optional[bool] = OMIT,
        vision: typing.Optional[bool] = OMIT,
        system_prompt_extension: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[AsyncWrappedStructuredTaskCreatedResponse[T], AsyncWrappedTaskCreatedResponse]:
        if schema is not None and schema is not OMIT:
            structured_output = json.dumps(schema.model_json_schema())

            res = await super().create_task(
                task=task,
                llm=llm,
                start_url=start_url,
                max_steps=max_steps,
                structured_output=structured_output,
                session_id=session_id,
                metadata=metadata,
                secrets=secrets,
                allowed_domains=allowed_domains,
                highlight_elements=highlight_elements,
                flash_mode=flash_mode,
                thinking=thinking,
                vision=vision,
                system_prompt_extension=system_prompt_extension,
                request_options=request_options,
            )
            return AsyncWrappedStructuredTaskCreatedResponse[T](id=res.id, schema=schema, client=self)

        else:
            res = await super().create_task(
                task=task,
                llm=llm,
                start_url=start_url,
                max_steps=max_steps,
                structured_output=structured_output,
                session_id=session_id,
                metadata=metadata,
                secrets=secrets,
                allowed_domains=allowed_domains,
                highlight_elements=highlight_elements,
                flash_mode=flash_mode,
                thinking=thinking,
                vision=vision,
                system_prompt_extension=system_prompt_extension,
                request_options=request_options,
            )
            return AsyncWrappedTaskCreatedResponse(id=res.id, client=self)

    @typing.overload
    async def get_task(
        self, task_id: str, schema: typing.Type[T], *, request_options: typing.Optional[RequestOptions] = None
    ) -> TaskViewWithOutput[T]: ...

    @typing.overload
    async def get_task(self, task_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> TaskView: ...

    async def get_task(
        self,
        task_id: str,
        schema: typing.Optional[typing.Type[T]] = OMIT,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[TaskViewWithOutput[T], TaskView]:
        res = await super().get_task(task_id, request_options=request_options)

        if schema is not None and schema is not OMIT:
            return _parse_task_view_with_output(res, schema)
        else:
            return res
