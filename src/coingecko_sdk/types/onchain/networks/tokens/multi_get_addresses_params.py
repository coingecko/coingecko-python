# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["MultiGetAddressesParams"]


class MultiGetAddressesParams(TypedDict, total=False):
    network: Required[str]

    include: Literal["top_pools"]
    """Attributes to include."""

    include_composition: bool
    """Include pool composition. Default: `false`"""

    include_inactive_source: bool
    """Include tokens from inactive pools using the most recent swap. Default: `false`"""
