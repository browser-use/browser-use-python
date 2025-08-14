# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from browser_use_sdk import BrowserUse, AsyncBrowserUse
from browser_use_sdk.types import (
    BrowserProfileView,
    BrowserProfileListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBrowserProfiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: BrowserUse) -> None:
        browser_profile = client.browser_profiles.create(
            name="x",
        )
        assert_matches_type(BrowserProfileView, browser_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: BrowserUse) -> None:
        browser_profile = client.browser_profiles.create(
            name="x",
            ad_blocker=True,
            browser_viewport_height=100,
            browser_viewport_width=100,
            description="x",
            is_mobile=True,
            persist=True,
            proxy=True,
            proxy_country_code="us",
            store_cache=True,
        )
        assert_matches_type(BrowserProfileView, browser_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: BrowserUse) -> None:
        response = client.browser_profiles.with_raw_response.create(
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser_profile = response.parse()
        assert_matches_type(BrowserProfileView, browser_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: BrowserUse) -> None:
        with client.browser_profiles.with_streaming_response.create(
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser_profile = response.parse()
            assert_matches_type(BrowserProfileView, browser_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: BrowserUse) -> None:
        browser_profile = client.browser_profiles.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(BrowserProfileView, browser_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: BrowserUse) -> None:
        response = client.browser_profiles.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser_profile = response.parse()
        assert_matches_type(BrowserProfileView, browser_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: BrowserUse) -> None:
        with client.browser_profiles.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser_profile = response.parse()
            assert_matches_type(BrowserProfileView, browser_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: BrowserUse) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            client.browser_profiles.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: BrowserUse) -> None:
        browser_profile = client.browser_profiles.update(
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(BrowserProfileView, browser_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: BrowserUse) -> None:
        browser_profile = client.browser_profiles.update(
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ad_blocker=True,
            browser_viewport_height=100,
            browser_viewport_width=100,
            description="x",
            is_mobile=True,
            name="x",
            persist=True,
            proxy=True,
            proxy_country_code="us",
            store_cache=True,
        )
        assert_matches_type(BrowserProfileView, browser_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: BrowserUse) -> None:
        response = client.browser_profiles.with_raw_response.update(
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser_profile = response.parse()
        assert_matches_type(BrowserProfileView, browser_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: BrowserUse) -> None:
        with client.browser_profiles.with_streaming_response.update(
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser_profile = response.parse()
            assert_matches_type(BrowserProfileView, browser_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: BrowserUse) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            client.browser_profiles.with_raw_response.update(
                profile_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: BrowserUse) -> None:
        browser_profile = client.browser_profiles.list()
        assert_matches_type(BrowserProfileListResponse, browser_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: BrowserUse) -> None:
        browser_profile = client.browser_profiles.list(
            page_number=1,
            page_size=1,
        )
        assert_matches_type(BrowserProfileListResponse, browser_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: BrowserUse) -> None:
        response = client.browser_profiles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser_profile = response.parse()
        assert_matches_type(BrowserProfileListResponse, browser_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: BrowserUse) -> None:
        with client.browser_profiles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser_profile = response.parse()
            assert_matches_type(BrowserProfileListResponse, browser_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: BrowserUse) -> None:
        browser_profile = client.browser_profiles.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert browser_profile is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: BrowserUse) -> None:
        response = client.browser_profiles.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser_profile = response.parse()
        assert browser_profile is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: BrowserUse) -> None:
        with client.browser_profiles.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser_profile = response.parse()
            assert browser_profile is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: BrowserUse) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            client.browser_profiles.with_raw_response.delete(
                "",
            )


class TestAsyncBrowserProfiles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncBrowserUse) -> None:
        browser_profile = await async_client.browser_profiles.create(
            name="x",
        )
        assert_matches_type(BrowserProfileView, browser_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncBrowserUse) -> None:
        browser_profile = await async_client.browser_profiles.create(
            name="x",
            ad_blocker=True,
            browser_viewport_height=100,
            browser_viewport_width=100,
            description="x",
            is_mobile=True,
            persist=True,
            proxy=True,
            proxy_country_code="us",
            store_cache=True,
        )
        assert_matches_type(BrowserProfileView, browser_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBrowserUse) -> None:
        response = await async_client.browser_profiles.with_raw_response.create(
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser_profile = await response.parse()
        assert_matches_type(BrowserProfileView, browser_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBrowserUse) -> None:
        async with async_client.browser_profiles.with_streaming_response.create(
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser_profile = await response.parse()
            assert_matches_type(BrowserProfileView, browser_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBrowserUse) -> None:
        browser_profile = await async_client.browser_profiles.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(BrowserProfileView, browser_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBrowserUse) -> None:
        response = await async_client.browser_profiles.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser_profile = await response.parse()
        assert_matches_type(BrowserProfileView, browser_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBrowserUse) -> None:
        async with async_client.browser_profiles.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser_profile = await response.parse()
            assert_matches_type(BrowserProfileView, browser_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBrowserUse) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            await async_client.browser_profiles.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncBrowserUse) -> None:
        browser_profile = await async_client.browser_profiles.update(
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(BrowserProfileView, browser_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncBrowserUse) -> None:
        browser_profile = await async_client.browser_profiles.update(
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ad_blocker=True,
            browser_viewport_height=100,
            browser_viewport_width=100,
            description="x",
            is_mobile=True,
            name="x",
            persist=True,
            proxy=True,
            proxy_country_code="us",
            store_cache=True,
        )
        assert_matches_type(BrowserProfileView, browser_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncBrowserUse) -> None:
        response = await async_client.browser_profiles.with_raw_response.update(
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser_profile = await response.parse()
        assert_matches_type(BrowserProfileView, browser_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncBrowserUse) -> None:
        async with async_client.browser_profiles.with_streaming_response.update(
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser_profile = await response.parse()
            assert_matches_type(BrowserProfileView, browser_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncBrowserUse) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            await async_client.browser_profiles.with_raw_response.update(
                profile_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncBrowserUse) -> None:
        browser_profile = await async_client.browser_profiles.list()
        assert_matches_type(BrowserProfileListResponse, browser_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBrowserUse) -> None:
        browser_profile = await async_client.browser_profiles.list(
            page_number=1,
            page_size=1,
        )
        assert_matches_type(BrowserProfileListResponse, browser_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBrowserUse) -> None:
        response = await async_client.browser_profiles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser_profile = await response.parse()
        assert_matches_type(BrowserProfileListResponse, browser_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBrowserUse) -> None:
        async with async_client.browser_profiles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser_profile = await response.parse()
            assert_matches_type(BrowserProfileListResponse, browser_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncBrowserUse) -> None:
        browser_profile = await async_client.browser_profiles.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert browser_profile is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncBrowserUse) -> None:
        response = await async_client.browser_profiles.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser_profile = await response.parse()
        assert browser_profile is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncBrowserUse) -> None:
        async with async_client.browser_profiles.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser_profile = await response.parse()
            assert browser_profile is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncBrowserUse) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            await async_client.browser_profiles.with_raw_response.delete(
                "",
            )
