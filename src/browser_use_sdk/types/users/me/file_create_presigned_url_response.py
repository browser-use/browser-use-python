# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["FileCreatePresignedURLResponse"]


class FileCreatePresignedURLResponse(BaseModel):
    expires_in: int = FieldInfo(alias="expiresIn")

    fields: Dict[str, str]

    file_name: str = FieldInfo(alias="fileName")

    method: Literal["POST"]

    url: str
