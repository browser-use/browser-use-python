# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from browser_use_sdk import BrowserUse, AsyncBrowserUse
from browser_use_sdk.types import (
    TaskView,
    TaskListResponse,
    TaskCreateResponse,
    TaskGetLogsResponse,
    TaskGetOutputFileResponse,
    TaskGetUserUploadedFileResponse,
)
from browser_use_sdk._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTasks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: BrowserUse) -> None:
        task = client.tasks.create(
            task="x",
        )
        assert_matches_type(TaskCreateResponse, task, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: BrowserUse) -> None:
        task = client.tasks.create(
            task="x",
            agent_settings={
                "llm": "gpt-4o",
                "profile_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "start_url": "startUrl",
            },
            browser_settings={
                "profile_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "session_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            included_file_names=["string"],
            metadata={"foo": "string"},
            secrets={"foo": "string"},
            structured_output_json="structuredOutputJson",
        )
        assert_matches_type(TaskCreateResponse, task, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: BrowserUse) -> None:
        response = client.tasks.with_raw_response.create(
            task="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskCreateResponse, task, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: BrowserUse) -> None:
        with client.tasks.with_streaming_response.create(
            task="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskCreateResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: BrowserUse) -> None:
        task = client.tasks.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TaskView, task, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: BrowserUse) -> None:
        response = client.tasks.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskView, task, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: BrowserUse) -> None:
        with client.tasks.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskView, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: BrowserUse) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.tasks.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: BrowserUse) -> None:
        task = client.tasks.update(
            task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            action="stop",
        )
        assert_matches_type(TaskView, task, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: BrowserUse) -> None:
        response = client.tasks.with_raw_response.update(
            task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            action="stop",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskView, task, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: BrowserUse) -> None:
        with client.tasks.with_streaming_response.update(
            task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            action="stop",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskView, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: BrowserUse) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.tasks.with_raw_response.update(
                task_id="",
                action="stop",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: BrowserUse) -> None:
        task = client.tasks.list()
        assert_matches_type(TaskListResponse, task, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: BrowserUse) -> None:
        task = client.tasks.list(
            after=parse_datetime("2019-12-27T18:11:19.117Z"),
            before=parse_datetime("2019-12-27T18:11:19.117Z"),
            filter_by="started",
            page_number=1,
            page_size=1,
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TaskListResponse, task, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: BrowserUse) -> None:
        response = client.tasks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskListResponse, task, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: BrowserUse) -> None:
        with client.tasks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskListResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_logs(self, client: BrowserUse) -> None:
        task = client.tasks.get_logs(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TaskGetLogsResponse, task, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_logs(self, client: BrowserUse) -> None:
        response = client.tasks.with_raw_response.get_logs(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskGetLogsResponse, task, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_logs(self, client: BrowserUse) -> None:
        with client.tasks.with_streaming_response.get_logs(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskGetLogsResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_logs(self, client: BrowserUse) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.tasks.with_raw_response.get_logs(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_output_file(self, client: BrowserUse) -> None:
        task = client.tasks.get_output_file(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TaskGetOutputFileResponse, task, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_output_file(self, client: BrowserUse) -> None:
        response = client.tasks.with_raw_response.get_output_file(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskGetOutputFileResponse, task, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_output_file(self, client: BrowserUse) -> None:
        with client.tasks.with_streaming_response.get_output_file(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskGetOutputFileResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_output_file(self, client: BrowserUse) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.tasks.with_raw_response.get_output_file(
                file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                task_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.tasks.with_raw_response.get_output_file(
                file_id="",
                task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_user_uploaded_file(self, client: BrowserUse) -> None:
        task = client.tasks.get_user_uploaded_file(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TaskGetUserUploadedFileResponse, task, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_user_uploaded_file(self, client: BrowserUse) -> None:
        response = client.tasks.with_raw_response.get_user_uploaded_file(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskGetUserUploadedFileResponse, task, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_user_uploaded_file(self, client: BrowserUse) -> None:
        with client.tasks.with_streaming_response.get_user_uploaded_file(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskGetUserUploadedFileResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_user_uploaded_file(self, client: BrowserUse) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.tasks.with_raw_response.get_user_uploaded_file(
                file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                task_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.tasks.with_raw_response.get_user_uploaded_file(
                file_id="",
                task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncTasks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncBrowserUse) -> None:
        task = await async_client.tasks.create(
            task="x",
        )
        assert_matches_type(TaskCreateResponse, task, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncBrowserUse) -> None:
        task = await async_client.tasks.create(
            task="x",
            agent_settings={
                "llm": "gpt-4o",
                "profile_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "start_url": "startUrl",
            },
            browser_settings={
                "profile_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "session_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            included_file_names=["string"],
            metadata={"foo": "string"},
            secrets={"foo": "string"},
            structured_output_json="structuredOutputJson",
        )
        assert_matches_type(TaskCreateResponse, task, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBrowserUse) -> None:
        response = await async_client.tasks.with_raw_response.create(
            task="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskCreateResponse, task, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBrowserUse) -> None:
        async with async_client.tasks.with_streaming_response.create(
            task="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskCreateResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBrowserUse) -> None:
        task = await async_client.tasks.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TaskView, task, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBrowserUse) -> None:
        response = await async_client.tasks.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskView, task, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBrowserUse) -> None:
        async with async_client.tasks.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskView, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBrowserUse) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.tasks.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncBrowserUse) -> None:
        task = await async_client.tasks.update(
            task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            action="stop",
        )
        assert_matches_type(TaskView, task, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncBrowserUse) -> None:
        response = await async_client.tasks.with_raw_response.update(
            task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            action="stop",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskView, task, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncBrowserUse) -> None:
        async with async_client.tasks.with_streaming_response.update(
            task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            action="stop",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskView, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncBrowserUse) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.tasks.with_raw_response.update(
                task_id="",
                action="stop",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncBrowserUse) -> None:
        task = await async_client.tasks.list()
        assert_matches_type(TaskListResponse, task, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBrowserUse) -> None:
        task = await async_client.tasks.list(
            after=parse_datetime("2019-12-27T18:11:19.117Z"),
            before=parse_datetime("2019-12-27T18:11:19.117Z"),
            filter_by="started",
            page_number=1,
            page_size=1,
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TaskListResponse, task, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBrowserUse) -> None:
        response = await async_client.tasks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskListResponse, task, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBrowserUse) -> None:
        async with async_client.tasks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskListResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_logs(self, async_client: AsyncBrowserUse) -> None:
        task = await async_client.tasks.get_logs(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TaskGetLogsResponse, task, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_logs(self, async_client: AsyncBrowserUse) -> None:
        response = await async_client.tasks.with_raw_response.get_logs(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskGetLogsResponse, task, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_logs(self, async_client: AsyncBrowserUse) -> None:
        async with async_client.tasks.with_streaming_response.get_logs(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskGetLogsResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_logs(self, async_client: AsyncBrowserUse) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.tasks.with_raw_response.get_logs(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_output_file(self, async_client: AsyncBrowserUse) -> None:
        task = await async_client.tasks.get_output_file(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TaskGetOutputFileResponse, task, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_output_file(self, async_client: AsyncBrowserUse) -> None:
        response = await async_client.tasks.with_raw_response.get_output_file(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskGetOutputFileResponse, task, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_output_file(self, async_client: AsyncBrowserUse) -> None:
        async with async_client.tasks.with_streaming_response.get_output_file(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskGetOutputFileResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_output_file(self, async_client: AsyncBrowserUse) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.tasks.with_raw_response.get_output_file(
                file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                task_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.tasks.with_raw_response.get_output_file(
                file_id="",
                task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_user_uploaded_file(self, async_client: AsyncBrowserUse) -> None:
        task = await async_client.tasks.get_user_uploaded_file(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TaskGetUserUploadedFileResponse, task, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_user_uploaded_file(self, async_client: AsyncBrowserUse) -> None:
        response = await async_client.tasks.with_raw_response.get_user_uploaded_file(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskGetUserUploadedFileResponse, task, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_user_uploaded_file(self, async_client: AsyncBrowserUse) -> None:
        async with async_client.tasks.with_streaming_response.get_user_uploaded_file(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskGetUserUploadedFileResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_user_uploaded_file(self, async_client: AsyncBrowserUse) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.tasks.with_raw_response.get_user_uploaded_file(
                file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                task_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.tasks.with_raw_response.get_user_uploaded_file(
                file_id="",
                task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
