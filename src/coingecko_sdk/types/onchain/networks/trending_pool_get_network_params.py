# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["TrendingPoolGetNetworkParams"]


class TrendingPoolGetNetworkParams(TypedDict, total=False):
    duration: Literal["5m", "1h", "6h", "24h"]
    """Duration to sort trending list by. Default: `24h`"""

    include: str
    """Attributes to include, comma-separated if more than one.

    Available values: `base_token`, `quote_token`, `dex`
    """

    include_gt_community_data: bool
    """Include GeckoTerminal community data (sentiment votes, suspicious reports).

    Default: `false`
    """

    page: int
    """Page through results. Default value: 1"""
