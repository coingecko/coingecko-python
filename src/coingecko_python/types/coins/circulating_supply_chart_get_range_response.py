# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional

from ..._models import BaseModel

__all__ = ["CirculatingSupplyChartGetRangeResponse"]


class CirculatingSupplyChartGetRangeResponse(BaseModel):
    circulating_supply: Optional[List[List[Union[float, str]]]] = None
