# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ExchangeGetParams"]


class ExchangeGetParams(TypedDict, total=False):
    order: Literal[
        "name_asc",
        "name_desc",
        "open_interest_btc_asc",
        "open_interest_btc_desc",
        "trade_volume_24h_btc_asc",
        "trade_volume_24h_btc_desc",
    ]
    """Sort order of responses. Default: `open_interest_btc_desc`"""

    page: int
    """Page through results. Default value: 1"""

    per_page: int
    """Total results per page."""
