# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["ExchangeGetIDResponse", "Ticker", "TickerConvertedLast", "TickerConvertedVolume"]


class TickerConvertedLast(BaseModel):
    btc: Optional[str] = None

    eth: Optional[str] = None

    usd: Optional[str] = None


class TickerConvertedVolume(BaseModel):
    btc: Optional[str] = None

    eth: Optional[str] = None

    usd: Optional[str] = None


class Ticker(BaseModel):
    base: Optional[str] = None
    """derivative base asset"""

    bid_ask_spread: Optional[float] = None
    """derivative bid ask spread"""

    coin_id: Optional[str] = None
    """derivative base asset coin ID"""

    contract_type: Optional[str] = None
    """derivative contract type"""

    converted_last: Optional[TickerConvertedLast] = None

    converted_volume: Optional[TickerConvertedVolume] = None

    expired_at: Optional[str] = None

    funding_rate: Optional[float] = None
    """derivative funding rate"""

    h24_percentage_change: Optional[float] = None
    """derivative price percentage change in 24 hours"""

    h24_volume: Optional[float] = None
    """derivative volume in 24 hours"""

    index: Optional[float] = None
    """derivative underlying asset price"""

    index_basis_percentage: Optional[float] = None
    """difference of derivative price and index price in percentage"""

    last: Optional[float] = None
    """derivative last price"""

    last_traded: Optional[float] = None
    """derivative last updated time"""

    open_interest_usd: Optional[float] = None
    """derivative open interest in USD"""

    symbol: Optional[str] = None
    """derivative ticker symbol"""

    target: Optional[str] = None
    """derivative target asset"""

    target_coin_id: Optional[str] = None
    """derivative target asset coin ID"""

    trade_url: Optional[str] = None
    """derivative trade url"""


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

    trade_volume_24h_btc: Optional[float] = None
    """derivatives exchange trade volume in BTC in 24 hours"""

    url: Optional[str] = None
    """derivatives exchange website url"""

    year_established: Optional[float] = None
    """derivatives exchange established year"""
