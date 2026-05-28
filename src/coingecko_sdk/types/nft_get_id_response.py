# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = [
    "NFTGetIDResponse",
    "Ath",
    "AthChangePercentage",
    "AthDate",
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
    """NFT collection all time highs"""

    native_currency: Optional[float] = None

    usd: Optional[float] = None


class AthChangePercentage(BaseModel):
    """NFT collection all time highs change percentage"""

    native_currency: Optional[float] = None

    usd: Optional[float] = None


class AthDate(BaseModel):
    """NFT collection all time highs date"""

    native_currency: Optional[datetime] = None

    usd: Optional[datetime] = None


class Explorer(BaseModel):
    link: Optional[str] = None

    name: Optional[str] = None


class FloorPrice(BaseModel):
    """NFT collection floor price"""

    native_currency: Optional[float] = None

    usd: Optional[float] = None


class FloorPrice14dPercentageChange(BaseModel):
    """NFT collection floor price 14 days percentage change"""

    native_currency: Optional[float] = None

    usd: Optional[float] = None


class FloorPrice1yPercentageChange(BaseModel):
    """NFT collection floor price 1 year percentage change"""

    native_currency: Optional[float] = None

    usd: Optional[float] = None


class FloorPrice24hPercentageChange(BaseModel):
    """NFT collection floor price 24 hours percentage change"""

    native_currency: Optional[float] = None

    usd: Optional[float] = None


class FloorPrice30dPercentageChange(BaseModel):
    """NFT collection floor price 30 days percentage change"""

    native_currency: Optional[float] = None

    usd: Optional[float] = None


class FloorPrice60dPercentageChange(BaseModel):
    """NFT collection floor price 60 days percentage change"""

    native_currency: Optional[float] = None

    usd: Optional[float] = None


class FloorPrice7dPercentageChange(BaseModel):
    """NFT collection floor price 7 days percentage change"""

    native_currency: Optional[float] = None

    usd: Optional[float] = None


class Image(BaseModel):
    """NFT collection image URLs"""

    small: Optional[str] = None

    small_2x: Optional[str] = None


class Links(BaseModel):
    """NFT collection links"""

    discord: Optional[str] = None

    homepage: Optional[str] = None

    twitter: Optional[str] = None


class MarketCap(BaseModel):
    """NFT collection market cap"""

    native_currency: Optional[float] = None

    usd: Optional[float] = None


class MarketCap24hPercentageChange(BaseModel):
    """NFT collection market cap 24 hours percentage change"""

    native_currency: Optional[float] = None

    usd: Optional[float] = None


class Volume24h(BaseModel):
    """NFT collection volume in 24 hours"""

    native_currency: Optional[float] = None

    usd: Optional[float] = None


class Volume24hPercentageChange(BaseModel):
    """NFT collection volume in 24 hours percentage change"""

    native_currency: Optional[float] = None

    usd: Optional[float] = None


class NFTGetIDResponse(BaseModel):
    id: str
    """NFT collection ID"""

    asset_platform_id: str
    """NFT collection asset platform ID"""

    ath: Ath
    """NFT collection all time highs"""

    ath_change_percentage: AthChangePercentage
    """NFT collection all time highs change percentage"""

    ath_date: AthDate
    """NFT collection all time highs date"""

    banner_image: str
    """NFT collection banner image URL"""

    contract_address: str
    """NFT collection contract address"""

    description: str
    """NFT collection description"""

    explorers: List[Explorer]
    """NFT collection block explorer links"""

    floor_price: FloorPrice
    """NFT collection floor price"""

    floor_price_14d_percentage_change: FloorPrice14dPercentageChange
    """NFT collection floor price 14 days percentage change"""

    floor_price_1y_percentage_change: FloorPrice1yPercentageChange
    """NFT collection floor price 1 year percentage change"""

    floor_price_24h_percentage_change: FloorPrice24hPercentageChange
    """NFT collection floor price 24 hours percentage change"""

    floor_price_30d_percentage_change: FloorPrice30dPercentageChange
    """NFT collection floor price 30 days percentage change"""

    floor_price_60d_percentage_change: FloorPrice60dPercentageChange
    """NFT collection floor price 60 days percentage change"""

    floor_price_7d_percentage_change: FloorPrice7dPercentageChange
    """NFT collection floor price 7 days percentage change"""

    floor_price_in_usd_24h_percentage_change: float
    """NFT collection floor price in USD 24 hours percentage change"""

    image: Image
    """NFT collection image URLs"""

    links: Links
    """NFT collection links"""

    market_cap: MarketCap
    """NFT collection market cap"""

    market_cap_24h_percentage_change: MarketCap24hPercentageChange
    """NFT collection market cap 24 hours percentage change"""

    market_cap_rank: Optional[int] = None
    """NFT collection market cap rank"""

    name: str
    """NFT collection name"""

    native_currency: str
    """NFT collection native currency"""

    native_currency_symbol: str
    """NFT collection native currency symbol"""

    number_of_unique_addresses: float
    """Number of unique addresses owning the NFTs"""

    number_of_unique_addresses_24h_percentage_change: float
    """Number of unique addresses 24 hours percentage change"""

    one_day_average_sale_price: Optional[float] = None
    """NFT collection one day average sale price"""

    one_day_average_sale_price_24h_percentage_change: float
    """NFT collection one day average sale price 24 hours percentage change"""

    one_day_sales: Optional[float] = None
    """NFT collection one day sales"""

    one_day_sales_24h_percentage_change: float
    """NFT collection one day sales 24 hours percentage change"""

    symbol: str
    """NFT collection symbol"""

    total_supply: float
    """NFT collection total supply"""

    user_favorites_count: int
    """NFT collection user favorites count"""

    volume_24h: Volume24h
    """NFT collection volume in 24 hours"""

    volume_24h_percentage_change: Volume24hPercentageChange
    """NFT collection volume in 24 hours percentage change"""

    volume_in_usd_24h_percentage_change: float
    """NFT collection volume in USD 24 hours percentage change"""

    web_slug: str
    """NFT collection web slug"""
