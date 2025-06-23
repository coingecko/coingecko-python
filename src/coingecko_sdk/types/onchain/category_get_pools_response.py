# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = [
    "CategoryGetPoolsResponse",
    "Data",
    "DataAttributes",
    "DataAttributesPriceChangePercentage",
    "DataRelationships",
    "DataRelationshipsBaseToken",
    "DataRelationshipsBaseTokenData",
    "DataRelationshipsDex",
    "DataRelationshipsDexData",
    "DataRelationshipsNetwork",
    "DataRelationshipsNetworkData",
    "DataRelationshipsQuoteToken",
    "DataRelationshipsQuoteTokenData",
    "Included",
    "IncludedAttributes",
]


class DataAttributesPriceChangePercentage(BaseModel):
    h1: Optional[str] = None

    h24: Optional[str] = None

    h6: Optional[str] = None

    m15: Optional[str] = None

    m30: Optional[str] = None

    m5: Optional[str] = None


class DataAttributes(BaseModel):
    address: Optional[str] = None

    base_token_price_native_currency: Optional[str] = None

    base_token_price_quote_token: Optional[str] = None

    base_token_price_usd: Optional[str] = None

    fdv_usd: Optional[str] = None

    h24_tx_count: Optional[int] = None

    h24_volume_usd: Optional[str] = None

    market_cap_usd: Optional[str] = None

    name: Optional[str] = None

    pool_created_at: Optional[datetime] = None

    price_change_percentage: Optional[DataAttributesPriceChangePercentage] = None

    quote_token_price_base_token: Optional[str] = None

    quote_token_price_native_currency: Optional[str] = None

    quote_token_price_usd: Optional[str] = None

    reserve_in_usd: Optional[str] = None


class DataRelationshipsBaseTokenData(BaseModel):
    id: Optional[str] = None

    type: Optional[str] = None


class DataRelationshipsBaseToken(BaseModel):
    data: Optional[DataRelationshipsBaseTokenData] = None


class DataRelationshipsDexData(BaseModel):
    id: Optional[str] = None

    type: Optional[str] = None


class DataRelationshipsDex(BaseModel):
    data: Optional[DataRelationshipsDexData] = None


class DataRelationshipsNetworkData(BaseModel):
    id: Optional[str] = None

    type: Optional[str] = None


class DataRelationshipsNetwork(BaseModel):
    data: Optional[DataRelationshipsNetworkData] = None


class DataRelationshipsQuoteTokenData(BaseModel):
    id: Optional[str] = None

    type: Optional[str] = None


class DataRelationshipsQuoteToken(BaseModel):
    data: Optional[DataRelationshipsQuoteTokenData] = None


class DataRelationships(BaseModel):
    base_token: Optional[DataRelationshipsBaseToken] = None

    dex: Optional[DataRelationshipsDex] = None

    network: Optional[DataRelationshipsNetwork] = None

    quote_token: Optional[DataRelationshipsQuoteToken] = None


class Data(BaseModel):
    id: Optional[str] = None

    attributes: Optional[DataAttributes] = None

    relationships: Optional[DataRelationships] = None

    type: Optional[str] = None


class IncludedAttributes(BaseModel):
    address: Optional[str] = None

    coingecko_coin_id: Optional[str] = None

    decimals: Optional[int] = None

    image_url: Optional[str] = None

    name: Optional[str] = None

    symbol: Optional[str] = None


class Included(BaseModel):
    id: Optional[str] = None

    attributes: Optional[IncludedAttributes] = None

    type: Optional[str] = None


class CategoryGetPoolsResponse(BaseModel):
    data: Optional[List[Data]] = None

    included: Optional[List[Included]] = None
