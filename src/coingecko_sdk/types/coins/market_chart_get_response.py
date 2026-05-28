# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["MarketChartGetResponse"]


class MarketChartGetResponse(BaseModel):
    market_caps: List[List[float]]
    """Market cap data points as [timestamp, market_cap] pairs"""

    prices: List[List[float]]
    """Price data points as [timestamp, price] pairs"""

    total_volumes: List[List[float]]
    """Total volume data points as [timestamp, volume] pairs"""
