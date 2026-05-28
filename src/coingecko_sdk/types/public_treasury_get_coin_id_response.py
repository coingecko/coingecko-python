# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = [
    "PublicTreasuryGetCoinIDResponse",
    "CompanyTreasury",
    "CompanyTreasuryCompany",
    "GovernmentTreasury",
    "GovernmentTreasuryGovernment",
]


class CompanyTreasuryCompany(BaseModel):
    country: str
    """Country code"""

    name: str
    """Company name"""

    percentage_of_total_supply: float
    """Percentage of total crypto supply"""

    symbol: Optional[str] = None
    """Company ticker symbol"""

    total_current_value_usd: float
    """Total current value of crypto holdings in USD"""

    total_entry_value_usd: float
    """Total entry value in USD"""

    total_holdings: float
    """Total crypto holdings"""


class CompanyTreasury(BaseModel):
    companies: List[CompanyTreasuryCompany]
    """List of companies holding crypto"""

    market_cap_dominance: float
    """Market cap dominance percentage"""

    total_holdings: float
    """Total crypto holdings"""

    total_value_usd: float
    """Total crypto holdings value in USD"""


class GovernmentTreasuryGovernment(BaseModel):
    country: str
    """Country code"""

    name: str
    """Government name"""

    percentage_of_total_supply: float
    """Percentage of total crypto supply"""

    symbol: Optional[str] = None
    """Government ticker symbol"""

    total_current_value_usd: float
    """Total current value of crypto holdings in USD"""

    total_entry_value_usd: float
    """Total entry value in USD"""

    total_holdings: float
    """Total crypto holdings"""


class GovernmentTreasury(BaseModel):
    governments: List[GovernmentTreasuryGovernment]
    """List of governments holding crypto"""

    market_cap_dominance: float
    """Market cap dominance percentage"""

    total_holdings: float
    """Total crypto holdings"""

    total_value_usd: float
    """Total crypto holdings value in USD"""


PublicTreasuryGetCoinIDResponse: TypeAlias = Union[CompanyTreasury, GovernmentTreasury]
