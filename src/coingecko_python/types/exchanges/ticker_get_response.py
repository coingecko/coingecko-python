# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["TickerGetResponse", "Ticker", "TickerConvertedLast", "TickerConvertedVolume", "TickerMarket"]


class TickerConvertedLast(BaseModel):
    btc: Optional[float] = None

    eth: Optional[float] = None

    usd: Optional[float] = None


class TickerConvertedVolume(BaseModel):
    btc: Optional[float] = None

    eth: Optional[float] = None

    usd: Optional[float] = None


class TickerMarket(BaseModel):
    has_trading_incentive: bool
    """exchange trading incentive"""

    identifier: str
    """exchange identifier"""

    name: str
    """exchange name"""

    logo: Optional[str] = None
    """exchange image url"""


class Ticker(BaseModel):
    base: Optional[str] = None
    """coin ticker base currency"""

    bid_ask_spread_percentage: Optional[float] = None
    """coin ticker bid ask spread percentage"""

    coin_id: Optional[str] = None
    """coin ticker base currency coin ID"""

    converted_last: Optional[TickerConvertedLast] = None
    """coin ticker converted last price"""

    converted_volume: Optional[TickerConvertedVolume] = None
    """coin ticker converted volume"""

    cost_to_move_down_usd: Optional[float] = None
    """coin ticker cost to move down in usd"""

    cost_to_move_up_usd: Optional[float] = None
    """coin ticker cost to move up in usd"""

    is_anomaly: Optional[bool] = None
    """coin ticker anomaly"""

    is_stale: Optional[bool] = None
    """coin ticker stale"""

    last: Optional[float] = None
    """coin ticker last price"""

    last_fetch_at: Optional[str] = None
    """coin ticker last fetch timestamp"""

    last_traded_at: Optional[str] = None
    """coin ticker last traded timestamp"""

    market: Optional[TickerMarket] = None
    """coin ticker exchange"""

    target: Optional[str] = None
    """coin ticker target currency"""

    target_coin_id: Optional[str] = None
    """coin ticker target currency coin ID"""

    timestamp: Optional[str] = None
    """coin ticker timestamp"""

    token_info_url: Optional[str] = None
    """coin ticker token info url"""

    trade_url: Optional[str] = None
    """coin ticker trade url"""

    trust_score: Optional[str] = None
    """coin ticker trust score"""

    volume: Optional[float] = None
    """coin ticker volume"""


class TickerGetResponse(BaseModel):
    name: Optional[str] = None
    """coin name"""

    tickers: Optional[List[Ticker]] = None
    """list of tickers"""
