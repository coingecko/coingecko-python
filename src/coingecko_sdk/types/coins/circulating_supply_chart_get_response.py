# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional

from ..._models import BaseModel

__all__ = ["CirculatingSupplyChartGetResponse"]


class CirculatingSupplyChartGetResponse(BaseModel):
    circulating_supply: Optional[List[List[Union[float, str]]]] = None
