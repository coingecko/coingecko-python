# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["HistoryGetParams"]


class HistoryGetParams(TypedDict, total=False):
    date: Required[str]
    """The date of data snapshot. Format: `YYYY-MM-DD`"""

    localization: bool
    """Include all the localized languages in response. Default: true"""
