# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["AssetPlatformGetParams"]


class AssetPlatformGetParams(TypedDict, total=False):
    filter: Literal["nft"]
    """apply relevant filters to results"""
