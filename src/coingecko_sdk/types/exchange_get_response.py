# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["ExchangeGetResponse", "ExchangeGetResponseItem"]


class ExchangeGetResponseItem(BaseModel):
    id: str
    """Exchange ID"""

    country: Optional[str] = None
    """Country where the exchange is based"""

    description: str
    """Exchange description"""

    has_trading_incentive: bool
    """Whether the exchange has trading incentive"""

    image: str
    """Exchange logo URL"""

    name: str
    """Exchange name"""

    trade_volume_24h_btc: float
    """Exchange 24h trading volume in BTC"""

    trust_score: Optional[float] = None
    """Exchange trust score"""

    trust_score_rank: Optional[float] = None
    """Exchange trust score rank"""

    url: str
    """Exchange website URL"""

    year_established: Optional[float] = None
    """Year the exchange was established"""


ExchangeGetResponse: TypeAlias = List[ExchangeGetResponseItem]
