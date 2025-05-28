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
from .....types.onchain.simple.networks import token_price_get_addresses_params
from .....types.onchain.simple.networks.token_price_get_addresses_response import TokenPriceGetAddressesResponse

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

    def get_addresses(
        self,
        addresses: str,
        *,
        network: str,
        include_24hr_price_change: bool | NotGiven = NOT_GIVEN,
        include_24hr_vol: bool | NotGiven = NOT_GIVEN,
        include_market_cap: bool | NotGiven = NOT_GIVEN,
        include_total_reserve_in_usd: bool | NotGiven = NOT_GIVEN,
        mcap_fdv_fallback: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TokenPriceGetAddressesResponse:
        """
        This endpoint allows you to **get token price based on the provided token
        contract address on a network**

        Args:
          include_24hr_price_change: include 24hr price change, default: false

          include_24hr_vol: include 24hr volume, default: false

          include_market_cap: include market capitalization, default: false

          include_total_reserve_in_usd: include total reserve in USD, default: false

          mcap_fdv_fallback: return FDV if market cap is not available, default: false

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not network:
            raise ValueError(f"Expected a non-empty value for `network` but received {network!r}")
        if not addresses:
            raise ValueError(f"Expected a non-empty value for `addresses` but received {addresses!r}")
        return self._get(
            f"/onchain/simple/networks/{network}/token_price/{addresses}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_24hr_price_change": include_24hr_price_change,
                        "include_24hr_vol": include_24hr_vol,
                        "include_market_cap": include_market_cap,
                        "include_total_reserve_in_usd": include_total_reserve_in_usd,
                        "mcap_fdv_fallback": mcap_fdv_fallback,
                    },
                    token_price_get_addresses_params.TokenPriceGetAddressesParams,
                ),
            ),
            cast_to=TokenPriceGetAddressesResponse,
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

    async def get_addresses(
        self,
        addresses: str,
        *,
        network: str,
        include_24hr_price_change: bool | NotGiven = NOT_GIVEN,
        include_24hr_vol: bool | NotGiven = NOT_GIVEN,
        include_market_cap: bool | NotGiven = NOT_GIVEN,
        include_total_reserve_in_usd: bool | NotGiven = NOT_GIVEN,
        mcap_fdv_fallback: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TokenPriceGetAddressesResponse:
        """
        This endpoint allows you to **get token price based on the provided token
        contract address on a network**

        Args:
          include_24hr_price_change: include 24hr price change, default: false

          include_24hr_vol: include 24hr volume, default: false

          include_market_cap: include market capitalization, default: false

          include_total_reserve_in_usd: include total reserve in USD, default: false

          mcap_fdv_fallback: return FDV if market cap is not available, default: false

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not network:
            raise ValueError(f"Expected a non-empty value for `network` but received {network!r}")
        if not addresses:
            raise ValueError(f"Expected a non-empty value for `addresses` but received {addresses!r}")
        return await self._get(
            f"/onchain/simple/networks/{network}/token_price/{addresses}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "include_24hr_price_change": include_24hr_price_change,
                        "include_24hr_vol": include_24hr_vol,
                        "include_market_cap": include_market_cap,
                        "include_total_reserve_in_usd": include_total_reserve_in_usd,
                        "mcap_fdv_fallback": mcap_fdv_fallback,
                    },
                    token_price_get_addresses_params.TokenPriceGetAddressesParams,
                ),
            ),
            cast_to=TokenPriceGetAddressesResponse,
        )


class TokenPriceResourceWithRawResponse:
    def __init__(self, token_price: TokenPriceResource) -> None:
        self._token_price = token_price

        self.get_addresses = to_raw_response_wrapper(
            token_price.get_addresses,
        )


class AsyncTokenPriceResourceWithRawResponse:
    def __init__(self, token_price: AsyncTokenPriceResource) -> None:
        self._token_price = token_price

        self.get_addresses = async_to_raw_response_wrapper(
            token_price.get_addresses,
        )


class TokenPriceResourceWithStreamingResponse:
    def __init__(self, token_price: TokenPriceResource) -> None:
        self._token_price = token_price

        self.get_addresses = to_streamed_response_wrapper(
            token_price.get_addresses,
        )


class AsyncTokenPriceResourceWithStreamingResponse:
    def __init__(self, token_price: AsyncTokenPriceResource) -> None:
        self._token_price = token_price

        self.get_addresses = async_to_streamed_response_wrapper(
            token_price.get_addresses,
        )
