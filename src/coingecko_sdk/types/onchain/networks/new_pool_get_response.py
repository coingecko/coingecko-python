# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = [
    "NewPoolGetResponse",
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
    "DataRelationshipsNetwork",
    "DataRelationshipsNetworkData",
    "DataRelationshipsQuoteToken",
    "DataRelationshipsQuoteTokenData",
    "Included",
    "IncludedAttributes",
]


class DataAttributesPriceChangePercentage(BaseModel):
    """Price change percentage over various timeframes"""

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
    """Transaction counts over various timeframes"""

    h1: Optional[DataAttributesTransactionsH1] = None

    h24: Optional[DataAttributesTransactionsH24] = None

    h6: Optional[DataAttributesTransactionsH6] = None

    m15: Optional[DataAttributesTransactionsM15] = None

    m30: Optional[DataAttributesTransactionsM30] = None

    m5: Optional[DataAttributesTransactionsM5] = None


class DataAttributesVolumeUsd(BaseModel):
    """Volume in USD over various timeframes"""

    h1: Optional[str] = None

    h24: Optional[str] = None

    h6: Optional[str] = None

    m15: Optional[str] = None

    m30: Optional[str] = None

    m5: Optional[str] = None


class DataAttributes(BaseModel):
    address: str
    """Pool contract address"""

    base_token_price_native_currency: Optional[str] = None
    """Base token price in native currency"""

    base_token_price_quote_token: Optional[str] = None
    """Base token price in quote token"""

    base_token_price_usd: str
    """Base token price in USD"""

    fdv_usd: Optional[str] = None
    """Fully diluted valuation in USD"""

    market_cap_usd: Optional[str] = None
    """Market cap in USD"""

    name: str
    """Pool name"""

    pool_created_at: str
    """Pool creation timestamp"""

    price_change_percentage: DataAttributesPriceChangePercentage
    """Price change percentage over various timeframes"""

    quote_token_price_base_token: Optional[str] = None
    """Quote token price in base token"""

    quote_token_price_native_currency: Optional[str] = None
    """Quote token price in native currency"""

    quote_token_price_usd: str
    """Quote token price in USD"""

    reserve_in_usd: Optional[str] = None
    """Total reserve in USD"""

    transactions: DataAttributesTransactions
    """Transaction counts over various timeframes"""

    volume_usd: DataAttributesVolumeUsd
    """Volume in USD over various timeframes"""

    community_sus_report: Optional[int] = None
    """GeckoTerminal community suspicious reports count"""

    sentiment_vote_negative_percentage: Optional[float] = None
    """GeckoTerminal community negative sentiment vote percentage"""

    sentiment_vote_positive_percentage: Optional[float] = None
    """GeckoTerminal community positive sentiment vote percentage"""

    token_price_usd: Optional[str] = None
    """Price of the queried token in USD, present when querying pools by token address"""


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
    """Related resources"""

    base_token: Optional[DataRelationshipsBaseToken] = None

    dex: Optional[DataRelationshipsDex] = None

    network: Optional[DataRelationshipsNetwork] = None

    quote_token: Optional[DataRelationshipsQuoteToken] = None


class Data(BaseModel):
    id: str
    """Pool identifier"""

    attributes: DataAttributes

    relationships: DataRelationships
    """Related resources"""

    type: str
    """Resource type"""


class IncludedAttributes(BaseModel):
    address: Optional[str] = None

    coingecko_asset_platform_id: Optional[str] = None

    coingecko_coin_id: Optional[str] = None

    decimals: Optional[int] = None

    image_url: Optional[str] = None

    name: Optional[str] = None

    symbol: Optional[str] = None


class Included(BaseModel):
    id: Optional[str] = None

    attributes: Optional[IncludedAttributes] = None

    type: Optional[str] = None


class NewPoolGetResponse(BaseModel):
    data: List[Data]

    included: Optional[List[Included]] = None
    """Included related resources, present when include parameter is specified"""
