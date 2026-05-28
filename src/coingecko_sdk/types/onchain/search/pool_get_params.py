# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PoolGetParams"]


class PoolGetParams(TypedDict, total=False):
    include: str
    """Attributes to include, comma-separated if more than one.

    Available values: `base_token`, `quote_token`, `dex`
    """

    network: str
    """Network ID. \\**refers to [`/onchain/networks`](/reference/networks-list)."""

    page: int
    """Page through results. Default value: 1"""

    query: str
    """
    Search query: pool contract address, token name, token symbol, or token contract
    address.
    """
