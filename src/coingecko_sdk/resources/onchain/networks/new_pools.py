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
from ....types.onchain.networks import new_pool_get_params, new_pool_get_network_params
from ....types.onchain.networks.new_pool_get_response import NewPoolGetResponse
from ....types.onchain.networks.new_pool_get_network_response import NewPoolGetNetworkResponse

__all__ = ["NewPoolsResource", "AsyncNewPoolsResource"]


class NewPoolsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NewPoolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return NewPoolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NewPoolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return NewPoolsResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        include: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NewPoolGetResponse:
        """
        This endpoint allows you to **query all the latest pools across all networks on
        GeckoTerminal**

        Args:
          include: attributes to include, comma-separated if more than one to include Available
              values: `base_token`, `quote_token`, `dex`, `network`

          page: page through results Default value: 1

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/onchain/networks/new_pools",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include": include,
                        "page": page,
                    },
                    new_pool_get_params.NewPoolGetParams,
                ),
            ),
            cast_to=NewPoolGetResponse,
        )

    def get_network(
        self,
        network: str,
        *,
        include: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NewPoolGetNetworkResponse:
        """
        This endpoint allows you to **query all the latest pools based on provided
        network**

        Args:
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
            f"/onchain/networks/{network}/new_pools",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include": include,
                        "page": page,
                    },
                    new_pool_get_network_params.NewPoolGetNetworkParams,
                ),
            ),
            cast_to=NewPoolGetNetworkResponse,
        )


class AsyncNewPoolsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNewPoolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNewPoolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNewPoolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return AsyncNewPoolsResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        include: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NewPoolGetResponse:
        """
        This endpoint allows you to **query all the latest pools across all networks on
        GeckoTerminal**

        Args:
          include: attributes to include, comma-separated if more than one to include Available
              values: `base_token`, `quote_token`, `dex`, `network`

          page: page through results Default value: 1

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/onchain/networks/new_pools",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "include": include,
                        "page": page,
                    },
                    new_pool_get_params.NewPoolGetParams,
                ),
            ),
            cast_to=NewPoolGetResponse,
        )

    async def get_network(
        self,
        network: str,
        *,
        include: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NewPoolGetNetworkResponse:
        """
        This endpoint allows you to **query all the latest pools based on provided
        network**

        Args:
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
            f"/onchain/networks/{network}/new_pools",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "include": include,
                        "page": page,
                    },
                    new_pool_get_network_params.NewPoolGetNetworkParams,
                ),
            ),
            cast_to=NewPoolGetNetworkResponse,
        )


class NewPoolsResourceWithRawResponse:
    def __init__(self, new_pools: NewPoolsResource) -> None:
        self._new_pools = new_pools

        self.get = to_raw_response_wrapper(
            new_pools.get,
        )
        self.get_network = to_raw_response_wrapper(
            new_pools.get_network,
        )


class AsyncNewPoolsResourceWithRawResponse:
    def __init__(self, new_pools: AsyncNewPoolsResource) -> None:
        self._new_pools = new_pools

        self.get = async_to_raw_response_wrapper(
            new_pools.get,
        )
        self.get_network = async_to_raw_response_wrapper(
            new_pools.get_network,
        )


class NewPoolsResourceWithStreamingResponse:
    def __init__(self, new_pools: NewPoolsResource) -> None:
        self._new_pools = new_pools

        self.get = to_streamed_response_wrapper(
            new_pools.get,
        )
        self.get_network = to_streamed_response_wrapper(
            new_pools.get_network,
        )


class AsyncNewPoolsResourceWithStreamingResponse:
    def __init__(self, new_pools: AsyncNewPoolsResource) -> None:
        self._new_pools = new_pools

        self.get = async_to_streamed_response_wrapper(
            new_pools.get,
        )
        self.get_network = async_to_streamed_response_wrapper(
            new_pools.get_network,
        )
