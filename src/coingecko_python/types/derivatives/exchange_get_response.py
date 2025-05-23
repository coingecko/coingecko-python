# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ExchangeGetResponse"]


class ExchangeGetResponse(BaseModel):
    id: Optional[str] = None
    """derivatives exchange ID"""

    country: Optional[str] = None
    """derivatives exchange incorporated country"""

    description: Optional[str] = None
    """derivatives exchange description"""

    image: Optional[str] = None
    """derivatives exchange image url"""

    name: Optional[str] = None
    """derivatives exchange name"""

    number_of_futures_pairs: Optional[float] = None
    """number of futures pairs in the derivatives exchange"""

    number_of_perpetual_pairs: Optional[float] = None
    """number of perpetual pairs in the derivatives exchange"""

    open_interest_btc: Optional[float] = None
    """derivatives exchange open interest in BTC"""

    trade_volume_24h_btc: Optional[str] = None
    """derivatives exchange trade volume in BTC in 24 hours"""

    url: Optional[str] = None
    """derivatives exchange website url"""

    year_established: Optional[float] = None
    """derivatives exchange established year"""
