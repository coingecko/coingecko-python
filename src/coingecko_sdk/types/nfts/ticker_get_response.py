# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["TickerGetResponse", "Ticker"]


class Ticker(BaseModel):
    floor_price_in_native_currency: float
    """NFT collection floor price in native currency"""

    h24_volume_in_native_currency: float
    """NFT collection volume in 24 hours in native currency"""

    image: str
    """NFT marketplace image URL"""

    name: str
    """NFT marketplace name"""

    native_currency: str
    """NFT collection native currency"""

    native_currency_symbol: str
    """NFT collection native currency symbol"""

    nft_collection_url: str
    """NFT collection URL in the NFT marketplace"""

    nft_marketplace_id: str
    """NFT marketplace ID"""

    updated_at: str
    """Last updated time"""


class TickerGetResponse(BaseModel):
    tickers: List[Ticker]
