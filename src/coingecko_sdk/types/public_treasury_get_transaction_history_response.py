# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PublicTreasuryGetTransactionHistoryResponse", "Transaction"]


class Transaction(BaseModel):
    average_entry_value_usd: Optional[float] = None
    """average entry value in usd after the transaction"""

    coin_id: Optional[str] = None
    """coin ID"""

    date: Optional[float] = None
    """transaction date in UNIX timestamp"""

    holding_balance: Optional[float] = None
    """total holding balance after the transaction"""

    holding_net_change: Optional[float] = None
    """net change in holdings after the transaction"""

    source_url: Optional[str] = None
    """source document URL"""

    transaction_value_usd: Optional[float] = None
    """transaction value in usd"""

    type: Optional[Literal["buy", "sell"]] = None
    """transaction type: buy or sell"""


class PublicTreasuryGetTransactionHistoryResponse(BaseModel):
    transactions: Optional[List[Transaction]] = None
