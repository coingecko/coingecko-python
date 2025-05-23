# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["AssetPlatformGetResponse", "AssetPlatformGetResponseItem", "AssetPlatformGetResponseItemImage"]


class AssetPlatformGetResponseItemImage(BaseModel):
    large: Optional[str] = None

    small: Optional[str] = None

    thumb: Optional[str] = None


class AssetPlatformGetResponseItem(BaseModel):
    id: Optional[str] = None
    """asset platform ID"""

    chain_identifier: Optional[float] = None
    """chainlist's chain ID"""

    image: Optional[AssetPlatformGetResponseItemImage] = None
    """image of the asset platform"""

    name: Optional[str] = None
    """chain name"""

    native_coin_id: Optional[str] = None
    """chain native coin ID"""

    shortname: Optional[str] = None
    """chain shortname"""


AssetPlatformGetResponse: TypeAlias = List[AssetPlatformGetResponseItem]
