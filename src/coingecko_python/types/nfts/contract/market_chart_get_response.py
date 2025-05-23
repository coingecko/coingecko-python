# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["MarketChartGetResponse"]


class MarketChartGetResponse(BaseModel):
    floor_price_native: Optional[List[List[float]]] = None
    """NFT collection floor price in native currency"""

    floor_price_usd: Optional[List[List[float]]] = None
    """NFT collection floor price in usd"""

    h24_volume_native: Optional[List[List[float]]] = None
    """NFT collection volume in 24 hours in native currency"""

    h24_volume_usd: Optional[List[List[float]]] = None
    """NFT collection volume in 24 hours in usd"""

    market_cap_native: Optional[List[List[float]]] = None
    """NFT collection market cap in native currency"""

    market_cap_usd: Optional[List[List[float]]] = None
    """NFT collection market cap in usd"""
