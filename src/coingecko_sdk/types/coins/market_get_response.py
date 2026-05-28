# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = [
    "MarketGetResponse",
    "MarketGetResponseItem",
    "MarketGetResponseItemRoi",
    "MarketGetResponseItemSparklineIn7d",
]


class MarketGetResponseItemRoi(BaseModel):
    """Return on investment data"""

    currency: Optional[str] = None
    """ROI currency"""

    percentage: Optional[float] = None
    """ROI percentage"""

    times: Optional[float] = None
    """ROI multiplier"""


class MarketGetResponseItemSparklineIn7d(BaseModel):
    """Sparkline price data for the last 7 days"""

    price: Optional[List[float]] = None
    """Array of price values"""


class MarketGetResponseItem(BaseModel):
    id: str
    """Coin ID"""

    ath: Optional[float] = None
    """All-time high price in target currency"""

    ath_change_percentage: Optional[float] = None
    """All-time high change percentage"""

    ath_date: Optional[datetime] = None
    """All-time high date"""

    atl: Optional[float] = None
    """All-time low price in target currency"""

    atl_change_percentage: Optional[float] = None
    """All-time low change percentage"""

    atl_date: Optional[datetime] = None
    """All-time low date"""

    circulating_supply: Optional[float] = None
    """Circulating supply"""

    current_price: Optional[float] = None
    """Current price in target currency"""

    fully_diluted_valuation: Optional[float] = None
    """Fully diluted valuation in target currency"""

    high_24h: Optional[float] = None
    """24-hour price high in target currency"""

    image: str
    """Coin image URL"""

    last_updated: datetime
    """Last updated timestamp"""

    low_24h: Optional[float] = None
    """24-hour price low in target currency"""

    market_cap: Optional[float] = None
    """Market cap in target currency"""

    market_cap_change_24h: Optional[float] = None
    """24-hour market cap change in target currency"""

    market_cap_change_percentage_24h: Optional[float] = None
    """24-hour market cap change percentage"""

    market_cap_rank: Optional[int] = None
    """Market cap rank"""

    max_supply: Optional[float] = None
    """Max supply"""

    name: str
    """Coin name"""

    price_change_24h: Optional[float] = None
    """24-hour price change in target currency"""

    price_change_percentage_24h: Optional[float] = None
    """24-hour price change percentage"""

    roi: Optional[MarketGetResponseItemRoi] = None
    """Return on investment data"""

    symbol: str
    """Coin symbol"""

    total_supply: Optional[float] = None
    """Total supply"""

    total_volume: Optional[float] = None
    """Total trading volume in target currency"""

    market_cap_rank_with_rehypothecated: Optional[int] = None
    """Market cap rank including rehypothecated tokens"""

    price_change_percentage_14d_in_currency: Optional[float] = None
    """14-day price change percentage in target currency"""

    price_change_percentage_1h_in_currency: Optional[float] = None
    """1-hour price change percentage in target currency"""

    price_change_percentage_1y_in_currency: Optional[float] = None
    """1-year price change percentage in target currency"""

    price_change_percentage_200d_in_currency: Optional[float] = None
    """200-day price change percentage in target currency"""

    price_change_percentage_24h_in_currency: Optional[float] = None
    """24-hour price change percentage in target currency"""

    price_change_percentage_30d_in_currency: Optional[float] = None
    """30-day price change percentage in target currency"""

    price_change_percentage_7d_in_currency: Optional[float] = None
    """7-day price change percentage in target currency"""

    sparkline_in_7d: Optional[MarketGetResponseItemSparklineIn7d] = None
    """Sparkline price data for the last 7 days"""


MarketGetResponse: TypeAlias = List[MarketGetResponseItem]
