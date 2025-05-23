# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TopGainersLoserGetParams"]


class TopGainersLoserGetParams(TypedDict, total=False):
    vs_currency: Required[str]
    """
    target currency of coins \\**refers to
    [`/simple/supported_vs_currencies`](/reference/simple-supported-currencies).
    """

    duration: Literal["1h", "24h", "7d", "14d", "30d", "60d", "1y"]
    """filter result by time range Default value: `24h`"""

    top_coins: Literal["300", "500", "1000", "all"]
    """
    filter result by market cap ranking (top 300 to 1000) or all coins (including
    coins that do not have market cap) Default value: `1000`
    """
