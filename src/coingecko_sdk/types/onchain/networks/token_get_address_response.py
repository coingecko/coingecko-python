# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = [
    "TokenGetAddressResponse",
    "Data",
    "DataAttributes",
    "DataAttributesVolumeUsd",
    "DataRelationships",
    "DataRelationshipsTopPools",
    "DataRelationshipsTopPoolsData",
    "Included",
    "IncludedAttributes",
    "IncludedAttributesPriceChangePercentage",
    "IncludedAttributesTransactions",
    "IncludedAttributesTransactionsH1",
    "IncludedAttributesTransactionsH24",
    "IncludedAttributesTransactionsM15",
    "IncludedAttributesTransactionsM30",
    "IncludedAttributesTransactionsM5",
    "IncludedAttributesVolumeUsd",
    "IncludedRelationships",
    "IncludedRelationshipsBaseToken",
    "IncludedRelationshipsBaseTokenData",
    "IncludedRelationshipsDex",
    "IncludedRelationshipsDexData",
    "IncludedRelationshipsQuoteToken",
    "IncludedRelationshipsQuoteTokenData",
]


class DataAttributesVolumeUsd(BaseModel):
    h24: Optional[str] = None


class DataAttributes(BaseModel):
    address: Optional[str] = None

    coingecko_coin_id: Optional[str] = None

    decimals: Optional[int] = None

    fdv_usd: Optional[str] = None

    image_url: Optional[str] = None

    market_cap_usd: Optional[str] = None

    name: Optional[str] = None

    normalized_total_supply: Optional[str] = None

    price_usd: Optional[str] = None

    symbol: Optional[str] = None

    total_reserve_in_usd: Optional[str] = None

    total_supply: Optional[str] = None

    volume_usd: Optional[DataAttributesVolumeUsd] = None


class DataRelationshipsTopPoolsData(BaseModel):
    id: Optional[str] = None

    type: Optional[str] = None


class DataRelationshipsTopPools(BaseModel):
    data: Optional[List[DataRelationshipsTopPoolsData]] = None


class DataRelationships(BaseModel):
    top_pools: Optional[DataRelationshipsTopPools] = None


class Data(BaseModel):
    id: Optional[str] = None

    attributes: Optional[DataAttributes] = None

    relationships: Optional[DataRelationships] = None

    type: Optional[str] = None


class IncludedAttributesPriceChangePercentage(BaseModel):
    h1: Optional[str] = None

    h24: Optional[str] = None

    h6: Optional[str] = None

    m15: Optional[str] = None

    m30: Optional[str] = None

    m5: Optional[str] = None


class IncludedAttributesTransactionsH1(BaseModel):
    buyers: Optional[int] = None

    buys: Optional[int] = None

    sellers: Optional[int] = None

    sells: Optional[int] = None


class IncludedAttributesTransactionsH24(BaseModel):
    buyers: Optional[int] = None

    buys: Optional[int] = None

    sellers: Optional[int] = None

    sells: Optional[int] = None


class IncludedAttributesTransactionsM15(BaseModel):
    buyers: Optional[int] = None

    buys: Optional[int] = None

    sellers: Optional[int] = None

    sells: Optional[int] = None


class IncludedAttributesTransactionsM30(BaseModel):
    buyers: Optional[int] = None

    buys: Optional[int] = None

    sellers: Optional[int] = None

    sells: Optional[int] = None


class IncludedAttributesTransactionsM5(BaseModel):
    buyers: Optional[int] = None

    buys: Optional[int] = None

    sellers: Optional[int] = None

    sells: Optional[int] = None


class IncludedAttributesTransactions(BaseModel):
    h1: Optional[IncludedAttributesTransactionsH1] = None

    h24: Optional[IncludedAttributesTransactionsH24] = None

    m15: Optional[IncludedAttributesTransactionsM15] = None

    m30: Optional[IncludedAttributesTransactionsM30] = None

    m5: Optional[IncludedAttributesTransactionsM5] = None


class IncludedAttributesVolumeUsd(BaseModel):
    h1: Optional[str] = None

    h24: Optional[str] = None

    h6: Optional[str] = None

    m15: Optional[str] = None

    m30: Optional[str] = None

    m5: Optional[str] = None


class IncludedAttributes(BaseModel):
    address: Optional[str] = None

    base_token_price_native_currency: Optional[str] = None

    base_token_price_quote_token: Optional[str] = None

    base_token_price_usd: Optional[str] = None

    fdv_usd: Optional[str] = None

    market_cap_usd: Optional[str] = None

    name: Optional[str] = None

    pool_created_at: Optional[str] = None

    price_change_percentage: Optional[IncludedAttributesPriceChangePercentage] = None

    quote_token_price_base_token: Optional[str] = None

    quote_token_price_native_currency: Optional[str] = None

    quote_token_price_usd: Optional[str] = None

    reserve_in_usd: Optional[str] = None

    token_price_usd: Optional[str] = None

    transactions: Optional[IncludedAttributesTransactions] = None

    volume_usd: Optional[IncludedAttributesVolumeUsd] = None


class IncludedRelationshipsBaseTokenData(BaseModel):
    id: Optional[str] = None

    type: Optional[str] = None


class IncludedRelationshipsBaseToken(BaseModel):
    data: Optional[IncludedRelationshipsBaseTokenData] = None


class IncludedRelationshipsDexData(BaseModel):
    id: Optional[str] = None

    type: Optional[str] = None


class IncludedRelationshipsDex(BaseModel):
    data: Optional[IncludedRelationshipsDexData] = None


class IncludedRelationshipsQuoteTokenData(BaseModel):
    id: Optional[str] = None

    type: Optional[str] = None


class IncludedRelationshipsQuoteToken(BaseModel):
    data: Optional[IncludedRelationshipsQuoteTokenData] = None


class IncludedRelationships(BaseModel):
    base_token: Optional[IncludedRelationshipsBaseToken] = None

    dex: Optional[IncludedRelationshipsDex] = None

    quote_token: Optional[IncludedRelationshipsQuoteToken] = None


class Included(BaseModel):
    id: Optional[str] = None

    attributes: Optional[IncludedAttributes] = None

    relationships: Optional[IncludedRelationships] = None

    type: Optional[str] = None


class TokenGetAddressResponse(BaseModel):
    data: Optional[Data] = None

    included: Optional[List[Included]] = None
