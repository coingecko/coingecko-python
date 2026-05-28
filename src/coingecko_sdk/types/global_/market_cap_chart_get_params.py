# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["MarketCapChartGetParams"]


class MarketCapChartGetParams(TypedDict, total=False):
    days: Required[Literal["1", "7", "14", "30", "90", "180", "365", "max"]]
    """Data up to number of days ago."""

    vs_currency: str
    """Target currency of market cap.

    Default: `usd` \\**refers to
    [`/simple/supported_vs_currencies`](/reference/simple-supported-currencies).
    """
