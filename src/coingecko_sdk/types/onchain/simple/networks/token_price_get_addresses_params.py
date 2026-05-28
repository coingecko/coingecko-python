# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TokenPriceGetAddressesParams"]


class TokenPriceGetAddressesParams(TypedDict, total=False):
    network: Required[str]

    include_24hr_price_change: bool
    """Include 24hr price change. Default: `false`"""

    include_24hr_vol: bool
    """Include 24hr volume. Default: `false`"""

    include_inactive_source: bool
    """Include token price data from inactive pools using the most recent swap.

    Default: `false`
    """

    include_market_cap: bool
    """Include market capitalization. Default: `false`"""

    include_total_reserve_in_usd: bool
    """Include total reserve in USD. Default: `false`"""

    mcap_fdv_fallback: bool
    """Return FDV if market cap is not available. Default: `false`"""
