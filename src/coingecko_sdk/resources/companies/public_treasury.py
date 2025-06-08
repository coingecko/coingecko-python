# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.companies.public_treasury_get_coin_id_response import PublicTreasuryGetCoinIDResponse

__all__ = ["PublicTreasuryResource", "AsyncPublicTreasuryResource"]


class PublicTreasuryResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PublicTreasuryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return PublicTreasuryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PublicTreasuryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return PublicTreasuryResourceWithStreamingResponse(self)

    def get_coin_id(
        self,
        coin_id: Literal["bitcoin", "ethereum"],
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PublicTreasuryGetCoinIDResponse:
        """
        This endpoint allows you **query public companies’ Bitcoin or Ethereum
        holdings**

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not coin_id:
            raise ValueError(f"Expected a non-empty value for `coin_id` but received {coin_id!r}")
        return self._get(
            f"/companies/public_treasury/{coin_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicTreasuryGetCoinIDResponse,
        )


class AsyncPublicTreasuryResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPublicTreasuryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPublicTreasuryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPublicTreasuryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return AsyncPublicTreasuryResourceWithStreamingResponse(self)

    async def get_coin_id(
        self,
        coin_id: Literal["bitcoin", "ethereum"],
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PublicTreasuryGetCoinIDResponse:
        """
        This endpoint allows you **query public companies’ Bitcoin or Ethereum
        holdings**

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not coin_id:
            raise ValueError(f"Expected a non-empty value for `coin_id` but received {coin_id!r}")
        return await self._get(
            f"/companies/public_treasury/{coin_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicTreasuryGetCoinIDResponse,
        )


class PublicTreasuryResourceWithRawResponse:
    def __init__(self, public_treasury: PublicTreasuryResource) -> None:
        self._public_treasury = public_treasury

        self.get_coin_id = to_raw_response_wrapper(
            public_treasury.get_coin_id,
        )


class AsyncPublicTreasuryResourceWithRawResponse:
    def __init__(self, public_treasury: AsyncPublicTreasuryResource) -> None:
        self._public_treasury = public_treasury

        self.get_coin_id = async_to_raw_response_wrapper(
            public_treasury.get_coin_id,
        )


class PublicTreasuryResourceWithStreamingResponse:
    def __init__(self, public_treasury: PublicTreasuryResource) -> None:
        self._public_treasury = public_treasury

        self.get_coin_id = to_streamed_response_wrapper(
            public_treasury.get_coin_id,
        )


class AsyncPublicTreasuryResourceWithStreamingResponse:
    def __init__(self, public_treasury: AsyncPublicTreasuryResource) -> None:
        self._public_treasury = public_treasury

        self.get_coin_id = async_to_streamed_response_wrapper(
            public_treasury.get_coin_id,
        )
