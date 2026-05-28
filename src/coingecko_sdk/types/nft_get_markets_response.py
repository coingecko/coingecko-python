# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = [
    "NFTGetMarketsResponse",
    "NFTGetMarketsResponseItem",
    "NFTGetMarketsResponseItemFloorPrice",
    "NFTGetMarketsResponseItemFloorPrice24hPercentageChange",
    "NFTGetMarketsResponseItemImage",
    "NFTGetMarketsResponseItemMarketCap",
    "NFTGetMarketsResponseItemMarketCap24hPercentageChange",
    "NFTGetMarketsResponseItemVolume24h",
    "NFTGetMarketsResponseItemVolume24hPercentageChange",
]


class NFTGetMarketsResponseItemFloorPrice(BaseModel):
    """NFT collection floor price"""

    native_currency: Optional[float] = None

    usd: Optional[float] = None


class NFTGetMarketsResponseItemFloorPrice24hPercentageChange(BaseModel):
    """NFT collection floor price 24 hours percentage change"""

    native_currency: Optional[float] = None

    usd: Optional[float] = None


class NFTGetMarketsResponseItemImage(BaseModel):
    """NFT collection image URLs"""

    small: Optional[str] = None

    small_2x: Optional[str] = None


class NFTGetMarketsResponseItemMarketCap(BaseModel):
    """NFT collection market cap"""

    native_currency: Optional[float] = None

    usd: Optional[float] = None


class NFTGetMarketsResponseItemMarketCap24hPercentageChange(BaseModel):
    """NFT collection market cap 24 hours percentage change"""

    native_currency: Optional[float] = None

    usd: Optional[float] = None


class NFTGetMarketsResponseItemVolume24h(BaseModel):
    """NFT collection volume in 24 hours"""

    native_currency: Optional[float] = None

    usd: Optional[float] = None


class NFTGetMarketsResponseItemVolume24hPercentageChange(BaseModel):
    """NFT collection volume in 24 hours percentage change"""

    native_currency: Optional[float] = None

    usd: Optional[float] = None


class NFTGetMarketsResponseItem(BaseModel):
    id: str
    """NFT collection ID"""

    asset_platform_id: str
    """NFT collection asset platform ID"""

    contract_address: Optional[str] = None
    """NFT collection contract address"""

    description: Optional[str] = None
    """NFT collection description"""

    floor_price: NFTGetMarketsResponseItemFloorPrice
    """NFT collection floor price"""

    floor_price_24h_percentage_change: NFTGetMarketsResponseItemFloorPrice24hPercentageChange
    """NFT collection floor price 24 hours percentage change"""

    floor_price_in_usd_24h_percentage_change: float
    """NFT collection floor price in USD 24 hours percentage change"""

    image: NFTGetMarketsResponseItemImage
    """NFT collection image URLs"""

    market_cap: NFTGetMarketsResponseItemMarketCap
    """NFT collection market cap"""

    market_cap_24h_percentage_change: NFTGetMarketsResponseItemMarketCap24hPercentageChange
    """NFT collection market cap 24 hours percentage change"""

    name: str
    """NFT collection name"""

    native_currency: str
    """NFT collection native currency"""

    native_currency_symbol: str
    """NFT collection native currency symbol"""

    number_of_unique_addresses: Optional[float] = None
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

    total_supply: Optional[float] = None
    """NFT collection total supply"""

    volume_24h: NFTGetMarketsResponseItemVolume24h
    """NFT collection volume in 24 hours"""

    volume_24h_percentage_change: NFTGetMarketsResponseItemVolume24hPercentageChange
    """NFT collection volume in 24 hours percentage change"""

    volume_in_usd_24h_percentage_change: float
    """NFT collection volume in USD 24 hours percentage change"""


NFTGetMarketsResponse: TypeAlias = List[NFTGetMarketsResponseItem]
