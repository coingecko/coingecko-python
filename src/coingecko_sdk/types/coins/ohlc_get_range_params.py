# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["OhlcGetRangeParams"]


class OhlcGetRangeParams(TypedDict, total=False):
    from_: Required[Annotated[str, PropertyInfo(alias="from")]]
    """
    starting date in ISO date string (`YYYY-MM-DD` or `YYYY-MM-DDTHH:MM`) or UNIX
    timestamp. **use ISO date string for best compatibility**
    """

    interval: Required[Literal["daily", "hourly"]]
    """data interval"""

    to: Required[str]
    """
    ending date in ISO date string (`YYYY-MM-DD` or `YYYY-MM-DDTHH:MM`) or UNIX
    timestamp. **use ISO date string for best compatibility**
    """

    vs_currency: Required[str]
    """
    target currency of price data \\**refers to
    [`/simple/supported_vs_currencies`](/reference/simple-supported-currencies).
    """
