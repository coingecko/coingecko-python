# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["NFTGetListResponse"]


class NFTGetListResponse(BaseModel):
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
