# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["TopGainersLoserGetResponse", "TopGainersLoserGetResponseItem"]


class TopGainersLoserGetResponseItem(BaseModel):
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

    usd_1y_change: Optional[float] = None
    """coin 1 year change in USD"""

    usd_24h_vol: Optional[float] = None
    """coin 24hr volume in USD"""


TopGainersLoserGetResponse: TypeAlias = List[TopGainersLoserGetResponseItem]
