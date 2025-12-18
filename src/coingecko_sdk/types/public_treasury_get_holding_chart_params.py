# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PublicTreasuryGetHoldingChartParams"]


class PublicTreasuryGetHoldingChartParams(TypedDict, total=False):
    entity_id: Required[str]

    days: Required[str]
    """data up to number of days ago Valid values: `7, 14, 30, 90, 180, 365, 730, max`"""

    include_empty_intervals: bool
    """include empty intervals with no transaction data, default: false"""
