# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = [
    "TokenGetMultiResponse",
    "Data",
    "DataAttributes",
    "DataAttributesVolumeUsd",
    "DataAttributesLaunchpadDetails",
    "DataRelationships",
    "DataRelationshipsTopPools",
    "DataRelationshipsTopPoolsData",
    "Included",
    "IncludedAttributes",
    "IncludedAttributesPriceChangePercentage",
    "IncludedAttributesTransactions",
    "IncludedAttributesTransactionsH1",
    "IncludedAttributesTransactionsH24",
    "IncludedAttributesTransactionsH6",
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
    """Volume in USD"""

    h24: Optional[str] = None


class DataAttributesLaunchpadDetails(BaseModel):
    """Launchpad details for pump-style tokens"""

    completed: Optional[bool] = None

    completed_at: Optional[str] = None

    graduation_percentage: Optional[float] = None

    migrated_destination_pool_address: Optional[str] = None


class DataAttributes(BaseModel):
    address: str
    """Token contract address"""

    coingecko_coin_id: Optional[str] = None
    """CoinGecko coin ID"""

    decimals: int
    """Token decimals"""

    fdv_usd: Optional[str] = None
    """Fully diluted valuation in USD"""

    image_url: Optional[str] = None
    """Token image URL"""

    market_cap_usd: Optional[str] = None
    """Market cap in USD"""

    name: str
    """Token name"""

    network: str
    """Network ID of the token"""

    normalized_total_supply: str
    """Normalized token total supply"""

    price_usd: Optional[str] = None
    """Token price in USD"""

    symbol: str
    """Token symbol"""

    total_reserve_in_usd: str
    """Total reserve in USD across all pools"""

    total_supply: str
    """Token total supply"""

    volume_usd: DataAttributesVolumeUsd
    """Volume in USD"""

    last_trade_timestamp: Optional[str] = None
    """Last trade timestamp in UNIX"""

    launchpad_details: Optional[DataAttributesLaunchpadDetails] = None
    """Launchpad details for pump-style tokens"""


class DataRelationshipsTopPoolsData(BaseModel):
    id: Optional[str] = None

    type: Optional[str] = None


class DataRelationshipsTopPools(BaseModel):
    data: Optional[List[DataRelationshipsTopPoolsData]] = None


class DataRelationships(BaseModel):
    top_pools: Optional[DataRelationshipsTopPools] = None


class Data(BaseModel):
    id: str
    """Token identifier"""

    attributes: DataAttributes

    relationships: DataRelationships

    type: str
    """Resource type"""


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


class IncludedAttributesTransactionsH6(BaseModel):
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

    h6: Optional[IncludedAttributesTransactionsH6] = None

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

    base_token_balance: Optional[str] = None
    """Base token balance in pool"""

    base_token_liquidity_usd: Optional[str] = None
    """Base token liquidity in USD"""

    base_token_price_native_currency: Optional[str] = None

    base_token_price_quote_token: Optional[str] = None

    base_token_price_usd: Optional[str] = None

    fdv_usd: Optional[str] = None

    last_trade_timestamp: Optional[str] = None
    """Last trade timestamp in UNIX"""

    market_cap_usd: Optional[str] = None

    name: Optional[str] = None

    pool_created_at: Optional[str] = None

    price_change_percentage: Optional[IncludedAttributesPriceChangePercentage] = None

    quote_token_balance: Optional[str] = None
    """Quote token balance in pool"""

    quote_token_liquidity_usd: Optional[str] = None
    """Quote token liquidity in USD"""

    quote_token_price_base_token: Optional[str] = None

    quote_token_price_native_currency: Optional[str] = None

    quote_token_price_usd: Optional[str] = None

    reserve_in_usd: Optional[str] = None

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


class TokenGetMultiResponse(BaseModel):
    data: List[Data]

    included: Optional[List[Included]] = None
    """Included top pool data, present when include=top_pools is specified"""
