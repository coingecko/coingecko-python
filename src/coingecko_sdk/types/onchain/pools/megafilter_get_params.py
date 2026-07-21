# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["MegafilterGetParams"]


class MegafilterGetParams(TypedDict, total=False):
    buy_tax_percentage_max: float
    """Maximum buy tax percentage."""

    buy_tax_percentage_min: float
    """Minimum buy tax percentage."""

    buys_duration: Literal["5m", "1h", "6h", "24h"]
    """Duration for buy transactions metric. Default: `24h`"""

    buys_max: int
    """Maximum number of buy transactions."""

    buys_min: int
    """Minimum number of buy transactions."""

    checks: str
    """Filter options for various checks, comma-separated if more than one.

    Available values: `no_honeypot`, `good_gt_score`, `on_coingecko`, `has_social`
    """

    dexes: str
    """Filter pools by DEXes, comma-separated if more than one.

    \\**refers to [`/onchain/networks/{network}/dexes`](/reference/dexes-list).
    """

    fdv_usd_max: float
    """Maximum fully diluted value in USD."""

    fdv_usd_min: float
    """Minimum fully diluted value in USD."""

    h24_volume_usd_max: float
    """Maximum 24hr volume in USD."""

    h24_volume_usd_min: float
    """Minimum 24hr volume in USD."""

    holder_count_max: int
    """Maximum holder count."""

    holder_count_min: int
    """Minimum holder count."""

    include: str
    """Attributes to include, comma-separated if more than one.

    Available values: `base_token`, `quote_token`, `dex`, `network`
    """

    include_unknown_honeypot_tokens: bool
    """
    When `checks` includes `no_honeypot`, set to `true` to also include unknown
    honeypot tokens. Default: `false`
    """

    networks: str
    """Filter pools by networks, comma-separated if more than one.

    \\**refers to [`/onchain/networks`](/reference/networks-list).
    """

    page: int
    """Page through results. Default value: 1"""

    pool_created_hour_max: float
    """Maximum pool age in hours."""

    pool_created_hour_min: float
    """Minimum pool age in hours."""

    price_change_percentage_duration: Literal["5m", "1h", "6h", "24h"]
    """Duration for price change percentage metric. Default: `24h`"""

    price_change_percentage_max: float
    """Maximum price change percentage."""

    price_change_percentage_min: float
    """Minimum price change percentage."""

    reserve_in_usd_max: float
    """Maximum reserve in USD."""

    reserve_in_usd_min: float
    """Minimum reserve in USD."""

    sell_tax_percentage_max: float
    """Maximum sell tax percentage."""

    sell_tax_percentage_min: float
    """Minimum sell tax percentage."""

    sells_duration: Literal["5m", "1h", "6h", "24h"]
    """Duration for sell transactions metric. Default: `24h`"""

    sells_max: int
    """Maximum number of sell transactions."""

    sells_min: int
    """Minimum number of sell transactions."""

    sort: Literal[
        "m5_trending",
        "h1_trending",
        "h6_trending",
        "h24_trending",
        "h24_tx_count_desc",
        "h24_tx_count_asc",
        "h24_volume_usd_desc",
        "h24_volume_usd_asc",
        "m5_price_change_percentage_asc",
        "h1_price_change_percentage_asc",
        "h6_price_change_percentage_asc",
        "h24_price_change_percentage_asc",
        "m5_price_change_percentage_desc",
        "h1_price_change_percentage_desc",
        "h6_price_change_percentage_desc",
        "h24_price_change_percentage_desc",
        "fdv_usd_asc",
        "fdv_usd_desc",
        "reserve_in_usd_asc",
        "reserve_in_usd_desc",
        "price_asc",
        "price_desc",
        "pool_created_at_desc",
    ]
    """Sort the pools by field. Default: `h6_trending`"""

    top_10_holders_percentage_max: float
    """Maximum top 10 holders percentage."""

    top_10_holders_percentage_min: float
    """Minimum top 10 holders percentage."""

    tx_count_duration: Literal["5m", "1h", "6h", "24h"]
    """Duration for transaction count metric. Default: `24h`"""

    tx_count_max: int
    """Maximum transaction count."""

    tx_count_min: int
    """Minimum transaction count."""
