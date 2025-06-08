# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from .....types.onchain.networks.pools import trade_get_params
from .....types.onchain.networks.pools.trade_get_response import TradeGetResponse

__all__ = ["TradesResource", "AsyncTradesResource"]


class TradesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TradesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return TradesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TradesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return TradesResourceWithStreamingResponse(self)

    def get(
        self,
        pool_address: str,
        *,
        network: str,
        token: str | NotGiven = NOT_GIVEN,
        trade_volume_in_usd_greater_than: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TradeGetResponse:
        """
        This endpoint allows you to **query the last 300 trades in the past 24 hours
        based on the provided pool address**

        Args:
          token: return trades for token use this to invert the chart Available values: 'base',
              'quote' or token address Default value: 'base'

          trade_volume_in_usd_greater_than: filter trades by trade volume in USD greater than this value Default value: 0

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not network:
            raise ValueError(f"Expected a non-empty value for `network` but received {network!r}")
        if not pool_address:
            raise ValueError(f"Expected a non-empty value for `pool_address` but received {pool_address!r}")
        return self._get(
            f"/onchain/networks/{network}/pools/{pool_address}/trades",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "token": token,
                        "trade_volume_in_usd_greater_than": trade_volume_in_usd_greater_than,
                    },
                    trade_get_params.TradeGetParams,
                ),
            ),
            cast_to=TradeGetResponse,
        )


class AsyncTradesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTradesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTradesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTradesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return AsyncTradesResourceWithStreamingResponse(self)

    async def get(
        self,
        pool_address: str,
        *,
        network: str,
        token: str | NotGiven = NOT_GIVEN,
        trade_volume_in_usd_greater_than: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TradeGetResponse:
        """
        This endpoint allows you to **query the last 300 trades in the past 24 hours
        based on the provided pool address**

        Args:
          token: return trades for token use this to invert the chart Available values: 'base',
              'quote' or token address Default value: 'base'

          trade_volume_in_usd_greater_than: filter trades by trade volume in USD greater than this value Default value: 0

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not network:
            raise ValueError(f"Expected a non-empty value for `network` but received {network!r}")
        if not pool_address:
            raise ValueError(f"Expected a non-empty value for `pool_address` but received {pool_address!r}")
        return await self._get(
            f"/onchain/networks/{network}/pools/{pool_address}/trades",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "token": token,
                        "trade_volume_in_usd_greater_than": trade_volume_in_usd_greater_than,
                    },
                    trade_get_params.TradeGetParams,
                ),
            ),
            cast_to=TradeGetResponse,
        )


class TradesResourceWithRawResponse:
    def __init__(self, trades: TradesResource) -> None:
        self._trades = trades

        self.get = to_raw_response_wrapper(
            trades.get,
        )


class AsyncTradesResourceWithRawResponse:
    def __init__(self, trades: AsyncTradesResource) -> None:
        self._trades = trades

        self.get = async_to_raw_response_wrapper(
            trades.get,
        )


class TradesResourceWithStreamingResponse:
    def __init__(self, trades: TradesResource) -> None:
        self._trades = trades

        self.get = to_streamed_response_wrapper(
            trades.get,
        )


class AsyncTradesResourceWithStreamingResponse:
    def __init__(self, trades: AsyncTradesResource) -> None:
        self._trades = trades

        self.get = async_to_streamed_response_wrapper(
            trades.get,
        )
