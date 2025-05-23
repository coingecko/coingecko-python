# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ExchangeGetIDParams"]


class ExchangeGetIDParams(TypedDict, total=False):
    include_tickers: Literal["all", "unexpired"]
    """include tickers data"""
