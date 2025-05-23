# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ExchangeGetListResponse"]


class ExchangeGetListResponse(BaseModel):
    id: Optional[str] = None
    """derivatives exchange ID"""

    name: Optional[str] = None
    """derivatives exchange name"""
