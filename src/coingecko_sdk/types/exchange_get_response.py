# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ExchangeGetResponse"]


class ExchangeGetResponse(BaseModel):
    id: Optional[str] = None
    """exchange ID"""

    country: Optional[str] = None
    """exchange country"""

    description: Optional[str] = None
    """exchange description"""

    has_trading_incentive: Optional[bool] = None
    """exchange trading incentive"""

    image: Optional[str] = None
    """exchange image url"""

    name: Optional[str] = None
    """exchange name"""

    trade_volume_24h_btc: Optional[float] = None
    """exchange trade volume in BTC in 24 hours"""

    trust_score: Optional[float] = None
    """exchange trust score"""

    trust_score_rank: Optional[float] = None
    """exchange trust score rank"""

    url: Optional[str] = None
    """exchange website url"""

    year_established: Optional[float] = None
    """exchange established year"""
