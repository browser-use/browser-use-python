# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import (
    ProxyCountryCode,
    browser_profile_list_params,
    browser_profile_create_params,
    browser_profile_update_params,
)
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
from .._base_client import make_request_options
from ..types.proxy_country_code import ProxyCountryCode
from ..types.browser_profile_view import BrowserProfileView
from ..types.browser_profile_list_response import BrowserProfileListResponse

__all__ = ["BrowserProfilesResource", "AsyncBrowserProfilesResource"]


class BrowserProfilesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BrowserProfilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/browser-use/browser-use-python#accessing-raw-response-data-eg-headers
        """
        return BrowserProfilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BrowserProfilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/browser-use/browser-use-python#with_streaming_response
        """
        return BrowserProfilesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        ad_blocker: bool | NotGiven = NOT_GIVEN,
        browser_viewport_height: int | NotGiven = NOT_GIVEN,
        browser_viewport_width: int | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        is_mobile: bool | NotGiven = NOT_GIVEN,
        persist: bool | NotGiven = NOT_GIVEN,
        proxy: bool | NotGiven = NOT_GIVEN,
        proxy_country_code: ProxyCountryCode | NotGiven = NOT_GIVEN,
        store_cache: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BrowserProfileView:
        """
        Create Browser Profile

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/browser-profiles",
            body=maybe_transform(
                {
                    "name": name,
                    "ad_blocker": ad_blocker,
                    "browser_viewport_height": browser_viewport_height,
                    "browser_viewport_width": browser_viewport_width,
                    "description": description,
                    "is_mobile": is_mobile,
                    "persist": persist,
                    "proxy": proxy,
                    "proxy_country_code": proxy_country_code,
                    "store_cache": store_cache,
                },
                browser_profile_create_params.BrowserProfileCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrowserProfileView,
        )

    def retrieve(
        self,
        profile_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BrowserProfileView:
        """
        Get Browser Profile

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return self._get(
            f"/browser-profiles/{profile_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrowserProfileView,
        )

    def update(
        self,
        profile_id: str,
        *,
        ad_blocker: Optional[bool] | NotGiven = NOT_GIVEN,
        browser_viewport_height: Optional[int] | NotGiven = NOT_GIVEN,
        browser_viewport_width: Optional[int] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        is_mobile: Optional[bool] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        persist: Optional[bool] | NotGiven = NOT_GIVEN,
        proxy: Optional[bool] | NotGiven = NOT_GIVEN,
        proxy_country_code: Optional[ProxyCountryCode] | NotGiven = NOT_GIVEN,
        store_cache: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BrowserProfileView:
        """
        Update Browser Profile

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return self._patch(
            f"/browser-profiles/{profile_id}",
            body=maybe_transform(
                {
                    "ad_blocker": ad_blocker,
                    "browser_viewport_height": browser_viewport_height,
                    "browser_viewport_width": browser_viewport_width,
                    "description": description,
                    "is_mobile": is_mobile,
                    "name": name,
                    "persist": persist,
                    "proxy": proxy,
                    "proxy_country_code": proxy_country_code,
                    "store_cache": store_cache,
                },
                browser_profile_update_params.BrowserProfileUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrowserProfileView,
        )

    def list(
        self,
        *,
        page_number: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BrowserProfileListResponse:
        """
        List Browser Profiles

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/browser-profiles",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    browser_profile_list_params.BrowserProfileListParams,
                ),
            ),
            cast_to=BrowserProfileListResponse,
        )

    def delete(
        self,
        profile_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Delete Browser Profile

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return self._delete(
            f"/browser-profiles/{profile_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncBrowserProfilesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBrowserProfilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/browser-use/browser-use-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBrowserProfilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBrowserProfilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/browser-use/browser-use-python#with_streaming_response
        """
        return AsyncBrowserProfilesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        ad_blocker: bool | NotGiven = NOT_GIVEN,
        browser_viewport_height: int | NotGiven = NOT_GIVEN,
        browser_viewport_width: int | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        is_mobile: bool | NotGiven = NOT_GIVEN,
        persist: bool | NotGiven = NOT_GIVEN,
        proxy: bool | NotGiven = NOT_GIVEN,
        proxy_country_code: ProxyCountryCode | NotGiven = NOT_GIVEN,
        store_cache: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BrowserProfileView:
        """
        Create Browser Profile

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/browser-profiles",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "ad_blocker": ad_blocker,
                    "browser_viewport_height": browser_viewport_height,
                    "browser_viewport_width": browser_viewport_width,
                    "description": description,
                    "is_mobile": is_mobile,
                    "persist": persist,
                    "proxy": proxy,
                    "proxy_country_code": proxy_country_code,
                    "store_cache": store_cache,
                },
                browser_profile_create_params.BrowserProfileCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrowserProfileView,
        )

    async def retrieve(
        self,
        profile_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BrowserProfileView:
        """
        Get Browser Profile

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return await self._get(
            f"/browser-profiles/{profile_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrowserProfileView,
        )

    async def update(
        self,
        profile_id: str,
        *,
        ad_blocker: Optional[bool] | NotGiven = NOT_GIVEN,
        browser_viewport_height: Optional[int] | NotGiven = NOT_GIVEN,
        browser_viewport_width: Optional[int] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        is_mobile: Optional[bool] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        persist: Optional[bool] | NotGiven = NOT_GIVEN,
        proxy: Optional[bool] | NotGiven = NOT_GIVEN,
        proxy_country_code: Optional[ProxyCountryCode] | NotGiven = NOT_GIVEN,
        store_cache: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BrowserProfileView:
        """
        Update Browser Profile

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return await self._patch(
            f"/browser-profiles/{profile_id}",
            body=await async_maybe_transform(
                {
                    "ad_blocker": ad_blocker,
                    "browser_viewport_height": browser_viewport_height,
                    "browser_viewport_width": browser_viewport_width,
                    "description": description,
                    "is_mobile": is_mobile,
                    "name": name,
                    "persist": persist,
                    "proxy": proxy,
                    "proxy_country_code": proxy_country_code,
                    "store_cache": store_cache,
                },
                browser_profile_update_params.BrowserProfileUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrowserProfileView,
        )

    async def list(
        self,
        *,
        page_number: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BrowserProfileListResponse:
        """
        List Browser Profiles

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/browser-profiles",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    browser_profile_list_params.BrowserProfileListParams,
                ),
            ),
            cast_to=BrowserProfileListResponse,
        )

    async def delete(
        self,
        profile_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Delete Browser Profile

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return await self._delete(
            f"/browser-profiles/{profile_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class BrowserProfilesResourceWithRawResponse:
    def __init__(self, browser_profiles: BrowserProfilesResource) -> None:
        self._browser_profiles = browser_profiles

        self.create = to_raw_response_wrapper(
            browser_profiles.create,
        )
        self.retrieve = to_raw_response_wrapper(
            browser_profiles.retrieve,
        )
        self.update = to_raw_response_wrapper(
            browser_profiles.update,
        )
        self.list = to_raw_response_wrapper(
            browser_profiles.list,
        )
        self.delete = to_raw_response_wrapper(
            browser_profiles.delete,
        )


class AsyncBrowserProfilesResourceWithRawResponse:
    def __init__(self, browser_profiles: AsyncBrowserProfilesResource) -> None:
        self._browser_profiles = browser_profiles

        self.create = async_to_raw_response_wrapper(
            browser_profiles.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            browser_profiles.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            browser_profiles.update,
        )
        self.list = async_to_raw_response_wrapper(
            browser_profiles.list,
        )
        self.delete = async_to_raw_response_wrapper(
            browser_profiles.delete,
        )


class BrowserProfilesResourceWithStreamingResponse:
    def __init__(self, browser_profiles: BrowserProfilesResource) -> None:
        self._browser_profiles = browser_profiles

        self.create = to_streamed_response_wrapper(
            browser_profiles.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            browser_profiles.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            browser_profiles.update,
        )
        self.list = to_streamed_response_wrapper(
            browser_profiles.list,
        )
        self.delete = to_streamed_response_wrapper(
            browser_profiles.delete,
        )


class AsyncBrowserProfilesResourceWithStreamingResponse:
    def __init__(self, browser_profiles: AsyncBrowserProfilesResource) -> None:
        self._browser_profiles = browser_profiles

        self.create = async_to_streamed_response_wrapper(
            browser_profiles.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            browser_profiles.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            browser_profiles.update,
        )
        self.list = async_to_streamed_response_wrapper(
            browser_profiles.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            browser_profiles.delete,
        )
