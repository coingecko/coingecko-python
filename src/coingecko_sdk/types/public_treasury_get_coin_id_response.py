# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel
from .treasury_entity import TreasuryEntity

__all__ = ["PublicTreasuryGetCoinIDResponse", "CompaniesTreasury", "GovernmentsTreasury"]


class CompaniesTreasury(BaseModel):
    companies: Optional[List[TreasuryEntity]] = None

    market_cap_dominance: Optional[float] = None
    """market cap dominance"""

    total_holdings: Optional[float] = None
    """total crypto holdings of companies"""

    total_value_usd: Optional[float] = None
    """total crypto holdings value in usd"""


class GovernmentsTreasury(BaseModel):
    governments: Optional[List[TreasuryEntity]] = None

    market_cap_dominance: Optional[float] = None
    """market cap dominance"""

    total_holdings: Optional[float] = None
    """total crypto holdings of governments"""

    total_value_usd: Optional[float] = None
    """total crypto holdings value in usd"""


PublicTreasuryGetCoinIDResponse: TypeAlias = Union[CompaniesTreasury, GovernmentsTreasury]
