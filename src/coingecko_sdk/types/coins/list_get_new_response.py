# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["ListGetNewResponse", "ListGetNewResponseItem"]


class ListGetNewResponseItem(BaseModel):
    id: str
    """Coin ID"""

    activated_at: int
    """Timestamp when coin was activated on CoinGecko"""

    name: str
    """Coin name"""

    symbol: str
    """Coin symbol"""


ListGetNewResponse: TypeAlias = List[ListGetNewResponseItem]
