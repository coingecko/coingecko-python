# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["DecentralizedFinanceDefiGetResponse", "Data"]


class Data(BaseModel):
    defi_dominance: str
    """DeFi dominance percentage"""

    defi_market_cap: str
    """DeFi market cap"""

    defi_to_eth_ratio: str
    """DeFi to ETH ratio"""

    eth_market_cap: str
    """ETH market cap"""

    top_coin_defi_dominance: float
    """DeFi top coin dominance percentage"""

    top_coin_name: str
    """DeFi top coin name"""

    trading_volume_24h: str
    """DeFi trading volume in 24 hours"""


class DecentralizedFinanceDefiGetResponse(BaseModel):
    data: Data
