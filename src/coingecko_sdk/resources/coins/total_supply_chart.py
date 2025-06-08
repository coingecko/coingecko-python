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
from ...types.coins import total_supply_chart_get_params, total_supply_chart_get_range_params
from ..._base_client import make_request_options
from ...types.coins.total_supply_chart_get_response import TotalSupplyChartGetResponse
from ...types.coins.total_supply_chart_get_range_response import TotalSupplyChartGetRangeResponse

__all__ = ["TotalSupplyChartResource", "AsyncTotalSupplyChartResource"]


class TotalSupplyChartResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TotalSupplyChartResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return TotalSupplyChartResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TotalSupplyChartResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return TotalSupplyChartResourceWithStreamingResponse(self)

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
    ) -> TotalSupplyChartGetResponse:
        """
        This endpoint allows you to **query historical total supply of a coin by number
        of days away from now based on provided coin ID**

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
            f"/coins/{id}/total_supply_chart",
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
                    total_supply_chart_get_params.TotalSupplyChartGetParams,
                ),
            ),
            cast_to=TotalSupplyChartGetResponse,
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
    ) -> TotalSupplyChartGetRangeResponse:
        """
        This endpoint allows you to **query historical total supply of a coin, within a
        range of timestamp based on the provided coin ID**

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
            f"/coins/{id}/total_supply_chart/range",
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
                    total_supply_chart_get_range_params.TotalSupplyChartGetRangeParams,
                ),
            ),
            cast_to=TotalSupplyChartGetRangeResponse,
        )


class AsyncTotalSupplyChartResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTotalSupplyChartResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTotalSupplyChartResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTotalSupplyChartResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return AsyncTotalSupplyChartResourceWithStreamingResponse(self)

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
    ) -> TotalSupplyChartGetResponse:
        """
        This endpoint allows you to **query historical total supply of a coin by number
        of days away from now based on provided coin ID**

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
            f"/coins/{id}/total_supply_chart",
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
                    total_supply_chart_get_params.TotalSupplyChartGetParams,
                ),
            ),
            cast_to=TotalSupplyChartGetResponse,
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
    ) -> TotalSupplyChartGetRangeResponse:
        """
        This endpoint allows you to **query historical total supply of a coin, within a
        range of timestamp based on the provided coin ID**

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
            f"/coins/{id}/total_supply_chart/range",
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
                    total_supply_chart_get_range_params.TotalSupplyChartGetRangeParams,
                ),
            ),
            cast_to=TotalSupplyChartGetRangeResponse,
        )


class TotalSupplyChartResourceWithRawResponse:
    def __init__(self, total_supply_chart: TotalSupplyChartResource) -> None:
        self._total_supply_chart = total_supply_chart

        self.get = to_raw_response_wrapper(
            total_supply_chart.get,
        )
        self.get_range = to_raw_response_wrapper(
            total_supply_chart.get_range,
        )


class AsyncTotalSupplyChartResourceWithRawResponse:
    def __init__(self, total_supply_chart: AsyncTotalSupplyChartResource) -> None:
        self._total_supply_chart = total_supply_chart

        self.get = async_to_raw_response_wrapper(
            total_supply_chart.get,
        )
        self.get_range = async_to_raw_response_wrapper(
            total_supply_chart.get_range,
        )


class TotalSupplyChartResourceWithStreamingResponse:
    def __init__(self, total_supply_chart: TotalSupplyChartResource) -> None:
        self._total_supply_chart = total_supply_chart

        self.get = to_streamed_response_wrapper(
            total_supply_chart.get,
        )
        self.get_range = to_streamed_response_wrapper(
            total_supply_chart.get_range,
        )


class AsyncTotalSupplyChartResourceWithStreamingResponse:
    def __init__(self, total_supply_chart: AsyncTotalSupplyChartResource) -> None:
        self._total_supply_chart = total_supply_chart

        self.get = async_to_streamed_response_wrapper(
            total_supply_chart.get,
        )
        self.get_range = async_to_streamed_response_wrapper(
            total_supply_chart.get_range,
        )
