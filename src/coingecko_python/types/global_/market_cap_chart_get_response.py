# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["MarketCapChartGetResponse", "MarketCapChart"]


class MarketCapChart(BaseModel):
    market_cap: Optional[List[List[float]]] = None

    volume: Optional[List[List[float]]] = None


class MarketCapChartGetResponse(BaseModel):
    market_cap_chart: Optional[MarketCapChart] = None
