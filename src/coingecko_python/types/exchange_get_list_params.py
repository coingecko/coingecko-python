# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ExchangeGetListParams"]


class ExchangeGetListParams(TypedDict, total=False):
    status: Literal["active", "inactive"]
    """filter by status of exchanges, default: active"""
