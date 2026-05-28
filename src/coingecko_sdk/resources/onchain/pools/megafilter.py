# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.onchain.pools import megafilter_get_params
from ....types.onchain.pools.megafilter_get_response import MegafilterGetResponse

__all__ = ["MegafilterResource", "AsyncMegafilterResource"]


class MegafilterResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MegafilterResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return MegafilterResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MegafilterResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return MegafilterResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        buy_tax_percentage_max: float | Omit = omit,
        buy_tax_percentage_min: float | Omit = omit,
        buys_duration: Literal["5m", "1h", "6h", "24h"] | Omit = omit,
        buys_max: int | Omit = omit,
        buys_min: int | Omit = omit,
        checks: str | Omit = omit,
        dexes: str | Omit = omit,
        fdv_usd_max: float | Omit = omit,
        fdv_usd_min: float | Omit = omit,
        h24_volume_usd_max: float | Omit = omit,
        h24_volume_usd_min: float | Omit = omit,
        include: str | Omit = omit,
        include_unknown_honeypot_tokens: bool | Omit = omit,
        networks: str | Omit = omit,
        page: int | Omit = omit,
        pool_created_hour_max: float | Omit = omit,
        pool_created_hour_min: float | Omit = omit,
        price_change_percentage_duration: Literal["5m", "1h", "6h", "24h"] | Omit = omit,
        price_change_percentage_max: float | Omit = omit,
        price_change_percentage_min: float | Omit = omit,
        reserve_in_usd_max: float | Omit = omit,
        reserve_in_usd_min: float | Omit = omit,
        sell_tax_percentage_max: float | Omit = omit,
        sell_tax_percentage_min: float | Omit = omit,
        sells_duration: Literal["5m", "1h", "6h", "24h"] | Omit = omit,
        sells_max: int | Omit = omit,
        sells_min: int | Omit = omit,
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
        | Omit = omit,
        tx_count_duration: Literal["5m", "1h", "6h", "24h"] | Omit = omit,
        tx_count_max: int | Omit = omit,
        tx_count_min: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MegafilterGetResponse:
        """
        To query pools based on various filters across all networks on GeckoTerminal

        Args:
          buy_tax_percentage_max: Maximum buy tax percentage.

          buy_tax_percentage_min: Minimum buy tax percentage.

          buys_duration: Duration for buy transactions metric. Default: `24h`

          buys_max: Maximum number of buy transactions.

          buys_min: Minimum number of buy transactions.

          checks: Filter options for various checks, comma-separated if more than one. Available
              values: `no_honeypot`, `good_gt_score`, `on_coingecko`, `has_social`

          dexes: Filter pools by DEXes, comma-separated if more than one. \\**refers to
              [`/onchain/networks/{network}/dexes`](/reference/dexes-list).

          fdv_usd_max: Maximum fully diluted value in USD.

          fdv_usd_min: Minimum fully diluted value in USD.

          h24_volume_usd_max: Maximum 24hr volume in USD.

          h24_volume_usd_min: Minimum 24hr volume in USD.

          include:
              Attributes to include, comma-separated if more than one. Available values:
              `base_token`, `quote_token`, `dex`, `network`

          include_unknown_honeypot_tokens: When `checks` includes `no_honeypot`, set to `true` to also include unknown
              honeypot tokens. Default: `false`

          networks: Filter pools by networks, comma-separated if more than one. \\**refers to
              [`/onchain/networks`](/reference/networks-list).

          page: Page through results. Default value: 1

          pool_created_hour_max: Maximum pool age in hours.

          pool_created_hour_min: Minimum pool age in hours.

          price_change_percentage_duration: Duration for price change percentage metric. Default: `24h`

          price_change_percentage_max: Maximum price change percentage.

          price_change_percentage_min: Minimum price change percentage.

          reserve_in_usd_max: Maximum reserve in USD.

          reserve_in_usd_min: Minimum reserve in USD.

          sell_tax_percentage_max: Maximum sell tax percentage.

          sell_tax_percentage_min: Minimum sell tax percentage.

          sells_duration: Duration for sell transactions metric. Default: `24h`

          sells_max: Maximum number of sell transactions.

          sells_min: Minimum number of sell transactions.

          sort: Sort the pools by field. Default: `h6_trending`

          tx_count_duration: Duration for transaction count metric. Default: `24h`

          tx_count_max: Maximum transaction count.

          tx_count_min: Minimum transaction count.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/onchain/pools/megafilter",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "buy_tax_percentage_max": buy_tax_percentage_max,
                        "buy_tax_percentage_min": buy_tax_percentage_min,
                        "buys_duration": buys_duration,
                        "buys_max": buys_max,
                        "buys_min": buys_min,
                        "checks": checks,
                        "dexes": dexes,
                        "fdv_usd_max": fdv_usd_max,
                        "fdv_usd_min": fdv_usd_min,
                        "h24_volume_usd_max": h24_volume_usd_max,
                        "h24_volume_usd_min": h24_volume_usd_min,
                        "include": include,
                        "include_unknown_honeypot_tokens": include_unknown_honeypot_tokens,
                        "networks": networks,
                        "page": page,
                        "pool_created_hour_max": pool_created_hour_max,
                        "pool_created_hour_min": pool_created_hour_min,
                        "price_change_percentage_duration": price_change_percentage_duration,
                        "price_change_percentage_max": price_change_percentage_max,
                        "price_change_percentage_min": price_change_percentage_min,
                        "reserve_in_usd_max": reserve_in_usd_max,
                        "reserve_in_usd_min": reserve_in_usd_min,
                        "sell_tax_percentage_max": sell_tax_percentage_max,
                        "sell_tax_percentage_min": sell_tax_percentage_min,
                        "sells_duration": sells_duration,
                        "sells_max": sells_max,
                        "sells_min": sells_min,
                        "sort": sort,
                        "tx_count_duration": tx_count_duration,
                        "tx_count_max": tx_count_max,
                        "tx_count_min": tx_count_min,
                    },
                    megafilter_get_params.MegafilterGetParams,
                ),
            ),
            cast_to=MegafilterGetResponse,
        )


class AsyncMegafilterResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMegafilterResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMegafilterResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMegafilterResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return AsyncMegafilterResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        buy_tax_percentage_max: float | Omit = omit,
        buy_tax_percentage_min: float | Omit = omit,
        buys_duration: Literal["5m", "1h", "6h", "24h"] | Omit = omit,
        buys_max: int | Omit = omit,
        buys_min: int | Omit = omit,
        checks: str | Omit = omit,
        dexes: str | Omit = omit,
        fdv_usd_max: float | Omit = omit,
        fdv_usd_min: float | Omit = omit,
        h24_volume_usd_max: float | Omit = omit,
        h24_volume_usd_min: float | Omit = omit,
        include: str | Omit = omit,
        include_unknown_honeypot_tokens: bool | Omit = omit,
        networks: str | Omit = omit,
        page: int | Omit = omit,
        pool_created_hour_max: float | Omit = omit,
        pool_created_hour_min: float | Omit = omit,
        price_change_percentage_duration: Literal["5m", "1h", "6h", "24h"] | Omit = omit,
        price_change_percentage_max: float | Omit = omit,
        price_change_percentage_min: float | Omit = omit,
        reserve_in_usd_max: float | Omit = omit,
        reserve_in_usd_min: float | Omit = omit,
        sell_tax_percentage_max: float | Omit = omit,
        sell_tax_percentage_min: float | Omit = omit,
        sells_duration: Literal["5m", "1h", "6h", "24h"] | Omit = omit,
        sells_max: int | Omit = omit,
        sells_min: int | Omit = omit,
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
        | Omit = omit,
        tx_count_duration: Literal["5m", "1h", "6h", "24h"] | Omit = omit,
        tx_count_max: int | Omit = omit,
        tx_count_min: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MegafilterGetResponse:
        """
        To query pools based on various filters across all networks on GeckoTerminal

        Args:
          buy_tax_percentage_max: Maximum buy tax percentage.

          buy_tax_percentage_min: Minimum buy tax percentage.

          buys_duration: Duration for buy transactions metric. Default: `24h`

          buys_max: Maximum number of buy transactions.

          buys_min: Minimum number of buy transactions.

          checks: Filter options for various checks, comma-separated if more than one. Available
              values: `no_honeypot`, `good_gt_score`, `on_coingecko`, `has_social`

          dexes: Filter pools by DEXes, comma-separated if more than one. \\**refers to
              [`/onchain/networks/{network}/dexes`](/reference/dexes-list).

          fdv_usd_max: Maximum fully diluted value in USD.

          fdv_usd_min: Minimum fully diluted value in USD.

          h24_volume_usd_max: Maximum 24hr volume in USD.

          h24_volume_usd_min: Minimum 24hr volume in USD.

          include:
              Attributes to include, comma-separated if more than one. Available values:
              `base_token`, `quote_token`, `dex`, `network`

          include_unknown_honeypot_tokens: When `checks` includes `no_honeypot`, set to `true` to also include unknown
              honeypot tokens. Default: `false`

          networks: Filter pools by networks, comma-separated if more than one. \\**refers to
              [`/onchain/networks`](/reference/networks-list).

          page: Page through results. Default value: 1

          pool_created_hour_max: Maximum pool age in hours.

          pool_created_hour_min: Minimum pool age in hours.

          price_change_percentage_duration: Duration for price change percentage metric. Default: `24h`

          price_change_percentage_max: Maximum price change percentage.

          price_change_percentage_min: Minimum price change percentage.

          reserve_in_usd_max: Maximum reserve in USD.

          reserve_in_usd_min: Minimum reserve in USD.

          sell_tax_percentage_max: Maximum sell tax percentage.

          sell_tax_percentage_min: Minimum sell tax percentage.

          sells_duration: Duration for sell transactions metric. Default: `24h`

          sells_max: Maximum number of sell transactions.

          sells_min: Minimum number of sell transactions.

          sort: Sort the pools by field. Default: `h6_trending`

          tx_count_duration: Duration for transaction count metric. Default: `24h`

          tx_count_max: Maximum transaction count.

          tx_count_min: Minimum transaction count.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/onchain/pools/megafilter",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "buy_tax_percentage_max": buy_tax_percentage_max,
                        "buy_tax_percentage_min": buy_tax_percentage_min,
                        "buys_duration": buys_duration,
                        "buys_max": buys_max,
                        "buys_min": buys_min,
                        "checks": checks,
                        "dexes": dexes,
                        "fdv_usd_max": fdv_usd_max,
                        "fdv_usd_min": fdv_usd_min,
                        "h24_volume_usd_max": h24_volume_usd_max,
                        "h24_volume_usd_min": h24_volume_usd_min,
                        "include": include,
                        "include_unknown_honeypot_tokens": include_unknown_honeypot_tokens,
                        "networks": networks,
                        "page": page,
                        "pool_created_hour_max": pool_created_hour_max,
                        "pool_created_hour_min": pool_created_hour_min,
                        "price_change_percentage_duration": price_change_percentage_duration,
                        "price_change_percentage_max": price_change_percentage_max,
                        "price_change_percentage_min": price_change_percentage_min,
                        "reserve_in_usd_max": reserve_in_usd_max,
                        "reserve_in_usd_min": reserve_in_usd_min,
                        "sell_tax_percentage_max": sell_tax_percentage_max,
                        "sell_tax_percentage_min": sell_tax_percentage_min,
                        "sells_duration": sells_duration,
                        "sells_max": sells_max,
                        "sells_min": sells_min,
                        "sort": sort,
                        "tx_count_duration": tx_count_duration,
                        "tx_count_max": tx_count_max,
                        "tx_count_min": tx_count_min,
                    },
                    megafilter_get_params.MegafilterGetParams,
                ),
            ),
            cast_to=MegafilterGetResponse,
        )


class MegafilterResourceWithRawResponse:
    def __init__(self, megafilter: MegafilterResource) -> None:
        self._megafilter = megafilter

        self.get = to_raw_response_wrapper(
            megafilter.get,
        )


class AsyncMegafilterResourceWithRawResponse:
    def __init__(self, megafilter: AsyncMegafilterResource) -> None:
        self._megafilter = megafilter

        self.get = async_to_raw_response_wrapper(
            megafilter.get,
        )


class MegafilterResourceWithStreamingResponse:
    def __init__(self, megafilter: MegafilterResource) -> None:
        self._megafilter = megafilter

        self.get = to_streamed_response_wrapper(
            megafilter.get,
        )


class AsyncMegafilterResourceWithStreamingResponse:
    def __init__(self, megafilter: AsyncMegafilterResource) -> None:
        self._megafilter = megafilter

        self.get = async_to_streamed_response_wrapper(
            megafilter.get,
        )
