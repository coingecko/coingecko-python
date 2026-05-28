# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["CategoryGetResponse", "CategoryGetResponseItem"]


class CategoryGetResponseItem(BaseModel):
    id: str
    """Category ID"""

    content: str
    """Category description"""

    market_cap: float
    """Category market cap"""

    market_cap_change_24h: float
    """Category market cap change in 24 hours"""

    name: str
    """Category name"""

    top_3_coins: List[str]
    """Image URLs of top 3 coins in the category"""

    top_3_coins_id: List[str]
    """IDs of top 3 coins in the category"""

    updated_at: str
    """Category last updated timestamp"""

    volume_24h: float
    """Category trading volume in 24 hours"""


CategoryGetResponse: TypeAlias = List[CategoryGetResponseItem]
