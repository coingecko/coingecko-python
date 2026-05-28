# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["PublicTreasuryGetHoldingChartResponse"]


class PublicTreasuryGetHoldingChartResponse(BaseModel):
    holding_value_in_usd: List[List[float]]
    """Historical holdings value in USD as [timestamp, value_usd] pairs"""

    holdings: List[List[float]]
    """Historical holdings data as [timestamp, amount] pairs"""
