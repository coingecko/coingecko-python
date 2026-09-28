# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["PnlGetResponse", "Data", "DataAttributes", "DataAttributesNetwork", "DataAttributesTokenStat"]


class DataAttributesNetwork(BaseModel):
    network: str
    """Network ID"""

    realized_pnl_usd: str
    """Realized PnL on this network in USD"""

    tokens: int
    """Number of tokens traded on this network"""

    unrealized_pnl_usd: str
    """Unrealized PnL on this network in USD"""


class DataAttributesTokenStat(BaseModel):
    address: str
    """Token contract address"""

    average_buy_price_usd: str
    """Average buy price in USD"""

    average_sell_price_usd: str
    """Average sell price in USD"""

    decimals: int
    """Token decimals"""

    name: str
    """Token name"""

    network: str
    """Network ID"""

    realized_pnl_usd: str
    """Realized PnL in USD"""

    symbol: str
    """Token symbol"""

    total_buy_count: int
    """Total number of buy transactions"""

    total_buy_token_amount: str
    """Total buy token amount"""

    total_buy_usd: str
    """Total buy amount in USD"""

    total_sell_count: int
    """Total number of sell transactions"""

    total_sell_token_amount: str
    """Total sell token amount"""

    total_sell_usd: str
    """Total sell amount in USD"""

    unrealized_pnl_usd: Optional[str] = None
    """Unrealized PnL in USD"""


class DataAttributes(BaseModel):
    networks: List[DataAttributesNetwork]
    """
    Realized PnL, unrealized PnL and token count per network, listing only networks
    where the wallet traded
    """

    token_stats: List[DataAttributesTokenStat]
    """Trading stats and PnL, one entry per token"""

    total_realized_pnl_usd: str
    """All-time realized PnL in USD, across the requested networks only"""

    total_tokens: int
    """Number of tokens traded across the requested networks only"""

    total_unrealized_pnl_usd: str
    """All-time unrealized PnL in USD, across the requested networks only"""

    wallet_address: str
    """Wallet address queried"""


class Data(BaseModel):
    id: str
    """Wallet address"""

    attributes: DataAttributes

    type: str
    """Response type"""


class PnlGetResponse(BaseModel):
    data: Data
