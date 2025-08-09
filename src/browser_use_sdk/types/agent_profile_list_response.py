# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .agent_profile_view import AgentProfileView

__all__ = ["AgentProfileListResponse"]


class AgentProfileListResponse(BaseModel):
    items: List[AgentProfileView]

    page_number: int = FieldInfo(alias="pageNumber")

    page_size: int = FieldInfo(alias="pageSize")

    total_items: int = FieldInfo(alias="totalItems")
