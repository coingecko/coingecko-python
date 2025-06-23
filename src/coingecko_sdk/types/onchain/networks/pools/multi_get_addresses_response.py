# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ....._models import BaseModel

__all__ = [
    "MultiGetAddressesResponse",
    "Data",
    "DataAttributes",
    "DataAttributesPriceChangePercentage",
    "DataAttributesTransactions",
    "DataAttributesTransactionsH1",
    "DataAttributesTransactionsH24",
    "DataAttributesTransactionsH6",
    "DataAttributesTransactionsM15",
    "DataAttributesTransactionsM30",
    "DataAttributesTransactionsM5",
    "DataAttributesVolumeUsd",
    "DataRelationships",
    "DataRelationshipsBaseToken",
    "DataRelationshipsBaseTokenData",
    "DataRelationshipsDex",
    "DataRelationshipsDexData",
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


class DataAttributesTransactionsH1(BaseModel):
    buyers: Optional[int] = None

    buys: Optional[int] = None

    sellers: Optional[int] = None

    sells: Optional[int] = None


class DataAttributesTransactionsH24(BaseModel):
    buyers: Optional[int] = None

    buys: Optional[int] = None

    sellers: Optional[int] = None

    sells: Optional[int] = None


class DataAttributesTransactionsH6(BaseModel):
    buyers: Optional[int] = None

    buys: Optional[int] = None

    sellers: Optional[int] = None

    sells: Optional[int] = None


class DataAttributesTransactionsM15(BaseModel):
    buyers: Optional[int] = None

    buys: Optional[int] = None

    sellers: Optional[int] = None

    sells: Optional[int] = None


class DataAttributesTransactionsM30(BaseModel):
    buyers: Optional[int] = None

    buys: Optional[int] = None

    sellers: Optional[int] = None

    sells: Optional[int] = None


class DataAttributesTransactionsM5(BaseModel):
    buyers: Optional[int] = None

    buys: Optional[int] = None

    sellers: Optional[int] = None

    sells: Optional[int] = None


class DataAttributesTransactions(BaseModel):
    h1: Optional[DataAttributesTransactionsH1] = None

    h24: Optional[DataAttributesTransactionsH24] = None

    h6: Optional[DataAttributesTransactionsH6] = None

    m15: Optional[DataAttributesTransactionsM15] = None

    m30: Optional[DataAttributesTransactionsM30] = None

    m5: Optional[DataAttributesTransactionsM5] = None


class DataAttributesVolumeUsd(BaseModel):
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

    locked_liquidity_percentage: Optional[str] = None

    market_cap_usd: Optional[str] = None

    name: Optional[str] = None

    pool_created_at: Optional[str] = None

    pool_fee_percentage: Optional[str] = None

    pool_name: Optional[str] = None

    price_change_percentage: Optional[DataAttributesPriceChangePercentage] = None

    quote_token_price_base_token: Optional[str] = None

    quote_token_price_native_currency: Optional[str] = None

    quote_token_price_usd: Optional[str] = None

    reserve_in_usd: Optional[str] = None

    transactions: Optional[DataAttributesTransactions] = None

    volume_usd: Optional[DataAttributesVolumeUsd] = None


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


class DataRelationshipsQuoteTokenData(BaseModel):
    id: Optional[str] = None

    type: Optional[str] = None


class DataRelationshipsQuoteToken(BaseModel):
    data: Optional[DataRelationshipsQuoteTokenData] = None


class DataRelationships(BaseModel):
    base_token: Optional[DataRelationshipsBaseToken] = None

    dex: Optional[DataRelationshipsDex] = None

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


class MultiGetAddressesResponse(BaseModel):
    data: Optional[List[Data]] = None

    included: Optional[List[Included]] = None
