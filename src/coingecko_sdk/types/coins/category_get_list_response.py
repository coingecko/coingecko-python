# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["CategoryGetListResponse", "CategoryGetListResponseItem"]


class CategoryGetListResponseItem(BaseModel):
    category_id: str
    """Category ID"""

    name: str
    """Category name"""


CategoryGetListResponse: TypeAlias = List[CategoryGetListResponseItem]
