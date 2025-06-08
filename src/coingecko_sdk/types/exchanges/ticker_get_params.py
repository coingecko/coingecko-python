# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["TickerGetParams"]


class TickerGetParams(TypedDict, total=False):
    coin_ids: str
    """
    filter tickers by coin IDs, comma-separated if querying more than 1 coin
    \\**refers to [`/coins/list`](/reference/coins-list).
    """

    depth: bool
    """
    include 2% orderbook depth (Example: cost_to_move_up_usd &
    cost_to_move_down_usd),default: false
    """

    dex_pair_format: Literal["contract_address", "symbol"]
    """
    set to `symbol` to display DEX pair base and target as symbols, default:
    `contract_address`
    """

    include_exchange_logo: bool
    """include exchange logo, default: false"""

    order: Literal["trust_score_desc", "trust_score_asc", "volume_desc", "volume_asc", "base_target"]
    """use this to sort the order of responses, default: trust_score_desc"""

    page: float
    """page through results"""
