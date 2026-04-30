# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["DetailPlatformData"]


class DetailPlatformData(BaseModel):
    contract_address: Optional[str] = None
    """contract address on the platform"""

    decimal_place: Optional[float] = None
    """decimal places for the token"""
