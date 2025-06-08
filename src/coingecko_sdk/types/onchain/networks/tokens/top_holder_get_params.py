# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TopHolderGetParams"]


class TopHolderGetParams(TypedDict, total=False):
    network: Required[str]

    holders: str
    """
    number of top token holders to return, you may use any integer or `max` Default
    value: 10
    """
