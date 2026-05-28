# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["NFTGetListResponse", "NFTGetListResponseItem"]


class NFTGetListResponseItem(BaseModel):
    id: str
    """NFT collection ID"""

    asset_platform_id: str
    """NFT collection asset platform ID"""

    contract_address: str
    """NFT collection contract address"""

    name: str
    """NFT collection name"""

    symbol: str
    """NFT collection symbol"""


NFTGetListResponse: TypeAlias = List[NFTGetListResponseItem]
