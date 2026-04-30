# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["TreasuryEntity"]


class TreasuryEntity(BaseModel):
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
