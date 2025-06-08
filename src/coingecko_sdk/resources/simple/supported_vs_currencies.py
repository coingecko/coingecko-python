# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.simple.supported_vs_currency_get_response import SupportedVsCurrencyGetResponse

__all__ = ["SupportedVsCurrenciesResource", "AsyncSupportedVsCurrenciesResource"]


class SupportedVsCurrenciesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SupportedVsCurrenciesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return SupportedVsCurrenciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SupportedVsCurrenciesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return SupportedVsCurrenciesResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SupportedVsCurrencyGetResponse:
        """This endpoint allows you to **query all the supported currencies on CoinGecko**"""
        return self._get(
            "/simple/supported_vs_currencies",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SupportedVsCurrencyGetResponse,
        )


class AsyncSupportedVsCurrenciesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSupportedVsCurrenciesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSupportedVsCurrenciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSupportedVsCurrenciesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return AsyncSupportedVsCurrenciesResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SupportedVsCurrencyGetResponse:
        """This endpoint allows you to **query all the supported currencies on CoinGecko**"""
        return await self._get(
            "/simple/supported_vs_currencies",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SupportedVsCurrencyGetResponse,
        )


class SupportedVsCurrenciesResourceWithRawResponse:
    def __init__(self, supported_vs_currencies: SupportedVsCurrenciesResource) -> None:
        self._supported_vs_currencies = supported_vs_currencies

        self.get = to_raw_response_wrapper(
            supported_vs_currencies.get,
        )


class AsyncSupportedVsCurrenciesResourceWithRawResponse:
    def __init__(self, supported_vs_currencies: AsyncSupportedVsCurrenciesResource) -> None:
        self._supported_vs_currencies = supported_vs_currencies

        self.get = async_to_raw_response_wrapper(
            supported_vs_currencies.get,
        )


class SupportedVsCurrenciesResourceWithStreamingResponse:
    def __init__(self, supported_vs_currencies: SupportedVsCurrenciesResource) -> None:
        self._supported_vs_currencies = supported_vs_currencies

        self.get = to_streamed_response_wrapper(
            supported_vs_currencies.get,
        )


class AsyncSupportedVsCurrenciesResourceWithStreamingResponse:
    def __init__(self, supported_vs_currencies: AsyncSupportedVsCurrenciesResource) -> None:
        self._supported_vs_currencies = supported_vs_currencies

        self.get = async_to_streamed_response_wrapper(
            supported_vs_currencies.get,
        )
