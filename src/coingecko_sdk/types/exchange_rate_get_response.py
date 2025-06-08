# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["ExchangeRateGetResponse", "Rates"]


class Rates(BaseModel):
    name: Optional[str] = None
    """name of the currency"""

    type: Optional[str] = None
    """type of the currency"""

    unit: Optional[str] = None
    """unit of the currency"""

    value: Optional[float] = None
    """value of the currency"""


class ExchangeRateGetResponse(BaseModel):
    rates: Optional[Dict[str, Rates]] = None
