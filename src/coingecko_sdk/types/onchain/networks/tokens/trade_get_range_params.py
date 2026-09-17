# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["TradeGetRangeParams"]


class TradeGetRangeParams(TypedDict, total=False):
    network: Required[str]

    from_: Required[Annotated[str, PropertyInfo(alias="from")]]
    """
    Starting date in ISO date string (`YYYY-MM-DD` or `YYYY-MM-DDTHH:MM`) or UNIX
    timestamp. **Use ISO date string for best compatibility.**
    """

    to: Required[str]
    """
    Ending date in ISO date string (`YYYY-MM-DD` or `YYYY-MM-DDTHH:MM`) or UNIX
    timestamp. **Use ISO date string for best compatibility.**
    """

    cursor: str
    """
    Cursor from the previous response, passed back unchanged to fetch the next page.
    """

    per_page: int
    """Total results per page. Default value: 100 Valid values: 1...300"""

    trade_volume_in_usd_greater_than: float
    """Filter trades by trade volume in USD greater than this value. Default value: 0"""
