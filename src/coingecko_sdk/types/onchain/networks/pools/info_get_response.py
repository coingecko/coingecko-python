# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional

from ....._models import BaseModel

__all__ = [
    "InfoGetResponse",
    "Data",
    "DataAttributes",
    "DataAttributesGtScoreDetails",
    "DataAttributesHolders",
    "DataAttributesImage",
    "DataRelationships",
    "DataRelationshipsPool",
    "DataRelationshipsPoolData",
    "Included",
    "IncludedAttributes",
]


class DataAttributesGtScoreDetails(BaseModel):
    """GeckoTerminal trust score breakdown"""

    creation: Optional[float] = None

    holders: Optional[float] = None

    info: Optional[float] = None

    pool: Optional[float] = None

    transaction: Optional[float] = None


class DataAttributesHolders(BaseModel):
    """Token holder information"""

    count: Optional[int] = None
    """Number of holders"""

    distribution_percentage: Optional[Dict[str, str]] = None
    """Holder distribution percentage (keys vary by chain, e.g.

    top_10, 11_30, 31_50, rest)
    """

    last_updated: Optional[str] = None
    """Last updated timestamp"""


class DataAttributesImage(BaseModel):
    """Token image URLs in different sizes"""

    large: Optional[str] = None

    small: Optional[str] = None

    thumb: Optional[str] = None


class DataAttributes(BaseModel):
    address: str
    """Token contract address"""

    banner_image_url: Optional[str] = None
    """Token banner image URL"""

    categories: List[str]
    """Token categories"""

    coingecko_coin_id: Optional[str] = None
    """CoinGecko coin ID"""

    decimals: int
    """Token decimals"""

    description: Optional[str] = None
    """Token description"""

    developer_address: Optional[str] = None
    """Developer wallet address"""

    developer_holding_percentage: Optional[str] = None
    """Developer holding as a percentage of total supply"""

    discord_url: Optional[str] = None
    """Discord URL"""

    farcaster_url: Optional[str] = None
    """Farcaster URL"""

    freeze_authority: Optional[str] = None
    """Freeze authority status"""

    gt_category_ids: List[str]
    """GeckoTerminal category IDs"""

    gt_score: float
    """GeckoTerminal trust score"""

    gt_score_details: DataAttributesGtScoreDetails
    """GeckoTerminal trust score breakdown"""

    gt_verified: bool
    """Whether the token is verified on GeckoTerminal"""

    holders: DataAttributesHolders
    """Token holder information"""

    image: DataAttributesImage
    """Token image URLs in different sizes"""

    image_url: Optional[str] = None
    """Token image URL"""

    is_honeypot: Union[bool, str]
    """Whether the token is a honeypot (boolean or 'unknown')"""

    mint_authority: Optional[str] = None
    """Mint authority status"""

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


class DataRelationshipsPoolData(BaseModel):
    id: Optional[str] = None

    type: Optional[str] = None


class DataRelationshipsPool(BaseModel):
    data: Optional[DataRelationshipsPoolData] = None


class DataRelationships(BaseModel):
    pool: Optional[DataRelationshipsPool] = None


class Data(BaseModel):
    id: str
    """Token identifier"""

    attributes: DataAttributes

    relationships: DataRelationships

    type: str
    """Resource type"""


class IncludedAttributes(BaseModel):
    base_token_address: Optional[str] = None
    """Base token contract address"""

    community_sus_report: Optional[int] = None
    """GeckoTerminal community suspicious reports count"""

    quote_token_address: Optional[str] = None
    """Quote token contract address"""

    quote_token_addresses: Optional[List[str]] = None
    """Quote token contract addresses, present for pools with more than 2 tokens"""

    sentiment_vote_negative_percentage: Optional[float] = None
    """GeckoTerminal community negative sentiment vote percentage"""

    sentiment_vote_positive_percentage: Optional[float] = None
    """GeckoTerminal community positive sentiment vote percentage"""


class Included(BaseModel):
    id: Optional[str] = None

    attributes: Optional[IncludedAttributes] = None

    type: Optional[str] = None


class InfoGetResponse(BaseModel):
    data: List[Data]

    included: Optional[List[Included]] = None
    """Included pool data, present when include=pool is specified"""
