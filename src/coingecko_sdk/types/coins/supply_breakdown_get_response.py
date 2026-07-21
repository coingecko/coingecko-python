# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["SupplyBreakdownGetResponse", "NonCirculatingWallet", "SupplyData"]


class NonCirculatingWallet(BaseModel):
    address: Optional[str] = None
    """Wallet address"""

    anomaly: Optional[bool] = None
    """
    Indicates an unreliable balance update; when true, circulating supply falls back
    to the last known-good balance
    """

    balance: Optional[float] = None
    """Wallet balance"""

    label: Optional[str] = None
    """Wallet label"""

    last_updated: Optional[str] = None
    """Last updated timestamp in ISO 8601 format"""

    percentage_of_total_supply: Optional[float] = None
    """Percentage of total supply held by this wallet"""


class SupplyData(BaseModel):
    """Supply data"""

    circulating_supply: Optional[float] = None
    """Circulating supply"""

    last_updated: Optional[str] = None
    """Last updated timestamp in ISO 8601 format"""

    non_circulating_supply: Optional[float] = None
    """Non-circulating supply"""

    outstanding_supply: Optional[float] = None
    """Outstanding supply"""

    total_supply: Optional[float] = None
    """Total supply"""


class SupplyBreakdownGetResponse(BaseModel):
    id: str
    """Coin ID"""

    name: str
    """Coin name"""

    non_circulating_wallets: List[NonCirculatingWallet]
    """List of non-circulating wallets"""

    supply_data: SupplyData
    """Supply data"""

    symbol: str
    """Coin symbol"""
