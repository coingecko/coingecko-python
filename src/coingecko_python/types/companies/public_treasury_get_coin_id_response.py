# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["PublicTreasuryGetCoinIDResponse", "Company"]


class Company(BaseModel):
    country: Optional[str] = None
    """company incorporated country"""

    name: Optional[str] = None
    """company name"""

    percentage_of_total_supply: Optional[float] = None
    """percentage of total btc/eth supply"""

    symbol: Optional[str] = None
    """company symbol"""

    total_current_value_usd: Optional[float] = None
    """total current value of btc/eth holdings in usd"""

    total_entry_value_usd: Optional[float] = None
    """total entry value in usd"""

    total_holdings: Optional[float] = None
    """total btc/eth holdings of company"""


class PublicTreasuryGetCoinIDResponse(BaseModel):
    companies: Optional[List[Company]] = None

    market_cap_dominance: Optional[float] = None
    """market cap dominance"""

    total_holdings: Optional[float] = None
    """total btc/eth holdings of companies"""

    total_value_usd: Optional[float] = None
    """total btc/eth holdings value in usd"""
