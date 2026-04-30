# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = [
    "PoolData",
    "Attributes",
    "AttributesBuyVolumeUsd",
    "AttributesNetBuyVolumeUsd",
    "AttributesPriceChangePercentage",
    "AttributesSellVolumeUsd",
    "AttributesTransactions",
    "AttributesTransactionsH1",
    "AttributesTransactionsH24",
    "AttributesTransactionsH6",
    "AttributesTransactionsM15",
    "AttributesTransactionsM30",
    "AttributesTransactionsM5",
    "AttributesVolumeUsd",
    "Relationships",
    "RelationshipsBaseToken",
    "RelationshipsBaseTokenData",
    "RelationshipsDex",
    "RelationshipsDexData",
    "RelationshipsQuoteToken",
    "RelationshipsQuoteTokenData",
]


class AttributesBuyVolumeUsd(BaseModel):
    h1: Optional[str] = None

    h24: Optional[str] = None

    h6: Optional[str] = None

    m15: Optional[str] = None

    m30: Optional[str] = None

    m5: Optional[str] = None


class AttributesNetBuyVolumeUsd(BaseModel):
    h1: Optional[str] = None

    h24: Optional[str] = None

    h6: Optional[str] = None

    m15: Optional[str] = None

    m30: Optional[str] = None

    m5: Optional[str] = None


class AttributesPriceChangePercentage(BaseModel):
    h1: Optional[str] = None

    h24: Optional[str] = None

    h6: Optional[str] = None

    m15: Optional[str] = None

    m30: Optional[str] = None

    m5: Optional[str] = None


class AttributesSellVolumeUsd(BaseModel):
    h1: Optional[str] = None

    h24: Optional[str] = None

    h6: Optional[str] = None

    m15: Optional[str] = None

    m30: Optional[str] = None

    m5: Optional[str] = None


class AttributesTransactionsH1(BaseModel):
    buyers: Optional[int] = None

    buys: Optional[int] = None

    sellers: Optional[int] = None

    sells: Optional[int] = None


class AttributesTransactionsH24(BaseModel):
    buyers: Optional[int] = None

    buys: Optional[int] = None

    sellers: Optional[int] = None

    sells: Optional[int] = None


class AttributesTransactionsH6(BaseModel):
    buyers: Optional[int] = None

    buys: Optional[int] = None

    sellers: Optional[int] = None

    sells: Optional[int] = None


class AttributesTransactionsM15(BaseModel):
    buyers: Optional[int] = None

    buys: Optional[int] = None

    sellers: Optional[int] = None

    sells: Optional[int] = None


class AttributesTransactionsM30(BaseModel):
    buyers: Optional[int] = None

    buys: Optional[int] = None

    sellers: Optional[int] = None

    sells: Optional[int] = None


class AttributesTransactionsM5(BaseModel):
    buyers: Optional[int] = None

    buys: Optional[int] = None

    sellers: Optional[int] = None

    sells: Optional[int] = None


class AttributesTransactions(BaseModel):
    h1: Optional[AttributesTransactionsH1] = None

    h24: Optional[AttributesTransactionsH24] = None

    h6: Optional[AttributesTransactionsH6] = None

    m15: Optional[AttributesTransactionsM15] = None

    m30: Optional[AttributesTransactionsM30] = None

    m5: Optional[AttributesTransactionsM5] = None


class AttributesVolumeUsd(BaseModel):
    h1: Optional[str] = None

    h24: Optional[str] = None

    h6: Optional[str] = None

    m15: Optional[str] = None

    m30: Optional[str] = None

    m5: Optional[str] = None


class Attributes(BaseModel):
    address: Optional[str] = None

    base_token_balance: Optional[str] = None

    base_token_liquidity_usd: Optional[str] = None

    base_token_price_native_currency: Optional[str] = None

    base_token_price_quote_token: Optional[str] = None

    base_token_price_usd: Optional[str] = None

    buy_volume_usd: Optional[AttributesBuyVolumeUsd] = None

    fdv_usd: Optional[str] = None

    locked_liquidity_percentage: Optional[str] = None

    market_cap_usd: Optional[str] = None

    name: Optional[str] = None

    net_buy_volume_usd: Optional[AttributesNetBuyVolumeUsd] = None

    pool_created_at: Optional[str] = None

    pool_fee_percentage: Optional[str] = None

    pool_name: Optional[str] = None

    price_change_percentage: Optional[AttributesPriceChangePercentage] = None

    quote_token_balance: Optional[str] = None

    quote_token_liquidity_usd: Optional[str] = None

    quote_token_price_base_token: Optional[str] = None

    quote_token_price_native_currency: Optional[str] = None

    quote_token_price_usd: Optional[str] = None

    reserve_in_usd: Optional[str] = None

    sell_volume_usd: Optional[AttributesSellVolumeUsd] = None

    transactions: Optional[AttributesTransactions] = None

    volume_usd: Optional[AttributesVolumeUsd] = None


class RelationshipsBaseTokenData(BaseModel):
    id: Optional[str] = None

    type: Optional[str] = None


class RelationshipsBaseToken(BaseModel):
    data: Optional[RelationshipsBaseTokenData] = None


class RelationshipsDexData(BaseModel):
    id: Optional[str] = None

    type: Optional[str] = None


class RelationshipsDex(BaseModel):
    data: Optional[RelationshipsDexData] = None


class RelationshipsQuoteTokenData(BaseModel):
    id: Optional[str] = None

    type: Optional[str] = None


class RelationshipsQuoteToken(BaseModel):
    data: Optional[RelationshipsQuoteTokenData] = None


class Relationships(BaseModel):
    base_token: Optional[RelationshipsBaseToken] = None

    dex: Optional[RelationshipsDex] = None

    quote_token: Optional[RelationshipsQuoteToken] = None


class PoolData(BaseModel):
    id: Optional[str] = None

    attributes: Optional[Attributes] = None

    relationships: Optional[Relationships] = None

    type: Optional[str] = None
