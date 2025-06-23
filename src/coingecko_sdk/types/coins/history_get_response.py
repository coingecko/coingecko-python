# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ..._models import BaseModel

__all__ = [
    "HistoryGetResponse",
    "CommunityData",
    "DeveloperData",
    "DeveloperDataCodeAdditionsDeletions4Weeks",
    "Image",
    "MarketData",
    "MarketDataCurrentPrice",
    "MarketDataMarketCap",
    "MarketDataTotalVolume",
    "PublicInterestStats",
]


class CommunityData(BaseModel):
    facebook_likes: Optional[float] = None
    """coin facebook likes"""

    reddit_accounts_active_48h: Optional[float] = None
    """coin reddit accounts active 48h"""

    reddit_average_comments_48h: Optional[float] = None
    """coin reddit average comments 48h"""

    reddit_average_posts_48h: Optional[float] = None
    """coin reddit average posts 48h"""

    reddit_subscribers: Optional[float] = None
    """coin reddit subscribers"""


class DeveloperDataCodeAdditionsDeletions4Weeks(BaseModel):
    additions: Optional[float] = None

    deletions: Optional[float] = None


class DeveloperData(BaseModel):
    closed_issues: Optional[float] = None
    """coin repository closed issues"""

    code_additions_deletions_4_weeks: Optional[DeveloperDataCodeAdditionsDeletions4Weeks] = None
    """coin code additions deletions 4 weeks"""

    commit_count_4_weeks: Optional[float] = None
    """coin commit count 4 weeks"""

    forks: Optional[float] = None
    """coin repository forks"""

    pull_request_contributors: Optional[float] = None
    """coin repository pull request contributors"""

    pull_requests_merged: Optional[float] = None
    """coin repository pull requests merged"""

    stars: Optional[float] = None
    """coin repository stars"""

    subscribers: Optional[float] = None
    """coin repository subscribers"""

    total_issues: Optional[float] = None
    """coin repository total issues"""


class Image(BaseModel):
    small: Optional[str] = None

    thumb: Optional[str] = None


class MarketDataCurrentPrice(BaseModel):
    btc: Optional[float] = None

    eur: Optional[float] = None

    usd: Optional[float] = None


class MarketDataMarketCap(BaseModel):
    btc: Optional[float] = None

    eur: Optional[float] = None

    usd: Optional[float] = None


class MarketDataTotalVolume(BaseModel):
    btc: Optional[float] = None

    eur: Optional[float] = None

    usd: Optional[float] = None


class MarketData(BaseModel):
    current_price: Optional[MarketDataCurrentPrice] = None
    """coin current price"""

    market_cap: Optional[MarketDataMarketCap] = None
    """coin market cap"""

    total_volume: Optional[MarketDataTotalVolume] = None
    """coin total volume"""


class PublicInterestStats(BaseModel):
    alexa_rank: Optional[float] = None
    """coin alexa rank"""

    bing_matches: Optional[float] = None
    """coin bing matches"""


class HistoryGetResponse(BaseModel):
    id: Optional[str] = None
    """coin ID"""

    community_data: Optional[CommunityData] = None
    """coin community data"""

    developer_data: Optional[DeveloperData] = None
    """coin developer data"""

    image: Optional[Image] = None
    """coin image url"""

    localization: Optional[Dict[str, str]] = None
    """coin localization"""

    market_data: Optional[MarketData] = None
    """coin market data"""

    name: Optional[str] = None
    """coin name"""

    public_interest_stats: Optional[PublicInterestStats] = None
    """coin public interest stats"""

    symbol: Optional[str] = None
    """coin symbol"""
