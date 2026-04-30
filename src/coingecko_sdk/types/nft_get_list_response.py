# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["NFTGetListResponse", "NFTGetListResponseItem"]


class NFTGetListResponseItem(BaseModel):
    id: Optional[str] = None
    """NFT collection ID"""

    asset_platform_id: Optional[str] = None
    """NFT collection asset platform ID"""

    contract_address: Optional[str] = None
    """NFT collection contract address"""

    name: Optional[str] = None
    """NFT collection name"""

    symbol: Optional[str] = None
    """NFT collection symbol"""


NFTGetListResponse: TypeAlias = List[NFTGetListResponseItem]
