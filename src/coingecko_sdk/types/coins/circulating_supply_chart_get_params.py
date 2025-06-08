# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CirculatingSupplyChartGetParams"]


class CirculatingSupplyChartGetParams(TypedDict, total=False):
    days: Required[str]
    """data up to number of days ago Valid values: any integer or `max`"""

    interval: Literal["daily"]
    """data interval"""
