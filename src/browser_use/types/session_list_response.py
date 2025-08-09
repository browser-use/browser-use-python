# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .session_view import SessionView

__all__ = ["SessionListResponse"]


class SessionListResponse(BaseModel):
    items: List[SessionView]

    page_number: int = FieldInfo(alias="pageNumber")

    page_size: int = FieldInfo(alias="pageSize")

    total_items: int = FieldInfo(alias="totalItems")
