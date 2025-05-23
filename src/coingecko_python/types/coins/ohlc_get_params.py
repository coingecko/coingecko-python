# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["OhlcGetParams"]


class OhlcGetParams(TypedDict, total=False):
    days: Required[Literal["1", "7", "14", "30", "90", "180", "365", "max"]]
    """data up to number of days ago"""

    vs_currency: Required[str]
    """
    target currency of price data \\**refers to
    [`/simple/supported_vs_currencies`](/reference/simple-supported-currencies).
    """

    interval: Literal["daily", "hourly"]
    """data interval, leave empty for auto granularity"""

    precision: Literal[
        "full", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18"
    ]
    """decimal place for currency price value"""
