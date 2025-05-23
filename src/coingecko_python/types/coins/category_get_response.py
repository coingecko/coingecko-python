# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["CategoryGetResponse"]


class CategoryGetResponse(BaseModel):
    id: Optional[str] = None
    """category ID"""

    content: Optional[str] = None
    """category description"""

    market_cap: Optional[float] = None
    """category market cap"""

    market_cap_change_24h: Optional[float] = None
    """category market cap change in 24 hours"""

    name: Optional[str] = None
    """category name"""

    top_3_coins: Optional[List[str]] = None
    """images of top 3 coins in the category"""

    top_3_coins_id: Optional[List[str]] = None
    """IDs of top 3 coins in the category"""

    updated_at: Optional[str] = None
    """category last updated time"""

    volume_24h: Optional[float] = None
    """category volume in 24 hours"""
