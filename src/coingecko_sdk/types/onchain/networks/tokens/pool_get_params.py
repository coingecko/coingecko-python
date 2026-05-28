# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PoolGetParams"]


class PoolGetParams(TypedDict, total=False):
    network: Required[str]

    include: str
    """Attributes to include, comma-separated if more than one.

    Available values: `base_token`, `quote_token`, `dex`
    """

    include_gt_community_data: bool
    """Include GeckoTerminal community data (sentiment votes, suspicious reports).

    Default: `false`
    """

    include_inactive_source: bool
    """Include tokens from inactive pools using the most recent swap. Default: `false`"""

    page: int
    """Page through results. Default value: 1"""

    sort: Literal["h24_volume_usd_liquidity_desc", "h24_tx_count_desc", "h24_volume_usd_desc"]
    """Sort the pools by field. Default: `h24_volume_usd_liquidity_desc`"""
