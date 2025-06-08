# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PoolGetParams"]


class PoolGetParams(TypedDict, total=False):
    include: str
    """
    attributes to include, comma-separated if more than one to include Available
    values: `base_token`, `quote_token`, `dex`
    """

    network: str
    """network ID \\**refers to [/networks](/reference/networks-list)"""

    page: int
    """page through results Default value: 1"""

    query: str
    """search query"""
