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
from ...types.simple import token_price_get_id_params
from ...types.simple.token_price_get_id_response import TokenPriceGetIDResponse

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

    def get_id(
        self,
        id: str,
        *,
        contract_addresses: str,
        vs_currencies: str,
        include_24hr_change: bool | NotGiven = NOT_GIVEN,
        include_24hr_vol: bool | NotGiven = NOT_GIVEN,
        include_last_updated_at: bool | NotGiven = NOT_GIVEN,
        include_market_cap: bool | NotGiven = NOT_GIVEN,
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
    ) -> TokenPriceGetIDResponse:
        """
        This endpoint allows you to **query one or more token prices using their token
        contract addresses**

        Args:
          contract_addresses: the contract addresses of tokens, comma-separated if querying more than 1
              token's contract address

          vs_currencies: target currency of coins, comma-separated if querying more than 1 currency.
              \\**refers to
              [`/simple/supported_vs_currencies`](/reference/simple-supported-currencies).

          include_24hr_change: include 24hr change default: false

          include_24hr_vol: include 24hr volume, default: false

          include_last_updated_at: include last updated price time in UNIX , default: false

          include_market_cap: include market capitalization, default: false

          precision: decimal place for currency price value

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/simple/token_price/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "contract_addresses": contract_addresses,
                        "vs_currencies": vs_currencies,
                        "include_24hr_change": include_24hr_change,
                        "include_24hr_vol": include_24hr_vol,
                        "include_last_updated_at": include_last_updated_at,
                        "include_market_cap": include_market_cap,
                        "precision": precision,
                    },
                    token_price_get_id_params.TokenPriceGetIDParams,
                ),
            ),
            cast_to=TokenPriceGetIDResponse,
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

    async def get_id(
        self,
        id: str,
        *,
        contract_addresses: str,
        vs_currencies: str,
        include_24hr_change: bool | NotGiven = NOT_GIVEN,
        include_24hr_vol: bool | NotGiven = NOT_GIVEN,
        include_last_updated_at: bool | NotGiven = NOT_GIVEN,
        include_market_cap: bool | NotGiven = NOT_GIVEN,
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
    ) -> TokenPriceGetIDResponse:
        """
        This endpoint allows you to **query one or more token prices using their token
        contract addresses**

        Args:
          contract_addresses: the contract addresses of tokens, comma-separated if querying more than 1
              token's contract address

          vs_currencies: target currency of coins, comma-separated if querying more than 1 currency.
              \\**refers to
              [`/simple/supported_vs_currencies`](/reference/simple-supported-currencies).

          include_24hr_change: include 24hr change default: false

          include_24hr_vol: include 24hr volume, default: false

          include_last_updated_at: include last updated price time in UNIX , default: false

          include_market_cap: include market capitalization, default: false

          precision: decimal place for currency price value

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/simple/token_price/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "contract_addresses": contract_addresses,
                        "vs_currencies": vs_currencies,
                        "include_24hr_change": include_24hr_change,
                        "include_24hr_vol": include_24hr_vol,
                        "include_last_updated_at": include_last_updated_at,
                        "include_market_cap": include_market_cap,
                        "precision": precision,
                    },
                    token_price_get_id_params.TokenPriceGetIDParams,
                ),
            ),
            cast_to=TokenPriceGetIDResponse,
        )


class TokenPriceResourceWithRawResponse:
    def __init__(self, token_price: TokenPriceResource) -> None:
        self._token_price = token_price

        self.get_id = to_raw_response_wrapper(
            token_price.get_id,
        )


class AsyncTokenPriceResourceWithRawResponse:
    def __init__(self, token_price: AsyncTokenPriceResource) -> None:
        self._token_price = token_price

        self.get_id = async_to_raw_response_wrapper(
            token_price.get_id,
        )


class TokenPriceResourceWithStreamingResponse:
    def __init__(self, token_price: TokenPriceResource) -> None:
        self._token_price = token_price

        self.get_id = to_streamed_response_wrapper(
            token_price.get_id,
        )


class AsyncTokenPriceResourceWithStreamingResponse:
    def __init__(self, token_price: AsyncTokenPriceResource) -> None:
        self._token_price = token_price

        self.get_id = async_to_streamed_response_wrapper(
            token_price.get_id,
        )
