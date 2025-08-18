# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["TaskStepView"]


class TaskStepView(BaseModel):
    actions: List[str]

    evaluation_previous_goal: str = FieldInfo(alias="evaluationPreviousGoal")

    memory: str

    next_goal: str = FieldInfo(alias="nextGoal")

    number: int

    url: str

    screenshot_url: Optional[str] = FieldInfo(alias="screenshotUrl", default=None)
