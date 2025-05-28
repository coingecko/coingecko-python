# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...types import search_get_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from .trending import (
    TrendingResource,
    AsyncTrendingResource,
    TrendingResourceWithRawResponse,
    AsyncTrendingResourceWithRawResponse,
    TrendingResourceWithStreamingResponse,
    AsyncTrendingResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.search_get_response import SearchGetResponse

__all__ = ["SearchResource", "AsyncSearchResource"]


class SearchResource(SyncAPIResource):
    @cached_property
    def trending(self) -> TrendingResource:
        return TrendingResource(self._client)

    @cached_property
    def with_raw_response(self) -> SearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return SearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return SearchResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        query: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SearchGetResponse:
        """
        This endpoint allows you to **search for coins, categories and markets listed on
        CoinGecko**

        Args:
          query: search query

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"query": query}, search_get_params.SearchGetParams),
            ),
            cast_to=SearchGetResponse,
        )


class AsyncSearchResource(AsyncAPIResource):
    @cached_property
    def trending(self) -> AsyncTrendingResource:
        return AsyncTrendingResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return AsyncSearchResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        query: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SearchGetResponse:
        """
        This endpoint allows you to **search for coins, categories and markets listed on
        CoinGecko**

        Args:
          query: search query

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"query": query}, search_get_params.SearchGetParams),
            ),
            cast_to=SearchGetResponse,
        )


class SearchResourceWithRawResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

        self.get = to_raw_response_wrapper(
            search.get,
        )

    @cached_property
    def trending(self) -> TrendingResourceWithRawResponse:
        return TrendingResourceWithRawResponse(self._search.trending)


class AsyncSearchResourceWithRawResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

        self.get = async_to_raw_response_wrapper(
            search.get,
        )

    @cached_property
    def trending(self) -> AsyncTrendingResourceWithRawResponse:
        return AsyncTrendingResourceWithRawResponse(self._search.trending)


class SearchResourceWithStreamingResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

        self.get = to_streamed_response_wrapper(
            search.get,
        )

    @cached_property
    def trending(self) -> TrendingResourceWithStreamingResponse:
        return TrendingResourceWithStreamingResponse(self._search.trending)


class AsyncSearchResourceWithStreamingResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

        self.get = async_to_streamed_response_wrapper(
            search.get,
        )

    @cached_property
    def trending(self) -> AsyncTrendingResourceWithStreamingResponse:
        return AsyncTrendingResourceWithStreamingResponse(self._search.trending)
