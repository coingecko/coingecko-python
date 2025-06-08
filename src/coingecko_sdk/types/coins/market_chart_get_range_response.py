# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["MarketChartGetRangeResponse"]


class MarketChartGetRangeResponse(BaseModel):
    market_caps: Optional[List[List[float]]] = None

    prices: Optional[List[List[float]]] = None

    total_volumes: Optional[List[List[float]]] = None
