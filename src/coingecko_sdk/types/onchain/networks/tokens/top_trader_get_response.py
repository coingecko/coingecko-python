# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ....._models import BaseModel

__all__ = ["TopTraderGetResponse", "Data", "DataAttributes", "DataAttributesTrader"]


class DataAttributesTrader(BaseModel):
    address: str
    """Trader wallet address"""

    average_buy_price_usd: str
    """Average buy price in USD"""

    average_sell_price_usd: str
    """Average sell price in USD"""

    explorer_url: str
    """Block explorer URL for the trader address"""

    realized_pnl_usd: str
    """Realized PnL in USD"""

    token_balance: Optional[str] = None
    """Current token balance"""

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

    label: Optional[str] = None
    """Address label"""

    name: Optional[str] = None
    """Address label name"""

    type: Optional[str] = None
    """Address type"""


class DataAttributes(BaseModel):
    traders: List[DataAttributesTrader]


class Data(BaseModel):
    id: str
    """Token identifier"""

    attributes: DataAttributes

    type: str
    """Resource type"""


class TopTraderGetResponse(BaseModel):
    data: Data
