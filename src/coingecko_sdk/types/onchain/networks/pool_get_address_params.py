# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PoolGetAddressParams"]


class PoolGetAddressParams(TypedDict, total=False):
    network: Required[str]

    include: str
    """
    attributes to include, comma-separated if more than one to include Available
    values: `base_token`, `quote_token`, `dex`
    """

    include_volume_breakdown: bool
    """include volume breakdown, default: false"""
