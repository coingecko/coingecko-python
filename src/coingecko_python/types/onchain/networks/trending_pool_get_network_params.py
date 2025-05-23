# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["TrendingPoolGetNetworkParams"]


class TrendingPoolGetNetworkParams(TypedDict, total=False):
    duration: Literal["5m", "1h", "6h", "24h"]
    """duration to sort trending list by Default value: 24h"""

    include: str
    """
    attributes to include, comma-separated if more than one to include Available
    values: `base_token`, `quote_token`, `dex`
    """

    page: int
    """page through results Default value: 1"""
