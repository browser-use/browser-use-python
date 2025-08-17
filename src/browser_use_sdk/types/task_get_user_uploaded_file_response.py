# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["TaskGetUserUploadedFileResponse"]


class TaskGetUserUploadedFileResponse(BaseModel):
    id: str

    download_url: str = FieldInfo(alias="downloadUrl")

    file_name: str = FieldInfo(alias="fileName")
