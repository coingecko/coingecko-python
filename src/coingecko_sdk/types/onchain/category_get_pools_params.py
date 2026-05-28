# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["CategoryGetPoolsParams"]


class CategoryGetPoolsParams(TypedDict, total=False):
    include: str
    """Attributes to include, comma-separated if more than one.

    Available values: `base_token`, `quote_token`, `dex`, `network`
    """

    page: int
    """Page through results. Default value: 1"""

    sort: Literal[
        "m5_trending",
        "h1_trending",
        "h6_trending",
        "h24_trending",
        "h24_tx_count_desc",
        "h24_volume_usd_desc",
        "pool_created_at_desc",
        "h24_price_change_percentage_desc",
    ]
    """Sort the pools by field. Default: `pool_created_at_desc`"""
