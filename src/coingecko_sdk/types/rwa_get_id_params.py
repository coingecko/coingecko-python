# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["RwaGetIDParams"]


class RwaGetIDParams(TypedDict, total=False):
    sparkline: bool
    """Include sparkline 7-day data. Default: false"""

    tokenized_market_data: bool
    """Include tokenized market data. Default: false"""

    tokens: bool
    """Include tokens data. Default: false"""
