# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AgentProfileCreateParams"]


class AgentProfileCreateParams(TypedDict, total=False):
    name: Required[str]

    allowed_domains: Annotated[List[str], PropertyInfo(alias="allowedDomains")]

    custom_system_prompt_extension: Annotated[str, PropertyInfo(alias="customSystemPromptExtension")]

    description: str

    flash_mode: Annotated[bool, PropertyInfo(alias="flashMode")]

    highlight_elements: Annotated[bool, PropertyInfo(alias="highlightElements")]

    max_agent_steps: Annotated[int, PropertyInfo(alias="maxAgentSteps")]

    thinking: bool

    vision: bool
