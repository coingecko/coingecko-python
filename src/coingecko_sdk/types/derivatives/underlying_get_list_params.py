# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["UnderlyingGetListParams"]


class UnderlyingGetListParams(TypedDict, total=False):
    underlying_type: Literal["coin", "rwa"]
    """Filter by underlying type."""
