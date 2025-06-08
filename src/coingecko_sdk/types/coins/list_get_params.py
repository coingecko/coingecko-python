# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ListGetParams"]


class ListGetParams(TypedDict, total=False):
    include_platform: bool
    """include platform and token's contract addresses, default: false"""

    status: Literal["active", "inactive"]
    """filter by status of coins, default: active"""
