# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PublicTreasuryGetCoinIDParams"]


class PublicTreasuryGetCoinIDParams(TypedDict, total=False):
    entity: Required[Literal["companies", "governments"]]

    order: Literal["total_holdings_usd_desc", "total_holdings_usd_asc"]
    """Sort order for results. Default: `total_holdings_usd_desc`"""

    page: int
    """Page through results. Default value: 1"""

    per_page: int
    """Total results per page. Default value: 250 Valid values: 1...250"""
