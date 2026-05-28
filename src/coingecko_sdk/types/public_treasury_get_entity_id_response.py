# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "PublicTreasuryGetEntityIDResponse",
    "Holding",
    "HoldingHoldingAmountChange",
    "HoldingHoldingChangePercentage",
]


class HoldingHoldingAmountChange(BaseModel):
    """Holding amount changes over different timeframes"""

    period_14d: Optional[float] = FieldInfo(alias="14d", default=None)

    period_1y: Optional[float] = FieldInfo(alias="1y", default=None)

    period_30d: Optional[float] = FieldInfo(alias="30d", default=None)

    period_7d: Optional[float] = FieldInfo(alias="7d", default=None)

    period_90d: Optional[float] = FieldInfo(alias="90d", default=None)

    ytd: Optional[float] = None


class HoldingHoldingChangePercentage(BaseModel):
    """Holding change percentages over different timeframes"""

    period_14d: Optional[float] = FieldInfo(alias="14d", default=None)

    period_1y: Optional[float] = FieldInfo(alias="1y", default=None)

    period_30d: Optional[float] = FieldInfo(alias="30d", default=None)

    period_7d: Optional[float] = FieldInfo(alias="7d", default=None)

    period_90d: Optional[float] = FieldInfo(alias="90d", default=None)

    ytd: Optional[float] = None


class Holding(BaseModel):
    amount: float
    """Amount of cryptocurrency held"""

    amount_per_share: float
    """Amount of cryptocurrency per share"""

    average_entry_value_usd: float
    """Average entry cost per unit in USD"""

    coin_id: str
    """Coin ID"""

    current_value_usd: float
    """Current value of holdings in USD"""

    entity_value_usd_percentage: float
    """Percentage of entity's total treasury value"""

    percentage_of_total_supply: float
    """Percentage of total crypto supply"""

    total_entry_value_usd: float
    """Total entry cost in USD"""

    unrealized_pnl: float
    """Unrealized profit and loss for this holding"""

    holding_amount_change: Optional[HoldingHoldingAmountChange] = None
    """Holding amount changes over different timeframes"""

    holding_change_percentage: Optional[HoldingHoldingChangePercentage] = None
    """Holding change percentages over different timeframes"""


class PublicTreasuryGetEntityIDResponse(BaseModel):
    id: str
    """Entity ID"""

    country: str
    """Country code"""

    holdings: List[Holding]
    """List of cryptocurrency assets held by the entity"""

    m_nav: float
    """Market to net asset value ratio"""

    name: str
    """Entity name"""

    symbol: Optional[str] = None
    """Stock market ticker symbol"""

    total_asset_value_per_share_usd: float
    """Total asset value per share in USD"""

    total_treasury_value_usd: float
    """Total current value of all holdings in USD"""

    twitter_screen_name: str
    """Official Twitter handle"""

    type: str
    """Entity type: company or government"""

    unrealized_pnl: float
    """Unrealized profit and loss (current value minus total entry value)"""

    website_url: str
    """Official website URL"""
