# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["NewPoolGetNetworkParams"]


class NewPoolGetNetworkParams(TypedDict, total=False):
    include: str
    """
    attributes to include, comma-separated if more than one to include Available
    values: `base_token`, `quote_token`, `dex`
    """

    page: int
    """page through results Default value: 1"""
