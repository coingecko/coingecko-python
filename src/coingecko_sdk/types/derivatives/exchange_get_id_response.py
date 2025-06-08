# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["ExchangeGetIDResponse", "Ticker"]


class Ticker(BaseModel):
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


class ExchangeGetIDResponse(BaseModel):
    country: Optional[str] = None
    """derivatives exchange incorporated country"""

    description: Optional[str] = None
    """derivatives exchange description"""

    image: Optional[str] = None
    """derivatives exchange image url"""

    name: Optional[str] = None
    """derivatives exchange name"""

    number_of_futures_pairs: Optional[float] = None
    """number of futures pairs in the derivatives exchange"""

    number_of_perpetual_pairs: Optional[float] = None
    """number of perpetual pairs in the derivatives exchange"""

    open_interest_btc: Optional[float] = None
    """derivatives exchange open interest in BTC"""

    tickers: Optional[List[Ticker]] = None

    trade_volume_24h_btc: Optional[str] = None
    """derivatives exchange trade volume in BTC in 24 hours"""

    url: Optional[str] = None
    """derivatives exchange website url"""

    year_established: Optional[float] = None
    """derivatives exchange established year"""
