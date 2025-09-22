# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["TopGainersLoserGetResponse", "TopGainer", "TopLoser"]


class TopGainer(BaseModel):
    id: Optional[str] = None
    """coin ID"""

    image: Optional[str] = None
    """coin image url"""

    market_cap_rank: Optional[float] = None
    """coin rank by market cap"""

    name: Optional[str] = None
    """coin name"""

    symbol: Optional[str] = None
    """coin symbol"""

    usd: Optional[float] = None
    """coin price in USD"""

    usd_14d_change: Optional[float] = None
    """coin 14 day change percentage in USD"""

    usd_1h_change: Optional[float] = None
    """coin 1hr change percentage in USD"""

    usd_1y_change: Optional[float] = None
    """coin 1 year change percentage in USD"""

    usd_200d_change: Optional[float] = None
    """coin 200 day change percentage in USD"""

    usd_24h_change: Optional[float] = None
    """coin 24hr change percentage in USD"""

    usd_24h_vol: Optional[float] = None
    """coin 24hr volume in USD"""

    usd_30d_change: Optional[float] = None
    """coin 30 day change percentage in USD"""

    usd_7d_change: Optional[float] = None
    """coin 7 day change percentage in USD"""


class TopLoser(BaseModel):
    id: Optional[str] = None
    """coin ID"""

    image: Optional[str] = None
    """coin image url"""

    market_cap_rank: Optional[float] = None
    """coin rank by market cap"""

    name: Optional[str] = None
    """coin name"""

    symbol: Optional[str] = None
    """coin symbol"""

    usd: Optional[float] = None
    """coin price in USD"""

    usd_14d_change: Optional[float] = None
    """coin 14 day change percentage in USD"""

    usd_1h_change: Optional[float] = None
    """coin 1hr change percentage in USD"""

    usd_1y_change: Optional[float] = None
    """coin 1 year change percentage in USD"""

    usd_200d_change: Optional[float] = None
    """coin 200 day change percentage in USD"""

    usd_24h_change: Optional[float] = None
    """coin 24hr change percentage in USD"""

    usd_24h_vol: Optional[float] = None
    """coin 24hr volume in USD"""

    usd_30d_change: Optional[float] = None
    """coin 30 day change percentage in USD"""

    usd_7d_change: Optional[float] = None
    """coin 7 day change percentage in USD"""


class TopGainersLoserGetResponse(BaseModel):
    top_gainers: Optional[List[TopGainer]] = None

    top_losers: Optional[List[TopLoser]] = None
