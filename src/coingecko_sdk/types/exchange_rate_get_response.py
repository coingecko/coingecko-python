# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from .._models import BaseModel

__all__ = ["ExchangeRateGetResponse", "Rates"]


class Rates(BaseModel):
    name: str
    """Currency name"""

    type: str
    """Currency type: crypto, fiat, or commodity"""

    unit: str
    """Currency unit symbol"""

    value: float
    """Exchange rate value relative to BTC"""


class ExchangeRateGetResponse(BaseModel):
    rates: Dict[str, Rates]
    """Exchange rates keyed by currency code"""
