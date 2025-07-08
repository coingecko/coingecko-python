# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["ExchangeGetListResponse", "ExchangeGetListResponseItem"]


class ExchangeGetListResponseItem(BaseModel):
    id: str
    """exchange ID"""

    name: str
    """exchange name"""


ExchangeGetListResponse: TypeAlias = List[ExchangeGetListResponseItem]
