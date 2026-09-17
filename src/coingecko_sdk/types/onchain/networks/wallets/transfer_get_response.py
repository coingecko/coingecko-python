# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ....._models import BaseModel

__all__ = ["TransferGetResponse", "Data", "DataAttributes", "Meta"]


class DataAttributes(BaseModel):
    amount: Optional[str] = None
    """Transfer amount at full precision"""

    amount_raw: str
    """Transfer amount in the smallest unit, before decimals are applied"""

    block_number: int
    """Block number of the transfer"""

    block_timestamp: datetime
    """Block timestamp of the transfer"""

    decimals: int
    """Token decimals"""

    direction: str
    """Transfer direction relative to the queried wallet, either in or out"""

    from_address: str
    """Sender address"""

    name: str
    """Token name"""

    symbol: str
    """Token symbol"""

    to_address: str
    """Recipient address"""

    token_address: str
    """Token contract address"""

    tx_hash: str
    """Transaction hash"""


class Data(BaseModel):
    id: str
    """Transfer identifier"""

    attributes: DataAttributes

    type: str
    """Resource type"""


class Meta(BaseModel):
    next_cursor: Optional[str] = None
    """Cursor for the next page, null when there are no further pages"""


class TransferGetResponse(BaseModel):
    data: List[Data]

    meta: Meta
