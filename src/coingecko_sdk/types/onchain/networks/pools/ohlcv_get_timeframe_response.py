# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ....._models import BaseModel

__all__ = ["OhlcvGetTimeframeResponse", "Data", "DataAttributes", "Meta", "MetaBase", "MetaQuote"]


class DataAttributes(BaseModel):
    ohlcv_list: List[List[float]]
    """OHLCV data as [timestamp, open, high, low, close, volume] arrays"""


class Data(BaseModel):
    id: str
    """Request ID"""

    attributes: DataAttributes

    type: str
    """Resource type"""


class MetaBase(BaseModel):
    """Base token metadata"""

    address: Optional[str] = None

    coingecko_coin_id: Optional[str] = None

    name: Optional[str] = None

    symbol: Optional[str] = None


class MetaQuote(BaseModel):
    """Quote token metadata"""

    address: Optional[str] = None

    coingecko_coin_id: Optional[str] = None

    name: Optional[str] = None

    symbol: Optional[str] = None


class Meta(BaseModel):
    base: Optional[MetaBase] = None
    """Base token metadata"""

    quote: Optional[MetaQuote] = None
    """Quote token metadata"""


class OhlcvGetTimeframeResponse(BaseModel):
    data: Data

    meta: Meta
