# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TradeGetParams"]


class TradeGetParams(TypedDict, total=False):
    network: Required[str]

    cursor: str
    """
    Cursor from the previous response, passed back unchanged to fetch the next page.
    """

    per_page: int
    """Total results per page. Default value: 300 Valid values: 1...300"""

    trade_volume_in_usd_greater_than: float
    """Filter trades by trade volume in USD greater than this value. Default value: 0"""

    trading_period: Literal["1d", "7d", "30d"]
    """Lookback period for trades. Default: `1d`"""
