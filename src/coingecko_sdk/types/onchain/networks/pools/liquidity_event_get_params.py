# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["LiquidityEventGetParams"]


class LiquidityEventGetParams(TypedDict, total=False):
    network: Required[str]

    cursor: str
    """
    Cursor from the previous response, passed back unchanged to fetch the next page.
    """

    kind: Literal["add", "remove"]
    """Filter by liquidity event kind, omit to return both.

    Available values: `add`, `remove`
    """

    per_page: int
    """Total results per page. Default value: 20 Valid values: 1...50"""

    volume_in_usd_greater_than: float
    """Filter liquidity events by volume in USD greater than this value.

    Must be a positive number.
    """
