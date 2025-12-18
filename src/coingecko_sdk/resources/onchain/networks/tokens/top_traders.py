# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from .....types.onchain.networks.tokens import top_trader_get_params
from .....types.onchain.networks.tokens.top_trader_get_response import TopTraderGetResponse

__all__ = ["TopTradersResource", "AsyncTopTradersResource"]


class TopTradersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TopTradersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return TopTradersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TopTradersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return TopTradersResourceWithStreamingResponse(self)

    def get(
        self,
        token_address: str,
        *,
        network_id: str,
        include_address_label: bool | Omit = omit,
        sort: Literal["realized_pnl_usd_desc", "unrealized_pnl_usd_desc", "total_buy_usd_desc", "total_sell_usd_desc"]
        | Omit = omit,
        traders: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TopTraderGetResponse:
        """
        This endpoint allows you to **query top token traders based on the provided
        token contract address on a network**

        Args:
          include_address_label: include address label data, default: false

          sort: sort the traders by field Default value: realized_pnl_usd_desc

          traders: number of top token traders to return, you may use any integer or `max` Default
              value: 10

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not network_id:
            raise ValueError(f"Expected a non-empty value for `network_id` but received {network_id!r}")
        if not token_address:
            raise ValueError(f"Expected a non-empty value for `token_address` but received {token_address!r}")
        return self._get(
            f"/onchain/networks/{network_id}/tokens/{token_address}/top_traders",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_address_label": include_address_label,
                        "sort": sort,
                        "traders": traders,
                    },
                    top_trader_get_params.TopTraderGetParams,
                ),
            ),
            cast_to=TopTraderGetResponse,
        )


class AsyncTopTradersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTopTradersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTopTradersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTopTradersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return AsyncTopTradersResourceWithStreamingResponse(self)

    async def get(
        self,
        token_address: str,
        *,
        network_id: str,
        include_address_label: bool | Omit = omit,
        sort: Literal["realized_pnl_usd_desc", "unrealized_pnl_usd_desc", "total_buy_usd_desc", "total_sell_usd_desc"]
        | Omit = omit,
        traders: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TopTraderGetResponse:
        """
        This endpoint allows you to **query top token traders based on the provided
        token contract address on a network**

        Args:
          include_address_label: include address label data, default: false

          sort: sort the traders by field Default value: realized_pnl_usd_desc

          traders: number of top token traders to return, you may use any integer or `max` Default
              value: 10

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not network_id:
            raise ValueError(f"Expected a non-empty value for `network_id` but received {network_id!r}")
        if not token_address:
            raise ValueError(f"Expected a non-empty value for `token_address` but received {token_address!r}")
        return await self._get(
            f"/onchain/networks/{network_id}/tokens/{token_address}/top_traders",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "include_address_label": include_address_label,
                        "sort": sort,
                        "traders": traders,
                    },
                    top_trader_get_params.TopTraderGetParams,
                ),
            ),
            cast_to=TopTraderGetResponse,
        )


class TopTradersResourceWithRawResponse:
    def __init__(self, top_traders: TopTradersResource) -> None:
        self._top_traders = top_traders

        self.get = to_raw_response_wrapper(
            top_traders.get,
        )


class AsyncTopTradersResourceWithRawResponse:
    def __init__(self, top_traders: AsyncTopTradersResource) -> None:
        self._top_traders = top_traders

        self.get = async_to_raw_response_wrapper(
            top_traders.get,
        )


class TopTradersResourceWithStreamingResponse:
    def __init__(self, top_traders: TopTradersResource) -> None:
        self._top_traders = top_traders

        self.get = to_streamed_response_wrapper(
            top_traders.get,
        )


class AsyncTopTradersResourceWithStreamingResponse:
    def __init__(self, top_traders: AsyncTopTradersResource) -> None:
        self._top_traders = top_traders

        self.get = async_to_streamed_response_wrapper(
            top_traders.get,
        )
