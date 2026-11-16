# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = ["UnderlyingGetListResponse", "UnderlyingGetListResponseItem"]


class UnderlyingGetListResponseItem(BaseModel):
    id: str
    """Underlying asset ID (coin ID or RWA ID)"""

    name: str
    """Underlying asset name"""

    symbol: str
    """Underlying asset symbol"""

    underlying_type: Literal["coin", "rwa"]
    """Underlying asset type"""


UnderlyingGetListResponse: TypeAlias = List[UnderlyingGetListResponseItem]
