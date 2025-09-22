# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["MarketChartGetRangeParams"]


class MarketChartGetRangeParams(TypedDict, total=False):
    id: Required[str]

    from_: Required[Annotated[str, PropertyInfo(alias="from")]]
    """
    starting date in ISO date string (`YYYY-MM-DD` or `YYYY-MM-DDTHH:MM`) or UNIX
    timestamp. **use ISO date string for best compatibility**
    """

    to: Required[str]
    """
    ending date in ISO date string (`YYYY-MM-DD` or `YYYY-MM-DDTHH:MM`) or UNIX
    timestamp. **use ISO date string for best compatibility**
    """

    vs_currency: Required[str]
    """
    target currency of market data \\**refers to
    [`/simple/supported_vs_currencies`](/reference/simple-supported-currencies).
    """

    interval: Literal["5m", "hourly", "daily"]
    """data interval, leave empty for auto granularity"""

    precision: Literal[
        "full", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18"
    ]
    """decimal place for currency price value"""
