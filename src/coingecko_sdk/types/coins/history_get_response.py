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
    "PublicInterestStats",
]


class CommunityData(BaseModel):
    """Community engagement data"""

    facebook_likes: Optional[float] = None
    """Number of Facebook likes"""

    reddit_accounts_active_48h: Optional[float] = None
    """Active Reddit accounts in 48 hours"""

    reddit_average_comments_48h: Optional[float] = None
    """Average Reddit comments in 48 hours"""

    reddit_average_posts_48h: Optional[float] = None
    """Average Reddit posts in 48 hours"""

    reddit_subscribers: Optional[float] = None
    """Number of Reddit subscribers"""


class DeveloperDataCodeAdditionsDeletions4Weeks(BaseModel):
    """Code additions and deletions in the last 4 weeks"""

    additions: Optional[float] = None
    """Lines added"""

    deletions: Optional[float] = None
    """Lines deleted"""


class DeveloperData(BaseModel):
    """Developer activity data"""

    closed_issues: Optional[float] = None
    """Closed issues"""

    code_additions_deletions_4_weeks: Optional[DeveloperDataCodeAdditionsDeletions4Weeks] = None
    """Code additions and deletions in the last 4 weeks"""

    commit_count_4_weeks: Optional[float] = None
    """Commit count in the last 4 weeks"""

    forks: Optional[float] = None
    """Repository forks"""

    pull_request_contributors: Optional[float] = None
    """Pull request contributors"""

    pull_requests_merged: Optional[float] = None
    """Pull requests merged"""

    stars: Optional[float] = None
    """Repository stars"""

    subscribers: Optional[float] = None
    """Repository subscribers"""

    total_issues: Optional[float] = None
    """Total issues"""


class Image(BaseModel):
    """Coin image URLs"""

    small: Optional[str] = None
    """Small image URL"""

    thumb: Optional[str] = None
    """Thumbnail image URL"""


class MarketData(BaseModel):
    """Market data at the given date"""

    current_price: Optional[Dict[str, float]] = None
    """Current price keyed by currency"""

    market_cap: Optional[Dict[str, float]] = None
    """Market capitalization keyed by currency"""

    total_volume: Optional[Dict[str, float]] = None
    """Total trading volume keyed by currency"""


class PublicInterestStats(BaseModel):
    """Public interest statistics"""

    alexa_rank: Optional[float] = None
    """Alexa rank"""

    bing_matches: Optional[float] = None
    """Bing search matches"""


class HistoryGetResponse(BaseModel):
    id: str
    """Coin ID"""

    community_data: CommunityData
    """Community engagement data"""

    developer_data: DeveloperData
    """Developer activity data"""

    image: Image
    """Coin image URLs"""

    market_data: MarketData
    """Market data at the given date"""

    name: str
    """Coin name"""

    public_interest_stats: PublicInterestStats
    """Public interest statistics"""

    symbol: str
    """Coin symbol"""

    localization: Optional[Dict[str, str]] = None
    """Localized coin names keyed by locale code"""
