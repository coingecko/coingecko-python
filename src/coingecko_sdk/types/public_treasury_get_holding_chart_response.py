# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["PublicTreasuryGetHoldingChartResponse"]


class PublicTreasuryGetHoldingChartResponse(BaseModel):
    holding_value_in_usd: Optional[List[List[float]]] = None

    holdings: Optional[List[List[float]]] = None
