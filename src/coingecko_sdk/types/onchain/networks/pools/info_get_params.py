# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["InfoGetParams"]


class InfoGetParams(TypedDict, total=False):
    network: Required[str]

    include: Literal["pool"]
    """attributes to include"""
