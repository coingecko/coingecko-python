# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ....._models import BaseModel

__all__ = ["TokenPriceGetAddressesResponse", "Data", "DataAttributes"]


class DataAttributes(BaseModel):
    token_prices: Optional[Dict[str, str]] = None


class Data(BaseModel):
    id: Optional[str] = None

    attributes: Optional[DataAttributes] = None

    type: Optional[str] = None


class TokenPriceGetAddressesResponse(BaseModel):
    data: Optional[Data] = None
