# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

import httpx

from ..types import agent_profile_list_params, agent_profile_create_params, agent_profile_update_params
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
from ..types.agent_profile_view import AgentProfileView
from ..types.agent_profile_list_response import AgentProfileListResponse

__all__ = ["AgentProfilesResource", "AsyncAgentProfilesResource"]


class AgentProfilesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AgentProfilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/browser-use/browser-use-python#accessing-raw-response-data-eg-headers
        """
        return AgentProfilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentProfilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/browser-use/browser-use-python#with_streaming_response
        """
        return AgentProfilesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        allowed_domains: List[str] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        flash_mode: bool | NotGiven = NOT_GIVEN,
        highlight_elements: bool | NotGiven = NOT_GIVEN,
        max_agent_steps: int | NotGiven = NOT_GIVEN,
        system_prompt: str | NotGiven = NOT_GIVEN,
        thinking: bool | NotGiven = NOT_GIVEN,
        vision: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentProfileView:
        """
        Create Agent Profile

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/agent-profiles",
            body=maybe_transform(
                {
                    "name": name,
                    "allowed_domains": allowed_domains,
                    "description": description,
                    "flash_mode": flash_mode,
                    "highlight_elements": highlight_elements,
                    "max_agent_steps": max_agent_steps,
                    "system_prompt": system_prompt,
                    "thinking": thinking,
                    "vision": vision,
                },
                agent_profile_create_params.AgentProfileCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentProfileView,
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
    ) -> AgentProfileView:
        """
        Get Agent Profile

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return self._get(
            f"/agent-profiles/{profile_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentProfileView,
        )

    def update(
        self,
        profile_id: str,
        *,
        allowed_domains: Optional[List[str]] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        flash_mode: Optional[bool] | NotGiven = NOT_GIVEN,
        highlight_elements: Optional[bool] | NotGiven = NOT_GIVEN,
        max_agent_steps: Optional[int] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        system_prompt: Optional[str] | NotGiven = NOT_GIVEN,
        thinking: Optional[bool] | NotGiven = NOT_GIVEN,
        vision: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentProfileView:
        """
        Update Agent Profile

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return self._patch(
            f"/agent-profiles/{profile_id}",
            body=maybe_transform(
                {
                    "allowed_domains": allowed_domains,
                    "description": description,
                    "flash_mode": flash_mode,
                    "highlight_elements": highlight_elements,
                    "max_agent_steps": max_agent_steps,
                    "name": name,
                    "system_prompt": system_prompt,
                    "thinking": thinking,
                    "vision": vision,
                },
                agent_profile_update_params.AgentProfileUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentProfileView,
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
    ) -> AgentProfileListResponse:
        """
        List Agent Profiles

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/agent-profiles",
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
                    agent_profile_list_params.AgentProfileListParams,
                ),
            ),
            cast_to=AgentProfileListResponse,
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
        Delete Agent Profile

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return self._delete(
            f"/agent-profiles/{profile_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncAgentProfilesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAgentProfilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/browser-use/browser-use-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAgentProfilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentProfilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/browser-use/browser-use-python#with_streaming_response
        """
        return AsyncAgentProfilesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        allowed_domains: List[str] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        flash_mode: bool | NotGiven = NOT_GIVEN,
        highlight_elements: bool | NotGiven = NOT_GIVEN,
        max_agent_steps: int | NotGiven = NOT_GIVEN,
        system_prompt: str | NotGiven = NOT_GIVEN,
        thinking: bool | NotGiven = NOT_GIVEN,
        vision: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentProfileView:
        """
        Create Agent Profile

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/agent-profiles",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "allowed_domains": allowed_domains,
                    "description": description,
                    "flash_mode": flash_mode,
                    "highlight_elements": highlight_elements,
                    "max_agent_steps": max_agent_steps,
                    "system_prompt": system_prompt,
                    "thinking": thinking,
                    "vision": vision,
                },
                agent_profile_create_params.AgentProfileCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentProfileView,
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
    ) -> AgentProfileView:
        """
        Get Agent Profile

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return await self._get(
            f"/agent-profiles/{profile_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentProfileView,
        )

    async def update(
        self,
        profile_id: str,
        *,
        allowed_domains: Optional[List[str]] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        flash_mode: Optional[bool] | NotGiven = NOT_GIVEN,
        highlight_elements: Optional[bool] | NotGiven = NOT_GIVEN,
        max_agent_steps: Optional[int] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        system_prompt: Optional[str] | NotGiven = NOT_GIVEN,
        thinking: Optional[bool] | NotGiven = NOT_GIVEN,
        vision: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentProfileView:
        """
        Update Agent Profile

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return await self._patch(
            f"/agent-profiles/{profile_id}",
            body=await async_maybe_transform(
                {
                    "allowed_domains": allowed_domains,
                    "description": description,
                    "flash_mode": flash_mode,
                    "highlight_elements": highlight_elements,
                    "max_agent_steps": max_agent_steps,
                    "name": name,
                    "system_prompt": system_prompt,
                    "thinking": thinking,
                    "vision": vision,
                },
                agent_profile_update_params.AgentProfileUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentProfileView,
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
    ) -> AgentProfileListResponse:
        """
        List Agent Profiles

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/agent-profiles",
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
                    agent_profile_list_params.AgentProfileListParams,
                ),
            ),
            cast_to=AgentProfileListResponse,
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
        Delete Agent Profile

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return await self._delete(
            f"/agent-profiles/{profile_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AgentProfilesResourceWithRawResponse:
    def __init__(self, agent_profiles: AgentProfilesResource) -> None:
        self._agent_profiles = agent_profiles

        self.create = to_raw_response_wrapper(
            agent_profiles.create,
        )
        self.retrieve = to_raw_response_wrapper(
            agent_profiles.retrieve,
        )
        self.update = to_raw_response_wrapper(
            agent_profiles.update,
        )
        self.list = to_raw_response_wrapper(
            agent_profiles.list,
        )
        self.delete = to_raw_response_wrapper(
            agent_profiles.delete,
        )


class AsyncAgentProfilesResourceWithRawResponse:
    def __init__(self, agent_profiles: AsyncAgentProfilesResource) -> None:
        self._agent_profiles = agent_profiles

        self.create = async_to_raw_response_wrapper(
            agent_profiles.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            agent_profiles.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            agent_profiles.update,
        )
        self.list = async_to_raw_response_wrapper(
            agent_profiles.list,
        )
        self.delete = async_to_raw_response_wrapper(
            agent_profiles.delete,
        )


class AgentProfilesResourceWithStreamingResponse:
    def __init__(self, agent_profiles: AgentProfilesResource) -> None:
        self._agent_profiles = agent_profiles

        self.create = to_streamed_response_wrapper(
            agent_profiles.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            agent_profiles.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            agent_profiles.update,
        )
        self.list = to_streamed_response_wrapper(
            agent_profiles.list,
        )
        self.delete = to_streamed_response_wrapper(
            agent_profiles.delete,
        )


class AsyncAgentProfilesResourceWithStreamingResponse:
    def __init__(self, agent_profiles: AsyncAgentProfilesResource) -> None:
        self._agent_profiles = agent_profiles

        self.create = async_to_streamed_response_wrapper(
            agent_profiles.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            agent_profiles.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            agent_profiles.update,
        )
        self.list = async_to_streamed_response_wrapper(
            agent_profiles.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            agent_profiles.delete,
        )
