# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["TaskCreateResponse"]


class TaskCreateResponse(BaseModel):
    id: str

    session_id: str = FieldInfo(alias="sessionId")
