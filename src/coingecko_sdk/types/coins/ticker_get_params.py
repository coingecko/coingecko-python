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

    include_exchange_logo: bool
    """Include exchange logo. Default: false"""

    order: Literal["trust_score_desc", "trust_score_asc", "volume_desc", "volume_asc"]
    """Sort the order of responses. Default: trust_score_desc"""

    page: int
    """Page through results"""
