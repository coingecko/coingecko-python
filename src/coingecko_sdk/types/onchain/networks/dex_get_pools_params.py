# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["DexGetPoolsParams"]


class DexGetPoolsParams(TypedDict, total=False):
    network: Required[str]

    include: str
    """Attributes to include, comma-separated if more than one.

    Available values: `base_token`, `quote_token`, `dex`
    """

    include_gt_community_data: bool
    """Include GeckoTerminal community data (sentiment votes, suspicious reports).

    Default: `false`
    """

    page: int
    """Page through results. Default value: 1"""

    sort: Literal["h24_tx_count_desc", "h24_volume_usd_desc"]
    """Sort the pools by field. Default: `h24_tx_count_desc`"""
