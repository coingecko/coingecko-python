# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel

__all__ = [
    "TrendingGetResponse",
    "Category",
    "CategoryData",
    "Coin",
    "CoinItem",
    "CoinItemData",
    "CoinItemDataContent",
    "NFT",
    "NFTData",
    "NFTDataContent",
]


class CategoryData(BaseModel):
    market_cap: float
    """Category market cap"""

    market_cap_btc: float
    """Category market cap in BTC"""

    market_cap_change_percentage_24h: Dict[str, float]
    """Category market cap change percentage in 24 hours by currency"""

    sparkline: str
    """Category sparkline image URL"""

    total_volume: float
    """Category total volume"""

    total_volume_btc: float
    """Category total volume in BTC"""


class Category(BaseModel):
    id: int
    """Category ID"""

    coins_count: str
    """Number of coins in the category"""

    data: CategoryData

    market_cap_1h_change: float
    """Category market cap 1 hour change"""

    name: str
    """Category name"""

    slug: str
    """Category web slug"""

    top_3_coins_images: List[str]
    """Top 3 coins image URLs in the category"""


class CoinItemDataContent(BaseModel):
    description: Optional[str] = None

    title: Optional[str] = None


class CoinItemData(BaseModel):
    content: Optional[CoinItemDataContent] = None

    market_cap: str
    """Coin market cap in USD"""

    market_cap_btc: str
    """Coin market cap in BTC"""

    price: float
    """Coin price in USD"""

    price_btc: str
    """Coin price in BTC"""

    price_change_percentage_24h: Dict[str, float]
    """Coin price change percentage in 24 hours by currency"""

    sparkline: str
    """Coin sparkline image URL"""

    total_volume: str
    """Coin total volume in USD"""

    total_volume_btc: str
    """Coin total volume in BTC"""


class CoinItem(BaseModel):
    id: str
    """Coin ID"""

    coin_id: int
    """Coin internal ID"""

    data: CoinItemData

    large: str
    """Coin large image URL"""

    market_cap_rank: int
    """Coin market cap rank"""

    name: str
    """Coin name"""

    price_btc: float
    """Coin price in BTC"""

    score: int
    """Coin trending rank (0-based)"""

    slug: str
    """Coin web slug"""

    small: str
    """Coin small image URL"""

    symbol: str
    """Coin symbol"""

    thumb: str
    """Coin thumb image URL"""


class Coin(BaseModel):
    item: CoinItem


class NFTDataContent(BaseModel):
    description: Optional[str] = None

    title: Optional[str] = None


class NFTData(BaseModel):
    content: Optional[NFTDataContent] = None

    floor_price: str
    """NFT collection floor price"""

    floor_price_in_usd_24h_percentage_change: str
    """NFT collection floor price in USD 24 hours percentage change"""

    h24_average_sale_price: str
    """NFT collection 24 hours average sale price"""

    h24_volume: str
    """NFT collection volume in 24 hours"""

    sparkline: str
    """NFT collection sparkline image URL"""


class NFT(BaseModel):
    id: str
    """NFT collection ID"""

    data: NFTData

    floor_price_24h_percentage_change: float
    """NFT collection floor price 24 hours percentage change"""

    floor_price_in_native_currency: float
    """NFT collection floor price in native currency"""

    name: str
    """NFT collection name"""

    native_currency_symbol: str
    """NFT collection native currency symbol"""

    nft_contract_id: int
    """NFT contract internal ID"""

    symbol: str
    """NFT collection symbol"""

    thumb: str
    """NFT collection thumb image URL"""


class TrendingGetResponse(BaseModel):
    categories: List[Category]

    coins: List[Coin]

    nfts: List[NFT]
