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
    "Included",
    "IncludedAttributes",
]


class DataAttributes(BaseModel):
    address: str
    """Token contract address"""

    coingecko_coin_id: Optional[str] = None
    """CoinGecko coin ID"""

    decimals: int
    """Token decimals"""

    description: Optional[str] = None
    """Token description"""

    discord_url: Optional[str] = None
    """Discord URL"""

    farcaster_url: Optional[str] = None
    """Farcaster URL"""

    gt_score: Optional[float] = None
    """GeckoTerminal trust score"""

    image_url: Optional[str] = None
    """Token image URL"""

    metadata_updated_at: str
    """Metadata last updated timestamp"""

    name: str
    """Token name"""

    symbol: str
    """Token symbol"""

    telegram_handle: Optional[str] = None
    """Telegram handle"""

    twitter_handle: Optional[str] = None
    """Twitter handle"""

    websites: List[str]
    """Token websites"""

    zora_url: Optional[str] = None
    """Zora URL"""


class DataRelationshipsNetworkData(BaseModel):
    id: Optional[str] = None

    type: Optional[str] = None


class DataRelationshipsNetwork(BaseModel):
    data: Optional[DataRelationshipsNetworkData] = None


class DataRelationships(BaseModel):
    network: Optional[DataRelationshipsNetwork] = None


class Data(BaseModel):
    id: str
    """Token identifier"""

    attributes: DataAttributes

    relationships: DataRelationships

    type: str
    """Resource type"""


class IncludedAttributes(BaseModel):
    coingecko_asset_platform_id: Optional[str] = None

    name: Optional[str] = None


class Included(BaseModel):
    id: Optional[str] = None

    attributes: Optional[IncludedAttributes] = None

    type: Optional[str] = None


class InfoRecentlyUpdatedGetResponse(BaseModel):
    data: List[Data]

    included: Optional[List[Included]] = None
    """Included network data, present when include=network is specified"""
