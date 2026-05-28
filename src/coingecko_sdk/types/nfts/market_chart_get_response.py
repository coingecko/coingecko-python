# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["MarketChartGetResponse"]


class MarketChartGetResponse(BaseModel):
    floor_price_native: List[List[float]]
    """NFT collection floor price in native currency as [timestamp, price] pairs"""

    floor_price_usd: List[List[float]]
    """NFT collection floor price in USD as [timestamp, price] pairs"""

    h24_volume_native: List[List[float]]
    """NFT collection 24h volume in native currency as [timestamp, volume] pairs"""

    h24_volume_usd: List[List[float]]
    """NFT collection 24h volume in USD as [timestamp, volume] pairs"""

    market_cap_native: List[List[float]]
    """NFT collection market cap in native currency as [timestamp, market_cap] pairs"""

    market_cap_usd: List[List[float]]
    """NFT collection market cap in USD as [timestamp, market_cap] pairs"""
