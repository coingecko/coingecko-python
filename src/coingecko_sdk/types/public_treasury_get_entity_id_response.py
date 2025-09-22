# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["PublicTreasuryGetEntityIDResponse", "Holding"]


class Holding(BaseModel):
    amount: Optional[int] = None
    """amount of the cryptocurrency held"""

    coin_id: Optional[str] = None
    """coin ID"""

    percentage_of_total_supply: Optional[float] = None
    """percentage of total crypto supply"""


class PublicTreasuryGetEntityIDResponse(BaseModel):
    id: Optional[str] = None
    """entity ID"""

    country: Optional[str] = None
    """country code of company or government location"""

    holdings: Optional[List[Holding]] = None
    """list of cryptocurrency assets held by the entity"""

    name: Optional[str] = None
    """entity name"""

    symbol: Optional[str] = None
    """stock market symbol for public company"""

    twitter_screen_name: Optional[str] = None
    """official Twitter handle of the entity"""

    type: Optional[str] = None
    """entity type: company or government"""

    website_url: Optional[str] = None
    """official website URL of the entity"""
