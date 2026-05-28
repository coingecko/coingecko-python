# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["DerivativeGetResponse", "DerivativeGetResponseItem"]


class DerivativeGetResponseItem(BaseModel):
    basis: float
    """Difference of derivative price and index price"""

    contract_type: str
    """Derivative contract type"""

    expired_at: Optional[float] = None
    """Derivative expiry time in UNIX timestamp"""

    funding_rate: float
    """Derivative funding rate"""

    index: float
    """Derivative underlying asset price"""

    index_id: str
    """Derivative underlying asset"""

    last_traded_at: float
    """Derivative last traded time in UNIX timestamp"""

    market: str
    """Derivative market name"""

    open_interest: float
    """Derivative open interest"""

    price: str
    """Derivative ticker price"""

    price_percentage_change_24h: float
    """Derivative ticker price percentage change in 24 hours"""

    spread: float
    """Derivative bid-ask spread"""

    symbol: str
    """Derivative ticker symbol"""

    volume_24h: float
    """Derivative trading volume in 24 hours"""


DerivativeGetResponse: TypeAlias = List[DerivativeGetResponseItem]
