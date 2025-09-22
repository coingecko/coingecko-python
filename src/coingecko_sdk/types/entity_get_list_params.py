# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["EntityGetListParams"]


class EntityGetListParams(TypedDict, total=False):
    entity_type: Literal["company", "government"]
    """filter by entity type, default: false"""

    page: int
    """page through results, default: 1"""

    per_page: int
    """total results per page, default: 100 Valid values: 1...250"""
