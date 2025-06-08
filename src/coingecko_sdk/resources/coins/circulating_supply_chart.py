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
from ...types.coins import circulating_supply_chart_get_params, circulating_supply_chart_get_range_params
from ..._base_client import make_request_options
from ...types.coins.circulating_supply_chart_get_response import CirculatingSupplyChartGetResponse
from ...types.coins.circulating_supply_chart_get_range_response import CirculatingSupplyChartGetRangeResponse

__all__ = ["CirculatingSupplyChartResource", "AsyncCirculatingSupplyChartResource"]


class CirculatingSupplyChartResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CirculatingSupplyChartResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return CirculatingSupplyChartResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CirculatingSupplyChartResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return CirculatingSupplyChartResourceWithStreamingResponse(self)

    def get(
        self,
        id: str,
        *,
        days: str,
        interval: Literal["daily"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CirculatingSupplyChartGetResponse:
        """
        This endpoint allows you to **query historical circulating supply of a coin by
        number of days away from now based on provided coin ID**

        Args:
          days: data up to number of days ago Valid values: any integer or `max`

          interval: data interval

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/coins/{id}/circulating_supply_chart",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "days": days,
                        "interval": interval,
                    },
                    circulating_supply_chart_get_params.CirculatingSupplyChartGetParams,
                ),
            ),
            cast_to=CirculatingSupplyChartGetResponse,
        )

    def get_range(
        self,
        id: str,
        *,
        from_: float,
        to: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CirculatingSupplyChartGetRangeResponse:
        """
        This endpoint allows you to **query historical circulating supply of a coin,
        within a range of timestamp based on the provided coin ID**

        Args:
          from_: starting date in UNIX timestamp

          to: ending date in UNIX timestamp

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/coins/{id}/circulating_supply_chart/range",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                    },
                    circulating_supply_chart_get_range_params.CirculatingSupplyChartGetRangeParams,
                ),
            ),
            cast_to=CirculatingSupplyChartGetRangeResponse,
        )


class AsyncCirculatingSupplyChartResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCirculatingSupplyChartResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCirculatingSupplyChartResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCirculatingSupplyChartResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return AsyncCirculatingSupplyChartResourceWithStreamingResponse(self)

    async def get(
        self,
        id: str,
        *,
        days: str,
        interval: Literal["daily"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CirculatingSupplyChartGetResponse:
        """
        This endpoint allows you to **query historical circulating supply of a coin by
        number of days away from now based on provided coin ID**

        Args:
          days: data up to number of days ago Valid values: any integer or `max`

          interval: data interval

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/coins/{id}/circulating_supply_chart",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "days": days,
                        "interval": interval,
                    },
                    circulating_supply_chart_get_params.CirculatingSupplyChartGetParams,
                ),
            ),
            cast_to=CirculatingSupplyChartGetResponse,
        )

    async def get_range(
        self,
        id: str,
        *,
        from_: float,
        to: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CirculatingSupplyChartGetRangeResponse:
        """
        This endpoint allows you to **query historical circulating supply of a coin,
        within a range of timestamp based on the provided coin ID**

        Args:
          from_: starting date in UNIX timestamp

          to: ending date in UNIX timestamp

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/coins/{id}/circulating_supply_chart/range",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                    },
                    circulating_supply_chart_get_range_params.CirculatingSupplyChartGetRangeParams,
                ),
            ),
            cast_to=CirculatingSupplyChartGetRangeResponse,
        )


class CirculatingSupplyChartResourceWithRawResponse:
    def __init__(self, circulating_supply_chart: CirculatingSupplyChartResource) -> None:
        self._circulating_supply_chart = circulating_supply_chart

        self.get = to_raw_response_wrapper(
            circulating_supply_chart.get,
        )
        self.get_range = to_raw_response_wrapper(
            circulating_supply_chart.get_range,
        )


class AsyncCirculatingSupplyChartResourceWithRawResponse:
    def __init__(self, circulating_supply_chart: AsyncCirculatingSupplyChartResource) -> None:
        self._circulating_supply_chart = circulating_supply_chart

        self.get = async_to_raw_response_wrapper(
            circulating_supply_chart.get,
        )
        self.get_range = async_to_raw_response_wrapper(
            circulating_supply_chart.get_range,
        )


class CirculatingSupplyChartResourceWithStreamingResponse:
    def __init__(self, circulating_supply_chart: CirculatingSupplyChartResource) -> None:
        self._circulating_supply_chart = circulating_supply_chart

        self.get = to_streamed_response_wrapper(
            circulating_supply_chart.get,
        )
        self.get_range = to_streamed_response_wrapper(
            circulating_supply_chart.get_range,
        )


class AsyncCirculatingSupplyChartResourceWithStreamingResponse:
    def __init__(self, circulating_supply_chart: AsyncCirculatingSupplyChartResource) -> None:
        self._circulating_supply_chart = circulating_supply_chart

        self.get = async_to_streamed_response_wrapper(
            circulating_supply_chart.get,
        )
        self.get_range = async_to_streamed_response_wrapper(
            circulating_supply_chart.get_range,
        )
