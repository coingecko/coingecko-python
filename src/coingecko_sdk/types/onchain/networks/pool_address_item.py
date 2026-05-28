# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = [
    "PoolAddressItem",
    "Attributes",
    "AttributesPriceChangePercentage",
    "AttributesTransactions",
    "AttributesTransactionsH1",
    "AttributesTransactionsH24",
    "AttributesTransactionsH6",
    "AttributesTransactionsM15",
    "AttributesTransactionsM30",
    "AttributesTransactionsM5",
    "AttributesVolumeUsd",
    "AttributesBuyVolumeUsd",
    "AttributesNetBuyVolumeUsd",
    "AttributesSellVolumeUsd",
    "Relationships",
    "RelationshipsBaseToken",
    "RelationshipsBaseTokenData",
    "RelationshipsDex",
    "RelationshipsDexData",
    "RelationshipsQuoteToken",
    "RelationshipsQuoteTokenData",
]


class AttributesPriceChangePercentage(BaseModel):
    """Price change percentage over various timeframes"""

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
    """Transaction counts over various timeframes"""

    h1: Optional[AttributesTransactionsH1] = None

    h24: Optional[AttributesTransactionsH24] = None

    h6: Optional[AttributesTransactionsH6] = None

    m15: Optional[AttributesTransactionsM15] = None

    m30: Optional[AttributesTransactionsM30] = None

    m5: Optional[AttributesTransactionsM5] = None


class AttributesVolumeUsd(BaseModel):
    """Volume in USD over various timeframes"""

    h1: Optional[str] = None

    h24: Optional[str] = None

    h6: Optional[str] = None

    m15: Optional[str] = None

    m30: Optional[str] = None

    m5: Optional[str] = None


class AttributesBuyVolumeUsd(BaseModel):
    """Buy volume in USD over various timeframes"""

    h1: Optional[str] = None

    h24: Optional[str] = None

    h6: Optional[str] = None

    m15: Optional[str] = None

    m30: Optional[str] = None

    m5: Optional[str] = None


class AttributesNetBuyVolumeUsd(BaseModel):
    """Net buy volume in USD over various timeframes"""

    h1: Optional[str] = None

    h24: Optional[str] = None

    h6: Optional[str] = None

    m15: Optional[str] = None

    m30: Optional[str] = None

    m5: Optional[str] = None


class AttributesSellVolumeUsd(BaseModel):
    """Sell volume in USD over various timeframes"""

    h1: Optional[str] = None

    h24: Optional[str] = None

    h6: Optional[str] = None

    m15: Optional[str] = None

    m30: Optional[str] = None

    m5: Optional[str] = None


class Attributes(BaseModel):
    address: str
    """Pool contract address"""

    base_token_price_native_currency: str
    """Base token price in native currency"""

    base_token_price_quote_token: str
    """Base token price in quote token"""

    base_token_price_usd: str
    """Base token price in USD"""

    fdv_usd: Optional[str] = None
    """Fully diluted valuation in USD"""

    locked_liquidity_percentage: str
    """Locked liquidity percentage"""

    market_cap_usd: Optional[str] = None
    """Market cap in USD"""

    name: str
    """Pool name with fee tier"""

    pool_created_at: str
    """Pool creation timestamp"""

    pool_fee_percentage: str
    """Pool fee percentage"""

    pool_name: str
    """Pool name without fee tier"""

    price_change_percentage: AttributesPriceChangePercentage
    """Price change percentage over various timeframes"""

    quote_token_price_base_token: str
    """Quote token price in base token"""

    quote_token_price_native_currency: str
    """Quote token price in native currency"""

    quote_token_price_usd: str
    """Quote token price in USD"""

    reserve_in_usd: str
    """Total reserve in USD"""

    transactions: AttributesTransactions
    """Transaction counts over various timeframes"""

    volume_usd: AttributesVolumeUsd
    """Volume in USD over various timeframes"""

    base_token_balance: Optional[str] = None
    """Base token balance in pool"""

    base_token_liquidity_usd: Optional[str] = None
    """Base token liquidity in USD"""

    buy_volume_usd: Optional[AttributesBuyVolumeUsd] = None
    """Buy volume in USD over various timeframes"""

    net_buy_volume_usd: Optional[AttributesNetBuyVolumeUsd] = None
    """Net buy volume in USD over various timeframes"""

    quote_token_balance: Optional[str] = None
    """Quote token balance in pool"""

    quote_token_liquidity_usd: Optional[str] = None
    """Quote token liquidity in USD"""

    sell_volume_usd: Optional[AttributesSellVolumeUsd] = None
    """Sell volume in USD over various timeframes"""


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
    """Related resources"""

    base_token: Optional[RelationshipsBaseToken] = None

    dex: Optional[RelationshipsDex] = None

    quote_token: Optional[RelationshipsQuoteToken] = None


class PoolAddressItem(BaseModel):
    id: str
    """Pool identifier"""

    attributes: Attributes

    relationships: Relationships
    """Related resources"""

    type: str
    """Resource type"""
