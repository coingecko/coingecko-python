# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TokenPriceGetIDParams"]


class TokenPriceGetIDParams(TypedDict, total=False):
    contract_addresses: Required[str]
    """
    the contract addresses of tokens, comma-separated if querying more than 1
    token's contract address
    """

    vs_currencies: Required[str]
    """target currency of coins, comma-separated if querying more than 1 currency.

    \\**refers to
    [`/simple/supported_vs_currencies`](/reference/simple-supported-currencies).
    """

    include_24hr_change: bool
    """include 24hr change default: false"""

    include_24hr_vol: bool
    """include 24hr volume, default: false"""

    include_last_updated_at: bool
    """include last updated price time in UNIX , default: false"""

    include_market_cap: bool
    """include market capitalization, default: false"""

    precision: Literal[
        "full", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18"
    ]
    """decimal place for currency price value"""
