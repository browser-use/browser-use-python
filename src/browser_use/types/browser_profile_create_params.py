# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .proxy_country_code import ProxyCountryCode

__all__ = ["BrowserProfileCreateParams"]


class BrowserProfileCreateParams(TypedDict, total=False):
    name: Required[str]

    ad_blocker: Annotated[bool, PropertyInfo(alias="adBlocker")]

    browser_viewport_height: Annotated[int, PropertyInfo(alias="browserViewportHeight")]

    browser_viewport_width: Annotated[int, PropertyInfo(alias="browserViewportWidth")]

    description: str

    is_mobile: Annotated[bool, PropertyInfo(alias="isMobile")]

    persist: bool

    proxy: bool

    proxy_country_code: Annotated[ProxyCountryCode, PropertyInfo(alias="proxyCountryCode")]

    store_cache: Annotated[bool, PropertyInfo(alias="storeCache")]
