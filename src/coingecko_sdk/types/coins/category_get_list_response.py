# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["CategoryGetListResponse", "CategoryGetListResponseItem"]


class CategoryGetListResponseItem(BaseModel):
    category_id: Optional[str] = None
    """category ID"""

    name: Optional[str] = None
    """category name"""


CategoryGetListResponse: TypeAlias = List[CategoryGetListResponseItem]
