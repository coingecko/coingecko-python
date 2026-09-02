# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["RwaGetMarketsParams"]


class RwaGetMarketsParams(TypedDict, total=False):
    asset_type: Literal["stock", "commodity", "etf"]
    """Filter by RWA asset type."""

    ids: str
    """RWAs' IDs, comma-separated if querying more than 1 RWA.

    \\**refers to [`/rwas/list`](/reference/rwas-list)
    """

    issuer: str
    """Filter based on RWAs' issuer.

    \\**refers to [`/rwas/issuers/list`](/reference/rwas-issuers-list)
    """

    names: str
    """RWAs' names, comma-separated if querying more than 1 RWA."""

    order: Literal["market_cap_asc", "market_cap_desc", "volume_asc", "volume_desc", "id_asc", "id_desc"]
    """Sort result by field. Default: market_cap_desc"""

    page: int
    """Page through results. Default: 1"""

    per_page: int
    """Total results per page. Default: 100 Valid values: 1...250"""

    precision: Literal[
        "full", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18"
    ]
    """Decimal places for currency price value"""

    price_change_percentage: str
    """
    Include price change percentage timeframe, comma-separated if querying more than
    1 timeframe. Valid values: `1h`, `24h`, `7d`, `14d`, `30d`, `200d`, `1y`
    """

    sparkline: bool
    """Include sparkline 7-day data. Default: false"""

    symbols: str
    """RWAs' symbols, comma-separated if querying more than 1 RWA."""
