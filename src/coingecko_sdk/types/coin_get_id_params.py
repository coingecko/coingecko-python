# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["CoinGetIDParams"]


class CoinGetIDParams(TypedDict, total=False):
    community_data: bool
    """Include community data. Default: true"""

    developer_data: bool
    """Include developer data. Default: true"""

    dex_pair_format: Literal["contract_address", "symbol"]
    """Set to `symbol` to display DEX pair base and target as symbols.

    Default: `contract_address`
    """

    include_categories_details: bool
    """Include categories details. Default: false"""

    localization: bool
    """Include all localized languages in the response. Default: true"""

    market_data: bool
    """Include market data. Default: true"""

    sparkline: bool
    """Include sparkline 7-day data. Default: false"""

    tickers: bool
    """Include tickers data. Default: true"""
