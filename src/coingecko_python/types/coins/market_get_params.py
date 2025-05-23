# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["MarketGetParams"]


class MarketGetParams(TypedDict, total=False):
    vs_currency: Required[str]
    """
    target currency of coins and market data \\**refers to
    [`/simple/supported_vs_currencies`](/reference/simple-supported-currencies).
    """

    category: str
    """
    filter based on coins' category \\**refers to
    [`/coins/categories/list`](/reference/coins-categories-list).
    """

    ids: str
    """coins' IDs, comma-separated if querying more than 1 coin.

    \\**refers to [`/coins/list`](/reference/coins-list).
    """

    include_tokens: Literal["top", "all"]
    """
    for `symbols` lookups, specify `all` to include all matching tokens Default
    `top` returns top-ranked tokens (by market cap or volume)
    """

    locale: Literal[
        "ar",
        "bg",
        "cs",
        "da",
        "de",
        "el",
        "en",
        "es",
        "fi",
        "fr",
        "he",
        "hi",
        "hr",
        "hu",
        "id",
        "it",
        "ja",
        "ko",
        "lt",
        "nl",
        "no",
        "pl",
        "pt",
        "ro",
        "ru",
        "sk",
        "sl",
        "sv",
        "th",
        "tr",
        "uk",
        "vi",
        "zh",
        "zh-tw",
    ]
    """language background, default: en"""

    names: str
    """coins' names, comma-separated if querying more than 1 coin."""

    order: Literal["market_cap_asc", "market_cap_desc", "volume_asc", "volume_desc", "id_asc", "id_desc"]
    """sort result by field, default: market_cap_desc"""

    page: float
    """page through results, default: 1"""

    per_page: float
    """total results per page, default: 100 Valid values: 1...250"""

    precision: Literal[
        "full", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18"
    ]
    """decimal place for currency price value"""

    price_change_percentage: str
    """
    include price change percentage timeframe, comma-separated if query more than 1
    price change percentage timeframe Valid values: 1h, 24h, 7d, 14d, 30d, 200d, 1y
    """

    sparkline: bool
    """include sparkline 7 days data, default: false"""

    symbols: str
    """coins' symbols, comma-separated if querying more than 1 coin."""
