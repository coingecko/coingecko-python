# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = [
    "TrendingSearchGetResponse",
    "Data",
    "DataAttributes",
    "DataAttributesVolumeUsd",
    "DataRelationships",
    "DataRelationshipsBaseToken",
    "DataRelationshipsBaseTokenData",
    "DataRelationshipsDex",
    "DataRelationshipsDexData",
    "DataRelationshipsNetwork",
    "DataRelationshipsNetworkData",
    "DataRelationshipsQuoteToken",
    "DataRelationshipsQuoteTokenData",
    "Included",
    "IncludedAttributes",
]


class DataAttributesVolumeUsd(BaseModel):
    """Volume in USD"""

    h24: Optional[str] = None


class DataAttributes(BaseModel):
    address: str
    """Pool contract address"""

    fdv_usd: Optional[str] = None
    """Fully diluted valuation in USD"""

    market_cap_usd: Optional[str] = None
    """Market cap in USD"""

    name: str
    """Pool name"""

    pool_created_at: str
    """Pool creation timestamp"""

    reserve_in_usd: Optional[str] = None
    """Total reserve in USD"""

    trending_rank: int
    """Trending search rank (0-based)"""

    volume_usd: DataAttributesVolumeUsd
    """Volume in USD"""


class DataRelationshipsBaseTokenData(BaseModel):
    id: Optional[str] = None

    type: Optional[str] = None


class DataRelationshipsBaseToken(BaseModel):
    data: Optional[DataRelationshipsBaseTokenData] = None


class DataRelationshipsDexData(BaseModel):
    id: Optional[str] = None

    type: Optional[str] = None


class DataRelationshipsDex(BaseModel):
    data: Optional[DataRelationshipsDexData] = None


class DataRelationshipsNetworkData(BaseModel):
    id: Optional[str] = None

    type: Optional[str] = None


class DataRelationshipsNetwork(BaseModel):
    data: Optional[DataRelationshipsNetworkData] = None


class DataRelationshipsQuoteTokenData(BaseModel):
    id: Optional[str] = None

    type: Optional[str] = None


class DataRelationshipsQuoteToken(BaseModel):
    data: Optional[DataRelationshipsQuoteTokenData] = None


class DataRelationships(BaseModel):
    """Related resources"""

    base_token: Optional[DataRelationshipsBaseToken] = None

    dex: Optional[DataRelationshipsDex] = None

    network: Optional[DataRelationshipsNetwork] = None

    quote_token: Optional[DataRelationshipsQuoteToken] = None


class Data(BaseModel):
    id: str
    """Pool identifier"""

    attributes: DataAttributes

    relationships: DataRelationships
    """Related resources"""

    type: str
    """Resource type"""


class IncludedAttributes(BaseModel):
    address: Optional[str] = None

    coingecko_asset_platform_id: Optional[str] = None

    coingecko_coin_id: Optional[str] = None

    decimals: Optional[int] = None

    image_url: Optional[str] = None

    name: Optional[str] = None

    symbol: Optional[str] = None


class Included(BaseModel):
    id: Optional[str] = None

    attributes: Optional[IncludedAttributes] = None

    type: Optional[str] = None


class TrendingSearchGetResponse(BaseModel):
    data: List[Data]

    included: Optional[List[Included]] = None
    """Included related resources, present when include parameter is specified"""
