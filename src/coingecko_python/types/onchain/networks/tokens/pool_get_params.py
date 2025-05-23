# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PoolGetParams"]


class PoolGetParams(TypedDict, total=False):
    network: Required[str]

    include: str
    """
    attributes to include, comma-separated if more than one to include Available
    values: `base_token`, `quote_token`, `dex`
    """

    page: int
    """page through results Default value: 1"""

    sort: Literal["h24_volume_usd_liquidity_desc", "h24_tx_count_desc", "h24_volume_usd_desc"]
    """sort the pools by field Default value: h24_volume_usd_liquidity_desc"""
