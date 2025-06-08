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
from ..._base_client import make_request_options
from ...types.global_ import market_cap_chart_get_params
from ...types.global_.market_cap_chart_get_response import MarketCapChartGetResponse

__all__ = ["MarketCapChartResource", "AsyncMarketCapChartResource"]


class MarketCapChartResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MarketCapChartResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return MarketCapChartResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MarketCapChartResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return MarketCapChartResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        days: Literal["1", "7", "14", "30", "90", "180", "365", "max"],
        vs_currency: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MarketCapChartGetResponse:
        """
        This endpoint allows you to **query historical global market cap and volume data
        by number of days away from now**

        Args:
          days: data up to number of days ago Valid values: any integer

          vs_currency: target currency of market cap, default: usd \\**refers to
              [`/simple/supported_vs_currencies`](/reference/simple-supported-currencies)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/global/market_cap_chart",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "days": days,
                        "vs_currency": vs_currency,
                    },
                    market_cap_chart_get_params.MarketCapChartGetParams,
                ),
            ),
            cast_to=MarketCapChartGetResponse,
        )


class AsyncMarketCapChartResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMarketCapChartResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMarketCapChartResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMarketCapChartResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return AsyncMarketCapChartResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        days: Literal["1", "7", "14", "30", "90", "180", "365", "max"],
        vs_currency: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MarketCapChartGetResponse:
        """
        This endpoint allows you to **query historical global market cap and volume data
        by number of days away from now**

        Args:
          days: data up to number of days ago Valid values: any integer

          vs_currency: target currency of market cap, default: usd \\**refers to
              [`/simple/supported_vs_currencies`](/reference/simple-supported-currencies)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/global/market_cap_chart",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "days": days,
                        "vs_currency": vs_currency,
                    },
                    market_cap_chart_get_params.MarketCapChartGetParams,
                ),
            ),
            cast_to=MarketCapChartGetResponse,
        )


class MarketCapChartResourceWithRawResponse:
    def __init__(self, market_cap_chart: MarketCapChartResource) -> None:
        self._market_cap_chart = market_cap_chart

        self.get = to_raw_response_wrapper(
            market_cap_chart.get,
        )


class AsyncMarketCapChartResourceWithRawResponse:
    def __init__(self, market_cap_chart: AsyncMarketCapChartResource) -> None:
        self._market_cap_chart = market_cap_chart

        self.get = async_to_raw_response_wrapper(
            market_cap_chart.get,
        )


class MarketCapChartResourceWithStreamingResponse:
    def __init__(self, market_cap_chart: MarketCapChartResource) -> None:
        self._market_cap_chart = market_cap_chart

        self.get = to_streamed_response_wrapper(
            market_cap_chart.get,
        )


class AsyncMarketCapChartResourceWithStreamingResponse:
    def __init__(self, market_cap_chart: AsyncMarketCapChartResource) -> None:
        self._market_cap_chart = market_cap_chart

        self.get = async_to_streamed_response_wrapper(
            market_cap_chart.get,
        )
