# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["TrendingGetParams"]


class TrendingGetParams(TypedDict, total=False):
    show_max: str
    """
    show max number of results available for the given type Available values:
    `coins`, `nfts`, `categories` Example: `coins` or `coins,nfts,categories`
    """
