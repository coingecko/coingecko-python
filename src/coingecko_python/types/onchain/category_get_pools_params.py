# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["CategoryGetPoolsParams"]


class CategoryGetPoolsParams(TypedDict, total=False):
    include: str
    """
    attributes to include, comma-separated if more than one to include Available
    values: `base_token`, `quote_token`, `dex`, `network`. Example: `base_token` or
    `base_token,dex`
    """

    page: int
    """page through results Default value: `1`"""

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
    """sort the pools by field Default value: `pool_created_at_desc`"""
