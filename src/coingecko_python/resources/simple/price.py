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
from ...types.simple import price_get_params
from ...types.simple.price_get_response import PriceGetResponse

__all__ = ["PriceResource", "AsyncPriceResource"]


class PriceResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PriceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return PriceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PriceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return PriceResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        vs_currencies: str,
        ids: str | NotGiven = NOT_GIVEN,
        include_24hr_change: bool | NotGiven = NOT_GIVEN,
        include_24hr_vol: bool | NotGiven = NOT_GIVEN,
        include_last_updated_at: bool | NotGiven = NOT_GIVEN,
        include_market_cap: bool | NotGiven = NOT_GIVEN,
        include_tokens: Literal["top", "all"] | NotGiven = NOT_GIVEN,
        names: str | NotGiven = NOT_GIVEN,
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
        symbols: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PriceGetResponse:
        """
        This endpoint allows you to **query the prices of one or more coins by using
        their unique Coin API IDs**

        Args:
          vs_currencies: target currency of coins, comma-separated if querying more than 1 currency.
              \\**refers to
              [`/simple/supported_vs_currencies`](/reference/simple-supported-currencies).

          ids: coins' IDs, comma-separated if querying more than 1 coin. \\**refers to
              [`/coins/list`](/reference/coins-list).

          include_24hr_change: include 24hr change, default: false

          include_24hr_vol: include 24hr volume, default: false

          include_last_updated_at: include last updated price time in UNIX, default: false

          include_market_cap: include market capitalization, default: false

          include_tokens: for `symbols` lookups, specify `all` to include all matching tokens Default
              `top` returns top-ranked tokens (by market cap or volume)

          names: coins' names, comma-separated if querying more than 1 coin.

          precision: decimal place for currency price value

          symbols: coins' symbols, comma-separated if querying more than 1 coin.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/simple/price",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "vs_currencies": vs_currencies,
                        "ids": ids,
                        "include_24hr_change": include_24hr_change,
                        "include_24hr_vol": include_24hr_vol,
                        "include_last_updated_at": include_last_updated_at,
                        "include_market_cap": include_market_cap,
                        "include_tokens": include_tokens,
                        "names": names,
                        "precision": precision,
                        "symbols": symbols,
                    },
                    price_get_params.PriceGetParams,
                ),
            ),
            cast_to=PriceGetResponse,
        )


class AsyncPriceResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPriceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPriceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPriceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return AsyncPriceResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        vs_currencies: str,
        ids: str | NotGiven = NOT_GIVEN,
        include_24hr_change: bool | NotGiven = NOT_GIVEN,
        include_24hr_vol: bool | NotGiven = NOT_GIVEN,
        include_last_updated_at: bool | NotGiven = NOT_GIVEN,
        include_market_cap: bool | NotGiven = NOT_GIVEN,
        include_tokens: Literal["top", "all"] | NotGiven = NOT_GIVEN,
        names: str | NotGiven = NOT_GIVEN,
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
        symbols: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PriceGetResponse:
        """
        This endpoint allows you to **query the prices of one or more coins by using
        their unique Coin API IDs**

        Args:
          vs_currencies: target currency of coins, comma-separated if querying more than 1 currency.
              \\**refers to
              [`/simple/supported_vs_currencies`](/reference/simple-supported-currencies).

          ids: coins' IDs, comma-separated if querying more than 1 coin. \\**refers to
              [`/coins/list`](/reference/coins-list).

          include_24hr_change: include 24hr change, default: false

          include_24hr_vol: include 24hr volume, default: false

          include_last_updated_at: include last updated price time in UNIX, default: false

          include_market_cap: include market capitalization, default: false

          include_tokens: for `symbols` lookups, specify `all` to include all matching tokens Default
              `top` returns top-ranked tokens (by market cap or volume)

          names: coins' names, comma-separated if querying more than 1 coin.

          precision: decimal place for currency price value

          symbols: coins' symbols, comma-separated if querying more than 1 coin.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/simple/price",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "vs_currencies": vs_currencies,
                        "ids": ids,
                        "include_24hr_change": include_24hr_change,
                        "include_24hr_vol": include_24hr_vol,
                        "include_last_updated_at": include_last_updated_at,
                        "include_market_cap": include_market_cap,
                        "include_tokens": include_tokens,
                        "names": names,
                        "precision": precision,
                        "symbols": symbols,
                    },
                    price_get_params.PriceGetParams,
                ),
            ),
            cast_to=PriceGetResponse,
        )


class PriceResourceWithRawResponse:
    def __init__(self, price: PriceResource) -> None:
        self._price = price

        self.get = to_raw_response_wrapper(
            price.get,
        )


class AsyncPriceResourceWithRawResponse:
    def __init__(self, price: AsyncPriceResource) -> None:
        self._price = price

        self.get = async_to_raw_response_wrapper(
            price.get,
        )


class PriceResourceWithStreamingResponse:
    def __init__(self, price: PriceResource) -> None:
        self._price = price

        self.get = to_streamed_response_wrapper(
            price.get,
        )


class AsyncPriceResourceWithStreamingResponse:
    def __init__(self, price: AsyncPriceResource) -> None:
        self._price = price

        self.get = async_to_streamed_response_wrapper(
            price.get,
        )
