# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["CoinGetIDParams"]


class CoinGetIDParams(TypedDict, total=False):
    community_data: bool
    """include community data, default: true"""

    developer_data: bool
    """include developer data, default: true"""

    dex_pair_format: Literal["contract_address", "symbol"]
    """
    set to `symbol` to display DEX pair base and target as symbols, default:
    `contract_address`
    """

    localization: bool
    """include all the localized languages in the response, default: true"""

    market_data: bool
    """include market data, default: true"""

    sparkline: bool
    """include sparkline 7 days data, default: false"""

    tickers: bool
    """include tickers data, default: true"""
