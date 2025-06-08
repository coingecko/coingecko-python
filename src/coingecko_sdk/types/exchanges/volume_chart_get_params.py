# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["VolumeChartGetParams"]


class VolumeChartGetParams(TypedDict, total=False):
    days: Required[Literal["1", "7", "14", "30", "90", "180", "365"]]
    """data up to number of days ago"""
