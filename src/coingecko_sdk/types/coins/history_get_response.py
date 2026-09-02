# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ..._models import BaseModel

__all__ = ["HistoryGetResponse", "Image", "MarketData", "PublicInterestStats"]


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
