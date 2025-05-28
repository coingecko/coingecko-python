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
from ....types.coins.contract import market_chart_get_params, market_chart_get_range_params
from ....types.coins.contract.market_chart_get_response import MarketChartGetResponse
from ....types.coins.contract.market_chart_get_range_response import MarketChartGetRangeResponse

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
        contract_address: str,
        *,
        id: str,
        days: str,
        vs_currency: str,
        interval: Literal["5m", "hourly", "daily"] | NotGiven = NOT_GIVEN,
        precision: Literal[
            "full",
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "11",
            "12",
            "13",
            "14",
            "15",
            "16",
            "17",
            "18",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MarketChartGetResponse:
        """
        This endpoint allows you to **get the historical chart data including time in
        UNIX, price, market cap and 24hr volume based on asset platform and particular
        token contract address**

        Args:
          days: data up to number of days ago You may use any integer or `max` for number of
              days

          vs_currency: target currency of market data \\**refers to
              [`/simple/supported_vs_currencies`](/reference/simple-supported-currencies).

          interval: data interval, leave empty for auto granularity

          precision: decimal place for currency price value

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not contract_address:
            raise ValueError(f"Expected a non-empty value for `contract_address` but received {contract_address!r}")
        return self._get(
            f"/coins/{id}/contract/{contract_address}/market_chart",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "days": days,
                        "vs_currency": vs_currency,
                        "interval": interval,
                        "precision": precision,
                    },
                    market_chart_get_params.MarketChartGetParams,
                ),
            ),
            cast_to=MarketChartGetResponse,
        )

    def get_range(
        self,
        contract_address: str,
        *,
        id: str,
        from_: float,
        to: float,
        vs_currency: str,
        interval: Literal["5m", "hourly", "daily"] | NotGiven = NOT_GIVEN,
        precision: Literal[
            "full",
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "11",
            "12",
            "13",
            "14",
            "15",
            "16",
            "17",
            "18",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MarketChartGetRangeResponse:
        """
        This endpoint allows you to **get the historical chart data within certain time
        range in UNIX along with price, market cap and 24hr volume based on asset
        platform and particular token contract address**

        Args:
          from_: starting date in UNIX timestamp

          to: ending date in UNIX timestamp

          vs_currency: target currency of market data \\**refers to
              [`/simple/supported_vs_currencies`](/reference/simple-supported-currencies).

          interval: data interval, leave empty for auto granularity

          precision: decimal place for currency price value

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not contract_address:
            raise ValueError(f"Expected a non-empty value for `contract_address` but received {contract_address!r}")
        return self._get(
            f"/coins/{id}/contract/{contract_address}/market_chart/range",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                        "vs_currency": vs_currency,
                        "interval": interval,
                        "precision": precision,
                    },
                    market_chart_get_range_params.MarketChartGetRangeParams,
                ),
            ),
            cast_to=MarketChartGetRangeResponse,
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
        contract_address: str,
        *,
        id: str,
        days: str,
        vs_currency: str,
        interval: Literal["5m", "hourly", "daily"] | NotGiven = NOT_GIVEN,
        precision: Literal[
            "full",
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "11",
            "12",
            "13",
            "14",
            "15",
            "16",
            "17",
            "18",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MarketChartGetResponse:
        """
        This endpoint allows you to **get the historical chart data including time in
        UNIX, price, market cap and 24hr volume based on asset platform and particular
        token contract address**

        Args:
          days: data up to number of days ago You may use any integer or `max` for number of
              days

          vs_currency: target currency of market data \\**refers to
              [`/simple/supported_vs_currencies`](/reference/simple-supported-currencies).

          interval: data interval, leave empty for auto granularity

          precision: decimal place for currency price value

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not contract_address:
            raise ValueError(f"Expected a non-empty value for `contract_address` but received {contract_address!r}")
        return await self._get(
            f"/coins/{id}/contract/{contract_address}/market_chart",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "days": days,
                        "vs_currency": vs_currency,
                        "interval": interval,
                        "precision": precision,
                    },
                    market_chart_get_params.MarketChartGetParams,
                ),
            ),
            cast_to=MarketChartGetResponse,
        )

    async def get_range(
        self,
        contract_address: str,
        *,
        id: str,
        from_: float,
        to: float,
        vs_currency: str,
        interval: Literal["5m", "hourly", "daily"] | NotGiven = NOT_GIVEN,
        precision: Literal[
            "full",
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "11",
            "12",
            "13",
            "14",
            "15",
            "16",
            "17",
            "18",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MarketChartGetRangeResponse:
        """
        This endpoint allows you to **get the historical chart data within certain time
        range in UNIX along with price, market cap and 24hr volume based on asset
        platform and particular token contract address**

        Args:
          from_: starting date in UNIX timestamp

          to: ending date in UNIX timestamp

          vs_currency: target currency of market data \\**refers to
              [`/simple/supported_vs_currencies`](/reference/simple-supported-currencies).

          interval: data interval, leave empty for auto granularity

          precision: decimal place for currency price value

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not contract_address:
            raise ValueError(f"Expected a non-empty value for `contract_address` but received {contract_address!r}")
        return await self._get(
            f"/coins/{id}/contract/{contract_address}/market_chart/range",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                        "vs_currency": vs_currency,
                        "interval": interval,
                        "precision": precision,
                    },
                    market_chart_get_range_params.MarketChartGetRangeParams,
                ),
            ),
            cast_to=MarketChartGetRangeResponse,
        )


class MarketChartResourceWithRawResponse:
    def __init__(self, market_chart: MarketChartResource) -> None:
        self._market_chart = market_chart

        self.get = to_raw_response_wrapper(
            market_chart.get,
        )
        self.get_range = to_raw_response_wrapper(
            market_chart.get_range,
        )


class AsyncMarketChartResourceWithRawResponse:
    def __init__(self, market_chart: AsyncMarketChartResource) -> None:
        self._market_chart = market_chart

        self.get = async_to_raw_response_wrapper(
            market_chart.get,
        )
        self.get_range = async_to_raw_response_wrapper(
            market_chart.get_range,
        )


class MarketChartResourceWithStreamingResponse:
    def __init__(self, market_chart: MarketChartResource) -> None:
        self._market_chart = market_chart

        self.get = to_streamed_response_wrapper(
            market_chart.get,
        )
        self.get_range = to_streamed_response_wrapper(
            market_chart.get_range,
        )


class AsyncMarketChartResourceWithStreamingResponse:
    def __init__(self, market_chart: AsyncMarketChartResource) -> None:
        self._market_chart = market_chart

        self.get = async_to_streamed_response_wrapper(
            market_chart.get,
        )
        self.get_range = async_to_streamed_response_wrapper(
            market_chart.get_range,
        )
