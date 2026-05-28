# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = [
    "TokenItem",
    "Attributes",
    "AttributesVolumeUsd",
    "AttributesLaunchpadDetails",
    "Relationships",
    "RelationshipsTopPools",
    "RelationshipsTopPoolsData",
]


class AttributesVolumeUsd(BaseModel):
    """Volume in USD"""

    h24: Optional[str] = None


class AttributesLaunchpadDetails(BaseModel):
    """Launchpad details for pump-style tokens"""

    completed: Optional[bool] = None

    completed_at: Optional[str] = None

    graduation_percentage: Optional[float] = None

    migrated_destination_pool_address: Optional[str] = None


class Attributes(BaseModel):
    address: str
    """Token contract address"""

    coingecko_coin_id: Optional[str] = None
    """CoinGecko coin ID"""

    decimals: int
    """Token decimals"""

    fdv_usd: Optional[str] = None
    """Fully diluted valuation in USD"""

    image_url: Optional[str] = None
    """Token image URL"""

    market_cap_usd: Optional[str] = None
    """Market cap in USD"""

    name: str
    """Token name"""

    normalized_total_supply: str
    """Normalized token total supply"""

    price_usd: Optional[str] = None
    """Token price in USD"""

    symbol: str
    """Token symbol"""

    total_reserve_in_usd: str
    """Total reserve in USD across all pools"""

    total_supply: str
    """Token total supply"""

    volume_usd: AttributesVolumeUsd
    """Volume in USD"""

    last_trade_timestamp: Optional[str] = None
    """Last trade timestamp in UNIX"""

    launchpad_details: Optional[AttributesLaunchpadDetails] = None
    """Launchpad details for pump-style tokens"""


class RelationshipsTopPoolsData(BaseModel):
    id: Optional[str] = None

    type: Optional[str] = None


class RelationshipsTopPools(BaseModel):
    data: Optional[List[RelationshipsTopPoolsData]] = None


class Relationships(BaseModel):
    top_pools: Optional[RelationshipsTopPools] = None


class TokenItem(BaseModel):
    id: str
    """Token identifier"""

    attributes: Attributes

    relationships: Relationships

    type: str
    """Resource type"""
