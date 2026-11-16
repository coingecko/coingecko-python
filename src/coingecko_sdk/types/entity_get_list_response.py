# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["EntityGetListResponse", "EntityGetListResponseItem"]


class EntityGetListResponseItem(BaseModel):
    id: str
    """Entity ID"""

    country: str
    """Country code"""

    name: str
    """Entity name"""

    symbol: str
    """Ticker symbol of public company"""

    figi: Optional[str] = None
    """Financial Instrument Global Identifier (FIGI) of the entity"""


EntityGetListResponse: TypeAlias = List[EntityGetListResponseItem]
