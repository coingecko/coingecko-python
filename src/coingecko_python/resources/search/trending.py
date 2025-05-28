# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...types.search import trending_get_params
from ...types.search.trending_get_response import TrendingGetResponse

__all__ = ["TrendingResource", "AsyncTrendingResource"]


class TrendingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TrendingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return TrendingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TrendingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return TrendingResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        show_max: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrendingGetResponse:
        """
        This endpoint allows you **query trending search coins, NFTs and categories on
        CoinGecko in the last 24 hours**

        Args:
          show_max:
              show max number of results available for the given type Available values:
              `coins`, `nfts`, `categories` Example: `coins` or `coins,nfts,categories`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/search/trending",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"show_max": show_max}, trending_get_params.TrendingGetParams),
            ),
            cast_to=TrendingGetResponse,
        )


class AsyncTrendingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTrendingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTrendingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTrendingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return AsyncTrendingResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        show_max: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrendingGetResponse:
        """
        This endpoint allows you **query trending search coins, NFTs and categories on
        CoinGecko in the last 24 hours**

        Args:
          show_max:
              show max number of results available for the given type Available values:
              `coins`, `nfts`, `categories` Example: `coins` or `coins,nfts,categories`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/search/trending",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"show_max": show_max}, trending_get_params.TrendingGetParams),
            ),
            cast_to=TrendingGetResponse,
        )


class TrendingResourceWithRawResponse:
    def __init__(self, trending: TrendingResource) -> None:
        self._trending = trending

        self.get = to_raw_response_wrapper(
            trending.get,
        )


class AsyncTrendingResourceWithRawResponse:
    def __init__(self, trending: AsyncTrendingResource) -> None:
        self._trending = trending

        self.get = async_to_raw_response_wrapper(
            trending.get,
        )


class TrendingResourceWithStreamingResponse:
    def __init__(self, trending: TrendingResource) -> None:
        self._trending = trending

        self.get = to_streamed_response_wrapper(
            trending.get,
        )


class AsyncTrendingResourceWithStreamingResponse:
    def __init__(self, trending: AsyncTrendingResource) -> None:
        self._trending = trending

        self.get = async_to_streamed_response_wrapper(
            trending.get,
        )
