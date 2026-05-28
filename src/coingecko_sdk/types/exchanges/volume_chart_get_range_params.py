# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["VolumeChartGetRangeParams"]


class VolumeChartGetRangeParams(TypedDict, total=False):
    from_: Required[Annotated[float, PropertyInfo(alias="from")]]
    """Starting date in UNIX timestamp."""

    to: Required[float]
    """Ending date in UNIX timestamp."""
