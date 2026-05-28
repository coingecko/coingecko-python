# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = [
    "PublicTreasuryGetCoinIDResponse",
    "UnionMember0",
    "UnionMember0Company",
    "UnionMember1",
    "UnionMember1Government",
]


class UnionMember0Company(BaseModel):
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


class UnionMember0(BaseModel):
    companies: List[UnionMember0Company]
    """List of companies holding crypto"""

    market_cap_dominance: float
    """Market cap dominance percentage"""

    total_holdings: float
    """Total crypto holdings"""

    total_value_usd: float
    """Total crypto holdings value in USD"""


class UnionMember1Government(BaseModel):
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


class UnionMember1(BaseModel):
    governments: List[UnionMember1Government]
    """List of governments holding crypto"""

    market_cap_dominance: float
    """Market cap dominance percentage"""

    total_holdings: float
    """Total crypto holdings"""

    total_value_usd: float
    """Total crypto holdings value in USD"""


PublicTreasuryGetCoinIDResponse: TypeAlias = Union[UnionMember0, UnionMember1]
