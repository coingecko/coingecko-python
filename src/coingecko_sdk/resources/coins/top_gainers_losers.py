# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.coins import top_gainers_loser_get_params
from ..._base_client import make_request_options
from ...types.coins.top_gainers_loser_get_response import TopGainersLoserGetResponse

__all__ = ["TopGainersLosersResource", "AsyncTopGainersLosersResource"]


class TopGainersLosersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TopGainersLosersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return TopGainersLosersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TopGainersLosersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return TopGainersLosersResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        vs_currency: str,
        duration: Literal["1h", "24h", "7d", "14d", "30d", "60d", "1y"] | NotGiven = NOT_GIVEN,
        top_coins: Literal["300", "500", "1000", "all"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TopGainersLoserGetResponse:
        """
        This endpoint allows you to **query the top 30 coins with largest price gain and
        loss by a specific time duration**

        Args:
          vs_currency: target currency of coins \\**refers to
              [`/simple/supported_vs_currencies`](/reference/simple-supported-currencies).

          duration: filter result by time range Default value: `24h`

          top_coins: filter result by market cap ranking (top 300 to 1000) or all coins (including
              coins that do not have market cap) Default value: `1000`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/coins/top_gainers_losers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "vs_currency": vs_currency,
                        "duration": duration,
                        "top_coins": top_coins,
                    },
                    top_gainers_loser_get_params.TopGainersLoserGetParams,
                ),
            ),
            cast_to=TopGainersLoserGetResponse,
        )


class AsyncTopGainersLosersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTopGainersLosersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTopGainersLosersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTopGainersLosersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return AsyncTopGainersLosersResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        vs_currency: str,
        duration: Literal["1h", "24h", "7d", "14d", "30d", "60d", "1y"] | NotGiven = NOT_GIVEN,
        top_coins: Literal["300", "500", "1000", "all"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TopGainersLoserGetResponse:
        """
        This endpoint allows you to **query the top 30 coins with largest price gain and
        loss by a specific time duration**

        Args:
          vs_currency: target currency of coins \\**refers to
              [`/simple/supported_vs_currencies`](/reference/simple-supported-currencies).

          duration: filter result by time range Default value: `24h`

          top_coins: filter result by market cap ranking (top 300 to 1000) or all coins (including
              coins that do not have market cap) Default value: `1000`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/coins/top_gainers_losers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "vs_currency": vs_currency,
                        "duration": duration,
                        "top_coins": top_coins,
                    },
                    top_gainers_loser_get_params.TopGainersLoserGetParams,
                ),
            ),
            cast_to=TopGainersLoserGetResponse,
        )


class TopGainersLosersResourceWithRawResponse:
    def __init__(self, top_gainers_losers: TopGainersLosersResource) -> None:
        self._top_gainers_losers = top_gainers_losers

        self.get = to_raw_response_wrapper(
            top_gainers_losers.get,
        )


class AsyncTopGainersLosersResourceWithRawResponse:
    def __init__(self, top_gainers_losers: AsyncTopGainersLosersResource) -> None:
        self._top_gainers_losers = top_gainers_losers

        self.get = async_to_raw_response_wrapper(
            top_gainers_losers.get,
        )


class TopGainersLosersResourceWithStreamingResponse:
    def __init__(self, top_gainers_losers: TopGainersLosersResource) -> None:
        self._top_gainers_losers = top_gainers_losers

        self.get = to_streamed_response_wrapper(
            top_gainers_losers.get,
        )


class AsyncTopGainersLosersResourceWithStreamingResponse:
    def __init__(self, top_gainers_losers: AsyncTopGainersLosersResource) -> None:
        self._top_gainers_losers = top_gainers_losers

        self.get = async_to_streamed_response_wrapper(
            top_gainers_losers.get,
        )
