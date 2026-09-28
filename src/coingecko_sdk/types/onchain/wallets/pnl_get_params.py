# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PnlGetParams"]


class PnlGetParams(TypedDict, total=False):
    networks: Required[str]
    """Query PnL by networks, comma-separated if more than one.

    \\**refers to [`/onchain/networks`](/reference/networks-list).
    """

    page: int
    """Page through results. Default value: 1"""

    per_page: int
    """Total results per page. Default value: 100 Valid values: 1...300"""

    sort: Literal["realized_pnl_usd_desc", "unrealized_pnl_usd_desc", "total_buy_usd_desc", "total_sell_usd_desc"]
    """Sort the token stats by field. Default: `realized_pnl_usd_desc`"""
