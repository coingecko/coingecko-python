# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["EntityGetListResponse", "EntityGetListResponseItem"]


class EntityGetListResponseItem(BaseModel):
    id: Optional[str] = None
    """entity ID"""

    country: Optional[str] = None
    """country code"""

    name: Optional[str] = None
    """entity name"""

    symbol: Optional[str] = None
    """ticker symbol of public company"""


EntityGetListResponse: TypeAlias = List[EntityGetListResponseItem]
