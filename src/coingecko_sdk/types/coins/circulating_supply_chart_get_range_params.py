# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CirculatingSupplyChartGetRangeParams"]


class CirculatingSupplyChartGetRangeParams(TypedDict, total=False):
    from_: Required[Annotated[str, PropertyInfo(alias="from")]]
    """
    starting date in ISO date string (`YYYY-MM-DD` or `YYYY-MM-DDTHH:MM`) or UNIX
    timestamp. **use ISO date string for best compatibility**
    """

    to: Required[str]
    """
    ending date in ISO date string (`YYYY-MM-DD` or `YYYY-MM-DDTHH:MM`) or UNIX
    timestamp. **use ISO date string for best compatibility**
    """
