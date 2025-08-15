# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["MeRetrieveResponse"]


class MeRetrieveResponse(BaseModel):
    additional_credits_balance_usd: float = FieldInfo(alias="additionalCreditsBalanceUsd")

    monthly_credits_balance_usd: float = FieldInfo(alias="monthlyCreditsBalanceUsd")

    signed_up_at: datetime = FieldInfo(alias="signedUpAt")

    email: Optional[str] = None

    name: Optional[str] = None
