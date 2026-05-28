# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["ExchangeGetIDResponse", "Ticker", "TickerConvertedLast", "TickerConvertedVolume"]


class TickerConvertedLast(BaseModel):
    """Derivative converted last price"""

    btc: Optional[str] = None

    eth: Optional[str] = None

    usd: Optional[str] = None


class TickerConvertedVolume(BaseModel):
    """Derivative converted volume"""

    btc: Optional[str] = None

    eth: Optional[str] = None

    usd: Optional[str] = None


class Ticker(BaseModel):
    base: str
    """Derivative base asset"""

    bid_ask_spread: float
    """Derivative bid-ask spread"""

    coin_id: str
    """Derivative base asset coin ID"""

    contract_type: str
    """Derivative contract type"""

    converted_last: TickerConvertedLast
    """Derivative converted last price"""

    converted_volume: TickerConvertedVolume
    """Derivative converted volume"""

    expired_at: Optional[float] = None
    """Derivative expiry time in UNIX timestamp"""

    funding_rate: float
    """Derivative funding rate"""

    h24_percentage_change: float
    """Derivative price percentage change in 24 hours"""

    h24_volume: float
    """Derivative volume in 24 hours"""

    index: float
    """Derivative underlying asset price"""

    index_basis_percentage: float
    """Difference of derivative price and index price in percentage"""

    last: float
    """Derivative last price"""

    last_traded: float
    """Derivative last traded time in UNIX timestamp"""

    open_interest_usd: float
    """Derivative open interest in USD"""

    symbol: str
    """Derivative ticker symbol"""

    target: str
    """Derivative target asset"""

    target_coin_id: str
    """Derivative target asset coin ID"""

    trade_url: str
    """Derivative trade URL"""


class ExchangeGetIDResponse(BaseModel):
    country: Optional[str] = None
    """Derivatives exchange incorporated country"""

    description: str
    """Derivatives exchange description"""

    image: str
    """Derivatives exchange image URL"""

    name: str
    """Derivatives exchange name"""

    number_of_futures_pairs: int
    """Number of futures pairs in the derivatives exchange"""

    number_of_perpetual_pairs: int
    """Number of perpetual pairs in the derivatives exchange"""

    open_interest_btc: Optional[float] = None
    """Derivatives exchange open interest in BTC"""

    trade_volume_24h_btc: str
    """Derivatives exchange trade volume in BTC in 24 hours"""

    url: str
    """Derivatives exchange website URL"""

    year_established: Optional[int] = None
    """Derivatives exchange established year"""

    tickers: Optional[List[Ticker]] = None
    """Derivative tickers data, available when include_tickers is specified"""
