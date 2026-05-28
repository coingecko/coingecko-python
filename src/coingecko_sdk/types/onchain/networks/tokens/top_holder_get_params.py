# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TopHolderGetParams"]


class TopHolderGetParams(TypedDict, total=False):
    network: Required[str]

    holders: str
    """Number of top token holders to return, any integer or `max`. Default value: 10"""

    include_pnl_details: bool
    """Include PnL details for token holders. Default: `false`"""
