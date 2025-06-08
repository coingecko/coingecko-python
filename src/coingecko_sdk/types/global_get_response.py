# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["GlobalGetResponse", "Data", "DataMarketCapPercentage", "DataTotalMarketCap", "DataTotalVolume"]


class DataMarketCapPercentage(BaseModel):
    btc: Optional[float] = None

    eth: Optional[float] = None


class DataTotalMarketCap(BaseModel):
    btc: Optional[float] = None

    eth: Optional[float] = None


class DataTotalVolume(BaseModel):
    btc: Optional[float] = None

    eth: Optional[float] = None


class Data(BaseModel):
    active_cryptocurrencies: Optional[float] = None
    """number of active cryptocurrencies"""

    ended_icos: Optional[float] = None
    """number of ended icos"""

    market_cap_change_percentage_24h_usd: Optional[float] = None
    """cryptocurrencies market cap change percentage in 24 hours in usd"""

    market_cap_percentage: Optional[DataMarketCapPercentage] = None
    """cryptocurrencies market cap percentage"""

    markets: Optional[float] = None
    """number of exchanges"""

    ongoing_icos: Optional[float] = None
    """number of ongoing icos"""

    total_market_cap: Optional[DataTotalMarketCap] = None
    """cryptocurrencies total market cap"""

    total_volume: Optional[DataTotalVolume] = None
    """cryptocurrencies total volume"""

    upcoming_icos: Optional[float] = None
    """number of upcoming icos"""

    updated_at: Optional[float] = None


class GlobalGetResponse(BaseModel):
    data: Optional[Data] = None
