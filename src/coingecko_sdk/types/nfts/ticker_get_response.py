# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["TickerGetResponse", "Ticker"]


class Ticker(BaseModel):
    floor_price_in_native_currency: Optional[float] = None
    """NFT collection floor price in native currency"""

    h24_volume_in_native_currency: Optional[float] = None
    """NFT collection volume in 24 hours in native currency"""

    image: Optional[str] = None
    """NFT marketplace image url"""

    name: Optional[str] = None
    """NFT marketplace name"""

    native_currency: Optional[str] = None
    """NFT collection native currency"""

    native_currency_symbol: Optional[str] = None
    """NFT collection native currency symbol"""

    nft_collection_url: Optional[str] = None
    """NFT collection url in the NFT marketplace"""

    nft_marketplace_id: Optional[str] = None
    """NFT marketplace ID"""

    updated_at: Optional[str] = None
    """last updated time"""


class TickerGetResponse(BaseModel):
    tickers: Optional[List[Ticker]] = None
