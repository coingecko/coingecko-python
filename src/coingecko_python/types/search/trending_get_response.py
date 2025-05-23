# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = [
    "TrendingGetResponse",
    "Category",
    "CategoryData",
    "CategoryDataMarketCapChangePercentage24h",
    "Coin",
    "CoinData",
    "CoinDataPriceChangePercentage24h",
    "NFT",
    "NFTData",
]


class CategoryDataMarketCapChangePercentage24h(BaseModel):
    btc: Optional[float] = None

    usd: Optional[float] = None


class CategoryData(BaseModel):
    market_cap: Optional[float] = None
    """category market cap"""

    market_cap_btc: Optional[float] = None
    """category market cap in btc"""

    market_cap_change_percentage_24h: Optional[CategoryDataMarketCapChangePercentage24h] = None
    """category market cap change percentage in 24 hours"""

    sparkline: Optional[str] = None
    """category sparkline image url"""

    total_volume: Optional[float] = None
    """category total volume"""

    total_volume_btc: Optional[float] = None
    """category total volume in btc"""


class Category(BaseModel):
    id: Optional[float] = None

    coins_count: Optional[float] = None
    """category number of coins"""

    data: Optional[CategoryData] = None

    market_cap_1h_change: Optional[float] = None
    """category market cap 1 hour change"""

    name: Optional[str] = None
    """category name"""

    slug: Optional[str] = None
    """category web slug"""


class CoinDataPriceChangePercentage24h(BaseModel):
    btc: Optional[float] = None

    usd: Optional[float] = None


class CoinData(BaseModel):
    content: Optional[str] = None

    market_cap: Optional[str] = None
    """coin market cap in usd"""

    market_cap_btc: Optional[str] = None
    """coin market cap in btc"""

    price: Optional[float] = None
    """coin price in usd"""

    price_btc: Optional[str] = None
    """coin price in btc"""

    price_change_percentage_24h: Optional[CoinDataPriceChangePercentage24h] = None
    """coin price change percentage in 24 hours"""

    sparkline: Optional[str] = None
    """coin sparkline image url"""

    total_volume: Optional[str] = None
    """coin total volume in usd"""

    total_volume_btc: Optional[str] = None
    """coin total volume in btc"""


class Coin(BaseModel):
    id: Optional[str] = None
    """coin ID"""

    coin_id: Optional[float] = None

    data: Optional[CoinData] = None

    large: Optional[str] = None
    """coin large image url"""

    market_cap_rank: Optional[float] = None
    """coin market cap rank"""

    name: Optional[str] = None
    """coin name"""

    price_btc: Optional[float] = None
    """coin price in btc"""

    score: Optional[float] = None
    """coin sequence in the list"""

    slug: Optional[str] = None
    """coin web slug"""

    small: Optional[str] = None
    """coin small image url"""

    symbol: Optional[str] = None
    """coin symbol"""

    thumb: Optional[str] = None
    """coin thumb image url"""


class NFTData(BaseModel):
    content: Optional[str] = None

    floor_price: Optional[str] = None
    """NFT collection floor price"""

    floor_price_in_usd_24h_percentage_change: Optional[str] = None
    """NFT collection floor price in usd 24 hours percentage change"""

    h24_average_sale_price: Optional[str] = None
    """NFT collection 24 hours average sale price"""

    h24_volume: Optional[str] = None
    """NFT collection volume in 24 hours"""

    sparkline: Optional[str] = None
    """NFT collection sparkline image url"""


class NFT(BaseModel):
    id: Optional[str] = None
    """NFT collection ID"""

    data: Optional[NFTData] = None

    floor_price_24h_percentage_change: Optional[float] = None
    """NFT collection floor price 24 hours percentage change"""

    floor_price_in_native_currency: Optional[float] = None
    """NFT collection floor price in native currency"""

    name: Optional[str] = None
    """NFT collection name"""

    native_currency_symbol: Optional[str] = None
    """NFT collection native currency symbol"""

    nft_contract_id: Optional[float] = None

    symbol: Optional[str] = None
    """NFT collection symbol"""

    thumb: Optional[str] = None
    """NFT collection thumb image url"""


class TrendingGetResponse(BaseModel):
    categories: Optional[List[Category]] = None

    coins: Optional[List[Coin]] = None

    nfts: Optional[List[NFT]] = None
