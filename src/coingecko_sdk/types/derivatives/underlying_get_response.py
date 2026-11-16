# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = ["UnderlyingGetResponse", "UnderlyingGetResponseItem"]


class UnderlyingGetResponseItem(BaseModel):
    id: str
    """Underlying asset ID (coin ID or RWA ID)"""

    current_price: float
    """Underlying asset price in USD"""

    funding_rate: float
    """Derivative funding rate"""

    name: str
    """Underlying asset name"""

    open_interest: Optional[float] = None
    """Derivative open interest in USD"""

    open_interest_change_percentage_1h: float
    """Derivative 1-hour open interest change percentage"""

    open_interest_change_percentage_24h: float
    """Derivative 24-hour open interest change percentage"""

    price_change_percentage_24h: float
    """Underlying asset 24-hour price change percentage"""

    symbol: str
    """Underlying asset symbol"""

    total_volume: Optional[float] = None
    """Derivative total trading volume in USD"""

    underlying_type: Literal["coin", "rwa"]
    """Underlying asset type"""


UnderlyingGetResponse: TypeAlias = List[UnderlyingGetResponseItem]
