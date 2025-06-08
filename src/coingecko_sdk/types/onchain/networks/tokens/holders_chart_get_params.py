# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["HoldersChartGetParams"]


class HoldersChartGetParams(TypedDict, total=False):
    network: Required[str]

    days: Literal["7", "30", "max"]
    """number of days to return the historical token holders chart Default value: 7"""
