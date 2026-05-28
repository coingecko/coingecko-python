# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ....._models import BaseModel

__all__ = ["TopHolderGetResponse", "Data", "DataAttributes", "DataAttributesHolder"]


class DataAttributesHolder(BaseModel):
    address: str
    """Holder wallet address"""

    amount: str
    """Token amount held"""

    label: Optional[str] = None
    """Address label"""

    percentage: str
    """Percentage of total supply held"""

    rank: int
    """Holder rank"""

    value: str
    """Value of holdings in USD"""

    average_buy_price_usd: Optional[str] = None
    """Average buy price in USD"""

    explorer_url: Optional[str] = None
    """Block explorer URL for the holder address"""

    realized_pnl_percentage: Optional[str] = None
    """Realized PnL percentage"""

    realized_pnl_usd: Optional[str] = None
    """Realized PnL in USD"""

    total_buy_count: Optional[int] = None
    """Total number of buy transactions"""

    total_sell_count: Optional[int] = None
    """Total number of sell transactions"""

    unrealized_pnl_percentage: Optional[str] = None
    """Unrealized PnL percentage"""

    unrealized_pnl_usd: Optional[str] = None
    """Unrealized PnL in USD"""


class DataAttributes(BaseModel):
    holders: List[DataAttributesHolder]

    last_updated_at: str
    """Data last updated timestamp"""


class Data(BaseModel):
    id: str
    """Token identifier"""

    attributes: DataAttributes

    type: str
    """Resource type"""


class TopHolderGetResponse(BaseModel):
    data: Data
