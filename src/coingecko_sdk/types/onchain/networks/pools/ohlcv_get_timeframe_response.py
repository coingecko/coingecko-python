# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ....._models import BaseModel

__all__ = ["OhlcvGetTimeframeResponse", "Data", "DataAttributes", "Meta", "MetaBase", "MetaQuote"]


class DataAttributes(BaseModel):
    ohlcv_list: Optional[List[List[float]]] = None


class Data(BaseModel):
    id: Optional[str] = None

    attributes: Optional[DataAttributes] = None

    type: Optional[str] = None


class MetaBase(BaseModel):
    address: Optional[str] = None

    coingecko_coin_id: Optional[str] = None

    name: Optional[str] = None

    symbol: Optional[str] = None


class MetaQuote(BaseModel):
    address: Optional[str] = None

    coingecko_coin_id: Optional[str] = None

    name: Optional[str] = None

    symbol: Optional[str] = None


class Meta(BaseModel):
    base: Optional[MetaBase] = None

    quote: Optional[MetaQuote] = None


class OhlcvGetTimeframeResponse(BaseModel):
    data: Optional[Data] = None

    meta: Optional[Meta] = None
