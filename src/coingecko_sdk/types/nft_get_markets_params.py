# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["NFTGetMarketsParams"]


class NFTGetMarketsParams(TypedDict, total=False):
    asset_platform_id: str
    """Filter result by asset platform (blockchain network).

    \\**refers to [`/asset_platforms`](/reference/asset-platforms-list) filter=`nft`.
    """

    order: Literal[
        "h24_volume_native_asc",
        "h24_volume_native_desc",
        "h24_volume_usd_asc",
        "h24_volume_usd_desc",
        "market_cap_usd_asc",
        "market_cap_usd_desc",
    ]
    """Sort results by field. Default: `market_cap_usd_desc`"""

    page: int
    """Page through results. Default value: 1"""

    per_page: int
    """Total results per page. Default value: 100 Valid values: 1...250"""
