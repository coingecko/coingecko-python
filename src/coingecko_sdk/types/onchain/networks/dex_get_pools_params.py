# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["DexGetPoolsParams"]


class DexGetPoolsParams(TypedDict, total=False):
    network: Required[str]

    include: str
    """
    attributes to include, comma-separated if more than one to include Available
    values: `base_token`, `quote_token`, `dex`
    """

    page: int
    """page through results Default value: 1"""

    sort: Literal["h24_tx_count_desc", "h24_volume_usd_desc"]
    """sort the pools by field Default value: h24_tx_count_desc"""
