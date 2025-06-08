# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["KeyGetResponse"]


class KeyGetResponse(BaseModel):
    current_remaining_monthly_calls: Optional[float] = None

    current_total_monthly_calls: Optional[float] = None

    monthly_call_credit: Optional[float] = None

    plan: Optional[str] = None

    rate_limit_request_per_minute: Optional[float] = None
