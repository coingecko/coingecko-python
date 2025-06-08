# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.onchain.networks.tokens import ohlcv_get_timeframe_params
from .....types.onchain.networks.tokens.ohlcv_get_timeframe_response import OhlcvGetTimeframeResponse

__all__ = ["OhlcvResource", "AsyncOhlcvResource"]


class OhlcvResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OhlcvResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return OhlcvResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OhlcvResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return OhlcvResourceWithStreamingResponse(self)

    def get_timeframe(
        self,
        timeframe: Literal["day", "hour", "minute"],
        *,
        network: str,
        token_address: str,
        aggregate: str | NotGiven = NOT_GIVEN,
        before_timestamp: int | NotGiven = NOT_GIVEN,
        currency: Literal["usd", "token"] | NotGiven = NOT_GIVEN,
        include_empty_intervals: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OhlcvGetTimeframeResponse:
        """
        This endpoint allows you to **get the OHLCV chart (Open, High, Low, Close,
        Volume) of a token based on the provided token address on a network**

        Args:
          aggregate: time period to aggregate each OHLCV Available values (day): `1` Available values
              (hour): `1` , `4` , `12` Available values (minute): `1` , `5` , `15` Default
              value: 1

          before_timestamp: return OHLCV data before this timestamp (integer seconds since epoch)

          currency: return OHLCV in USD or quote token Default value: usd

          include_empty_intervals: include empty intervals with no trade data, default: false

          limit: number of OHLCV results to return, maximum 1000 Default value: 100

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not network:
            raise ValueError(f"Expected a non-empty value for `network` but received {network!r}")
        if not token_address:
            raise ValueError(f"Expected a non-empty value for `token_address` but received {token_address!r}")
        if not timeframe:
            raise ValueError(f"Expected a non-empty value for `timeframe` but received {timeframe!r}")
        return self._get(
            f"/onchain/networks/{network}/tokens/{token_address}/ohlcv/{timeframe}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "aggregate": aggregate,
                        "before_timestamp": before_timestamp,
                        "currency": currency,
                        "include_empty_intervals": include_empty_intervals,
                        "limit": limit,
                    },
                    ohlcv_get_timeframe_params.OhlcvGetTimeframeParams,
                ),
            ),
            cast_to=OhlcvGetTimeframeResponse,
        )


class AsyncOhlcvResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOhlcvResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOhlcvResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOhlcvResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return AsyncOhlcvResourceWithStreamingResponse(self)

    async def get_timeframe(
        self,
        timeframe: Literal["day", "hour", "minute"],
        *,
        network: str,
        token_address: str,
        aggregate: str | NotGiven = NOT_GIVEN,
        before_timestamp: int | NotGiven = NOT_GIVEN,
        currency: Literal["usd", "token"] | NotGiven = NOT_GIVEN,
        include_empty_intervals: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OhlcvGetTimeframeResponse:
        """
        This endpoint allows you to **get the OHLCV chart (Open, High, Low, Close,
        Volume) of a token based on the provided token address on a network**

        Args:
          aggregate: time period to aggregate each OHLCV Available values (day): `1` Available values
              (hour): `1` , `4` , `12` Available values (minute): `1` , `5` , `15` Default
              value: 1

          before_timestamp: return OHLCV data before this timestamp (integer seconds since epoch)

          currency: return OHLCV in USD or quote token Default value: usd

          include_empty_intervals: include empty intervals with no trade data, default: false

          limit: number of OHLCV results to return, maximum 1000 Default value: 100

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not network:
            raise ValueError(f"Expected a non-empty value for `network` but received {network!r}")
        if not token_address:
            raise ValueError(f"Expected a non-empty value for `token_address` but received {token_address!r}")
        if not timeframe:
            raise ValueError(f"Expected a non-empty value for `timeframe` but received {timeframe!r}")
        return await self._get(
            f"/onchain/networks/{network}/tokens/{token_address}/ohlcv/{timeframe}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "aggregate": aggregate,
                        "before_timestamp": before_timestamp,
                        "currency": currency,
                        "include_empty_intervals": include_empty_intervals,
                        "limit": limit,
                    },
                    ohlcv_get_timeframe_params.OhlcvGetTimeframeParams,
                ),
            ),
            cast_to=OhlcvGetTimeframeResponse,
        )


class OhlcvResourceWithRawResponse:
    def __init__(self, ohlcv: OhlcvResource) -> None:
        self._ohlcv = ohlcv

        self.get_timeframe = to_raw_response_wrapper(
            ohlcv.get_timeframe,
        )


class AsyncOhlcvResourceWithRawResponse:
    def __init__(self, ohlcv: AsyncOhlcvResource) -> None:
        self._ohlcv = ohlcv

        self.get_timeframe = async_to_raw_response_wrapper(
            ohlcv.get_timeframe,
        )


class OhlcvResourceWithStreamingResponse:
    def __init__(self, ohlcv: OhlcvResource) -> None:
        self._ohlcv = ohlcv

        self.get_timeframe = to_streamed_response_wrapper(
            ohlcv.get_timeframe,
        )


class AsyncOhlcvResourceWithStreamingResponse:
    def __init__(self, ohlcv: AsyncOhlcvResource) -> None:
        self._ohlcv = ohlcv

        self.get_timeframe = async_to_streamed_response_wrapper(
            ohlcv.get_timeframe,
        )
