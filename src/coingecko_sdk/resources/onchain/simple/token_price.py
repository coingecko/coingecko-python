# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ....types.onchain.simple import token_price_get_multi_params
from ....types.onchain.simple.token_price_get_multi_response import TokenPriceGetMultiResponse

__all__ = ["TokenPriceResource", "AsyncTokenPriceResource"]


class TokenPriceResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TokenPriceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return TokenPriceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TokenPriceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return TokenPriceResourceWithStreamingResponse(self)

    def get_multi(
        self,
        *,
        tokens: str,
        include_24hr_price_change: bool | Omit = omit,
        include_24hr_vol: bool | Omit = omit,
        include_inactive_source: bool | Omit = omit,
        include_market_cap: bool | Omit = omit,
        include_total_reserve_in_usd: bool | Omit = omit,
        mcap_fdv_fallback: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TokenPriceGetMultiResponse:
        """
        To get token prices based on the provided token contract addresses across
        multiple networks in a single request

        Args:
          tokens: Network ID and token contract address pairs in `network_id:token_address`
              format, comma-separated if more than one. Maximum: 50 \\**refers to
              [`/onchain/networks`](/reference/networks-list).

          include_24hr_price_change: Include 24hr price change. Default: `false`

          include_24hr_vol: Include 24hr volume. Default: `false`

          include_inactive_source: Include token price data from inactive pools using the most recent swap.
              Default: `false`

          include_market_cap: Include market capitalization. Default: `false`

          include_total_reserve_in_usd: Include total reserve in USD. Default: `false`

          mcap_fdv_fallback: Return FDV if market cap is not available. Default: `false`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/onchain/simple/token_price/multi",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "tokens": tokens,
                        "include_24hr_price_change": include_24hr_price_change,
                        "include_24hr_vol": include_24hr_vol,
                        "include_inactive_source": include_inactive_source,
                        "include_market_cap": include_market_cap,
                        "include_total_reserve_in_usd": include_total_reserve_in_usd,
                        "mcap_fdv_fallback": mcap_fdv_fallback,
                    },
                    token_price_get_multi_params.TokenPriceGetMultiParams,
                ),
            ),
            cast_to=TokenPriceGetMultiResponse,
        )


class AsyncTokenPriceResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTokenPriceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTokenPriceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTokenPriceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return AsyncTokenPriceResourceWithStreamingResponse(self)

    async def get_multi(
        self,
        *,
        tokens: str,
        include_24hr_price_change: bool | Omit = omit,
        include_24hr_vol: bool | Omit = omit,
        include_inactive_source: bool | Omit = omit,
        include_market_cap: bool | Omit = omit,
        include_total_reserve_in_usd: bool | Omit = omit,
        mcap_fdv_fallback: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TokenPriceGetMultiResponse:
        """
        To get token prices based on the provided token contract addresses across
        multiple networks in a single request

        Args:
          tokens: Network ID and token contract address pairs in `network_id:token_address`
              format, comma-separated if more than one. Maximum: 50 \\**refers to
              [`/onchain/networks`](/reference/networks-list).

          include_24hr_price_change: Include 24hr price change. Default: `false`

          include_24hr_vol: Include 24hr volume. Default: `false`

          include_inactive_source: Include token price data from inactive pools using the most recent swap.
              Default: `false`

          include_market_cap: Include market capitalization. Default: `false`

          include_total_reserve_in_usd: Include total reserve in USD. Default: `false`

          mcap_fdv_fallback: Return FDV if market cap is not available. Default: `false`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/onchain/simple/token_price/multi",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "tokens": tokens,
                        "include_24hr_price_change": include_24hr_price_change,
                        "include_24hr_vol": include_24hr_vol,
                        "include_inactive_source": include_inactive_source,
                        "include_market_cap": include_market_cap,
                        "include_total_reserve_in_usd": include_total_reserve_in_usd,
                        "mcap_fdv_fallback": mcap_fdv_fallback,
                    },
                    token_price_get_multi_params.TokenPriceGetMultiParams,
                ),
            ),
            cast_to=TokenPriceGetMultiResponse,
        )


class TokenPriceResourceWithRawResponse:
    def __init__(self, token_price: TokenPriceResource) -> None:
        self._token_price = token_price

        self.get_multi = to_raw_response_wrapper(
            token_price.get_multi,
        )


class AsyncTokenPriceResourceWithRawResponse:
    def __init__(self, token_price: AsyncTokenPriceResource) -> None:
        self._token_price = token_price

        self.get_multi = async_to_raw_response_wrapper(
            token_price.get_multi,
        )


class TokenPriceResourceWithStreamingResponse:
    def __init__(self, token_price: TokenPriceResource) -> None:
        self._token_price = token_price

        self.get_multi = to_streamed_response_wrapper(
            token_price.get_multi,
        )


class AsyncTokenPriceResourceWithStreamingResponse:
    def __init__(self, token_price: AsyncTokenPriceResource) -> None:
        self._token_price = token_price

        self.get_multi = async_to_streamed_response_wrapper(
            token_price.get_multi,
        )
