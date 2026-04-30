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
    """
    holding amount changes over different timeframes (only present if holding_amount_change param is used)
    """

    period_14d: Optional[float] = FieldInfo(alias="14d", default=None)

    period_1y: Optional[float] = FieldInfo(alias="1y", default=None)

    period_30d: Optional[float] = FieldInfo(alias="30d", default=None)

    period_7d: Optional[float] = FieldInfo(alias="7d", default=None)

    period_90d: Optional[float] = FieldInfo(alias="90d", default=None)

    ytd: Optional[float] = None


class HoldingHoldingChangePercentage(BaseModel):
    """
    holding change percentages over different timeframes (only present if holding_change_percentage param is used)
    """

    period_14d: Optional[float] = FieldInfo(alias="14d", default=None)

    period_1y: Optional[float] = FieldInfo(alias="1y", default=None)

    period_30d: Optional[float] = FieldInfo(alias="30d", default=None)

    period_7d: Optional[float] = FieldInfo(alias="7d", default=None)

    period_90d: Optional[float] = FieldInfo(alias="90d", default=None)

    ytd: Optional[float] = None


class Holding(BaseModel):
    amount: Optional[int] = None
    """amount of the cryptocurrency held"""

    amount_per_share: Optional[float] = None
    """amount of cryptocurrency per share"""

    average_entry_value_usd: Optional[float] = None
    """average entry cost per unit in USD"""

    coin_id: Optional[str] = None
    """coin ID"""

    current_value_usd: Optional[float] = None
    """current value of holdings in USD"""

    entity_value_usd_percentage: Optional[float] = None
    """percentage of entity's total treasury value"""

    holding_amount_change: Optional[HoldingHoldingAmountChange] = None
    """
    holding amount changes over different timeframes (only present if
    holding_amount_change param is used)
    """

    holding_change_percentage: Optional[HoldingHoldingChangePercentage] = None
    """
    holding change percentages over different timeframes (only present if
    holding_change_percentage param is used)
    """

    percentage_of_total_supply: Optional[float] = None
    """percentage of total crypto supply"""

    total_entry_value_usd: Optional[float] = None
    """total entry cost/purchase value in USD"""

    unrealized_pnl: Optional[float] = None
    """unrealized profit and loss for this holding"""


class PublicTreasuryGetEntityIDResponse(BaseModel):
    id: Optional[str] = None
    """entity ID"""

    country: Optional[str] = None
    """country code of company or government location"""

    holdings: Optional[List[Holding]] = None
    """list of cryptocurrency assets held by the entity"""

    m_nav: Optional[float] = None
    """market to net asset value ratio"""

    name: Optional[str] = None
    """entity name"""

    symbol: Optional[str] = None
    """stock market symbol for public company"""

    total_asset_value_per_share_usd: Optional[float] = None
    """total asset value per share in USD"""

    total_treasury_value_usd: Optional[float] = None
    """total current value of all holdings in USD"""

    twitter_screen_name: Optional[str] = None
    """official Twitter handle of the entity"""

    type: Optional[str] = None
    """entity type: company or government"""

    unrealized_pnl: Optional[float] = None
    """unrealized profit and loss (current value - total entry value)"""

    website_url: Optional[str] = None
    """official website URL of the entity"""
