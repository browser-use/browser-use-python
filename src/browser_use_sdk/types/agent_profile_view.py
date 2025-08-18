# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AgentProfileView"]


class AgentProfileView(BaseModel):
    id: str

    allowed_domains: List[str] = FieldInfo(alias="allowedDomains")

    created_at: datetime = FieldInfo(alias="createdAt")

    custom_system_prompt_extension: str = FieldInfo(alias="customSystemPromptExtension")

    description: str

    flash_mode: bool = FieldInfo(alias="flashMode")

    highlight_elements: bool = FieldInfo(alias="highlightElements")

    max_agent_steps: int = FieldInfo(alias="maxAgentSteps")

    name: str

    thinking: bool

    updated_at: datetime = FieldInfo(alias="updatedAt")

    vision: bool
