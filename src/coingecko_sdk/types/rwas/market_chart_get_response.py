# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["MarketChartGetResponse"]


class MarketChartGetResponse(BaseModel):
    tokenized_market_caps: List[List[float]]
    """Tokenized market cap data points as [timestamp, market_cap] pairs"""

    tokenized_prices: List[List[float]]
    """Tokenized price data points as [timestamp, price] pairs"""

    tokenized_total_volumes: List[List[float]]
    """Tokenized total volume data points as [timestamp, volume] pairs"""
