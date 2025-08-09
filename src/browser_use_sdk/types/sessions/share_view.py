# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ShareView"]


class ShareView(BaseModel):
    share_token: str = FieldInfo(alias="shareToken")

    share_url: str = FieldInfo(alias="shareUrl")

    view_count: int = FieldInfo(alias="viewCount")

    last_viewed_at: Optional[datetime] = FieldInfo(alias="lastViewedAt", default=None)
