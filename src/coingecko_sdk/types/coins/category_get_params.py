# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["CategoryGetParams"]


class CategoryGetParams(TypedDict, total=False):
    order: Literal[
        "market_cap_desc",
        "market_cap_asc",
        "name_desc",
        "name_asc",
        "market_cap_change_24h_desc",
        "market_cap_change_24h_asc",
    ]
    """sort results by field, default: market_cap_desc"""
