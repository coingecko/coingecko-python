# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["MarketCapChartGetResponse", "MarketCapChart"]


class MarketCapChart(BaseModel):
    market_cap: List[List[float]]
    """Market cap data as [timestamp, market_cap] pairs"""

    volume: List[List[float]]
    """Volume data as [timestamp, volume] pairs"""


class MarketCapChartGetResponse(BaseModel):
    market_cap_chart: MarketCapChart
