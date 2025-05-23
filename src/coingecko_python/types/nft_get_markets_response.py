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
    native_currency: Optional[float] = None

    usd: Optional[float] = None


class NFTGetMarketsResponseItemFloorPrice24hPercentageChange(BaseModel):
    native_currency: Optional[float] = None

    usd: Optional[float] = None


class NFTGetMarketsResponseItemImage(BaseModel):
    small: Optional[str] = None

    small_2x: Optional[str] = None


class NFTGetMarketsResponseItemMarketCap(BaseModel):
    native_currency: Optional[float] = None

    usd: Optional[float] = None


class NFTGetMarketsResponseItemMarketCap24hPercentageChange(BaseModel):
    native_currency: Optional[float] = None

    usd: Optional[float] = None


class NFTGetMarketsResponseItemVolume24h(BaseModel):
    native_currency: Optional[float] = None

    usd: Optional[float] = None


class NFTGetMarketsResponseItemVolume24hPercentageChange(BaseModel):
    native_currency: Optional[float] = None

    usd: Optional[float] = None


class NFTGetMarketsResponseItem(BaseModel):
    id: Optional[str] = None
    """NFT collection ID"""

    asset_platform_id: Optional[str] = None
    """NFT collection asset platform ID"""

    contract_address: Optional[str] = None
    """NFT collection contract address"""

    description: Optional[str] = None
    """NFT collection description"""

    floor_price: Optional[NFTGetMarketsResponseItemFloorPrice] = None
    """NFT collection floor price"""

    floor_price_24h_percentage_change: Optional[NFTGetMarketsResponseItemFloorPrice24hPercentageChange] = None
    """NFT collection floor price 24 hours percentage change"""

    floor_price_in_usd_24h_percentage_change: Optional[float] = None
    """NFT collection floor price in usd 24 hours percentage change"""

    image: Optional[NFTGetMarketsResponseItemImage] = None
    """NFT collection image url"""

    market_cap: Optional[NFTGetMarketsResponseItemMarketCap] = None
    """NFT collection market cap"""

    market_cap_24h_percentage_change: Optional[NFTGetMarketsResponseItemMarketCap24hPercentageChange] = None
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

    volume_24h: Optional[NFTGetMarketsResponseItemVolume24h] = None
    """NFT collection volume in 24 hours"""

    volume_24h_percentage_change: Optional[NFTGetMarketsResponseItemVolume24hPercentageChange] = None
    """NFT collection volume in 24 hours percentage change"""

    volume_in_usd_24h_percentage_change: Optional[float] = None
    """NFT collection volume in usd 24 hours percentage change"""


NFTGetMarketsResponse: TypeAlias = List[NFTGetMarketsResponseItem]
