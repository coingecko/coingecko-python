# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PublicTreasuryGetTransactionHistoryResponse", "Transaction"]


class Transaction(BaseModel):
    average_entry_value_usd: float
    """Average entry value in USD after the transaction"""

    coin_id: str
    """Coin ID"""

    date: float
    """Transaction date in UNIX timestamp"""

    holding_balance: float
    """Total holding balance after the transaction"""

    holding_net_change: float
    """Net change in holdings after the transaction"""

    source_url: str
    """Source document URL"""

    transaction_value_usd: float
    """Transaction value in USD"""

    type: Literal["buy", "sell"]
    """Transaction type"""


class PublicTreasuryGetTransactionHistoryResponse(BaseModel):
    transactions: List[Transaction]
