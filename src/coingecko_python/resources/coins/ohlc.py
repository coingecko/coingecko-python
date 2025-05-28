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
from ...types.coins import ohlc_get_params, ohlc_get_range_params
from ..._base_client import make_request_options
from ...types.coins.ohlc_get_response import OhlcGetResponse
from ...types.coins.ohlc_get_range_response import OhlcGetRangeResponse

__all__ = ["OhlcResource", "AsyncOhlcResource"]


class OhlcResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OhlcResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return OhlcResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OhlcResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return OhlcResourceWithStreamingResponse(self)

    def get(
        self,
        id: str,
        *,
        days: Literal["1", "7", "14", "30", "90", "180", "365", "max"],
        vs_currency: str,
        interval: Literal["daily", "hourly"] | NotGiven = NOT_GIVEN,
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
    ) -> OhlcGetResponse:
        """
        This endpoint allows you to **get the OHLC chart (Open, High, Low, Close) of a
        coin based on particular coin ID**

        Args:
          days: data up to number of days ago

          vs_currency: target currency of price data \\**refers to
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
        return self._get(
            f"/coins/{id}/ohlc",
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
                    ohlc_get_params.OhlcGetParams,
                ),
            ),
            cast_to=OhlcGetResponse,
        )

    def get_range(
        self,
        id: str,
        *,
        from_: float,
        interval: Literal["daily", "hourly"],
        to: float,
        vs_currency: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OhlcGetRangeResponse:
        """
        This endpoint allows you to **get the OHLC chart (Open, High, Low, Close) of a
        coin within a range of timestamp based on particular coin ID**

        Args:
          from_: starting date in UNIX timestamp

          interval: data interval

          to: ending date in UNIX timestamp

          vs_currency: target currency of price data \\**refers to
              [`/simple/supported_vs_currencies`](/reference/simple-supported-currencies).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/coins/{id}/ohlc/range",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_": from_,
                        "interval": interval,
                        "to": to,
                        "vs_currency": vs_currency,
                    },
                    ohlc_get_range_params.OhlcGetRangeParams,
                ),
            ),
            cast_to=OhlcGetRangeResponse,
        )


class AsyncOhlcResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOhlcResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOhlcResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOhlcResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return AsyncOhlcResourceWithStreamingResponse(self)

    async def get(
        self,
        id: str,
        *,
        days: Literal["1", "7", "14", "30", "90", "180", "365", "max"],
        vs_currency: str,
        interval: Literal["daily", "hourly"] | NotGiven = NOT_GIVEN,
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
    ) -> OhlcGetResponse:
        """
        This endpoint allows you to **get the OHLC chart (Open, High, Low, Close) of a
        coin based on particular coin ID**

        Args:
          days: data up to number of days ago

          vs_currency: target currency of price data \\**refers to
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
        return await self._get(
            f"/coins/{id}/ohlc",
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
                    ohlc_get_params.OhlcGetParams,
                ),
            ),
            cast_to=OhlcGetResponse,
        )

    async def get_range(
        self,
        id: str,
        *,
        from_: float,
        interval: Literal["daily", "hourly"],
        to: float,
        vs_currency: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OhlcGetRangeResponse:
        """
        This endpoint allows you to **get the OHLC chart (Open, High, Low, Close) of a
        coin within a range of timestamp based on particular coin ID**

        Args:
          from_: starting date in UNIX timestamp

          interval: data interval

          to: ending date in UNIX timestamp

          vs_currency: target currency of price data \\**refers to
              [`/simple/supported_vs_currencies`](/reference/simple-supported-currencies).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/coins/{id}/ohlc/range",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_": from_,
                        "interval": interval,
                        "to": to,
                        "vs_currency": vs_currency,
                    },
                    ohlc_get_range_params.OhlcGetRangeParams,
                ),
            ),
            cast_to=OhlcGetRangeResponse,
        )


class OhlcResourceWithRawResponse:
    def __init__(self, ohlc: OhlcResource) -> None:
        self._ohlc = ohlc

        self.get = to_raw_response_wrapper(
            ohlc.get,
        )
        self.get_range = to_raw_response_wrapper(
            ohlc.get_range,
        )


class AsyncOhlcResourceWithRawResponse:
    def __init__(self, ohlc: AsyncOhlcResource) -> None:
        self._ohlc = ohlc

        self.get = async_to_raw_response_wrapper(
            ohlc.get,
        )
        self.get_range = async_to_raw_response_wrapper(
            ohlc.get_range,
        )


class OhlcResourceWithStreamingResponse:
    def __init__(self, ohlc: OhlcResource) -> None:
        self._ohlc = ohlc

        self.get = to_streamed_response_wrapper(
            ohlc.get,
        )
        self.get_range = to_streamed_response_wrapper(
            ohlc.get_range,
        )


class AsyncOhlcResourceWithStreamingResponse:
    def __init__(self, ohlc: AsyncOhlcResource) -> None:
        self._ohlc = ohlc

        self.get = async_to_streamed_response_wrapper(
            ohlc.get,
        )
        self.get_range = async_to_streamed_response_wrapper(
            ohlc.get_range,
        )
