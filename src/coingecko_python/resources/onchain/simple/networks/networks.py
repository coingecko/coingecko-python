# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ....._compat import cached_property
from .token_price import (
    TokenPriceResource,
    AsyncTokenPriceResource,
    TokenPriceResourceWithRawResponse,
    AsyncTokenPriceResourceWithRawResponse,
    TokenPriceResourceWithStreamingResponse,
    AsyncTokenPriceResourceWithStreamingResponse,
)
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["NetworksResource", "AsyncNetworksResource"]


class NetworksResource(SyncAPIResource):
    @cached_property
    def token_price(self) -> TokenPriceResource:
        return TokenPriceResource(self._client)

    @cached_property
    def with_raw_response(self) -> NetworksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return NetworksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NetworksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return NetworksResourceWithStreamingResponse(self)


class AsyncNetworksResource(AsyncAPIResource):
    @cached_property
    def token_price(self) -> AsyncTokenPriceResource:
        return AsyncTokenPriceResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncNetworksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNetworksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNetworksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return AsyncNetworksResourceWithStreamingResponse(self)


class NetworksResourceWithRawResponse:
    def __init__(self, networks: NetworksResource) -> None:
        self._networks = networks

    @cached_property
    def token_price(self) -> TokenPriceResourceWithRawResponse:
        return TokenPriceResourceWithRawResponse(self._networks.token_price)


class AsyncNetworksResourceWithRawResponse:
    def __init__(self, networks: AsyncNetworksResource) -> None:
        self._networks = networks

    @cached_property
    def token_price(self) -> AsyncTokenPriceResourceWithRawResponse:
        return AsyncTokenPriceResourceWithRawResponse(self._networks.token_price)


class NetworksResourceWithStreamingResponse:
    def __init__(self, networks: NetworksResource) -> None:
        self._networks = networks

    @cached_property
    def token_price(self) -> TokenPriceResourceWithStreamingResponse:
        return TokenPriceResourceWithStreamingResponse(self._networks.token_price)


class AsyncNetworksResourceWithStreamingResponse:
    def __init__(self, networks: AsyncNetworksResource) -> None:
        self._networks = networks

    @cached_property
    def token_price(self) -> AsyncTokenPriceResourceWithStreamingResponse:
        return AsyncTokenPriceResourceWithStreamingResponse(self._networks.token_price)
