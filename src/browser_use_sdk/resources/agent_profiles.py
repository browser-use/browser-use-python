# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

import httpx

from ..types import agent_profile_list_params, agent_profile_create_params, agent_profile_update_params
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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
        custom_system_prompt_extension: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        flash_mode: bool | NotGiven = NOT_GIVEN,
        highlight_elements: bool | NotGiven = NOT_GIVEN,
        max_agent_steps: int | NotGiven = NOT_GIVEN,
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
        Create a new agent profile for the authenticated user.

        Agent profiles define how your AI agents behave during tasks. You can create
        multiple profiles for different use cases (e.g., customer support, data
        analysis, web scraping). Free users can create 1 profile; paid users can create
        unlimited profiles.

        Key features you can configure:

        - System prompt: The core instructions that define the agent's personality and
          behavior
        - Allowed domains: Restrict which websites the agent can access
        - Max steps: Limit how many actions the agent can take in a single task
        - Vision: Enable/disable the agent's ability to see and analyze screenshots
        - Thinking: Enable/disable the agent's reasoning process

        Args:

        - request: The agent profile configuration including name, description, and
          behavior settings

        Returns:

        - The newly created agent profile with all its details

        Raises:

        - 402: If user needs a subscription to create additional profiles

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
                    "custom_system_prompt_extension": custom_system_prompt_extension,
                    "description": description,
                    "flash_mode": flash_mode,
                    "highlight_elements": highlight_elements,
                    "max_agent_steps": max_agent_steps,
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
        Get a specific agent profile by its ID.

        Retrieves the complete details of an agent profile, including all its
        configuration settings like system prompts, allowed domains, and behavior flags.

        Args:

        - profile_id: The unique identifier of the agent profile

        Returns:

        - Complete agent profile information

        Raises:

        - 404: If the user agent profile doesn't exist

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
        custom_system_prompt_extension: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        flash_mode: Optional[bool] | NotGiven = NOT_GIVEN,
        highlight_elements: Optional[bool] | NotGiven = NOT_GIVEN,
        max_agent_steps: Optional[int] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
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
        Update an existing agent profile.

        Modify any aspect of an agent profile, such as its name, description, system
        prompt, or behavior settings. Only the fields you provide will be updated; other
        fields remain unchanged.

        Args:

        - profile_id: The unique identifier of the agent profile to update
        - request: The fields to update (only provided fields will be changed)

        Returns:

        - The updated agent profile with all its current details

        Raises:

        - 404: If the user agent profile doesn't exist

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
                    "custom_system_prompt_extension": custom_system_prompt_extension,
                    "description": description,
                    "flash_mode": flash_mode,
                    "highlight_elements": highlight_elements,
                    "max_agent_steps": max_agent_steps,
                    "name": name,
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
        Get a paginated list of all agent profiles for the authenticated user.

        Agent profiles define how your AI agents behave, including their personality,
        capabilities, and limitations. Use this endpoint to see all your configured
        agent profiles.

        Returns:

        - A paginated list of agent profiles
        - Total count of profiles
        - Page information for navigation

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
    ) -> None:
        """
        Delete an agent profile.

        Permanently removes an agent profile and all its configuration. This action
        cannot be undone. Any tasks that were using this profile will continue to work,
        but you won't be able to create new tasks with the deleted profile.

        Args:

        - profile_id: The unique identifier of the agent profile to delete

        Returns:

        - 204 No Content on successful deletion (idempotent)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/agent-profiles/{profile_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
        custom_system_prompt_extension: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        flash_mode: bool | NotGiven = NOT_GIVEN,
        highlight_elements: bool | NotGiven = NOT_GIVEN,
        max_agent_steps: int | NotGiven = NOT_GIVEN,
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
        Create a new agent profile for the authenticated user.

        Agent profiles define how your AI agents behave during tasks. You can create
        multiple profiles for different use cases (e.g., customer support, data
        analysis, web scraping). Free users can create 1 profile; paid users can create
        unlimited profiles.

        Key features you can configure:

        - System prompt: The core instructions that define the agent's personality and
          behavior
        - Allowed domains: Restrict which websites the agent can access
        - Max steps: Limit how many actions the agent can take in a single task
        - Vision: Enable/disable the agent's ability to see and analyze screenshots
        - Thinking: Enable/disable the agent's reasoning process

        Args:

        - request: The agent profile configuration including name, description, and
          behavior settings

        Returns:

        - The newly created agent profile with all its details

        Raises:

        - 402: If user needs a subscription to create additional profiles

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
                    "custom_system_prompt_extension": custom_system_prompt_extension,
                    "description": description,
                    "flash_mode": flash_mode,
                    "highlight_elements": highlight_elements,
                    "max_agent_steps": max_agent_steps,
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
        Get a specific agent profile by its ID.

        Retrieves the complete details of an agent profile, including all its
        configuration settings like system prompts, allowed domains, and behavior flags.

        Args:

        - profile_id: The unique identifier of the agent profile

        Returns:

        - Complete agent profile information

        Raises:

        - 404: If the user agent profile doesn't exist

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
        custom_system_prompt_extension: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        flash_mode: Optional[bool] | NotGiven = NOT_GIVEN,
        highlight_elements: Optional[bool] | NotGiven = NOT_GIVEN,
        max_agent_steps: Optional[int] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
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
        Update an existing agent profile.

        Modify any aspect of an agent profile, such as its name, description, system
        prompt, or behavior settings. Only the fields you provide will be updated; other
        fields remain unchanged.

        Args:

        - profile_id: The unique identifier of the agent profile to update
        - request: The fields to update (only provided fields will be changed)

        Returns:

        - The updated agent profile with all its current details

        Raises:

        - 404: If the user agent profile doesn't exist

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
                    "custom_system_prompt_extension": custom_system_prompt_extension,
                    "description": description,
                    "flash_mode": flash_mode,
                    "highlight_elements": highlight_elements,
                    "max_agent_steps": max_agent_steps,
                    "name": name,
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
        Get a paginated list of all agent profiles for the authenticated user.

        Agent profiles define how your AI agents behave, including their personality,
        capabilities, and limitations. Use this endpoint to see all your configured
        agent profiles.

        Returns:

        - A paginated list of agent profiles
        - Total count of profiles
        - Page information for navigation

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
    ) -> None:
        """
        Delete an agent profile.

        Permanently removes an agent profile and all its configuration. This action
        cannot be undone. Any tasks that were using this profile will continue to work,
        but you won't be able to create new tasks with the deleted profile.

        Args:

        - profile_id: The unique identifier of the agent profile to delete

        Returns:

        - 204 No Content on successful deletion (idempotent)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/agent-profiles/{profile_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
