# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .proxy_country_code import ProxyCountryCode

__all__ = ["BrowserProfileView"]


class BrowserProfileView(BaseModel):
    id: str

    ad_blocker: bool = FieldInfo(alias="adBlocker")

    browser_viewport_height: int = FieldInfo(alias="browserViewportHeight")

    browser_viewport_width: int = FieldInfo(alias="browserViewportWidth")

    created_at: datetime = FieldInfo(alias="createdAt")

    description: str

    is_mobile: bool = FieldInfo(alias="isMobile")

    name: str

    persist: bool

    proxy: bool

    proxy_country_code: ProxyCountryCode = FieldInfo(alias="proxyCountryCode")

    store_cache: bool = FieldInfo(alias="storeCache")

    updated_at: datetime = FieldInfo(alias="updatedAt")
