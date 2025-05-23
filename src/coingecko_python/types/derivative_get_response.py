# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["DerivativeGetResponse"]


class DerivativeGetResponse(BaseModel):
    basis: Optional[float] = None
    """difference of derivative price and index price"""

    contract_type: Optional[str] = None
    """derivative contract type"""

    expired_at: Optional[str] = None

    funding_rate: Optional[float] = None
    """derivative funding rate"""

    index: Optional[float] = None
    """derivative underlying asset price"""

    index_id: Optional[str] = None
    """derivative underlying asset"""

    last_traded_at: Optional[float] = None
    """derivative last updated time"""

    market: Optional[str] = None
    """derivative market name"""

    open_interest: Optional[float] = None
    """derivative open interest"""

    price: Optional[str] = None
    """derivative ticker price"""

    price_percentage_change_24h: Optional[float] = None
    """derivative ticker price percentage change in 24 hours"""

    spread: Optional[float] = None
    """derivative bid ask spread"""

    symbol: Optional[str] = None
    """derivative ticker symbol"""

    volume_24h: Optional[float] = None
    """derivative volume in 24 hours"""
