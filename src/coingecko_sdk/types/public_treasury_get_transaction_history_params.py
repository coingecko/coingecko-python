# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["PublicTreasuryGetTransactionHistoryParams"]


class PublicTreasuryGetTransactionHistoryParams(TypedDict, total=False):
    coin_ids: str
    """Filter transactions by coin IDs, comma-separated if querying more than 1 coin.

    \\**refers to [`/coins/list`](/reference/coins-list).
    """

    order: Literal[
        "date_desc",
        "date_asc",
        "holding_net_change_desc",
        "holding_net_change_asc",
        "transaction_value_usd_desc",
        "transaction_value_usd_asc",
        "average_cost_desc",
        "average_cost_asc",
    ]
    """Sort order of transactions. Default: `date_desc`"""

    page: int
    """Page through results. Default value: 1"""

    per_page: int
    """Total results per page. Default value: 100 Valid values: 1...250"""
