# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["ExchangeGetResponse", "ExchangeGetResponseItem"]


class ExchangeGetResponseItem(BaseModel):
    id: str
    """Derivatives exchange ID"""

    country: Optional[str] = None
    """Derivatives exchange incorporated country"""

    description: str
    """Derivatives exchange description"""

    image: str
    """Derivatives exchange image URL"""

    name: str
    """Derivatives exchange name"""

    number_of_futures_pairs: int
    """Number of futures pairs in the derivatives exchange"""

    number_of_perpetual_pairs: int
    """Number of perpetual pairs in the derivatives exchange"""

    open_interest_btc: float
    """Derivatives exchange open interest in BTC"""

    trade_volume_24h_btc: str
    """Derivatives exchange trade volume in BTC in 24 hours"""

    url: str
    """Derivatives exchange website URL"""

    year_established: Optional[int] = None
    """Derivatives exchange established year"""


ExchangeGetResponse: TypeAlias = List[ExchangeGetResponseItem]
