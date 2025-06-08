# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["SearchGetResponse", "Category", "Coin", "Exchange", "NFT"]


class Category(BaseModel):
    id: Optional[str] = None
    """category ID"""

    name: Optional[str] = None
    """category name"""


class Coin(BaseModel):
    id: Optional[str] = None
    """coin ID"""

    api_symbol: Optional[str] = None
    """coin api symbol"""

    large: Optional[str] = None
    """coin large image url"""

    market_cap_rank: Optional[float] = None
    """coin market cap rank"""

    name: Optional[str] = None
    """coin name"""

    symbol: Optional[str] = None
    """coin symbol"""

    thumb: Optional[str] = None
    """coin thumb image url"""


class Exchange(BaseModel):
    id: Optional[str] = None
    """exchange ID"""

    large: Optional[str] = None
    """exchange large image url"""

    market_type: Optional[str] = None
    """exchange market type"""

    name: Optional[str] = None
    """exchange name"""

    thumb: Optional[str] = None
    """exchange thumb image url"""


class NFT(BaseModel):
    id: Optional[str] = None
    """NFT collection ID"""

    name: Optional[str] = None
    """NFT name"""

    symbol: Optional[str] = None
    """NFT collection symbol"""

    thumb: Optional[str] = None
    """NFT collection thumb image url"""


class SearchGetResponse(BaseModel):
    categories: Optional[List[Category]] = None

    coins: Optional[List[Coin]] = None

    exchanges: Optional[List[Exchange]] = None

    icos: Optional[List[str]] = None

    nfts: Optional[List[NFT]] = None
