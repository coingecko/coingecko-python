# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["ListGetNewResponse", "ListGetNewResponseItem"]


class ListGetNewResponseItem(BaseModel):
    id: Optional[str] = None
    """coin ID"""

    activated_at: Optional[float] = None
    """timestamp when coin was activated on CoinGecko"""

    name: Optional[str] = None
    """coin name"""

    symbol: Optional[str] = None
    """coin symbol"""


ListGetNewResponse: TypeAlias = List[ListGetNewResponseItem]
