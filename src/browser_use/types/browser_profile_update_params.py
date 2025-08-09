# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .proxy_country_code import ProxyCountryCode

__all__ = ["BrowserProfileUpdateParams"]


class BrowserProfileUpdateParams(TypedDict, total=False):
    ad_blocker: Annotated[Optional[bool], PropertyInfo(alias="adBlocker")]

    browser_viewport_height: Annotated[Optional[int], PropertyInfo(alias="browserViewportHeight")]

    browser_viewport_width: Annotated[Optional[int], PropertyInfo(alias="browserViewportWidth")]

    description: Optional[str]

    is_mobile: Annotated[Optional[bool], PropertyInfo(alias="isMobile")]

    name: Optional[str]

    persist: Optional[bool]

    proxy: Optional[bool]

    proxy_country_code: Annotated[Optional[ProxyCountryCode], PropertyInfo(alias="proxyCountryCode")]

    store_cache: Annotated[Optional[bool], PropertyInfo(alias="storeCache")]
