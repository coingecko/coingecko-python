# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["KeyGetResponse"]


class KeyGetResponse(BaseModel):
    api_key_current_total_monthly_calls: int
    """Total API calls made this month by this API key"""

    api_key_monthly_call_credit: int
    """Monthly call credit limit configured for this API key"""

    api_key_rate_limit_request_per_minute: int
    """Rate limit per minute configured for this API key"""

    current_remaining_monthly_calls: int
    """Remaining API call credits this month"""

    current_total_monthly_calls: int
    """Total API calls made this month"""

    monthly_call_credit: int
    """Total monthly API call credits for the plan"""

    plan: str
    """Current subscription plan"""

    rate_limit_request_per_minute: int
    """Rate limit per minute for the plan"""
