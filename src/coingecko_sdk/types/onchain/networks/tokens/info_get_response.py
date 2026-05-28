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

    categories: List[str]
    """Token categories"""

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


class Data(BaseModel):
    id: str
    """Token identifier"""

    attributes: DataAttributes

    type: str
    """Resource type"""


class InfoGetResponse(BaseModel):
    data: Data
