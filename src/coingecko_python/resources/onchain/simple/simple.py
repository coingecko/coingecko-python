# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .networks.networks import (
    NetworksResource,
    AsyncNetworksResource,
    NetworksResourceWithRawResponse,
    AsyncNetworksResourceWithRawResponse,
    NetworksResourceWithStreamingResponse,
    AsyncNetworksResourceWithStreamingResponse,
)

__all__ = ["SimpleResource", "AsyncSimpleResource"]


class SimpleResource(SyncAPIResource):
    @cached_property
    def networks(self) -> NetworksResource:
        return NetworksResource(self._client)

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
    def networks(self) -> AsyncNetworksResource:
        return AsyncNetworksResource(self._client)

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
    def networks(self) -> NetworksResourceWithRawResponse:
        return NetworksResourceWithRawResponse(self._simple.networks)


class AsyncSimpleResourceWithRawResponse:
    def __init__(self, simple: AsyncSimpleResource) -> None:
        self._simple = simple

    @cached_property
    def networks(self) -> AsyncNetworksResourceWithRawResponse:
        return AsyncNetworksResourceWithRawResponse(self._simple.networks)


class SimpleResourceWithStreamingResponse:
    def __init__(self, simple: SimpleResource) -> None:
        self._simple = simple

    @cached_property
    def networks(self) -> NetworksResourceWithStreamingResponse:
        return NetworksResourceWithStreamingResponse(self._simple.networks)


class AsyncSimpleResourceWithStreamingResponse:
    def __init__(self, simple: AsyncSimpleResource) -> None:
        self._simple = simple

    @cached_property
    def networks(self) -> AsyncNetworksResourceWithStreamingResponse:
        return AsyncNetworksResourceWithStreamingResponse(self._simple.networks)
