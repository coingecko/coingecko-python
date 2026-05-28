# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["TrendingSearchGetParams"]


class TrendingSearchGetParams(TypedDict, total=False):
    include: str
    """Attributes to include, comma-separated if more than one.

    Available values: `base_token`, `quote_token`, `dex`, `network`
    """

    pools: int
    """Number of pools to return, maximum 10. Default value: 4"""
