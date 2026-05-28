# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["OhlcvGetTimeframeParams"]


class OhlcvGetTimeframeParams(TypedDict, total=False):
    network: Required[str]

    token_address: Required[str]

    aggregate: str
    """Time period to aggregate each OHLCV.

    Available values (day): `1` Available values (hour): `1`, `4`, `12` Available
    values (minute): `1`, `5`, `15` Available values (second): `1`, `15`, `30`
    Default value: 1
    """

    before_timestamp: int
    """Return OHLCV data before this timestamp (integer seconds since epoch)."""

    currency: Literal["usd", "token"]
    """Return OHLCV in USD or quote token. Default: `usd`"""

    include_empty_intervals: bool
    """Include empty intervals with no trade data. Default: `false`"""

    include_inactive_source: bool
    """Include token data from inactive pools using the most recent swap.

    Default: `false`
    """

    limit: int
    """Number of OHLCV results to return, maximum 1000. Default value: 100"""
