# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional

from ..._models import BaseModel

__all__ = ["TotalSupplyChartGetRangeResponse"]


class TotalSupplyChartGetRangeResponse(BaseModel):
    total_supply: Optional[List[List[Union[float, str]]]] = None
