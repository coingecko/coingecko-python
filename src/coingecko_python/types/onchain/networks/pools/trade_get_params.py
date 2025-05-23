# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TradeGetParams"]


class TradeGetParams(TypedDict, total=False):
    network: Required[str]

    token: str
    """
    return trades for token use this to invert the chart Available values: 'base',
    'quote' or token address Default value: 'base'
    """

    trade_volume_in_usd_greater_than: float
    """filter trades by trade volume in USD greater than this value Default value: 0"""
