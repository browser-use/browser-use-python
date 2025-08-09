# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TaskListParams"]


class TaskListParams(TypedDict, total=False):
    include_output_files: Annotated[bool, PropertyInfo(alias="includeOutputFiles")]

    include_steps: Annotated[bool, PropertyInfo(alias="includeSteps")]

    include_user_uploaded_files: Annotated[bool, PropertyInfo(alias="includeUserUploadedFiles")]

    page_number: Annotated[int, PropertyInfo(alias="pageNumber")]

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]
