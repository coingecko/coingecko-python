# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import path_template, maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.onchain.networks.pools import liquidity_event_get_params
from .....types.onchain.networks.pools.liquidity_event_get_response import LiquidityEventGetResponse

__all__ = ["LiquidityEventsResource", "AsyncLiquidityEventsResource"]


class LiquidityEventsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LiquidityEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return LiquidityEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LiquidityEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return LiquidityEventsResourceWithStreamingResponse(self)

    def get(
        self,
        pool_address: str,
        *,
        network: str,
        cursor: str | Omit = omit,
        kind: Literal["add", "remove"] | Omit = omit,
        per_page: int | Omit = omit,
        volume_in_usd_greater_than: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LiquidityEventGetResponse:
        """
        To query the add and remove liquidity events based on the provided pool address

        Args:
          cursor: Cursor from the previous response, passed back unchanged to fetch the next page.

          kind: Filter by liquidity event kind, omit to return both. Available values: `add`,
              `remove`

          per_page: Total results per page. Default value: 20 Valid values: 1...50

          volume_in_usd_greater_than: Filter liquidity events by volume in USD greater than this value. Must be a
              positive number.

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
            path_template(
                "/onchain/networks/{network}/pools/{pool_address}/liquidity_events",
                network=network,
                pool_address=pool_address,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "kind": kind,
                        "per_page": per_page,
                        "volume_in_usd_greater_than": volume_in_usd_greater_than,
                    },
                    liquidity_event_get_params.LiquidityEventGetParams,
                ),
            ),
            cast_to=LiquidityEventGetResponse,
        )


class AsyncLiquidityEventsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLiquidityEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLiquidityEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLiquidityEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return AsyncLiquidityEventsResourceWithStreamingResponse(self)

    async def get(
        self,
        pool_address: str,
        *,
        network: str,
        cursor: str | Omit = omit,
        kind: Literal["add", "remove"] | Omit = omit,
        per_page: int | Omit = omit,
        volume_in_usd_greater_than: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LiquidityEventGetResponse:
        """
        To query the add and remove liquidity events based on the provided pool address

        Args:
          cursor: Cursor from the previous response, passed back unchanged to fetch the next page.

          kind: Filter by liquidity event kind, omit to return both. Available values: `add`,
              `remove`

          per_page: Total results per page. Default value: 20 Valid values: 1...50

          volume_in_usd_greater_than: Filter liquidity events by volume in USD greater than this value. Must be a
              positive number.

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
            path_template(
                "/onchain/networks/{network}/pools/{pool_address}/liquidity_events",
                network=network,
                pool_address=pool_address,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "kind": kind,
                        "per_page": per_page,
                        "volume_in_usd_greater_than": volume_in_usd_greater_than,
                    },
                    liquidity_event_get_params.LiquidityEventGetParams,
                ),
            ),
            cast_to=LiquidityEventGetResponse,
        )


class LiquidityEventsResourceWithRawResponse:
    def __init__(self, liquidity_events: LiquidityEventsResource) -> None:
        self._liquidity_events = liquidity_events

        self.get = to_raw_response_wrapper(
            liquidity_events.get,
        )


class AsyncLiquidityEventsResourceWithRawResponse:
    def __init__(self, liquidity_events: AsyncLiquidityEventsResource) -> None:
        self._liquidity_events = liquidity_events

        self.get = async_to_raw_response_wrapper(
            liquidity_events.get,
        )


class LiquidityEventsResourceWithStreamingResponse:
    def __init__(self, liquidity_events: LiquidityEventsResource) -> None:
        self._liquidity_events = liquidity_events

        self.get = to_streamed_response_wrapper(
            liquidity_events.get,
        )


class AsyncLiquidityEventsResourceWithStreamingResponse:
    def __init__(self, liquidity_events: AsyncLiquidityEventsResource) -> None:
        self._liquidity_events = liquidity_events

        self.get = async_to_streamed_response_wrapper(
            liquidity_events.get,
        )
