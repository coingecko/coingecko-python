# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ExchangeGetIDParams"]


class ExchangeGetIDParams(TypedDict, total=False):
    dex_pair_format: Literal["contract_address", "symbol"]
    """
    set to `symbol` to display DEX pair base and target as symbols, default:
    `contract_address`
    """
