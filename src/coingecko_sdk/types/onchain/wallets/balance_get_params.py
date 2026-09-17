# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["BalanceGetParams"]


class BalanceGetParams(TypedDict, total=False):
    networks: Required[str]
    """Query balances by networks, comma-separated if more than one.

    \\**refers to
    [supported networks](/reference/wallet-token-balances#supported-networks).
    """

    page: int
    """Page through results. Default value: 1"""

    per_page: int
    """Total results per page. Default value: 50 Valid values: 1...100"""

    reserve_in_usd_min: float
    """Minimum total reserve in USD of the holding's token."""

    sort: Literal["value_usd_desc", "value_usd_asc"]
    """Sort the holdings by field. Default: `value_usd_desc`"""

    token_type: Literal["native", "non_native"]
    """Filter holdings by token type. Omit to return both."""

    value_usd_min: float
    """Minimum holding value in USD."""
