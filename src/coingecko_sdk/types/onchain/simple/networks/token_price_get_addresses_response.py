# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ....._models import BaseModel

__all__ = ["TokenPriceGetAddressesResponse", "Data", "DataAttributes"]


class DataAttributes(BaseModel):
    token_prices: Dict[str, str]
    """Token prices keyed by contract address"""

    h24_price_change_percentage: Optional[Dict[str, str]] = None
    """24hr price change percentage keyed by contract address"""

    h24_volume_usd: Optional[Dict[str, str]] = None
    """24hr volume in USD keyed by contract address"""

    last_trade_timestamp: Optional[Dict[str, str]] = None
    """Last trade timestamp keyed by contract address"""

    market_cap_usd: Optional[Dict[str, str]] = None
    """Market cap in USD keyed by contract address"""

    total_reserve_in_usd: Optional[Dict[str, str]] = None
    """Total reserve in USD keyed by contract address"""


class Data(BaseModel):
    id: str
    """Request ID"""

    attributes: DataAttributes

    type: str
    """Response type"""


class TokenPriceGetAddressesResponse(BaseModel):
    data: Data
