# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["FileCreatePresignedURLParams"]


class FileCreatePresignedURLParams(TypedDict, total=False):
    content_type: Required[
        Annotated[
            Literal[
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
            PropertyInfo(alias="contentType"),
        ]
    ]

    file_name: Required[Annotated[str, PropertyInfo(alias="fileName")]]

    size_bytes: Required[Annotated[int, PropertyInfo(alias="sizeBytes")]]
