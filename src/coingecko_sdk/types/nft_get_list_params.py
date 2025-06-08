# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["NFTGetListParams"]


class NFTGetListParams(TypedDict, total=False):
    order: Literal[
        "h24_volume_usd_asc",
        "h24_volume_usd_desc",
        "h24_volume_native_asc",
        "h24_volume_native_desc",
        "floor_price_native_asc",
        "floor_price_native_desc",
        "market_cap_native_asc",
        "market_cap_native_desc",
        "market_cap_usd_asc",
        "market_cap_usd_desc",
    ]
    """use this to sort the order of responses"""

    page: float
    """page through results"""

    per_page: float
    """total results per page Valid values: 1...250"""
