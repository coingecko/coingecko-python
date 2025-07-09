# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["MarketGetResponse", "MarketGetResponseItem", "MarketGetResponseItemRoi"]


class MarketGetResponseItemRoi(BaseModel):
    currency: str
    """ROI currency"""

    percentage: float
    """ROI percentage"""

    times: float
    """ROI multiplier"""


class MarketGetResponseItem(BaseModel):
    id: Optional[str] = None
    """coin ID"""

    ath: Optional[float] = None
    """coin all time high (ATH) in currency"""

    ath_change_percentage: Optional[float] = None
    """coin all time high (ATH) change in percentage"""

    ath_date: Optional[datetime] = None
    """coin all time high (ATH) date"""

    atl: Optional[float] = None
    """coin all time low (atl) in currency"""

    atl_change_percentage: Optional[float] = None
    """coin all time low (atl) change in percentage"""

    atl_date: Optional[datetime] = None
    """coin all time low (atl) date"""

    circulating_supply: Optional[float] = None
    """coin circulating supply"""

    current_price: Optional[float] = None
    """coin current price in currency"""

    fully_diluted_valuation: Optional[float] = None
    """coin fully diluted valuation (fdv) in currency"""

    high_24h: Optional[float] = None
    """coin 24hr price high in currency"""

    image: Optional[str] = None
    """coin image url"""

    last_updated: Optional[datetime] = None
    """coin last updated timestamp"""

    low_24h: Optional[float] = None
    """coin 24hr price low in currency"""

    market_cap: Optional[float] = None
    """coin market cap in currency"""

    market_cap_change_24h: Optional[float] = None
    """coin 24hr market cap change in currency"""

    market_cap_change_percentage_24h: Optional[float] = None
    """coin 24hr market cap change in percentage"""

    market_cap_rank: Optional[float] = None
    """coin rank by market cap"""

    max_supply: Optional[float] = None
    """coin max supply"""

    name: Optional[str] = None
    """coin name"""

    price_change_24h: Optional[float] = None
    """coin 24hr price change in currency"""

    price_change_percentage_24h: Optional[float] = None
    """coin 24hr price change in percentage"""

    roi: Optional[MarketGetResponseItemRoi] = None
    """return on investment data"""

    symbol: Optional[str] = None
    """coin symbol"""

    total_supply: Optional[float] = None
    """coin total supply"""

    total_volume: Optional[float] = None
    """coin total trading volume in currency"""


MarketGetResponse: TypeAlias = List[MarketGetResponseItem]
