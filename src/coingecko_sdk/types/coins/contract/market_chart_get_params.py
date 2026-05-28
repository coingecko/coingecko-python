# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["MarketChartGetParams"]


class MarketChartGetParams(TypedDict, total=False):
    id: Required[str]

    days: Required[str]
    """Data up to number of days ago.

    You may use any integer or `max` for number of days.
    """

    vs_currency: Required[str]
    """Target currency of market data.

    \\**refers to
    [`/simple/supported_vs_currencies`](/reference/simple-supported-currencies).
    """

    interval: Literal["5m", "hourly", "daily"]
    """Data interval, leave empty for auto granularity."""

    precision: Literal[
        "full", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18"
    ]
    """Decimal place for currency price value."""
