# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = ["LiquidityEventGetResponse", "Data", "DataAttributes", "Meta"]


class DataAttributes(BaseModel):
    base_token_address: str
    """Base token contract address"""

    base_token_amount: str
    """Amount of base token added or removed"""

    base_token_price_in_usd: str
    """Price of base token in USD at the time of the event"""

    block_number: int
    """Block number of the liquidity event"""

    block_timestamp: str
    """Block timestamp"""

    kind: Literal["add", "remove"]
    """Liquidity event kind (add or remove)"""

    quote_token_address: str
    """Quote token contract address"""

    quote_token_amount: str
    """Amount of quote token added or removed"""

    quote_token_price_in_usd: str
    """Price of quote token in USD at the time of the event"""

    tx_from_address: str
    """Transaction sender address"""

    tx_hash: str
    """Transaction hash"""

    volume_in_usd: str
    """Total value of the liquidity event in USD"""


class Data(BaseModel):
    id: str
    """Liquidity event identifier"""

    attributes: DataAttributes

    type: str
    """Resource type"""


class Meta(BaseModel):
    next_cursor: Optional[str] = None
    """Cursor for the next page, null when there are no further pages"""


class LiquidityEventGetResponse(BaseModel):
    data: List[Data]

    meta: Optional[Meta] = None
