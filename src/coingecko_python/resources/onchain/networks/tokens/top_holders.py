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
from .....types.onchain.networks.tokens import top_holder_get_params
from .....types.onchain.networks.tokens.top_holder_get_response import TopHolderGetResponse

__all__ = ["TopHoldersResource", "AsyncTopHoldersResource"]


class TopHoldersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TopHoldersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return TopHoldersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TopHoldersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return TopHoldersResourceWithStreamingResponse(self)

    def get(
        self,
        address: str,
        *,
        network: str,
        holders: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TopHolderGetResponse:
        """
        This endpoint allows you to **query top token holders based on the provided
        token contract address on a network**

        Args:
          holders: number of top token holders to return, you may use any integer or `max` Default
              value: 10

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
            f"/onchain/networks/{network}/tokens/{address}/top_holders",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"holders": holders}, top_holder_get_params.TopHolderGetParams),
            ),
            cast_to=TopHolderGetResponse,
        )


class AsyncTopHoldersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTopHoldersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTopHoldersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTopHoldersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return AsyncTopHoldersResourceWithStreamingResponse(self)

    async def get(
        self,
        address: str,
        *,
        network: str,
        holders: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TopHolderGetResponse:
        """
        This endpoint allows you to **query top token holders based on the provided
        token contract address on a network**

        Args:
          holders: number of top token holders to return, you may use any integer or `max` Default
              value: 10

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
            f"/onchain/networks/{network}/tokens/{address}/top_holders",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"holders": holders}, top_holder_get_params.TopHolderGetParams),
            ),
            cast_to=TopHolderGetResponse,
        )


class TopHoldersResourceWithRawResponse:
    def __init__(self, top_holders: TopHoldersResource) -> None:
        self._top_holders = top_holders

        self.get = to_raw_response_wrapper(
            top_holders.get,
        )


class AsyncTopHoldersResourceWithRawResponse:
    def __init__(self, top_holders: AsyncTopHoldersResource) -> None:
        self._top_holders = top_holders

        self.get = async_to_raw_response_wrapper(
            top_holders.get,
        )


class TopHoldersResourceWithStreamingResponse:
    def __init__(self, top_holders: TopHoldersResource) -> None:
        self._top_holders = top_holders

        self.get = to_streamed_response_wrapper(
            top_holders.get,
        )


class AsyncTopHoldersResourceWithStreamingResponse:
    def __init__(self, top_holders: AsyncTopHoldersResource) -> None:
        self._top_holders = top_holders

        self.get = async_to_streamed_response_wrapper(
            top_holders.get,
        )
