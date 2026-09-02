# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = ["RwaGetListResponse", "RwaGetListResponseItem"]


class RwaGetListResponseItem(BaseModel):
    id: str
    """RWA ID"""

    asset_type: Literal["stock", "commodity", "etf"]
    """RWA asset type"""

    name: str
    """RWA name"""

    symbol: str
    """RWA symbol"""


RwaGetListResponse: TypeAlias = List[RwaGetListResponseItem]
