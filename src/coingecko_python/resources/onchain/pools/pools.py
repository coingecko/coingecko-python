# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._compat import cached_property
from .megafilter import (
    MegafilterResource,
    AsyncMegafilterResource,
    MegafilterResourceWithRawResponse,
    AsyncMegafilterResourceWithRawResponse,
    MegafilterResourceWithStreamingResponse,
    AsyncMegafilterResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from .trending_search import (
    TrendingSearchResource,
    AsyncTrendingSearchResource,
    TrendingSearchResourceWithRawResponse,
    AsyncTrendingSearchResourceWithRawResponse,
    TrendingSearchResourceWithStreamingResponse,
    AsyncTrendingSearchResourceWithStreamingResponse,
)

__all__ = ["PoolsResource", "AsyncPoolsResource"]


class PoolsResource(SyncAPIResource):
    @cached_property
    def megafilter(self) -> MegafilterResource:
        return MegafilterResource(self._client)

    @cached_property
    def trending_search(self) -> TrendingSearchResource:
        return TrendingSearchResource(self._client)

    @cached_property
    def with_raw_response(self) -> PoolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return PoolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PoolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return PoolsResourceWithStreamingResponse(self)


class AsyncPoolsResource(AsyncAPIResource):
    @cached_property
    def megafilter(self) -> AsyncMegafilterResource:
        return AsyncMegafilterResource(self._client)

    @cached_property
    def trending_search(self) -> AsyncTrendingSearchResource:
        return AsyncTrendingSearchResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPoolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPoolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPoolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return AsyncPoolsResourceWithStreamingResponse(self)


class PoolsResourceWithRawResponse:
    def __init__(self, pools: PoolsResource) -> None:
        self._pools = pools

    @cached_property
    def megafilter(self) -> MegafilterResourceWithRawResponse:
        return MegafilterResourceWithRawResponse(self._pools.megafilter)

    @cached_property
    def trending_search(self) -> TrendingSearchResourceWithRawResponse:
        return TrendingSearchResourceWithRawResponse(self._pools.trending_search)


class AsyncPoolsResourceWithRawResponse:
    def __init__(self, pools: AsyncPoolsResource) -> None:
        self._pools = pools

    @cached_property
    def megafilter(self) -> AsyncMegafilterResourceWithRawResponse:
        return AsyncMegafilterResourceWithRawResponse(self._pools.megafilter)

    @cached_property
    def trending_search(self) -> AsyncTrendingSearchResourceWithRawResponse:
        return AsyncTrendingSearchResourceWithRawResponse(self._pools.trending_search)


class PoolsResourceWithStreamingResponse:
    def __init__(self, pools: PoolsResource) -> None:
        self._pools = pools

    @cached_property
    def megafilter(self) -> MegafilterResourceWithStreamingResponse:
        return MegafilterResourceWithStreamingResponse(self._pools.megafilter)

    @cached_property
    def trending_search(self) -> TrendingSearchResourceWithStreamingResponse:
        return TrendingSearchResourceWithStreamingResponse(self._pools.trending_search)


class AsyncPoolsResourceWithStreamingResponse:
    def __init__(self, pools: AsyncPoolsResource) -> None:
        self._pools = pools

    @cached_property
    def megafilter(self) -> AsyncMegafilterResourceWithStreamingResponse:
        return AsyncMegafilterResourceWithStreamingResponse(self._pools.megafilter)

    @cached_property
    def trending_search(self) -> AsyncTrendingSearchResourceWithStreamingResponse:
        return AsyncTrendingSearchResourceWithStreamingResponse(self._pools.trending_search)
