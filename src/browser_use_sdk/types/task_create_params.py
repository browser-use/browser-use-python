# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .llm_model import LlmModel

__all__ = ["TaskCreateParams", "AgentSettings", "BrowserSettings"]


class TaskCreateParams(TypedDict, total=False):
    task: Required[str]

    agent_settings: Annotated[AgentSettings, PropertyInfo(alias="agentSettings")]
    """Configuration settings for the AI agent

    Attributes: llm: The LLM model to use for the agent (default: O3 - best
    performance for now) profile_id: ID of the agent profile to use for the task
    (None for default)
    """

    browser_settings: Annotated[BrowserSettings, PropertyInfo(alias="browserSettings")]
    """Configuration settings for the browser session

    Attributes: session_id: ID of existing session to continue (None for new
    session) profile_id: ID of browser profile to use (None for default)
    save_browser_data: Whether to save browser state/data for the user to download
    later
    """

    included_file_names: Annotated[Optional[List[str]], PropertyInfo(alias="includedFileNames")]

    metadata: Optional[Dict[str, str]]

    secrets: Optional[Dict[str, str]]

    structured_output_json: Annotated[Optional[str], PropertyInfo(alias="structuredOutputJson")]


class AgentSettings(TypedDict, total=False):
    llm: LlmModel

    profile_id: Annotated[Optional[str], PropertyInfo(alias="profileId")]


class BrowserSettings(TypedDict, total=False):
    profile_id: Annotated[Optional[str], PropertyInfo(alias="profileId")]

    save_browser_data: Annotated[bool, PropertyInfo(alias="saveBrowserData")]

    session_id: Annotated[Optional[str], PropertyInfo(alias="sessionId")]
