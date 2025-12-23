# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = [
    "PublicTreasuryGetCoinIDResponse",
    "CompaniesTreasury",
    "CompaniesTreasuryCompany",
    "GovernmentsTreasury",
    "GovernmentsTreasuryGovernment",
]


class CompaniesTreasuryCompany(BaseModel):
    country: Optional[str] = None
    """company incorporated or government country"""

    name: Optional[str] = None
    """company or government name"""

    percentage_of_total_supply: Optional[float] = None
    """percentage of total crypto supply"""

    symbol: Optional[str] = None
    """company symbol"""

    total_current_value_usd: Optional[float] = None
    """total current value of crypto holdings in usd"""

    total_entry_value_usd: Optional[float] = None
    """total entry value in usd"""

    total_holdings: Optional[float] = None
    """total crypto holdings"""


class CompaniesTreasury(BaseModel):
    companies: List[CompaniesTreasuryCompany]

    market_cap_dominance: float
    """market cap dominance"""

    total_holdings: float
    """total crypto holdings of companies"""

    total_value_usd: float
    """total crypto holdings value in usd"""


class GovernmentsTreasuryGovernment(BaseModel):
    country: Optional[str] = None
    """company incorporated or government country"""

    name: Optional[str] = None
    """company or government name"""

    percentage_of_total_supply: Optional[float] = None
    """percentage of total crypto supply"""

    symbol: Optional[str] = None
    """company symbol"""

    total_current_value_usd: Optional[float] = None
    """total current value of crypto holdings in usd"""

    total_entry_value_usd: Optional[float] = None
    """total entry value in usd"""

    total_holdings: Optional[float] = None
    """total crypto holdings"""


class GovernmentsTreasury(BaseModel):
    governments: List[GovernmentsTreasuryGovernment]

    market_cap_dominance: float
    """market cap dominance"""

    total_holdings: float
    """total crypto holdings of governments"""

    total_value_usd: float
    """total crypto holdings value in usd"""


PublicTreasuryGetCoinIDResponse: TypeAlias = Union[CompaniesTreasury, GovernmentsTreasury]
