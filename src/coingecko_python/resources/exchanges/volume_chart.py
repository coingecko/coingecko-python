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
from ...types.exchanges import volume_chart_get_params, volume_chart_get_range_params
from ...types.exchanges.volume_chart_get_response import VolumeChartGetResponse
from ...types.exchanges.volume_chart_get_range_response import VolumeChartGetRangeResponse

__all__ = ["VolumeChartResource", "AsyncVolumeChartResource"]


class VolumeChartResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VolumeChartResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return VolumeChartResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VolumeChartResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return VolumeChartResourceWithStreamingResponse(self)

    def get(
        self,
        id: str,
        *,
        days: Literal["1", "7", "14", "30", "90", "180", "365"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VolumeChartGetResponse:
        """
        This endpoint allows you to **query the historical volume chart data with time
        in UNIX and trading volume data in BTC based on exchange’s ID**

        Args:
          days: data up to number of days ago

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/exchanges/{id}/volume_chart",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"days": days}, volume_chart_get_params.VolumeChartGetParams),
            ),
            cast_to=VolumeChartGetResponse,
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
    ) -> VolumeChartGetRangeResponse:
        """
        This endpoint allows you to **query the historical volume chart data in BTC by
        specifying date range in UNIX based on exchange’s ID**

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
            f"/exchanges/{id}/volume_chart/range",
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
                    volume_chart_get_range_params.VolumeChartGetRangeParams,
                ),
            ),
            cast_to=VolumeChartGetRangeResponse,
        )


class AsyncVolumeChartResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVolumeChartResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVolumeChartResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVolumeChartResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return AsyncVolumeChartResourceWithStreamingResponse(self)

    async def get(
        self,
        id: str,
        *,
        days: Literal["1", "7", "14", "30", "90", "180", "365"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VolumeChartGetResponse:
        """
        This endpoint allows you to **query the historical volume chart data with time
        in UNIX and trading volume data in BTC based on exchange’s ID**

        Args:
          days: data up to number of days ago

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/exchanges/{id}/volume_chart",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"days": days}, volume_chart_get_params.VolumeChartGetParams),
            ),
            cast_to=VolumeChartGetResponse,
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
    ) -> VolumeChartGetRangeResponse:
        """
        This endpoint allows you to **query the historical volume chart data in BTC by
        specifying date range in UNIX based on exchange’s ID**

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
            f"/exchanges/{id}/volume_chart/range",
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
                    volume_chart_get_range_params.VolumeChartGetRangeParams,
                ),
            ),
            cast_to=VolumeChartGetRangeResponse,
        )


class VolumeChartResourceWithRawResponse:
    def __init__(self, volume_chart: VolumeChartResource) -> None:
        self._volume_chart = volume_chart

        self.get = to_raw_response_wrapper(
            volume_chart.get,
        )
        self.get_range = to_raw_response_wrapper(
            volume_chart.get_range,
        )


class AsyncVolumeChartResourceWithRawResponse:
    def __init__(self, volume_chart: AsyncVolumeChartResource) -> None:
        self._volume_chart = volume_chart

        self.get = async_to_raw_response_wrapper(
            volume_chart.get,
        )
        self.get_range = async_to_raw_response_wrapper(
            volume_chart.get_range,
        )


class VolumeChartResourceWithStreamingResponse:
    def __init__(self, volume_chart: VolumeChartResource) -> None:
        self._volume_chart = volume_chart

        self.get = to_streamed_response_wrapper(
            volume_chart.get,
        )
        self.get_range = to_streamed_response_wrapper(
            volume_chart.get_range,
        )


class AsyncVolumeChartResourceWithStreamingResponse:
    def __init__(self, volume_chart: AsyncVolumeChartResource) -> None:
        self._volume_chart = volume_chart

        self.get = async_to_streamed_response_wrapper(
            volume_chart.get,
        )
        self.get_range = async_to_streamed_response_wrapper(
            volume_chart.get_range,
        )
