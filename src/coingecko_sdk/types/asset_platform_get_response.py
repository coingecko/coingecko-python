# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["AssetPlatformGetResponse", "AssetPlatformGetResponseItem", "AssetPlatformGetResponseItemImage"]


class AssetPlatformGetResponseItemImage(BaseModel):
    """Asset platform image URLs"""

    large: Optional[str] = None
    """Large image URL"""

    small: Optional[str] = None
    """Small image URL"""

    thumb: Optional[str] = None
    """Thumbnail image URL"""


class AssetPlatformGetResponseItem(BaseModel):
    id: str
    """Asset platform ID"""

    chain_identifier: Optional[float] = None
    """Chainlist's chain ID"""

    image: AssetPlatformGetResponseItemImage
    """Asset platform image URLs"""

    name: str
    """Chain name"""

    native_coin_id: Optional[str] = None
    """Chain native coin ID"""

    shortname: str
    """Chain shortname"""


AssetPlatformGetResponse: TypeAlias = List[AssetPlatformGetResponseItem]
