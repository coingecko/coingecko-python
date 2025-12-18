# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ....._models import BaseModel

__all__ = ["TokenPriceGetAddressesResponse", "Data", "DataAttributes"]


class DataAttributes(BaseModel):
    h24_price_change_percentage: Optional[Dict[str, str]] = None

    h24_volume_usd: Optional[Dict[str, str]] = None

    last_trade_timestamp: Optional[Dict[str, int]] = None

    market_cap_usd: Optional[Dict[str, str]] = None

    token_prices: Optional[Dict[str, str]] = None

    total_reserve_in_usd: Optional[Dict[str, str]] = None


class Data(BaseModel):
    id: Optional[str] = None

    attributes: Optional[DataAttributes] = None

    type: Optional[str] = None


class TokenPriceGetAddressesResponse(BaseModel):
    data: Optional[Data] = None
