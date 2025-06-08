# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.exchange_rate_get_response import ExchangeRateGetResponse

__all__ = ["ExchangeRatesResource", "AsyncExchangeRatesResource"]


class ExchangeRatesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExchangeRatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return ExchangeRatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExchangeRatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return ExchangeRatesResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExchangeRateGetResponse:
        """This endpoint allows you to **query BTC exchange rates with other currencies**"""
        return self._get(
            "/exchange_rates",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExchangeRateGetResponse,
        )


class AsyncExchangeRatesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExchangeRatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExchangeRatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExchangeRatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return AsyncExchangeRatesResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExchangeRateGetResponse:
        """This endpoint allows you to **query BTC exchange rates with other currencies**"""
        return await self._get(
            "/exchange_rates",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExchangeRateGetResponse,
        )


class ExchangeRatesResourceWithRawResponse:
    def __init__(self, exchange_rates: ExchangeRatesResource) -> None:
        self._exchange_rates = exchange_rates

        self.get = to_raw_response_wrapper(
            exchange_rates.get,
        )


class AsyncExchangeRatesResourceWithRawResponse:
    def __init__(self, exchange_rates: AsyncExchangeRatesResource) -> None:
        self._exchange_rates = exchange_rates

        self.get = async_to_raw_response_wrapper(
            exchange_rates.get,
        )


class ExchangeRatesResourceWithStreamingResponse:
    def __init__(self, exchange_rates: ExchangeRatesResource) -> None:
        self._exchange_rates = exchange_rates

        self.get = to_streamed_response_wrapper(
            exchange_rates.get,
        )


class AsyncExchangeRatesResourceWithStreamingResponse:
    def __init__(self, exchange_rates: AsyncExchangeRatesResource) -> None:
        self._exchange_rates = exchange_rates

        self.get = async_to_streamed_response_wrapper(
            exchange_rates.get,
        )
