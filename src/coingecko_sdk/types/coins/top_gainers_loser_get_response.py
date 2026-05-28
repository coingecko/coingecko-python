# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .top_gainers_losers_item import TopGainersLosersItem

__all__ = ["TopGainersLoserGetResponse"]


class TopGainersLoserGetResponse(BaseModel):
    top_gainers: List[TopGainersLosersItem]

    top_losers: List[TopGainersLosersItem]
