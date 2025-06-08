# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...types.nfts import market_chart_get_params
from ..._base_client import make_request_options
from ...types.nfts.market_chart_get_response import MarketChartGetResponse

__all__ = ["MarketChartResource", "AsyncMarketChartResource"]


class MarketChartResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MarketChartResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return MarketChartResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MarketChartResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return MarketChartResourceWithStreamingResponse(self)

    def get(
        self,
        id: str,
        *,
        days: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MarketChartGetResponse:
        """
        This endpoint allows you **query historical market data of a NFT collection,
        including floor price, market cap, and 24hr volume, by number of days away from
        now**

        Args:
          days: data up to number of days Valid values: any integer or max

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/nfts/{id}/market_chart",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"days": days}, market_chart_get_params.MarketChartGetParams),
            ),
            cast_to=MarketChartGetResponse,
        )


class AsyncMarketChartResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMarketChartResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMarketChartResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMarketChartResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return AsyncMarketChartResourceWithStreamingResponse(self)

    async def get(
        self,
        id: str,
        *,
        days: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MarketChartGetResponse:
        """
        This endpoint allows you **query historical market data of a NFT collection,
        including floor price, market cap, and 24hr volume, by number of days away from
        now**

        Args:
          days: data up to number of days Valid values: any integer or max

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/nfts/{id}/market_chart",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"days": days}, market_chart_get_params.MarketChartGetParams),
            ),
            cast_to=MarketChartGetResponse,
        )


class MarketChartResourceWithRawResponse:
    def __init__(self, market_chart: MarketChartResource) -> None:
        self._market_chart = market_chart

        self.get = to_raw_response_wrapper(
            market_chart.get,
        )


class AsyncMarketChartResourceWithRawResponse:
    def __init__(self, market_chart: AsyncMarketChartResource) -> None:
        self._market_chart = market_chart

        self.get = async_to_raw_response_wrapper(
            market_chart.get,
        )


class MarketChartResourceWithStreamingResponse:
    def __init__(self, market_chart: MarketChartResource) -> None:
        self._market_chart = market_chart

        self.get = to_streamed_response_wrapper(
            market_chart.get,
        )


class AsyncMarketChartResourceWithStreamingResponse:
    def __init__(self, market_chart: AsyncMarketChartResource) -> None:
        self._market_chart = market_chart

        self.get = async_to_streamed_response_wrapper(
            market_chart.get,
        )
