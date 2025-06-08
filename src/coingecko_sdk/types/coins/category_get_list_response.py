# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["CategoryGetListResponse"]


class CategoryGetListResponse(BaseModel):
    category_id: Optional[str] = None
    """category ID"""

    name: Optional[str] = None
    """category name"""
