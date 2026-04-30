# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["ExchangeGetListResponse", "ExchangeGetListResponseItem"]


class ExchangeGetListResponseItem(BaseModel):
    id: Optional[str] = None
    """derivatives exchange ID"""

    name: Optional[str] = None
    """derivatives exchange name"""


ExchangeGetListResponse: TypeAlias = List[ExchangeGetListResponseItem]
