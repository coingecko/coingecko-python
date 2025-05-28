# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .dexes import (
    DexesResource,
    AsyncDexesResource,
    DexesResourceWithRawResponse,
    AsyncDexesResourceWithRawResponse,
    DexesResourceWithStreamingResponse,
    AsyncDexesResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform, async_maybe_transform
from .new_pools import (
    NewPoolsResource,
    AsyncNewPoolsResource,
    NewPoolsResourceWithRawResponse,
    AsyncNewPoolsResourceWithRawResponse,
    NewPoolsResourceWithStreamingResponse,
    AsyncNewPoolsResourceWithStreamingResponse,
)
from ...._compat import cached_property
from .pools.pools import (
    PoolsResource,
    AsyncPoolsResource,
    PoolsResourceWithRawResponse,
    AsyncPoolsResourceWithRawResponse,
    PoolsResourceWithStreamingResponse,
    AsyncPoolsResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .tokens.tokens import (
    TokensResource,
    AsyncTokensResource,
    TokensResourceWithRawResponse,
    AsyncTokensResourceWithRawResponse,
    TokensResourceWithStreamingResponse,
    AsyncTokensResourceWithStreamingResponse,
)
from .trending_pools import (
    TrendingPoolsResource,
    AsyncTrendingPoolsResource,
    TrendingPoolsResourceWithRawResponse,
    AsyncTrendingPoolsResourceWithRawResponse,
    TrendingPoolsResourceWithStreamingResponse,
    AsyncTrendingPoolsResourceWithStreamingResponse,
)
from ...._base_client import make_request_options
from ....types.onchain import network_get_params
from ....types.onchain.network_get_response import NetworkGetResponse

__all__ = ["NetworksResource", "AsyncNetworksResource"]


class NetworksResource(SyncAPIResource):
    @cached_property
    def new_pools(self) -> NewPoolsResource:
        return NewPoolsResource(self._client)

    @cached_property
    def trending_pools(self) -> TrendingPoolsResource:
        return TrendingPoolsResource(self._client)

    @cached_property
    def dexes(self) -> DexesResource:
        return DexesResource(self._client)

    @cached_property
    def pools(self) -> PoolsResource:
        return PoolsResource(self._client)

    @cached_property
    def tokens(self) -> TokensResource:
        return TokensResource(self._client)

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

    def get(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NetworkGetResponse:
        """
        This endpoint allows you to **query all the supported networks on
        GeckoTerminal**

        Args:
          page: page through results Default value: 1

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/onchain/networks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"page": page}, network_get_params.NetworkGetParams),
            ),
            cast_to=NetworkGetResponse,
        )


class AsyncNetworksResource(AsyncAPIResource):
    @cached_property
    def new_pools(self) -> AsyncNewPoolsResource:
        return AsyncNewPoolsResource(self._client)

    @cached_property
    def trending_pools(self) -> AsyncTrendingPoolsResource:
        return AsyncTrendingPoolsResource(self._client)

    @cached_property
    def dexes(self) -> AsyncDexesResource:
        return AsyncDexesResource(self._client)

    @cached_property
    def pools(self) -> AsyncPoolsResource:
        return AsyncPoolsResource(self._client)

    @cached_property
    def tokens(self) -> AsyncTokensResource:
        return AsyncTokensResource(self._client)

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

    async def get(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NetworkGetResponse:
        """
        This endpoint allows you to **query all the supported networks on
        GeckoTerminal**

        Args:
          page: page through results Default value: 1

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/onchain/networks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"page": page}, network_get_params.NetworkGetParams),
            ),
            cast_to=NetworkGetResponse,
        )


class NetworksResourceWithRawResponse:
    def __init__(self, networks: NetworksResource) -> None:
        self._networks = networks

        self.get = to_raw_response_wrapper(
            networks.get,
        )

    @cached_property
    def new_pools(self) -> NewPoolsResourceWithRawResponse:
        return NewPoolsResourceWithRawResponse(self._networks.new_pools)

    @cached_property
    def trending_pools(self) -> TrendingPoolsResourceWithRawResponse:
        return TrendingPoolsResourceWithRawResponse(self._networks.trending_pools)

    @cached_property
    def dexes(self) -> DexesResourceWithRawResponse:
        return DexesResourceWithRawResponse(self._networks.dexes)

    @cached_property
    def pools(self) -> PoolsResourceWithRawResponse:
        return PoolsResourceWithRawResponse(self._networks.pools)

    @cached_property
    def tokens(self) -> TokensResourceWithRawResponse:
        return TokensResourceWithRawResponse(self._networks.tokens)


class AsyncNetworksResourceWithRawResponse:
    def __init__(self, networks: AsyncNetworksResource) -> None:
        self._networks = networks

        self.get = async_to_raw_response_wrapper(
            networks.get,
        )

    @cached_property
    def new_pools(self) -> AsyncNewPoolsResourceWithRawResponse:
        return AsyncNewPoolsResourceWithRawResponse(self._networks.new_pools)

    @cached_property
    def trending_pools(self) -> AsyncTrendingPoolsResourceWithRawResponse:
        return AsyncTrendingPoolsResourceWithRawResponse(self._networks.trending_pools)

    @cached_property
    def dexes(self) -> AsyncDexesResourceWithRawResponse:
        return AsyncDexesResourceWithRawResponse(self._networks.dexes)

    @cached_property
    def pools(self) -> AsyncPoolsResourceWithRawResponse:
        return AsyncPoolsResourceWithRawResponse(self._networks.pools)

    @cached_property
    def tokens(self) -> AsyncTokensResourceWithRawResponse:
        return AsyncTokensResourceWithRawResponse(self._networks.tokens)


class NetworksResourceWithStreamingResponse:
    def __init__(self, networks: NetworksResource) -> None:
        self._networks = networks

        self.get = to_streamed_response_wrapper(
            networks.get,
        )

    @cached_property
    def new_pools(self) -> NewPoolsResourceWithStreamingResponse:
        return NewPoolsResourceWithStreamingResponse(self._networks.new_pools)

    @cached_property
    def trending_pools(self) -> TrendingPoolsResourceWithStreamingResponse:
        return TrendingPoolsResourceWithStreamingResponse(self._networks.trending_pools)

    @cached_property
    def dexes(self) -> DexesResourceWithStreamingResponse:
        return DexesResourceWithStreamingResponse(self._networks.dexes)

    @cached_property
    def pools(self) -> PoolsResourceWithStreamingResponse:
        return PoolsResourceWithStreamingResponse(self._networks.pools)

    @cached_property
    def tokens(self) -> TokensResourceWithStreamingResponse:
        return TokensResourceWithStreamingResponse(self._networks.tokens)


class AsyncNetworksResourceWithStreamingResponse:
    def __init__(self, networks: AsyncNetworksResource) -> None:
        self._networks = networks

        self.get = async_to_streamed_response_wrapper(
            networks.get,
        )

    @cached_property
    def new_pools(self) -> AsyncNewPoolsResourceWithStreamingResponse:
        return AsyncNewPoolsResourceWithStreamingResponse(self._networks.new_pools)

    @cached_property
    def trending_pools(self) -> AsyncTrendingPoolsResourceWithStreamingResponse:
        return AsyncTrendingPoolsResourceWithStreamingResponse(self._networks.trending_pools)

    @cached_property
    def dexes(self) -> AsyncDexesResourceWithStreamingResponse:
        return AsyncDexesResourceWithStreamingResponse(self._networks.dexes)

    @cached_property
    def pools(self) -> AsyncPoolsResourceWithStreamingResponse:
        return AsyncPoolsResourceWithStreamingResponse(self._networks.pools)

    @cached_property
    def tokens(self) -> AsyncTokensResourceWithStreamingResponse:
        return AsyncTokensResourceWithStreamingResponse(self._networks.tokens)
