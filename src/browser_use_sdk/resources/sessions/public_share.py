# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.sessions.share_view import ShareView

__all__ = ["PublicShareResource", "AsyncPublicShareResource"]


class PublicShareResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PublicShareResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/browser-use/browser-use-python#accessing-raw-response-data-eg-headers
        """
        return PublicShareResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PublicShareResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/browser-use/browser-use-python#with_streaming_response
        """
        return PublicShareResourceWithStreamingResponse(self)

    def create(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ShareView:
        """
        Create a public share for a session.

        Generates a public sharing link that allows anyone with the URL to view the
        session and its tasks. If a public share already exists for the session, it will
        return the existing share instead of creating a new one.

        Public shares are useful for:

        - Sharing results with clients or team members
        - Demonstrating AI agent capabilities
        - Collaborative review of automated tasks

        Args:

        - session_id: The unique identifier of the agent session to share

        Returns:

        - Public share information including the share URL and usage statistics

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
        return self._post(
            f"/sessions/{session_id}/public-share",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShareView,
        )

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
    ) -> ShareView:
        """
        Get information about the public share for a session.

        Retrieves details about the public sharing link for a session, including the
        share token, public URL, view count, and last viewed timestamp. This is useful
        for monitoring how your shared sessions are being accessed.

        Args:

        - session_id: The unique identifier of the agent session

        Returns:

        - Public share information including the share URL and usage statistics

        Raises:

        - 404: If the user agent session doesn't exist or doesn't have a public share

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            f"/sessions/{session_id}/public-share",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShareView,
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
        Remove the public share for a session.

        Deletes the public sharing link for a session, making it no longer accessible to
        anyone with the previous share URL. This is useful for removing access to
        sensitive sessions or when you no longer want to share the results.

        Args:

        - session_id: The unique identifier of the agent session

        Returns:

        - 204 No Content on successful deletion (idempotent)

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/sessions/{session_id}/public-share",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncPublicShareResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPublicShareResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/browser-use/browser-use-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPublicShareResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPublicShareResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/browser-use/browser-use-python#with_streaming_response
        """
        return AsyncPublicShareResourceWithStreamingResponse(self)

    async def create(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ShareView:
        """
        Create a public share for a session.

        Generates a public sharing link that allows anyone with the URL to view the
        session and its tasks. If a public share already exists for the session, it will
        return the existing share instead of creating a new one.

        Public shares are useful for:

        - Sharing results with clients or team members
        - Demonstrating AI agent capabilities
        - Collaborative review of automated tasks

        Args:

        - session_id: The unique identifier of the agent session to share

        Returns:

        - Public share information including the share URL and usage statistics

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
        return await self._post(
            f"/sessions/{session_id}/public-share",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShareView,
        )

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
    ) -> ShareView:
        """
        Get information about the public share for a session.

        Retrieves details about the public sharing link for a session, including the
        share token, public URL, view count, and last viewed timestamp. This is useful
        for monitoring how your shared sessions are being accessed.

        Args:

        - session_id: The unique identifier of the agent session

        Returns:

        - Public share information including the share URL and usage statistics

        Raises:

        - 404: If the user agent session doesn't exist or doesn't have a public share

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            f"/sessions/{session_id}/public-share",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShareView,
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
        Remove the public share for a session.

        Deletes the public sharing link for a session, making it no longer accessible to
        anyone with the previous share URL. This is useful for removing access to
        sensitive sessions or when you no longer want to share the results.

        Args:

        - session_id: The unique identifier of the agent session

        Returns:

        - 204 No Content on successful deletion (idempotent)

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/sessions/{session_id}/public-share",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class PublicShareResourceWithRawResponse:
    def __init__(self, public_share: PublicShareResource) -> None:
        self._public_share = public_share

        self.create = to_raw_response_wrapper(
            public_share.create,
        )
        self.retrieve = to_raw_response_wrapper(
            public_share.retrieve,
        )
        self.delete = to_raw_response_wrapper(
            public_share.delete,
        )


class AsyncPublicShareResourceWithRawResponse:
    def __init__(self, public_share: AsyncPublicShareResource) -> None:
        self._public_share = public_share

        self.create = async_to_raw_response_wrapper(
            public_share.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            public_share.retrieve,
        )
        self.delete = async_to_raw_response_wrapper(
            public_share.delete,
        )


class PublicShareResourceWithStreamingResponse:
    def __init__(self, public_share: PublicShareResource) -> None:
        self._public_share = public_share

        self.create = to_streamed_response_wrapper(
            public_share.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            public_share.retrieve,
        )
        self.delete = to_streamed_response_wrapper(
            public_share.delete,
        )


class AsyncPublicShareResourceWithStreamingResponse:
    def __init__(self, public_share: AsyncPublicShareResource) -> None:
        self._public_share = public_share

        self.create = async_to_streamed_response_wrapper(
            public_share.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            public_share.retrieve,
        )
        self.delete = async_to_streamed_response_wrapper(
            public_share.delete,
        )
