# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["CategoryGetParams"]


class CategoryGetParams(TypedDict, total=False):
    page: int
    """page through results Default value: `1`"""

    sort: Literal[
        "h1_volume_percentage_desc",
        "h6_volume_percentage_desc",
        "h12_volume_percentage_desc",
        "h24_tx_count_desc",
        "h24_volume_usd_desc",
        "fdv_usd_desc",
        "reserve_in_usd_desc",
    ]
    """sort the categories by field Default value: `h6_volume_percentage_desc`"""
