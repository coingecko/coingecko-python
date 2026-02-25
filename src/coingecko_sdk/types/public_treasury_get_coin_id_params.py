# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PublicTreasuryGetCoinIDParams"]


class PublicTreasuryGetCoinIDParams(TypedDict, total=False):
    entity: Required[Literal["companies", "governments"]]

    order: Literal["total_holdings_usd_desc", "total_holdings_usd_asc"]
    """Sort order for results"""

    page: int
    """Page number to return"""

    per_page: int
    """Number of results to return per page"""
