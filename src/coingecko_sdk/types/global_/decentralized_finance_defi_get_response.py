# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["DecentralizedFinanceDefiGetResponse", "Data"]


class Data(BaseModel):
    defi_dominance: Optional[str] = None
    """defi dominance"""

    defi_market_cap: Optional[str] = None
    """defi market cap"""

    defi_to_eth_ratio: Optional[str] = None
    """defi to eth ratio"""

    eth_market_cap: Optional[str] = None
    """eth market cap"""

    top_coin_defi_dominance: Optional[float] = None
    """defi top coin dominance"""

    top_coin_name: Optional[str] = None
    """defi top coin name"""

    trading_volume_24h: Optional[str] = None
    """defi trading volume in 24 hours"""


class DecentralizedFinanceDefiGetResponse(BaseModel):
    data: Optional[Data] = None
