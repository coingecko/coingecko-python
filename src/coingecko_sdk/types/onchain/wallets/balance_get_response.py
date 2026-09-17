# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["BalanceGetResponse", "Data", "DataAttributes", "DataAttributesBalance", "DataAttributesNetwork"]


class DataAttributesBalance(BaseModel):
    address: str
    """Token contract address"""

    balance: Optional[str] = None
    """Token balance at full precision"""

    balance_raw: str
    """Token balance in the smallest unit, before decimals are applied"""

    coingecko_coin_id: Optional[str] = None
    """CoinGecko coin ID"""

    decimals: int
    """Token decimals"""

    h24_price_change_percentage: Optional[str] = None
    """24hr price change percentage"""

    name: str
    """Token name"""

    network: str
    """Network ID"""

    price_usd: Optional[str] = None
    """Token price in USD"""

    symbol: str
    """Token symbol"""

    token_type: str
    """Token type, such as native, erc20 or spl"""

    total_reserve_in_usd: Optional[str] = None
    """Total reserve in USD across all pools of the token"""

    value_usd: Optional[str] = None
    """Value of the holding in USD"""


class DataAttributesNetwork(BaseModel):
    holdings: int
    """Number of matching holdings on this network"""

    last_updated_at: datetime
    """Last updated timestamp"""

    network: str
    """Network ID"""

    value_usd: str
    """Total value of matching holdings on this network in USD"""


class DataAttributes(BaseModel):
    balances: List[DataAttributesBalance]
    """Token holdings, one entry per token"""

    networks: List[DataAttributesNetwork]
    """
    Value and holding count per network, listing only networks holding a matching
    balance
    """

    total_holdings: int
    """Number of matching holdings across the requested networks only"""

    total_value_usd: str
    """Total value of matching holdings in USD, across the requested networks only"""

    wallet_address: str
    """Wallet address queried"""


class Data(BaseModel):
    id: str
    """Wallet address"""

    attributes: DataAttributes

    type: str
    """Response type"""


class BalanceGetResponse(BaseModel):
    data: Data
