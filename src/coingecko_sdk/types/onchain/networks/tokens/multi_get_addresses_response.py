# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ....._models import BaseModel

__all__ = [
    "MultiGetAddressesResponse",
    "Data",
    "DataAttributes",
    "DataAttributesVolumeUsd",
    "DataRelationships",
    "DataRelationshipsTopPools",
    "DataRelationshipsTopPoolsData",
]


class DataAttributesVolumeUsd(BaseModel):
    h24: Optional[str] = None


class DataAttributes(BaseModel):
    address: Optional[str] = None

    coingecko_coin_id: Optional[str] = None

    decimals: Optional[int] = None

    fdv_usd: Optional[str] = None

    image_url: Optional[str] = None

    market_cap_usd: Optional[str] = None

    name: Optional[str] = None

    normalized_total_supply: Optional[str] = None

    price_usd: Optional[str] = None

    symbol: Optional[str] = None

    total_reserve_in_usd: Optional[str] = None

    total_supply: Optional[str] = None

    volume_usd: Optional[DataAttributesVolumeUsd] = None


class DataRelationshipsTopPoolsData(BaseModel):
    id: Optional[str] = None

    type: Optional[str] = None


class DataRelationshipsTopPools(BaseModel):
    data: Optional[List[DataRelationshipsTopPoolsData]] = None


class DataRelationships(BaseModel):
    top_pools: Optional[DataRelationshipsTopPools] = None


class Data(BaseModel):
    id: Optional[str] = None

    attributes: Optional[DataAttributes] = None

    relationships: Optional[DataRelationships] = None

    type: Optional[str] = None


class MultiGetAddressesResponse(BaseModel):
    data: Optional[List[Data]] = None
