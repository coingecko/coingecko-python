# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["TopGainersLosersItem"]


class TopGainersLosersItem(BaseModel):
    id: str
    """Coin ID"""

    image: str
    """Coin image URL"""

    market_cap_rank: Optional[int] = None
    """Coin market cap rank"""

    name: str
    """Coin name"""

    symbol: str
    """Coin symbol"""

    usd: float
    """Coin price in the target currency"""

    usd_24h_change: Optional[float] = None
    """24-hour price change percentage"""

    usd_24h_vol: float
    """24-hour trading volume in the target currency"""

    usd_14d_change: Optional[float] = None
    """14-day price change percentage"""

    usd_1h_change: Optional[float] = None
    """1-hour price change percentage"""

    usd_1y_change: Optional[float] = None
    """1-year price change percentage"""

    usd_200d_change: Optional[float] = None
    """200-day price change percentage"""

    usd_30d_change: Optional[float] = None
    """30-day price change percentage"""

    usd_60d_change: Optional[float] = None
    """60-day price change percentage"""

    usd_7d_change: Optional[float] = None
    """7-day price change percentage"""
