# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["SearchGetResponse", "Category", "Coin", "Exchange", "Ico", "NFT"]


class Category(BaseModel):
    id: str
    """Category ID"""

    name: str
    """Category name"""


class Coin(BaseModel):
    id: str
    """Coin ID"""

    api_symbol: str
    """Coin API symbol"""

    large: str
    """Coin large image URL"""

    market_cap_rank: Optional[int] = None
    """Coin market cap rank"""

    name: str
    """Coin name"""

    symbol: str
    """Coin symbol"""

    thumb: str
    """Coin thumb image URL"""


class Exchange(BaseModel):
    id: str
    """Exchange ID"""

    large: str
    """Exchange large image URL"""

    market_type: str
    """Exchange market type"""

    name: str
    """Exchange name"""

    thumb: str
    """Exchange thumb image URL"""


class Ico(BaseModel):
    pass


class NFT(BaseModel):
    id: str
    """NFT collection ID"""

    name: str
    """NFT collection name"""

    symbol: str
    """NFT collection symbol"""

    thumb: str
    """NFT collection thumb image URL"""


class SearchGetResponse(BaseModel):
    categories: List[Category]

    coins: List[Coin]

    exchanges: List[Exchange]

    icos: List[Ico]

    nfts: List[NFT]
