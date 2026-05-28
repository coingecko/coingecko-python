# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel

__all__ = ["DexGetResponse", "Data", "DataAttributes"]


class DataAttributes(BaseModel):
    name: str
    """DEX name"""


class Data(BaseModel):
    id: str
    """DEX identifier"""

    attributes: DataAttributes

    type: str
    """Resource type"""


class DexGetResponse(BaseModel):
    data: List[Data]
