# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "RwaGetMarketsResponse",
    "RwaGetMarketsResponseItem",
    "RwaGetMarketsResponseItemTokenizedMarketData",
    "RwaGetMarketsResponseItemTokenizedMarketDataSparklineIn7d",
]


class RwaGetMarketsResponseItemTokenizedMarketDataSparklineIn7d(BaseModel):
    """Sparkline price data for the last 7 days"""

    price: Optional[List[float]] = None
    """Array of price values"""


class RwaGetMarketsResponseItemTokenizedMarketData(BaseModel):
    """Aggregated tokenized market data"""

    current_price: Optional[float] = None
    """Current price in target currency"""

    high_24h: Optional[float] = None
    """24-hour price high in target currency"""

    last_updated: Optional[datetime] = None
    """Last updated timestamp"""

    low_24h: Optional[float] = None
    """24-hour price low in target currency"""

    market_cap: Optional[float] = None
    """Market cap in target currency"""

    market_cap_change_24h: Optional[float] = None
    """24-hour market cap change in target currency"""

    market_cap_change_percentage_24h: Optional[float] = None
    """24-hour market cap change percentage"""

    price_change_24h: Optional[float] = None
    """24-hour price change in target currency"""

    price_change_percentage_14d_in_currency: Optional[float] = None
    """14-day price change percentage in target currency"""

    price_change_percentage_1h_in_currency: Optional[float] = None
    """1-hour price change percentage in target currency"""

    price_change_percentage_1y_in_currency: Optional[float] = None
    """1-year price change percentage in target currency"""

    price_change_percentage_200d_in_currency: Optional[float] = None
    """200-day price change percentage in target currency"""

    price_change_percentage_24h: Optional[float] = None
    """24-hour price change percentage"""

    price_change_percentage_24h_in_currency: Optional[float] = None
    """24-hour price change percentage in target currency"""

    price_change_percentage_30d_in_currency: Optional[float] = None
    """30-day price change percentage in target currency"""

    price_change_percentage_7d_in_currency: Optional[float] = None
    """7-day price change percentage in target currency"""

    sparkline_in_7d: Optional[RwaGetMarketsResponseItemTokenizedMarketDataSparklineIn7d] = None
    """Sparkline price data for the last 7 days"""

    total_volume: Optional[float] = None
    """Total trading volume in target currency"""


class RwaGetMarketsResponseItem(BaseModel):
    id: str
    """RWA ID"""

    asset_type: Literal["stock", "commodity", "etf"]
    """RWA asset type"""

    image: str
    """Large image URL of the token with the largest market cap"""

    name: str
    """RWA name"""

    symbol: str
    """RWA symbol"""

    tokenized_market_data: RwaGetMarketsResponseItemTokenizedMarketData
    """Aggregated tokenized market data"""


RwaGetMarketsResponse: TypeAlias = List[RwaGetMarketsResponseItem]
