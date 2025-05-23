# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["HistoryGetParams"]


class HistoryGetParams(TypedDict, total=False):
    date: Required[str]
    """the date of data snapshot Format: `dd-mm-yyyy`"""

    localization: bool
    """include all the localized languages in response, default: true"""
