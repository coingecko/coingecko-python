# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["MarketChartGetParams"]


class MarketChartGetParams(TypedDict, total=False):
    days: Required[str]
    """data up to number of days Valid values: any integer or max"""
