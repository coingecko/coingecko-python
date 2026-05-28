# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["TickerGetResponse", "Ticker", "TickerConvertedLast", "TickerConvertedVolume", "TickerMarket"]


class TickerConvertedLast(BaseModel):
    """Converted last price"""

    btc: Optional[float] = None

    eth: Optional[float] = None

    usd: Optional[float] = None


class TickerConvertedVolume(BaseModel):
    """Converted trading volume"""

    btc: Optional[float] = None

    eth: Optional[float] = None

    usd: Optional[float] = None


class TickerMarket(BaseModel):
    """Exchange information"""

    has_trading_incentive: Optional[bool] = None
    """Exchange trading incentive"""

    identifier: Optional[str] = None
    """Exchange identifier"""

    logo: Optional[str] = None
    """Exchange logo URL"""

    name: Optional[str] = None
    """Exchange name"""


class Ticker(BaseModel):
    base: str
    """Ticker base currency"""

    bid_ask_spread_percentage: float
    """Bid-ask spread percentage"""

    coin_id: str
    """Base currency coin ID"""

    coin_mcap_usd: float
    """Coin market cap in USD"""

    converted_last: TickerConvertedLast
    """Converted last price"""

    converted_volume: TickerConvertedVolume
    """Converted trading volume"""

    is_anomaly: bool
    """Whether ticker is anomalous"""

    is_stale: bool
    """Whether ticker is stale"""

    last: float
    """Last price"""

    last_fetch_at: str
    """Last fetch timestamp"""

    last_traded_at: str
    """Last traded timestamp"""

    market: TickerMarket
    """Exchange information"""

    target: str
    """Ticker target currency"""

    target_coin_id: str
    """Target currency coin ID"""

    timestamp: str
    """Ticker timestamp"""

    token_info_url: Optional[str] = None
    """Token info URL"""

    trade_url: str
    """Trade URL"""

    trust_score: Optional[str] = None
    """Trust score"""

    volume: float
    """Trading volume"""

    cost_to_move_down_usd: Optional[float] = None
    """Cost to move price down by 2% in USD"""

    cost_to_move_up_usd: Optional[float] = None
    """Cost to move price up by 2% in USD"""


class TickerGetResponse(BaseModel):
    name: str
    """Coin name"""

    tickers: List[Ticker]
    """List of tickers"""
