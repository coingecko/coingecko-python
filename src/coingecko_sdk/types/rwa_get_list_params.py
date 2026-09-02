# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["RwaGetListParams"]


class RwaGetListParams(TypedDict, total=False):
    asset_type: Literal["stock", "commodity", "etf"]
    """Filter by RWA asset type."""
