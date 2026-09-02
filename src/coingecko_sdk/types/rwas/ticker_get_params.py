# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["TickerGetParams"]


class TickerGetParams(TypedDict, total=False):
    depth: bool
    """Include 2% orderbook depth, i.e.

    `cost_to_move_up_usd` and `cost_to_move_down_usd`. Default: false
    """

    dex_pair_format: Literal["contract_address", "symbol"]
    """Set to `symbol` to display DEX pair base and target as symbols.

    Default: `contract_address`
    """

    exchange_ids: str
    """Exchange ID. \\**refers to [`/exchanges/list`](/reference/exchanges-list)"""

    issuer_ids: str
    """Issuer ID. \\**refers to [`/rwas/issuers/list`](/reference/rwas-issuers-list)"""

    order: Literal["last_traded_at_desc", "last_traded_at_asc", "volume_desc", "volume_asc"]
    """Sort the order of responses. Default: last_traded_at_desc"""

    page: int
    """Page through results"""
