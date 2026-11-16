# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["UnderlyingGetParams"]


class UnderlyingGetParams(TypedDict, total=False):
    coin_ids: str
    """Coins' IDs, comma-separated if querying more than 1 coin.

    \\**refers to [`/coins/list`](/reference/coins-list)
    """

    order: Literal["open_interest_desc", "open_interest_asc", "volume_desc", "volume_asc"]
    """Sort result by field. Default: open_interest_desc"""

    page: int
    """Page through results. Default: 1"""

    per_page: int
    """Total results per page. Default: 100 Valid values: 1...250"""

    rwa_ids: str
    """RWAs' IDs, comma-separated if querying more than 1 RWA.

    \\**refers to [`/rwas/list`](/reference/rwas-list)
    """

    underlying_type: Literal["coin", "rwa"]
    """Filter by underlying type."""
