# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["EntityGetListParams"]


class EntityGetListParams(TypedDict, total=False):
    entity_type: Literal["company", "government"]
    """Filter by entity type."""

    page: int
    """Page through results. Default value: 1"""

    per_page: int
    """Total results per page. Default value: 100 Valid values: 1...250"""
