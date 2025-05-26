# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = [
    "InfoRecentlyUpdatedGetResponse",
    "Data",
    "DataAttributes",
    "DataRelationships",
    "DataRelationshipsNetwork",
    "DataRelationshipsNetworkData",
]


class DataAttributes(BaseModel):
    address: Optional[str] = None

    coingecko_coin_id: Optional[str] = None

    description: Optional[str] = None

    gt_score: Optional[float] = None

    image_url: Optional[str] = None

    metadata_updated_at: Optional[str] = None

    name: Optional[str] = None

    symbol: Optional[str] = None

    websites: Optional[List[str]] = None


class DataRelationshipsNetworkData(BaseModel):
    id: Optional[str] = None

    type: Optional[str] = None


class DataRelationshipsNetwork(BaseModel):
    data: Optional[DataRelationshipsNetworkData] = None


class DataRelationships(BaseModel):
    network: Optional[DataRelationshipsNetwork] = None


class Data(BaseModel):
    id: Optional[str] = None

    attributes: Optional[DataAttributes] = None

    relationships: Optional[DataRelationships] = None

    type: Optional[str] = None


class InfoRecentlyUpdatedGetResponse(BaseModel):
    data: Optional[Data] = None
