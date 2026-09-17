# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TokenGetMultiParams"]


class TokenGetMultiParams(TypedDict, total=False):
    tokens: Required[str]
    """
    Network ID and token contract address pairs in `network_id:token_address`
    format, comma-separated if more than one. Maximum: 50 \\**refers to
    [`/onchain/networks`](/reference/networks-list).
    """

    include: Literal["top_pools"]
    """Attributes to include."""

    include_composition: bool
    """Include pool composition. Default: `false`"""

    include_inactive_source: bool
    """Include tokens from inactive pools using the most recent swap. Default: `false`"""
