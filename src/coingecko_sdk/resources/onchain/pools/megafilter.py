# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
        buy_tax_percentage_max: float | NotGiven = NOT_GIVEN,
        buy_tax_percentage_min: float | NotGiven = NOT_GIVEN,
        buys_duration: Literal["5m", "1h", "6h", "24h"] | NotGiven = NOT_GIVEN,
        buys_max: int | NotGiven = NOT_GIVEN,
        buys_min: int | NotGiven = NOT_GIVEN,
        checks: str | NotGiven = NOT_GIVEN,
        dexes: str | NotGiven = NOT_GIVEN,
        fdv_usd_max: float | NotGiven = NOT_GIVEN,
        fdv_usd_min: float | NotGiven = NOT_GIVEN,
        h24_volume_usd_max: float | NotGiven = NOT_GIVEN,
        h24_volume_usd_min: float | NotGiven = NOT_GIVEN,
        include: str | NotGiven = NOT_GIVEN,
        networks: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        pool_created_hour_max: float | NotGiven = NOT_GIVEN,
        pool_created_hour_min: float | NotGiven = NOT_GIVEN,
        reserve_in_usd_max: float | NotGiven = NOT_GIVEN,
        reserve_in_usd_min: float | NotGiven = NOT_GIVEN,
        sell_tax_percentage_max: float | NotGiven = NOT_GIVEN,
        sell_tax_percentage_min: float | NotGiven = NOT_GIVEN,
        sells_duration: Literal["5m", "1h", "6h", "24h"] | NotGiven = NOT_GIVEN,
        sells_max: int | NotGiven = NOT_GIVEN,
        sells_min: int | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        tx_count_duration: Literal["5m", "1h", "6h", "24h"] | NotGiven = NOT_GIVEN,
        tx_count_max: int | NotGiven = NOT_GIVEN,
        tx_count_min: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MegafilterGetResponse:
        """
        This endpoint allows you to **query pools based on various filters across all
        networks on GeckoTerminal**

        Args:
          buy_tax_percentage_max: maximum buy tax percentage

          buy_tax_percentage_min: minimum buy tax percentage

          buys_duration: duration for buy transactions metric Default value: 24h

          buys_max: maximum number of buy transactions

          buys_min: minimum number of buy transactions

          checks: filter options for various checks, comma-separated if more than one Available
              values: `no_honeypot`, `good_gt_score`, `on_coingecko`, `has_social`

          dexes: filter pools by DEXes, comma-separated if more than one DEX ID refers to
              [/networks/{network}/dexes](/reference/dexes-list)

          fdv_usd_max: maximum fully diluted value in USD

          fdv_usd_min: minimum fully diluted value in USD

          h24_volume_usd_max: maximum 24hr volume in USD

          h24_volume_usd_min: minimum 24hr volume in USD

          include: attributes to include, comma-separated if more than one to include Available
              values: `base_token`, `quote_token`, `dex`, `network`

          networks: filter pools by networks, comma-separated if more than one Network ID refers to
              [/networks](/reference/networks-list)

          page: page through results Default value: 1

          pool_created_hour_max: maximum pool age in hours

          pool_created_hour_min: minimum pool age in hours

          reserve_in_usd_max: maximum reserve in USD

          reserve_in_usd_min: minimum reserve in USD

          sell_tax_percentage_max: maximum sell tax percentage

          sell_tax_percentage_min: minimum sell tax percentage

          sells_duration: duration for sell transactions metric Default value: 24h

          sells_max: maximum number of sell transactions

          sells_min: minimum number of sell transactions

          sort: sort the pools by field Default value: h6_trending

          tx_count_duration: duration for transaction count metric Default value: 24h

          tx_count_max: maximum transaction count

          tx_count_min: minimum transaction count

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
                        "networks": networks,
                        "page": page,
                        "pool_created_hour_max": pool_created_hour_max,
                        "pool_created_hour_min": pool_created_hour_min,
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
        buy_tax_percentage_max: float | NotGiven = NOT_GIVEN,
        buy_tax_percentage_min: float | NotGiven = NOT_GIVEN,
        buys_duration: Literal["5m", "1h", "6h", "24h"] | NotGiven = NOT_GIVEN,
        buys_max: int | NotGiven = NOT_GIVEN,
        buys_min: int | NotGiven = NOT_GIVEN,
        checks: str | NotGiven = NOT_GIVEN,
        dexes: str | NotGiven = NOT_GIVEN,
        fdv_usd_max: float | NotGiven = NOT_GIVEN,
        fdv_usd_min: float | NotGiven = NOT_GIVEN,
        h24_volume_usd_max: float | NotGiven = NOT_GIVEN,
        h24_volume_usd_min: float | NotGiven = NOT_GIVEN,
        include: str | NotGiven = NOT_GIVEN,
        networks: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        pool_created_hour_max: float | NotGiven = NOT_GIVEN,
        pool_created_hour_min: float | NotGiven = NOT_GIVEN,
        reserve_in_usd_max: float | NotGiven = NOT_GIVEN,
        reserve_in_usd_min: float | NotGiven = NOT_GIVEN,
        sell_tax_percentage_max: float | NotGiven = NOT_GIVEN,
        sell_tax_percentage_min: float | NotGiven = NOT_GIVEN,
        sells_duration: Literal["5m", "1h", "6h", "24h"] | NotGiven = NOT_GIVEN,
        sells_max: int | NotGiven = NOT_GIVEN,
        sells_min: int | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        tx_count_duration: Literal["5m", "1h", "6h", "24h"] | NotGiven = NOT_GIVEN,
        tx_count_max: int | NotGiven = NOT_GIVEN,
        tx_count_min: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MegafilterGetResponse:
        """
        This endpoint allows you to **query pools based on various filters across all
        networks on GeckoTerminal**

        Args:
          buy_tax_percentage_max: maximum buy tax percentage

          buy_tax_percentage_min: minimum buy tax percentage

          buys_duration: duration for buy transactions metric Default value: 24h

          buys_max: maximum number of buy transactions

          buys_min: minimum number of buy transactions

          checks: filter options for various checks, comma-separated if more than one Available
              values: `no_honeypot`, `good_gt_score`, `on_coingecko`, `has_social`

          dexes: filter pools by DEXes, comma-separated if more than one DEX ID refers to
              [/networks/{network}/dexes](/reference/dexes-list)

          fdv_usd_max: maximum fully diluted value in USD

          fdv_usd_min: minimum fully diluted value in USD

          h24_volume_usd_max: maximum 24hr volume in USD

          h24_volume_usd_min: minimum 24hr volume in USD

          include: attributes to include, comma-separated if more than one to include Available
              values: `base_token`, `quote_token`, `dex`, `network`

          networks: filter pools by networks, comma-separated if more than one Network ID refers to
              [/networks](/reference/networks-list)

          page: page through results Default value: 1

          pool_created_hour_max: maximum pool age in hours

          pool_created_hour_min: minimum pool age in hours

          reserve_in_usd_max: maximum reserve in USD

          reserve_in_usd_min: minimum reserve in USD

          sell_tax_percentage_max: maximum sell tax percentage

          sell_tax_percentage_min: minimum sell tax percentage

          sells_duration: duration for sell transactions metric Default value: 24h

          sells_max: maximum number of sell transactions

          sells_min: minimum number of sell transactions

          sort: sort the pools by field Default value: h6_trending

          tx_count_duration: duration for transaction count metric Default value: 24h

          tx_count_max: maximum transaction count

          tx_count_min: minimum transaction count

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
                        "networks": networks,
                        "page": page,
                        "pool_created_hour_max": pool_created_hour_max,
                        "pool_created_hour_min": pool_created_hour_min,
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
