# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["MultiGetAddressesParams"]


class MultiGetAddressesParams(TypedDict, total=False):
    network: Required[str]

    include: str
    """Attributes to include, comma-separated if more than one.

    Available values: `base_token`, `quote_token`, `dex`
    """

    include_composition: bool
    """Include pool composition. Default: `false`"""

    include_volume_breakdown: bool
    """Include volume breakdown. Default: `false`"""
