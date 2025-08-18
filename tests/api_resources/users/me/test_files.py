# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from browser_use_sdk import BrowserUse, AsyncBrowserUse
from browser_use_sdk.types.users.me import FileCreatePresignedURLResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_presigned_url(self, client: BrowserUse) -> None:
        file = client.users.me.files.create_presigned_url(
            content_type="image/jpg",
            file_name="x",
            size_bytes=1,
        )
        assert_matches_type(FileCreatePresignedURLResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_presigned_url(self, client: BrowserUse) -> None:
        response = client.users.me.files.with_raw_response.create_presigned_url(
            content_type="image/jpg",
            file_name="x",
            size_bytes=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileCreatePresignedURLResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_presigned_url(self, client: BrowserUse) -> None:
        with client.users.me.files.with_streaming_response.create_presigned_url(
            content_type="image/jpg",
            file_name="x",
            size_bytes=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileCreatePresignedURLResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFiles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_presigned_url(self, async_client: AsyncBrowserUse) -> None:
        file = await async_client.users.me.files.create_presigned_url(
            content_type="image/jpg",
            file_name="x",
            size_bytes=1,
        )
        assert_matches_type(FileCreatePresignedURLResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_presigned_url(self, async_client: AsyncBrowserUse) -> None:
        response = await async_client.users.me.files.with_raw_response.create_presigned_url(
            content_type="image/jpg",
            file_name="x",
            size_bytes=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileCreatePresignedURLResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_presigned_url(self, async_client: AsyncBrowserUse) -> None:
        async with async_client.users.me.files.with_streaming_response.create_presigned_url(
            content_type="image/jpg",
            file_name="x",
            size_bytes=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileCreatePresignedURLResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True
