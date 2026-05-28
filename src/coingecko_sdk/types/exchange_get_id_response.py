# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = [
    "ExchangeGetIDResponse",
    "StatusUpdate",
    "StatusUpdateProject",
    "StatusUpdateProjectImage",
    "Ticker",
    "TickerConvertedLast",
    "TickerConvertedVolume",
    "TickerMarket",
]


class StatusUpdateProjectImage(BaseModel):
    """Project image URLs"""

    large: Optional[str] = None

    small: Optional[str] = None

    thumb: Optional[str] = None


class StatusUpdateProject(BaseModel):
    """Project information"""

    id: Optional[str] = None
    """Project ID"""

    image: Optional[StatusUpdateProjectImage] = None
    """Project image URLs"""

    name: Optional[str] = None
    """Project name"""

    type: Optional[str] = None
    """Project type"""


class StatusUpdate(BaseModel):
    category: Optional[str] = None
    """Status update category"""

    created_at: Optional[str] = None
    """Status update creation time"""

    description: Optional[str] = None
    """Status update description"""

    pin: Optional[bool] = None
    """Whether status update is pinned"""

    project: Optional[StatusUpdateProject] = None
    """Project information"""

    user: Optional[str] = None
    """Status update user"""

    user_title: Optional[str] = None
    """Status update user title"""


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

    name: Optional[str] = None
    """Exchange name"""


class Ticker(BaseModel):
    base: Optional[str] = None
    """Ticker base currency"""

    bid_ask_spread_percentage: Optional[float] = None
    """Bid-ask spread percentage"""

    coin_id: Optional[str] = None
    """Base currency coin ID"""

    coin_mcap_usd: Optional[float] = None
    """Coin market cap in USD"""

    converted_last: Optional[TickerConvertedLast] = None
    """Converted last price"""

    converted_volume: Optional[TickerConvertedVolume] = None
    """Converted trading volume"""

    is_anomaly: Optional[bool] = None
    """Whether ticker is anomalous"""

    is_stale: Optional[bool] = None
    """Whether ticker is stale"""

    last: Optional[float] = None
    """Last price"""

    last_fetch_at: Optional[str] = None
    """Last fetch timestamp"""

    last_traded_at: Optional[str] = None
    """Last traded timestamp"""

    market: Optional[TickerMarket] = None
    """Exchange information"""

    target: Optional[str] = None
    """Ticker target currency"""

    target_coin_id: Optional[str] = None
    """Target currency coin ID"""

    timestamp: Optional[str] = None
    """Ticker timestamp"""

    token_info_url: Optional[str] = None
    """Token info URL"""

    trade_url: Optional[str] = None
    """Trade URL"""

    trust_score: Optional[str] = None
    """Trust score"""

    volume: Optional[float] = None
    """Trading volume"""


class ExchangeGetIDResponse(BaseModel):
    alert_notice: str
    """Alert notice"""

    centralized: bool
    """Whether the exchange is centralized"""

    coins: float
    """Number of coins listed"""

    country: Optional[str] = None
    """Country where the exchange is based"""

    description: str
    """Exchange description"""

    facebook_url: str
    """Facebook URL"""

    has_trading_incentive: bool
    """Whether the exchange has trading incentive"""

    image: str
    """Exchange logo URL"""

    name: str
    """Exchange name"""

    other_url_1: str
    """Other URL 1"""

    other_url_2: str
    """Other URL 2"""

    pairs: float
    """Number of trading pairs"""

    public_notice: str
    """Public notice"""

    reddit_url: str
    """Reddit URL"""

    slack_url: str
    """Slack URL"""

    status_updates: List[StatusUpdate]
    """Status updates"""

    telegram_url: str
    """Telegram URL"""

    tickers: List[Ticker]
    """Exchange tickers"""

    trade_volume_24h_btc: float
    """Exchange 24h trading volume in BTC"""

    trust_score: Optional[float] = None
    """Exchange trust score"""

    trust_score_rank: Optional[float] = None
    """Exchange trust score rank"""

    twitter_handle: str
    """Twitter handle"""

    url: str
    """Exchange website URL"""

    year_established: Optional[float] = None
    """Year the exchange was established"""
