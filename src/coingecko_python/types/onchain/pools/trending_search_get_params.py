# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["TrendingSearchGetParams"]


class TrendingSearchGetParams(TypedDict, total=False):
    include: str
    """
    attributes to include, comma-separated if more than one to include Available
    values: `base_token`, `quote_token`, `dex`, `network`
    """

    pools: int
    """number of pools to return, maximum 10 Default value: 4"""
