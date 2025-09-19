# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ....types.onchain.networks import dex_get_params, dex_get_pools_params
from ....types.onchain.networks.dex_get_response import DexGetResponse
from ....types.onchain.networks.dex_get_pools_response import DexGetPoolsResponse

__all__ = ["DexesResource", "AsyncDexesResource"]


class DexesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DexesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return DexesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DexesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return DexesResourceWithStreamingResponse(self)

    def get(
        self,
        network: str,
        *,
        page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DexGetResponse:
        """
        This endpoint allows you to **query all the supported decentralized exchanges
        (DEXs) based on the provided network on GeckoTerminal**

        Args:
          page: page through results Default value: 1

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not network:
            raise ValueError(f"Expected a non-empty value for `network` but received {network!r}")
        return self._get(
            f"/onchain/networks/{network}/dexes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"page": page}, dex_get_params.DexGetParams),
            ),
            cast_to=DexGetResponse,
        )

    def get_pools(
        self,
        dex: str,
        *,
        network: str,
        include: str | Omit = omit,
        page: int | Omit = omit,
        sort: Literal["h24_tx_count_desc", "h24_volume_usd_desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DexGetPoolsResponse:
        """
        This endpoint allows you to **query all the top pools based on the provided
        network and decentralized exchange (DEX)**

        Args:
          include: attributes to include, comma-separated if more than one to include Available
              values: `base_token`, `quote_token`, `dex`

          page: page through results Default value: 1

          sort: sort the pools by field Default value: h24_tx_count_desc

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not network:
            raise ValueError(f"Expected a non-empty value for `network` but received {network!r}")
        if not dex:
            raise ValueError(f"Expected a non-empty value for `dex` but received {dex!r}")
        return self._get(
            f"/onchain/networks/{network}/dexes/{dex}/pools",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include": include,
                        "page": page,
                        "sort": sort,
                    },
                    dex_get_pools_params.DexGetPoolsParams,
                ),
            ),
            cast_to=DexGetPoolsResponse,
        )


class AsyncDexesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDexesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDexesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDexesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return AsyncDexesResourceWithStreamingResponse(self)

    async def get(
        self,
        network: str,
        *,
        page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DexGetResponse:
        """
        This endpoint allows you to **query all the supported decentralized exchanges
        (DEXs) based on the provided network on GeckoTerminal**

        Args:
          page: page through results Default value: 1

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not network:
            raise ValueError(f"Expected a non-empty value for `network` but received {network!r}")
        return await self._get(
            f"/onchain/networks/{network}/dexes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"page": page}, dex_get_params.DexGetParams),
            ),
            cast_to=DexGetResponse,
        )

    async def get_pools(
        self,
        dex: str,
        *,
        network: str,
        include: str | Omit = omit,
        page: int | Omit = omit,
        sort: Literal["h24_tx_count_desc", "h24_volume_usd_desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DexGetPoolsResponse:
        """
        This endpoint allows you to **query all the top pools based on the provided
        network and decentralized exchange (DEX)**

        Args:
          include: attributes to include, comma-separated if more than one to include Available
              values: `base_token`, `quote_token`, `dex`

          page: page through results Default value: 1

          sort: sort the pools by field Default value: h24_tx_count_desc

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not network:
            raise ValueError(f"Expected a non-empty value for `network` but received {network!r}")
        if not dex:
            raise ValueError(f"Expected a non-empty value for `dex` but received {dex!r}")
        return await self._get(
            f"/onchain/networks/{network}/dexes/{dex}/pools",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "include": include,
                        "page": page,
                        "sort": sort,
                    },
                    dex_get_pools_params.DexGetPoolsParams,
                ),
            ),
            cast_to=DexGetPoolsResponse,
        )


class DexesResourceWithRawResponse:
    def __init__(self, dexes: DexesResource) -> None:
        self._dexes = dexes

        self.get = to_raw_response_wrapper(
            dexes.get,
        )
        self.get_pools = to_raw_response_wrapper(
            dexes.get_pools,
        )


class AsyncDexesResourceWithRawResponse:
    def __init__(self, dexes: AsyncDexesResource) -> None:
        self._dexes = dexes

        self.get = async_to_raw_response_wrapper(
            dexes.get,
        )
        self.get_pools = async_to_raw_response_wrapper(
            dexes.get_pools,
        )


class DexesResourceWithStreamingResponse:
    def __init__(self, dexes: DexesResource) -> None:
        self._dexes = dexes

        self.get = to_streamed_response_wrapper(
            dexes.get,
        )
        self.get_pools = to_streamed_response_wrapper(
            dexes.get_pools,
        )


class AsyncDexesResourceWithStreamingResponse:
    def __init__(self, dexes: AsyncDexesResource) -> None:
        self._dexes = dexes

        self.get = async_to_streamed_response_wrapper(
            dexes.get,
        )
        self.get_pools = async_to_streamed_response_wrapper(
            dexes.get_pools,
        )
