# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PriceGetParams"]


class PriceGetParams(TypedDict, total=False):
    vs_currencies: Required[str]
    """Target currency of coins, comma-separated if querying more than 1 currency.

    \\**refers to
    [`/simple/supported_vs_currencies`](/reference/simple-supported-currencies)
    """

    ids: str
    """Coins' IDs, comma-separated if querying more than 1 coin.

    \\**refers to [`/coins/list`](/reference/coins-list)
    """

    include_24hr_change: bool
    """Include 24-hour change percentage. Default: false"""

    include_24hr_vol: bool
    """Include 24-hour trading volume. Default: false"""

    include_last_updated_at: bool
    """Include last updated price time as a UNIX timestamp. Default: false"""

    include_market_cap: bool
    """Include market capitalization. Default: false"""

    include_tokens: Literal["top", "all"]
    """For `symbols` lookups, specify `all` to include all matching tokens.

    Default `top` returns top-ranked tokens by market cap or volume.
    """

    names: str
    """Coins' names, comma-separated if querying more than 1 coin."""

    precision: Literal[
        "full", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18"
    ]
    """Decimal places for currency price value"""

    symbols: str
    """Coins' symbols, comma-separated if querying more than 1 coin."""
