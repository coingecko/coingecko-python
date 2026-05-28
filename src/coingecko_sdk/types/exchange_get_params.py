# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ExchangeGetParams"]


class ExchangeGetParams(TypedDict, total=False):
    page: float
    """Page through results. Default: 1"""

    per_page: float
    """Total results per page. Default: 100. Valid values: 1...250"""
