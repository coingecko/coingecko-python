# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["GlobalGetResponse", "Data", "DataFearAndGreedIndex"]


class DataFearAndGreedIndex(BaseModel):
    """Crypto Fear & Greed Index"""

    sentiment: Literal["extreme_fear", "fear", "neutral", "greed", "extreme_greed"]
    """Sentiment label based on the index value"""

    value: int
    """Crypto Fear & Greed Index value"""


class Data(BaseModel):
    active_cryptocurrencies: int
    """Number of active cryptocurrencies"""

    ended_icos: int
    """Number of ended ICOs"""

    market_cap_change_percentage_24h_usd: float
    """Market cap change percentage in 24 hours in USD"""

    market_cap_percentage: Dict[str, float]
    """Market cap percentage by coin"""

    markets: int
    """Number of exchanges"""

    ongoing_icos: int
    """Number of ongoing ICOs"""

    total_market_cap: Dict[str, float]
    """Total cryptocurrency market cap by currency"""

    total_volume: Dict[str, float]
    """Total cryptocurrency volume by currency"""

    upcoming_icos: int
    """Number of upcoming ICOs"""

    updated_at: int
    """Last updated time in UNIX timestamp"""

    volume_change_percentage_24h_usd: float
    """Volume change percentage in 24 hours in USD"""

    fear_and_greed_index: Optional[DataFearAndGreedIndex] = None
    """Crypto Fear & Greed Index"""


class GlobalGetResponse(BaseModel):
    data: Data
