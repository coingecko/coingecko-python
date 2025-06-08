# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .price import (
    PriceResource,
    AsyncPriceResource,
    PriceResourceWithRawResponse,
    AsyncPriceResourceWithRawResponse,
    PriceResourceWithStreamingResponse,
    AsyncPriceResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .token_price import (
    TokenPriceResource,
    AsyncTokenPriceResource,
    TokenPriceResourceWithRawResponse,
    AsyncTokenPriceResourceWithRawResponse,
    TokenPriceResourceWithStreamingResponse,
    AsyncTokenPriceResourceWithStreamingResponse,
)
from .supported_vs_currencies import (
    SupportedVsCurrenciesResource,
    AsyncSupportedVsCurrenciesResource,
    SupportedVsCurrenciesResourceWithRawResponse,
    AsyncSupportedVsCurrenciesResourceWithRawResponse,
    SupportedVsCurrenciesResourceWithStreamingResponse,
    AsyncSupportedVsCurrenciesResourceWithStreamingResponse,
)

__all__ = ["SimpleResource", "AsyncSimpleResource"]


class SimpleResource(SyncAPIResource):
    @cached_property
    def price(self) -> PriceResource:
        return PriceResource(self._client)

    @cached_property
    def supported_vs_currencies(self) -> SupportedVsCurrenciesResource:
        return SupportedVsCurrenciesResource(self._client)

    @cached_property
    def token_price(self) -> TokenPriceResource:
        return TokenPriceResource(self._client)

    @cached_property
    def with_raw_response(self) -> SimpleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return SimpleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SimpleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return SimpleResourceWithStreamingResponse(self)


class AsyncSimpleResource(AsyncAPIResource):
    @cached_property
    def price(self) -> AsyncPriceResource:
        return AsyncPriceResource(self._client)

    @cached_property
    def supported_vs_currencies(self) -> AsyncSupportedVsCurrenciesResource:
        return AsyncSupportedVsCurrenciesResource(self._client)

    @cached_property
    def token_price(self) -> AsyncTokenPriceResource:
        return AsyncTokenPriceResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSimpleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSimpleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSimpleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return AsyncSimpleResourceWithStreamingResponse(self)


class SimpleResourceWithRawResponse:
    def __init__(self, simple: SimpleResource) -> None:
        self._simple = simple

    @cached_property
    def price(self) -> PriceResourceWithRawResponse:
        return PriceResourceWithRawResponse(self._simple.price)

    @cached_property
    def supported_vs_currencies(self) -> SupportedVsCurrenciesResourceWithRawResponse:
        return SupportedVsCurrenciesResourceWithRawResponse(self._simple.supported_vs_currencies)

    @cached_property
    def token_price(self) -> TokenPriceResourceWithRawResponse:
        return TokenPriceResourceWithRawResponse(self._simple.token_price)


class AsyncSimpleResourceWithRawResponse:
    def __init__(self, simple: AsyncSimpleResource) -> None:
        self._simple = simple

    @cached_property
    def price(self) -> AsyncPriceResourceWithRawResponse:
        return AsyncPriceResourceWithRawResponse(self._simple.price)

    @cached_property
    def supported_vs_currencies(self) -> AsyncSupportedVsCurrenciesResourceWithRawResponse:
        return AsyncSupportedVsCurrenciesResourceWithRawResponse(self._simple.supported_vs_currencies)

    @cached_property
    def token_price(self) -> AsyncTokenPriceResourceWithRawResponse:
        return AsyncTokenPriceResourceWithRawResponse(self._simple.token_price)


class SimpleResourceWithStreamingResponse:
    def __init__(self, simple: SimpleResource) -> None:
        self._simple = simple

    @cached_property
    def price(self) -> PriceResourceWithStreamingResponse:
        return PriceResourceWithStreamingResponse(self._simple.price)

    @cached_property
    def supported_vs_currencies(self) -> SupportedVsCurrenciesResourceWithStreamingResponse:
        return SupportedVsCurrenciesResourceWithStreamingResponse(self._simple.supported_vs_currencies)

    @cached_property
    def token_price(self) -> TokenPriceResourceWithStreamingResponse:
        return TokenPriceResourceWithStreamingResponse(self._simple.token_price)


class AsyncSimpleResourceWithStreamingResponse:
    def __init__(self, simple: AsyncSimpleResource) -> None:
        self._simple = simple

    @cached_property
    def price(self) -> AsyncPriceResourceWithStreamingResponse:
        return AsyncPriceResourceWithStreamingResponse(self._simple.price)

    @cached_property
    def supported_vs_currencies(self) -> AsyncSupportedVsCurrenciesResourceWithStreamingResponse:
        return AsyncSupportedVsCurrenciesResourceWithStreamingResponse(self._simple.supported_vs_currencies)

    @cached_property
    def token_price(self) -> AsyncTokenPriceResourceWithStreamingResponse:
        return AsyncTokenPriceResourceWithStreamingResponse(self._simple.token_price)
