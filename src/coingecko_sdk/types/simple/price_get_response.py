# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["PriceGetResponse", "PriceGetResponseItem"]


class PriceGetResponseItem(BaseModel):
    last_updated_at: Optional[float] = None
    """last updated timestamp"""

    usd: Optional[float] = None
    """price in USD"""

    usd_24h_change: Optional[float] = None
    """24hr change in USD"""

    usd_24h_vol: Optional[float] = None
    """24hr volume in USD"""

    usd_market_cap: Optional[float] = None
    """market cap in USD"""


PriceGetResponse: TypeAlias = Dict[str, PriceGetResponseItem]
