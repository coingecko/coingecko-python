# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union

from .._models import BaseModel

__all__ = ["GlobalGetFearAndGreedChartResponse"]


class GlobalGetFearAndGreedChartResponse(BaseModel):
    fear_and_greed: List[List[Union[int, str]]]
    """Fear and greed data points as [timestamp, value, sentiment]"""
