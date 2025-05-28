# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

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
from ....types.onchain.networks import trending_pool_get_params, trending_pool_get_network_params
from ....types.onchain.networks.trending_pool_get_response import TrendingPoolGetResponse
from ....types.onchain.networks.trending_pool_get_network_response import TrendingPoolGetNetworkResponse

__all__ = ["TrendingPoolsResource", "AsyncTrendingPoolsResource"]


class TrendingPoolsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TrendingPoolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return TrendingPoolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TrendingPoolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return TrendingPoolsResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        duration: Literal["5m", "1h", "6h", "24h"] | NotGiven = NOT_GIVEN,
        include: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrendingPoolGetResponse:
        """
        This endpoint allows you to **query all the trending pools across all networks
        on GeckoTerminal**

        Args:
          duration: duration to sort trending list by Default value: 24h

          include: attributes to include, comma-separated if more than one to include Available
              values: `base_token`, `quote_token`, `dex`, `network`. Example: `base_token` or
              `base_token,dex`

          page: page through results Default value: 1

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/onchain/networks/trending_pools",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "duration": duration,
                        "include": include,
                        "page": page,
                    },
                    trending_pool_get_params.TrendingPoolGetParams,
                ),
            ),
            cast_to=TrendingPoolGetResponse,
        )

    def get_network(
        self,
        network: str,
        *,
        duration: Literal["5m", "1h", "6h", "24h"] | NotGiven = NOT_GIVEN,
        include: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrendingPoolGetNetworkResponse:
        """
        This endpoint allows you to **query the trending pools based on the provided
        network**

        Args:
          duration: duration to sort trending list by Default value: 24h

          include: attributes to include, comma-separated if more than one to include Available
              values: `base_token`, `quote_token`, `dex`

          page: page through results Default value: 1

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not network:
            raise ValueError(f"Expected a non-empty value for `network` but received {network!r}")
        return self._get(
            f"/onchain/networks/{network}/trending_pools",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "duration": duration,
                        "include": include,
                        "page": page,
                    },
                    trending_pool_get_network_params.TrendingPoolGetNetworkParams,
                ),
            ),
            cast_to=TrendingPoolGetNetworkResponse,
        )


class AsyncTrendingPoolsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTrendingPoolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTrendingPoolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTrendingPoolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return AsyncTrendingPoolsResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        duration: Literal["5m", "1h", "6h", "24h"] | NotGiven = NOT_GIVEN,
        include: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrendingPoolGetResponse:
        """
        This endpoint allows you to **query all the trending pools across all networks
        on GeckoTerminal**

        Args:
          duration: duration to sort trending list by Default value: 24h

          include: attributes to include, comma-separated if more than one to include Available
              values: `base_token`, `quote_token`, `dex`, `network`. Example: `base_token` or
              `base_token,dex`

          page: page through results Default value: 1

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/onchain/networks/trending_pools",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "duration": duration,
                        "include": include,
                        "page": page,
                    },
                    trending_pool_get_params.TrendingPoolGetParams,
                ),
            ),
            cast_to=TrendingPoolGetResponse,
        )

    async def get_network(
        self,
        network: str,
        *,
        duration: Literal["5m", "1h", "6h", "24h"] | NotGiven = NOT_GIVEN,
        include: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrendingPoolGetNetworkResponse:
        """
        This endpoint allows you to **query the trending pools based on the provided
        network**

        Args:
          duration: duration to sort trending list by Default value: 24h

          include: attributes to include, comma-separated if more than one to include Available
              values: `base_token`, `quote_token`, `dex`

          page: page through results Default value: 1

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not network:
            raise ValueError(f"Expected a non-empty value for `network` but received {network!r}")
        return await self._get(
            f"/onchain/networks/{network}/trending_pools",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "duration": duration,
                        "include": include,
                        "page": page,
                    },
                    trending_pool_get_network_params.TrendingPoolGetNetworkParams,
                ),
            ),
            cast_to=TrendingPoolGetNetworkResponse,
        )


class TrendingPoolsResourceWithRawResponse:
    def __init__(self, trending_pools: TrendingPoolsResource) -> None:
        self._trending_pools = trending_pools

        self.get = to_raw_response_wrapper(
            trending_pools.get,
        )
        self.get_network = to_raw_response_wrapper(
            trending_pools.get_network,
        )


class AsyncTrendingPoolsResourceWithRawResponse:
    def __init__(self, trending_pools: AsyncTrendingPoolsResource) -> None:
        self._trending_pools = trending_pools

        self.get = async_to_raw_response_wrapper(
            trending_pools.get,
        )
        self.get_network = async_to_raw_response_wrapper(
            trending_pools.get_network,
        )


class TrendingPoolsResourceWithStreamingResponse:
    def __init__(self, trending_pools: TrendingPoolsResource) -> None:
        self._trending_pools = trending_pools

        self.get = to_streamed_response_wrapper(
            trending_pools.get,
        )
        self.get_network = to_streamed_response_wrapper(
            trending_pools.get_network,
        )


class AsyncTrendingPoolsResourceWithStreamingResponse:
    def __init__(self, trending_pools: AsyncTrendingPoolsResource) -> None:
        self._trending_pools = trending_pools

        self.get = async_to_streamed_response_wrapper(
            trending_pools.get,
        )
        self.get_network = async_to_streamed_response_wrapper(
            trending_pools.get_network,
        )
