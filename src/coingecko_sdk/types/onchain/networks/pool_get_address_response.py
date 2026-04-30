# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .pool_data import PoolData
from ...._models import BaseModel

__all__ = ["PoolGetAddressResponse", "Included", "IncludedAttributes"]


class IncludedAttributes(BaseModel):
    address: Optional[str] = None

    coingecko_coin_id: Optional[str] = None

    decimals: Optional[int] = None

    image_url: Optional[str] = None

    name: Optional[str] = None

    symbol: Optional[str] = None


class Included(BaseModel):
    id: Optional[str] = None

    attributes: Optional[IncludedAttributes] = None

    type: Optional[str] = None


class PoolGetAddressResponse(BaseModel):
    data: Optional[PoolData] = None

    included: Optional[List[Included]] = None
