# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["InfoRecentlyUpdatedGetParams"]


class InfoRecentlyUpdatedGetParams(TypedDict, total=False):
    include: Literal["network"]
    """Attributes for related resources to include."""

    network: str
    """Filter tokens by provided network.

    \\**refers to [`/onchain/networks`](/reference/networks-list).
    """
