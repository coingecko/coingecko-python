# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union

from ..._models import BaseModel

__all__ = ["CirculatingSupplyChartGetResponse"]


class CirculatingSupplyChartGetResponse(BaseModel):
    circulating_supply: List[List[Union[float, str]]]
    """Circulating supply data points as [timestamp, supply] pairs"""
