# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["TradeGetParams"]


class TradeGetParams(TypedDict, total=False):
    network: Required[str]

    token: str
    """
    Filter trades by token contract address, returning only trades involving this
    token.
    """

    cursor: str
    """
    Cursor from the previous response, passed back unchanged to fetch the next page.
    """

    from_: Annotated[str, PropertyInfo(alias="from")]
    """
    Starting date in ISO date string (`YYYY-MM-DD` or `YYYY-MM-DDTHH:MM`) or UNIX
    timestamp. **Use ISO date string for best compatibility.** Must be provided
    together with `to`.
    """

    per_page: int
    """Total results per page. Default value: 100 Valid values: 1...300"""

    to: str
    """
    Ending date in ISO date string (`YYYY-MM-DD` or `YYYY-MM-DDTHH:MM`) or UNIX
    timestamp. **Use ISO date string for best compatibility.** Must be provided
    together with `from`.
    """
