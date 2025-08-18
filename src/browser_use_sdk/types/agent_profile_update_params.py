# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AgentProfileUpdateParams"]


class AgentProfileUpdateParams(TypedDict, total=False):
    allowed_domains: Annotated[Optional[List[str]], PropertyInfo(alias="allowedDomains")]

    custom_system_prompt_extension: Annotated[Optional[str], PropertyInfo(alias="customSystemPromptExtension")]

    description: Optional[str]

    flash_mode: Annotated[Optional[bool], PropertyInfo(alias="flashMode")]

    highlight_elements: Annotated[Optional[bool], PropertyInfo(alias="highlightElements")]

    max_agent_steps: Annotated[Optional[int], PropertyInfo(alias="maxAgentSteps")]

    name: Optional[str]

    thinking: Optional[bool]

    vision: Optional[bool]
