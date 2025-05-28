# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.onchain.pools import trending_search_get_params
from ....types.onchain.pools.trending_search_get_response import TrendingSearchGetResponse

__all__ = ["TrendingSearchResource", "AsyncTrendingSearchResource"]


class TrendingSearchResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TrendingSearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return TrendingSearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TrendingSearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return TrendingSearchResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        include: str | NotGiven = NOT_GIVEN,
        pools: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrendingSearchGetResponse:
        """
        This endpoint allows you to **query all the trending search pools across all
        networks on GeckoTerminal**

        Args:
          include: attributes to include, comma-separated if more than one to include Available
              values: `base_token`, `quote_token`, `dex`, `network`

          pools: number of pools to return, maximum 10 Default value: 4

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/onchain/pools/trending_search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include": include,
                        "pools": pools,
                    },
                    trending_search_get_params.TrendingSearchGetParams,
                ),
            ),
            cast_to=TrendingSearchGetResponse,
        )


class AsyncTrendingSearchResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTrendingSearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTrendingSearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTrendingSearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return AsyncTrendingSearchResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        include: str | NotGiven = NOT_GIVEN,
        pools: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrendingSearchGetResponse:
        """
        This endpoint allows you to **query all the trending search pools across all
        networks on GeckoTerminal**

        Args:
          include: attributes to include, comma-separated if more than one to include Available
              values: `base_token`, `quote_token`, `dex`, `network`

          pools: number of pools to return, maximum 10 Default value: 4

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/onchain/pools/trending_search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "include": include,
                        "pools": pools,
                    },
                    trending_search_get_params.TrendingSearchGetParams,
                ),
            ),
            cast_to=TrendingSearchGetResponse,
        )


class TrendingSearchResourceWithRawResponse:
    def __init__(self, trending_search: TrendingSearchResource) -> None:
        self._trending_search = trending_search

        self.get = to_raw_response_wrapper(
            trending_search.get,
        )


class AsyncTrendingSearchResourceWithRawResponse:
    def __init__(self, trending_search: AsyncTrendingSearchResource) -> None:
        self._trending_search = trending_search

        self.get = async_to_raw_response_wrapper(
            trending_search.get,
        )


class TrendingSearchResourceWithStreamingResponse:
    def __init__(self, trending_search: TrendingSearchResource) -> None:
        self._trending_search = trending_search

        self.get = to_streamed_response_wrapper(
            trending_search.get,
        )


class AsyncTrendingSearchResourceWithStreamingResponse:
    def __init__(self, trending_search: AsyncTrendingSearchResource) -> None:
        self._trending_search = trending_search

        self.get = async_to_streamed_response_wrapper(
            trending_search.get,
        )
