# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PublicTreasuryGetEntityIDParams"]


class PublicTreasuryGetEntityIDParams(TypedDict, total=False):
    holding_amount_change: str
    """
    Include holding amount change for specified timeframes, comma-separated if
    querying more than 1 timeframe. Valid values: `7d`, `14d`, `30d`, `90d`, `1y`,
    `ytd`
    """

    holding_change_percentage: str
    """
    Include holding change percentage for specified timeframes, comma-separated if
    querying more than 1 timeframe. Valid values: `7d`, `14d`, `30d`, `90d`, `1y`,
    `ytd`
    """
