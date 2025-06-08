# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TokenPriceGetAddressesParams"]


class TokenPriceGetAddressesParams(TypedDict, total=False):
    network: Required[str]

    include_24hr_price_change: bool
    """include 24hr price change, default: false"""

    include_24hr_vol: bool
    """include 24hr volume, default: false"""

    include_market_cap: bool
    """include market capitalization, default: false"""

    include_total_reserve_in_usd: bool
    """include total reserve in USD, default: false"""

    mcap_fdv_fallback: bool
    """return FDV if market cap is not available, default: false"""
