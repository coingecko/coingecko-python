# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["MegafilterGetParams"]


class MegafilterGetParams(TypedDict, total=False):
    buy_tax_percentage_max: float
    """maximum buy tax percentage"""

    buy_tax_percentage_min: float
    """minimum buy tax percentage"""

    buys_duration: Literal["5m", "1h", "6h", "24h"]
    """duration for buy transactions metric Default value: 24h"""

    buys_max: int
    """maximum number of buy transactions"""

    buys_min: int
    """minimum number of buy transactions"""

    checks: str
    """
    filter options for various checks, comma-separated if more than one Available
    values: `no_honeypot`, `good_gt_score`, `on_coingecko`, `has_social`
    """

    dexes: str
    """
    filter pools by DEXes, comma-separated if more than one DEX ID refers to
    [/networks/{network}/dexes](/reference/dexes-list)
    """

    fdv_usd_max: float
    """maximum fully diluted value in USD"""

    fdv_usd_min: float
    """minimum fully diluted value in USD"""

    h24_volume_usd_max: float
    """maximum 24hr volume in USD"""

    h24_volume_usd_min: float
    """minimum 24hr volume in USD"""

    include: str
    """
    attributes to include, comma-separated if more than one to include Available
    values: `base_token`, `quote_token`, `dex`, `network`
    """

    networks: str
    """
    filter pools by networks, comma-separated if more than one Network ID refers to
    [/networks](/reference/networks-list)
    """

    page: int
    """page through results Default value: 1"""

    pool_created_hour_max: float
    """maximum pool age in hours"""

    pool_created_hour_min: float
    """minimum pool age in hours"""

    reserve_in_usd_max: float
    """maximum reserve in USD"""

    reserve_in_usd_min: float
    """minimum reserve in USD"""

    sell_tax_percentage_max: float
    """maximum sell tax percentage"""

    sell_tax_percentage_min: float
    """minimum sell tax percentage"""

    sells_duration: Literal["5m", "1h", "6h", "24h"]
    """duration for sell transactions metric Default value: 24h"""

    sells_max: int
    """maximum number of sell transactions"""

    sells_min: int
    """minimum number of sell transactions"""

    sort: Literal[
        "m5_trending",
        "h1_trending",
        "h6_trending",
        "h24_trending",
        "h24_tx_count_desc",
        "h24_volume_usd_desc",
        "h24_price_change_percentage_desc",
        "pool_created_at_desc",
    ]
    """sort the pools by field Default value: h6_trending"""

    tx_count_duration: Literal["5m", "1h", "6h", "24h"]
    """duration for transaction count metric Default value: 24h"""

    tx_count_max: int
    """maximum transaction count"""

    tx_count_min: int
    """minimum transaction count"""
