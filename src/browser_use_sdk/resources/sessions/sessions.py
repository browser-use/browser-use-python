# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ...types import SessionStatus, session_list_params, session_update_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .public_share import (
    PublicShareResource,
    AsyncPublicShareResource,
    PublicShareResourceWithRawResponse,
    AsyncPublicShareResourceWithRawResponse,
    PublicShareResourceWithStreamingResponse,
    AsyncPublicShareResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from ...types.session_view import SessionView
from ...types.session_status import SessionStatus
from ...types.session_list_response import SessionListResponse

__all__ = ["SessionsResource", "AsyncSessionsResource"]


class SessionsResource(SyncAPIResource):
    @cached_property
    def public_share(self) -> PublicShareResource:
        return PublicShareResource(self._client)

    @cached_property
    def with_raw_response(self) -> SessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/browser-use/browser-use-python#accessing-raw-response-data-eg-headers
        """
        return SessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/browser-use/browser-use-python#with_streaming_response
        """
        return SessionsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionView:
        """
        Get detailed information about a specific AI agent session.

        Retrieves comprehensive information about a session, including its current
        status, live browser URL (if active), recording URL (if completed), and optional
        task details. This endpoint is useful for monitoring active sessions or
        reviewing completed ones.

        Args:

        - session_id: The unique identifier of the agent session
        - params: Optional parameters to control what data is included

        Returns:

        - Complete session information including status, URLs, and optional task details

        Raises:

        - 404: If the user agent session doesn't exist

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            f"/sessions/{session_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionView,
        )

    def update(
        self,
        session_id: str,
        *,
        action: Literal["stop"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionView:
        """
        Update a session's status or perform actions on it.

        Currently supports stopping a session, which will:

        1. Stop any running tasks in the session
        2. End the browser session
        3. Generate a recording URL if available
        4. Update the session status to 'stopped'

        This is useful for manually stopping long-running sessions or when you want to
        end a session before all tasks are complete.

        Args:

        - session_id: The unique identifier of the agent session to update
        - request: The action to perform on the session

        Returns:

        - The updated session information including the new status and recording URL

        Raises:

        - 404: If the user agent session doesn't exist

        Args:
          action: Available actions that can be performed on a session

              Attributes: STOP: Stop the session and all its associated tasks (cannot be
              undone)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._patch(
            f"/sessions/{session_id}",
            body=maybe_transform({"action": action}, session_update_params.SessionUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionView,
        )

    def list(
        self,
        *,
        filter_by: Optional[SessionStatus] | NotGiven = NOT_GIVEN,
        page_number: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionListResponse:
        """
        Get a paginated list of all AI agent sessions for the authenticated user.

        AI agent sessions represent active or completed browsing sessions where your AI
        agents perform tasks. Each session can contain multiple tasks and maintains
        browser state throughout the session lifecycle.

        You can filter sessions by status and optionally include task details for each
        session.

        Returns:

        - A paginated list of agent sessions
        - Total count of sessions
        - Page information for navigation
        - Optional task details for each session (if requested)

        Args:
          filter_by: Enumeration of possible (browser) session states

              Attributes: ACTIVE: Session is currently active and running (browser is running)
              STOPPED: Session has been stopped and is no longer active (browser is stopped)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/sessions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_by": filter_by,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    session_list_params.SessionListParams,
                ),
            ),
            cast_to=SessionListResponse,
        )

    def delete(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a session and all its associated data.

        Permanently removes a session and all its tasks, browser data, and public
        shares. This action cannot be undone. Use this endpoint to clean up old sessions
        and free up storage space.

        Args:

        - session_id: The unique identifier of the agent session to delete

        Returns:

        - 204 No Content on successful deletion (idempotent)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/sessions/{session_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncSessionsResource(AsyncAPIResource):
    @cached_property
    def public_share(self) -> AsyncPublicShareResource:
        return AsyncPublicShareResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/browser-use/browser-use-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/browser-use/browser-use-python#with_streaming_response
        """
        return AsyncSessionsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionView:
        """
        Get detailed information about a specific AI agent session.

        Retrieves comprehensive information about a session, including its current
        status, live browser URL (if active), recording URL (if completed), and optional
        task details. This endpoint is useful for monitoring active sessions or
        reviewing completed ones.

        Args:

        - session_id: The unique identifier of the agent session
        - params: Optional parameters to control what data is included

        Returns:

        - Complete session information including status, URLs, and optional task details

        Raises:

        - 404: If the user agent session doesn't exist

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            f"/sessions/{session_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionView,
        )

    async def update(
        self,
        session_id: str,
        *,
        action: Literal["stop"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionView:
        """
        Update a session's status or perform actions on it.

        Currently supports stopping a session, which will:

        1. Stop any running tasks in the session
        2. End the browser session
        3. Generate a recording URL if available
        4. Update the session status to 'stopped'

        This is useful for manually stopping long-running sessions or when you want to
        end a session before all tasks are complete.

        Args:

        - session_id: The unique identifier of the agent session to update
        - request: The action to perform on the session

        Returns:

        - The updated session information including the new status and recording URL

        Raises:

        - 404: If the user agent session doesn't exist

        Args:
          action: Available actions that can be performed on a session

              Attributes: STOP: Stop the session and all its associated tasks (cannot be
              undone)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._patch(
            f"/sessions/{session_id}",
            body=await async_maybe_transform({"action": action}, session_update_params.SessionUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionView,
        )

    async def list(
        self,
        *,
        filter_by: Optional[SessionStatus] | NotGiven = NOT_GIVEN,
        page_number: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionListResponse:
        """
        Get a paginated list of all AI agent sessions for the authenticated user.

        AI agent sessions represent active or completed browsing sessions where your AI
        agents perform tasks. Each session can contain multiple tasks and maintains
        browser state throughout the session lifecycle.

        You can filter sessions by status and optionally include task details for each
        session.

        Returns:

        - A paginated list of agent sessions
        - Total count of sessions
        - Page information for navigation
        - Optional task details for each session (if requested)

        Args:
          filter_by: Enumeration of possible (browser) session states

              Attributes: ACTIVE: Session is currently active and running (browser is running)
              STOPPED: Session has been stopped and is no longer active (browser is stopped)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/sessions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter_by": filter_by,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    session_list_params.SessionListParams,
                ),
            ),
            cast_to=SessionListResponse,
        )

    async def delete(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a session and all its associated data.

        Permanently removes a session and all its tasks, browser data, and public
        shares. This action cannot be undone. Use this endpoint to clean up old sessions
        and free up storage space.

        Args:

        - session_id: The unique identifier of the agent session to delete

        Returns:

        - 204 No Content on successful deletion (idempotent)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/sessions/{session_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class SessionsResourceWithRawResponse:
    def __init__(self, sessions: SessionsResource) -> None:
        self._sessions = sessions

        self.retrieve = to_raw_response_wrapper(
            sessions.retrieve,
        )
        self.update = to_raw_response_wrapper(
            sessions.update,
        )
        self.list = to_raw_response_wrapper(
            sessions.list,
        )
        self.delete = to_raw_response_wrapper(
            sessions.delete,
        )

    @cached_property
    def public_share(self) -> PublicShareResourceWithRawResponse:
        return PublicShareResourceWithRawResponse(self._sessions.public_share)


class AsyncSessionsResourceWithRawResponse:
    def __init__(self, sessions: AsyncSessionsResource) -> None:
        self._sessions = sessions

        self.retrieve = async_to_raw_response_wrapper(
            sessions.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            sessions.update,
        )
        self.list = async_to_raw_response_wrapper(
            sessions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            sessions.delete,
        )

    @cached_property
    def public_share(self) -> AsyncPublicShareResourceWithRawResponse:
        return AsyncPublicShareResourceWithRawResponse(self._sessions.public_share)


class SessionsResourceWithStreamingResponse:
    def __init__(self, sessions: SessionsResource) -> None:
        self._sessions = sessions

        self.retrieve = to_streamed_response_wrapper(
            sessions.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            sessions.update,
        )
        self.list = to_streamed_response_wrapper(
            sessions.list,
        )
        self.delete = to_streamed_response_wrapper(
            sessions.delete,
        )

    @cached_property
    def public_share(self) -> PublicShareResourceWithStreamingResponse:
        return PublicShareResourceWithStreamingResponse(self._sessions.public_share)


class AsyncSessionsResourceWithStreamingResponse:
    def __init__(self, sessions: AsyncSessionsResource) -> None:
        self._sessions = sessions

        self.retrieve = async_to_streamed_response_wrapper(
            sessions.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            sessions.update,
        )
        self.list = async_to_streamed_response_wrapper(
            sessions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            sessions.delete,
        )

    @cached_property
    def public_share(self) -> AsyncPublicShareResourceWithStreamingResponse:
        return AsyncPublicShareResourceWithStreamingResponse(self._sessions.public_share)
