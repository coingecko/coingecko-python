# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ExchangeGetParams"]


class ExchangeGetParams(TypedDict, total=False):
    page: float
    """page through results, default: 1"""

    per_page: float
    """total results per page, default: 100 Valid values: 1...250"""
