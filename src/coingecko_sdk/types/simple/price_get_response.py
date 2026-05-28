# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["PriceGetResponse", "PriceGetResponseItem"]


class PriceGetResponseItem(BaseModel):
    last_updated_at: Optional[float] = None
    """Last updated timestamp in UNIX seconds"""

    usd: Optional[float] = None
    """Price in the target currency"""

    usd_24h_change: Optional[float] = None
    """24-hour price change percentage in the target currency"""

    usd_24h_vol: Optional[float] = None
    """24-hour trading volume in the target currency"""

    usd_market_cap: Optional[float] = None
    """Market capitalization in the target currency"""


PriceGetResponse: TypeAlias = Dict[str, PriceGetResponseItem]
