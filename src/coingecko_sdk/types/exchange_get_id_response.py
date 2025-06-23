# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = [
    "ExchangeGetIDResponse",
    "Ticker",
    "TickerTicker",
    "TickerTickerConvertedLast",
    "TickerTickerConvertedVolume",
    "TickerTickerMarket",
]


class TickerTickerConvertedLast(BaseModel):
    btc: Optional[float] = None

    eth: Optional[float] = None

    usd: Optional[float] = None


class TickerTickerConvertedVolume(BaseModel):
    btc: Optional[float] = None

    eth: Optional[float] = None

    usd: Optional[float] = None


class TickerTickerMarket(BaseModel):
    has_trading_incentive: bool
    """exchange trading incentive"""

    identifier: str
    """exchange identifier"""

    name: str
    """exchange name"""

    logo: Optional[str] = None
    """exchange image url"""


class TickerTicker(BaseModel):
    base: Optional[str] = None
    """coin ticker base currency"""

    bid_ask_spread_percentage: Optional[float] = None
    """coin ticker bid ask spread percentage"""

    coin_id: Optional[str] = None
    """coin ticker base currency coin ID"""

    converted_last: Optional[TickerTickerConvertedLast] = None
    """coin ticker converted last price"""

    converted_volume: Optional[TickerTickerConvertedVolume] = None
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

    market: Optional[TickerTickerMarket] = None
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


class Ticker(BaseModel):
    name: Optional[str] = None
    """coin name"""

    tickers: Optional[List[TickerTicker]] = None
    """list of tickers"""


class ExchangeGetIDResponse(BaseModel):
    alert_notice: Optional[str] = None
    """alert notice for exchange"""

    centralized: Optional[bool] = None
    """exchange type (true for centralized, false for decentralized)"""

    coins: Optional[float] = None
    """number of coins listed on the exchange"""

    country: Optional[str] = None
    """exchange incorporated country"""

    description: Optional[str] = None
    """exchange description"""

    facebook_url: Optional[str] = None
    """exchange facebook url"""

    has_trading_incentive: Optional[bool] = None
    """exchange trading incentive"""

    image: Optional[str] = None
    """exchange image url"""

    name: Optional[str] = None
    """exchange name"""

    other_url_1: Optional[str] = None

    other_url_2: Optional[str] = None

    pairs: Optional[float] = None
    """number of trading pairs on the exchange"""

    public_notice: Optional[str] = None
    """public notice for exchange"""

    reddit_url: Optional[str] = None
    """exchange reddit url"""

    slack_url: Optional[str] = None
    """exchange slack url"""

    telegram_url: Optional[str] = None
    """exchange telegram url"""

    tickers: Optional[List[Ticker]] = None

    trade_volume_24h_btc: Optional[float] = None

    trust_score: Optional[float] = None
    """exchange trust score"""

    trust_score_rank: Optional[float] = None
    """exchange trust score rank"""

    twitter_handle: Optional[str] = None
    """exchange twitter handle"""

    url: Optional[str] = None
    """exchange website url"""

    year_established: Optional[float] = None
    """exchange established year"""
