# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TopTraderGetParams"]


class TopTraderGetParams(TypedDict, total=False):
    network_id: Required[str]

    include_address_label: bool
    """include address label data, default: false"""

    sort: Literal["realized_pnl_usd_desc", "unrealized_pnl_usd_desc", "total_buy_usd_desc", "total_sell_usd_desc"]
    """sort the traders by field Default value: realized_pnl_usd_desc"""

    traders: str
    """
    number of top token traders to return, you may use any integer or `max` Default
    value: 10
    """
