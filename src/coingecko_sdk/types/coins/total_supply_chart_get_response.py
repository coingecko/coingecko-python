# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union

from ..._models import BaseModel

__all__ = ["TotalSupplyChartGetResponse"]


class TotalSupplyChartGetResponse(BaseModel):
    total_supply: List[List[Union[float, str]]]
    """Total supply data points as [timestamp, supply] pairs"""
