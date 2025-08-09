# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .browser_profile_view import BrowserProfileView

__all__ = ["BrowserProfileListResponse"]


class BrowserProfileListResponse(BaseModel):
    items: List[BrowserProfileView]

    page_number: int = FieldInfo(alias="pageNumber")

    page_size: int = FieldInfo(alias="pageSize")

    total_items: int = FieldInfo(alias="totalItems")
