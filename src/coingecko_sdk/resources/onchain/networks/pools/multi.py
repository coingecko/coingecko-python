# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

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
from .....types.onchain.networks.pools import multi_get_addresses_params
from .....types.onchain.networks.pools.multi_get_addresses_response import MultiGetAddressesResponse

__all__ = ["MultiResource", "AsyncMultiResource"]


class MultiResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MultiResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return MultiResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MultiResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return MultiResourceWithStreamingResponse(self)

    def get_addresses(
        self,
        addresses: str,
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
    ) -> MultiGetAddressesResponse:
        """
        This endpoint allows you to **query multiple pools based on the provided network
        and pool address**

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
        if not addresses:
            raise ValueError(f"Expected a non-empty value for `addresses` but received {addresses!r}")
        return self._get(
            f"/onchain/networks/{network}/pools/multi/{addresses}",
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
                    multi_get_addresses_params.MultiGetAddressesParams,
                ),
            ),
            cast_to=MultiGetAddressesResponse,
        )


class AsyncMultiResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMultiResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMultiResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMultiResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return AsyncMultiResourceWithStreamingResponse(self)

    async def get_addresses(
        self,
        addresses: str,
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
    ) -> MultiGetAddressesResponse:
        """
        This endpoint allows you to **query multiple pools based on the provided network
        and pool address**

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
        if not addresses:
            raise ValueError(f"Expected a non-empty value for `addresses` but received {addresses!r}")
        return await self._get(
            f"/onchain/networks/{network}/pools/multi/{addresses}",
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
                    multi_get_addresses_params.MultiGetAddressesParams,
                ),
            ),
            cast_to=MultiGetAddressesResponse,
        )


class MultiResourceWithRawResponse:
    def __init__(self, multi: MultiResource) -> None:
        self._multi = multi

        self.get_addresses = to_raw_response_wrapper(
            multi.get_addresses,
        )


class AsyncMultiResourceWithRawResponse:
    def __init__(self, multi: AsyncMultiResource) -> None:
        self._multi = multi

        self.get_addresses = async_to_raw_response_wrapper(
            multi.get_addresses,
        )


class MultiResourceWithStreamingResponse:
    def __init__(self, multi: MultiResource) -> None:
        self._multi = multi

        self.get_addresses = to_streamed_response_wrapper(
            multi.get_addresses,
        )


class AsyncMultiResourceWithStreamingResponse:
    def __init__(self, multi: AsyncMultiResource) -> None:
        self._multi = multi

        self.get_addresses = async_to_streamed_response_wrapper(
            multi.get_addresses,
        )
