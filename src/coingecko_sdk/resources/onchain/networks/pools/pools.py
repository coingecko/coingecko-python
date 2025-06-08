# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .info import (
    InfoResource,
    AsyncInfoResource,
    InfoResourceWithRawResponse,
    AsyncInfoResourceWithRawResponse,
    InfoResourceWithStreamingResponse,
    AsyncInfoResourceWithStreamingResponse,
)
from .multi import (
    MultiResource,
    AsyncMultiResource,
    MultiResourceWithRawResponse,
    AsyncMultiResourceWithRawResponse,
    MultiResourceWithStreamingResponse,
    AsyncMultiResourceWithStreamingResponse,
)
from .ohlcv import (
    OhlcvResource,
    AsyncOhlcvResource,
    OhlcvResourceWithRawResponse,
    AsyncOhlcvResourceWithRawResponse,
    OhlcvResourceWithStreamingResponse,
    AsyncOhlcvResourceWithStreamingResponse,
)
from .trades import (
    TradesResource,
    AsyncTradesResource,
    TradesResourceWithRawResponse,
    AsyncTradesResourceWithRawResponse,
    TradesResourceWithStreamingResponse,
    AsyncTradesResourceWithStreamingResponse,
)
from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.onchain.networks import pool_get_params, pool_get_address_params
from .....types.onchain.networks.pool_get_response import PoolGetResponse
from .....types.onchain.networks.pool_get_address_response import PoolGetAddressResponse

__all__ = ["PoolsResource", "AsyncPoolsResource"]


class PoolsResource(SyncAPIResource):
    @cached_property
    def multi(self) -> MultiResource:
        return MultiResource(self._client)

    @cached_property
    def info(self) -> InfoResource:
        return InfoResource(self._client)

    @cached_property
    def ohlcv(self) -> OhlcvResource:
        return OhlcvResource(self._client)

    @cached_property
    def trades(self) -> TradesResource:
        return TradesResource(self._client)

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

    def get(
        self,
        network: str,
        *,
        include: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        sort: Literal["h24_tx_count_desc", "h24_volume_usd_desc"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PoolGetResponse:
        """
        This endpoint allows you to **query all the top pools based on the provided
        network**

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
        return self._get(
            f"/onchain/networks/{network}/pools",
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
                    pool_get_params.PoolGetParams,
                ),
            ),
            cast_to=PoolGetResponse,
        )

    def get_address(
        self,
        address: str,
        *,
        network: str,
        include: str | NotGiven = NOT_GIVEN,
        include_volume_breakdown: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PoolGetAddressResponse:
        """
        This endpoint allows you to **query the specific pool based on the provided
        network and pool address**

        Args:
          include: attributes to include, comma-separated if more than one to include Available
              values: `base_token`, `quote_token`, `dex`

          include_volume_breakdown: include volume breakdown, default: false

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not network:
            raise ValueError(f"Expected a non-empty value for `network` but received {network!r}")
        if not address:
            raise ValueError(f"Expected a non-empty value for `address` but received {address!r}")
        return self._get(
            f"/onchain/networks/{network}/pools/{address}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include": include,
                        "include_volume_breakdown": include_volume_breakdown,
                    },
                    pool_get_address_params.PoolGetAddressParams,
                ),
            ),
            cast_to=PoolGetAddressResponse,
        )


class AsyncPoolsResource(AsyncAPIResource):
    @cached_property
    def multi(self) -> AsyncMultiResource:
        return AsyncMultiResource(self._client)

    @cached_property
    def info(self) -> AsyncInfoResource:
        return AsyncInfoResource(self._client)

    @cached_property
    def ohlcv(self) -> AsyncOhlcvResource:
        return AsyncOhlcvResource(self._client)

    @cached_property
    def trades(self) -> AsyncTradesResource:
        return AsyncTradesResource(self._client)

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

    async def get(
        self,
        network: str,
        *,
        include: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        sort: Literal["h24_tx_count_desc", "h24_volume_usd_desc"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PoolGetResponse:
        """
        This endpoint allows you to **query all the top pools based on the provided
        network**

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
        return await self._get(
            f"/onchain/networks/{network}/pools",
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
                    pool_get_params.PoolGetParams,
                ),
            ),
            cast_to=PoolGetResponse,
        )

    async def get_address(
        self,
        address: str,
        *,
        network: str,
        include: str | NotGiven = NOT_GIVEN,
        include_volume_breakdown: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PoolGetAddressResponse:
        """
        This endpoint allows you to **query the specific pool based on the provided
        network and pool address**

        Args:
          include: attributes to include, comma-separated if more than one to include Available
              values: `base_token`, `quote_token`, `dex`

          include_volume_breakdown: include volume breakdown, default: false

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not network:
            raise ValueError(f"Expected a non-empty value for `network` but received {network!r}")
        if not address:
            raise ValueError(f"Expected a non-empty value for `address` but received {address!r}")
        return await self._get(
            f"/onchain/networks/{network}/pools/{address}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "include": include,
                        "include_volume_breakdown": include_volume_breakdown,
                    },
                    pool_get_address_params.PoolGetAddressParams,
                ),
            ),
            cast_to=PoolGetAddressResponse,
        )


class PoolsResourceWithRawResponse:
    def __init__(self, pools: PoolsResource) -> None:
        self._pools = pools

        self.get = to_raw_response_wrapper(
            pools.get,
        )
        self.get_address = to_raw_response_wrapper(
            pools.get_address,
        )

    @cached_property
    def multi(self) -> MultiResourceWithRawResponse:
        return MultiResourceWithRawResponse(self._pools.multi)

    @cached_property
    def info(self) -> InfoResourceWithRawResponse:
        return InfoResourceWithRawResponse(self._pools.info)

    @cached_property
    def ohlcv(self) -> OhlcvResourceWithRawResponse:
        return OhlcvResourceWithRawResponse(self._pools.ohlcv)

    @cached_property
    def trades(self) -> TradesResourceWithRawResponse:
        return TradesResourceWithRawResponse(self._pools.trades)


class AsyncPoolsResourceWithRawResponse:
    def __init__(self, pools: AsyncPoolsResource) -> None:
        self._pools = pools

        self.get = async_to_raw_response_wrapper(
            pools.get,
        )
        self.get_address = async_to_raw_response_wrapper(
            pools.get_address,
        )

    @cached_property
    def multi(self) -> AsyncMultiResourceWithRawResponse:
        return AsyncMultiResourceWithRawResponse(self._pools.multi)

    @cached_property
    def info(self) -> AsyncInfoResourceWithRawResponse:
        return AsyncInfoResourceWithRawResponse(self._pools.info)

    @cached_property
    def ohlcv(self) -> AsyncOhlcvResourceWithRawResponse:
        return AsyncOhlcvResourceWithRawResponse(self._pools.ohlcv)

    @cached_property
    def trades(self) -> AsyncTradesResourceWithRawResponse:
        return AsyncTradesResourceWithRawResponse(self._pools.trades)


class PoolsResourceWithStreamingResponse:
    def __init__(self, pools: PoolsResource) -> None:
        self._pools = pools

        self.get = to_streamed_response_wrapper(
            pools.get,
        )
        self.get_address = to_streamed_response_wrapper(
            pools.get_address,
        )

    @cached_property
    def multi(self) -> MultiResourceWithStreamingResponse:
        return MultiResourceWithStreamingResponse(self._pools.multi)

    @cached_property
    def info(self) -> InfoResourceWithStreamingResponse:
        return InfoResourceWithStreamingResponse(self._pools.info)

    @cached_property
    def ohlcv(self) -> OhlcvResourceWithStreamingResponse:
        return OhlcvResourceWithStreamingResponse(self._pools.ohlcv)

    @cached_property
    def trades(self) -> TradesResourceWithStreamingResponse:
        return TradesResourceWithStreamingResponse(self._pools.trades)


class AsyncPoolsResourceWithStreamingResponse:
    def __init__(self, pools: AsyncPoolsResource) -> None:
        self._pools = pools

        self.get = async_to_streamed_response_wrapper(
            pools.get,
        )
        self.get_address = async_to_streamed_response_wrapper(
            pools.get_address,
        )

    @cached_property
    def multi(self) -> AsyncMultiResourceWithStreamingResponse:
        return AsyncMultiResourceWithStreamingResponse(self._pools.multi)

    @cached_property
    def info(self) -> AsyncInfoResourceWithStreamingResponse:
        return AsyncInfoResourceWithStreamingResponse(self._pools.info)

    @cached_property
    def ohlcv(self) -> AsyncOhlcvResourceWithStreamingResponse:
        return AsyncOhlcvResourceWithStreamingResponse(self._pools.ohlcv)

    @cached_property
    def trades(self) -> AsyncTradesResourceWithStreamingResponse:
        return AsyncTradesResourceWithStreamingResponse(self._pools.trades)
