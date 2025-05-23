# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["OhlcGetRangeParams"]


class OhlcGetRangeParams(TypedDict, total=False):
    from_: Required[Annotated[float, PropertyInfo(alias="from")]]
    """starting date in UNIX timestamp"""

    interval: Required[Literal["daily", "hourly"]]
    """data interval"""

    to: Required[float]
    """ending date in UNIX timestamp"""

    vs_currency: Required[str]
    """
    target currency of price data \\**refers to
    [`/simple/supported_vs_currencies`](/reference/simple-supported-currencies).
    """
