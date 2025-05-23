# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["NFTGetMarketsParams"]


class NFTGetMarketsParams(TypedDict, total=False):
    asset_platform_id: str
    """
    filter result by asset platform (blockchain network) \\**refers to
    [`/asset_platforms`](/reference/asset-platforms-list) filter=`nft`
    """

    order: Literal[
        "h24_volume_native_asc",
        "h24_volume_native_desc",
        "h24_volume_usd_asc",
        "h24_volume_usd_desc",
        "market_cap_usd_asc",
        "market_cap_usd_desc",
    ]
    """sort results by field Default: `market_cap_usd_desc`"""

    page: float
    """page through results Default: `1`"""

    per_page: float
    """
    total results per page Valid values: any integer between 1 and 250 Default:
    `100`
    """
