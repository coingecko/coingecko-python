# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["InsightGetParams"]


class InsightGetParams(TypedDict, total=False):
    coin_id: str
    """Filter insights by coin ID. \\**refers to [`/coins/list`](/reference/coins-list)."""

    from_: Annotated[str, PropertyInfo(alias="from")]
    """Starting date in ISO date string (`YYYY-MM-DD`)."""

    page: int
    """Page through results. Default value: 1 Valid values: 1...20"""

    per_page: int
    """Total results per page. Default value: 10 Valid values: 1...20"""

    to: str
    """Ending date in ISO date string (`YYYY-MM-DD`)."""
