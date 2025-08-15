# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.users.me import file_create_presigned_url_params
from ....types.users.me.file_create_presigned_url_response import FileCreatePresignedURLResponse

__all__ = ["FilesResource", "AsyncFilesResource"]


class FilesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/browser-use/browser-use-python#accessing-raw-response-data-eg-headers
        """
        return FilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/browser-use/browser-use-python#with_streaming_response
        """
        return FilesResourceWithStreamingResponse(self)

    def create_presigned_url(
        self,
        *,
        content_type: Literal[
            "image/jpg",
            "image/jpeg",
            "image/png",
            "image/gif",
            "image/webp",
            "image/svg+xml",
            "application/pdf",
            "application/msword",
            "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            "application/vnd.ms-excel",
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            "text/plain",
            "text/csv",
            "text/markdown",
        ],
        file_name: str,
        size_bytes: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FileCreatePresignedURLResponse:
        """
        Get a presigned URL for uploading files that AI agents can use during tasks.

        This endpoint generates a secure, time-limited upload URL that allows you to
        upload files directly to our storage system. These files can then be referenced
        in AI agent tasks for the agent to work with.

        Supported use cases:

        - Uploading documents for data extraction tasks
        - Providing reference materials for agents
        - Sharing files that agents need to process
        - Including images or PDFs for analysis

        The upload URL expires after 2 minutes for security. Files are automatically
        organized by user ID and can be referenced in task creation using the returned
        file name.

        Args:

        - request: File upload details including name, content type, and size

        Returns:

        - Presigned upload URL and form fields for direct file upload

        Raises:

        - 400: If the content type is unsupported
        - 500: If the upload URL generation fails (should not happen)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/users/me/files/presigned-url",
            body=maybe_transform(
                {
                    "content_type": content_type,
                    "file_name": file_name,
                    "size_bytes": size_bytes,
                },
                file_create_presigned_url_params.FileCreatePresignedURLParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileCreatePresignedURLResponse,
        )


class AsyncFilesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/browser-use/browser-use-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/browser-use/browser-use-python#with_streaming_response
        """
        return AsyncFilesResourceWithStreamingResponse(self)

    async def create_presigned_url(
        self,
        *,
        content_type: Literal[
            "image/jpg",
            "image/jpeg",
            "image/png",
            "image/gif",
            "image/webp",
            "image/svg+xml",
            "application/pdf",
            "application/msword",
            "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            "application/vnd.ms-excel",
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            "text/plain",
            "text/csv",
            "text/markdown",
        ],
        file_name: str,
        size_bytes: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FileCreatePresignedURLResponse:
        """
        Get a presigned URL for uploading files that AI agents can use during tasks.

        This endpoint generates a secure, time-limited upload URL that allows you to
        upload files directly to our storage system. These files can then be referenced
        in AI agent tasks for the agent to work with.

        Supported use cases:

        - Uploading documents for data extraction tasks
        - Providing reference materials for agents
        - Sharing files that agents need to process
        - Including images or PDFs for analysis

        The upload URL expires after 2 minutes for security. Files are automatically
        organized by user ID and can be referenced in task creation using the returned
        file name.

        Args:

        - request: File upload details including name, content type, and size

        Returns:

        - Presigned upload URL and form fields for direct file upload

        Raises:

        - 400: If the content type is unsupported
        - 500: If the upload URL generation fails (should not happen)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/users/me/files/presigned-url",
            body=await async_maybe_transform(
                {
                    "content_type": content_type,
                    "file_name": file_name,
                    "size_bytes": size_bytes,
                },
                file_create_presigned_url_params.FileCreatePresignedURLParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileCreatePresignedURLResponse,
        )


class FilesResourceWithRawResponse:
    def __init__(self, files: FilesResource) -> None:
        self._files = files

        self.create_presigned_url = to_raw_response_wrapper(
            files.create_presigned_url,
        )


class AsyncFilesResourceWithRawResponse:
    def __init__(self, files: AsyncFilesResource) -> None:
        self._files = files

        self.create_presigned_url = async_to_raw_response_wrapper(
            files.create_presigned_url,
        )


class FilesResourceWithStreamingResponse:
    def __init__(self, files: FilesResource) -> None:
        self._files = files

        self.create_presigned_url = to_streamed_response_wrapper(
            files.create_presigned_url,
        )


class AsyncFilesResourceWithStreamingResponse:
    def __init__(self, files: AsyncFilesResource) -> None:
        self._files = files

        self.create_presigned_url = async_to_streamed_response_wrapper(
            files.create_presigned_url,
        )
