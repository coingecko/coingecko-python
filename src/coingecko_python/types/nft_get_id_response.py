# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = [
    "NFTGetIDResponse",
    "Ath",
    "AthChangePercentage",
    "AthDate",
    "BannerImage",
    "Explorer",
    "FloorPrice",
    "FloorPrice14dPercentageChange",
    "FloorPrice1yPercentageChange",
    "FloorPrice24hPercentageChange",
    "FloorPrice30dPercentageChange",
    "FloorPrice60dPercentageChange",
    "FloorPrice7dPercentageChange",
    "Image",
    "Links",
    "MarketCap",
    "MarketCap24hPercentageChange",
    "Volume24h",
    "Volume24hPercentageChange",
]


class Ath(BaseModel):
    native_currency: Optional[float] = None

    usd: Optional[float] = None


class AthChangePercentage(BaseModel):
    native_currency: Optional[float] = None

    usd: Optional[float] = None


class AthDate(BaseModel):
    native_currency: Optional[datetime] = None

    usd: Optional[datetime] = None


class BannerImage(BaseModel):
    small: Optional[str] = None


class Explorer(BaseModel):
    link: Optional[str] = None

    name: Optional[str] = None


class FloorPrice(BaseModel):
    native_currency: Optional[float] = None

    usd: Optional[float] = None


class FloorPrice14dPercentageChange(BaseModel):
    native_currency: Optional[float] = None

    usd: Optional[float] = None


class FloorPrice1yPercentageChange(BaseModel):
    native_currency: Optional[float] = None

    usd: Optional[float] = None


class FloorPrice24hPercentageChange(BaseModel):
    native_currency: Optional[float] = None

    usd: Optional[float] = None


class FloorPrice30dPercentageChange(BaseModel):
    native_currency: Optional[float] = None

    usd: Optional[float] = None


class FloorPrice60dPercentageChange(BaseModel):
    native_currency: Optional[float] = None

    usd: Optional[float] = None


class FloorPrice7dPercentageChange(BaseModel):
    native_currency: Optional[float] = None

    usd: Optional[float] = None


class Image(BaseModel):
    small: Optional[str] = None

    small_2x: Optional[str] = None


class Links(BaseModel):
    discord: Optional[str] = None

    homepage: Optional[str] = None

    twitter: Optional[str] = None


class MarketCap(BaseModel):
    native_currency: Optional[float] = None

    usd: Optional[float] = None


class MarketCap24hPercentageChange(BaseModel):
    native_currency: Optional[float] = None

    usd: Optional[float] = None


class Volume24h(BaseModel):
    native_currency: Optional[float] = None

    usd: Optional[float] = None


class Volume24hPercentageChange(BaseModel):
    native_currency: Optional[float] = None

    usd: Optional[float] = None


class NFTGetIDResponse(BaseModel):
    id: Optional[str] = None
    """NFT collection ID"""

    asset_platform_id: Optional[str] = None
    """NFT collection asset platform ID"""

    ath: Optional[Ath] = None
    """NFT collection all time highs"""

    ath_change_percentage: Optional[AthChangePercentage] = None
    """NFT collection all time highs change percentage"""

    ath_date: Optional[AthDate] = None
    """NFT collection all time highs date"""

    banner_image: Optional[BannerImage] = None
    """NFT collection banner image url"""

    contract_address: Optional[str] = None
    """NFT collection contract address"""

    description: Optional[str] = None
    """NFT collection description"""

    explorers: Optional[List[Explorer]] = None
    """NFT collection block explorers links"""

    floor_price: Optional[FloorPrice] = None
    """NFT collection floor price"""

    floor_price_14d_percentage_change: Optional[FloorPrice14dPercentageChange] = None
    """NFT collection floor price 14 days percentage change"""

    floor_price_1y_percentage_change: Optional[FloorPrice1yPercentageChange] = None
    """NFT collection floor price 1 year percentage change"""

    floor_price_24h_percentage_change: Optional[FloorPrice24hPercentageChange] = None

    floor_price_30d_percentage_change: Optional[FloorPrice30dPercentageChange] = None
    """NFT collection floor price 30 days percentage change"""

    floor_price_60d_percentage_change: Optional[FloorPrice60dPercentageChange] = None
    """NFT collection floor price 60 days percentage change"""

    floor_price_7d_percentage_change: Optional[FloorPrice7dPercentageChange] = None
    """NFT collection floor price 7 days percentage change"""

    floor_price_in_usd_24h_percentage_change: Optional[float] = None
    """NFT collection floor price in usd 24 hours percentage change"""

    image: Optional[Image] = None
    """NFT collection image url"""

    links: Optional[Links] = None
    """NFT collection links"""

    market_cap: Optional[MarketCap] = None
    """NFT collection market cap"""

    market_cap_24h_percentage_change: Optional[MarketCap24hPercentageChange] = None
    """NFT collection market cap 24 hours percentage change"""

    market_cap_rank: Optional[float] = None
    """coin market cap rank"""

    name: Optional[str] = None
    """NFT collection name"""

    native_currency: Optional[str] = None
    """NFT collection native currency"""

    native_currency_symbol: Optional[str] = None
    """NFT collection native currency symbol"""

    number_of_unique_addresses: Optional[float] = None
    """number of unique address owning the NFTs"""

    number_of_unique_addresses_24h_percentage_change: Optional[float] = None
    """number of unique address owning the NFTs 24 hours percentage change"""

    one_day_average_sale_price: Optional[float] = None
    """NFT collection one day average sale price"""

    one_day_average_sale_price_24h_percentage_change: Optional[float] = None
    """NFT collection one day average sale price 24 hours percentage change"""

    one_day_sales: Optional[float] = None
    """NFT collection one day sales"""

    one_day_sales_24h_percentage_change: Optional[float] = None
    """NFT collection one day sales 24 hours percentage change"""

    symbol: Optional[str] = None
    """NFT collection symbol"""

    total_supply: Optional[float] = None
    """NFT collection total supply"""

    user_favorites_count: Optional[float] = None
    """NFT collection user favorites count"""

    volume_24h: Optional[Volume24h] = None
    """NFT collection volume in 24 hours"""

    volume_24h_percentage_change: Optional[Volume24hPercentageChange] = None
    """NFT collection volume in 24 hours percentage change"""

    volume_in_usd_24h_percentage_change: Optional[float] = None
    """NFT collection volume in usd 24 hours percentage change"""
