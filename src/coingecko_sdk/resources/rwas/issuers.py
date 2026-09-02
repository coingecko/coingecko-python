# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.rwas.issuer_get_id_response import IssuerGetIDResponse
from ...types.rwas.issuer_get_list_response import IssuerGetListResponse

__all__ = ["IssuersResource", "AsyncIssuersResource"]


class IssuersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IssuersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return IssuersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IssuersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return IssuersResourceWithStreamingResponse(self)

    def get_id(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IssuerGetIDResponse:
        """
        To query the market data (market cap, volume, etc.) and tokens of an issuer
        based on a particular issuer ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/rwas/issuers/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IssuerGetIDResponse,
        )

    def get_list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IssuerGetListResponse:
        """To query all the supported RWA issuers on CoinGecko"""
        return self._get(
            "/rwas/issuers/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IssuerGetListResponse,
        )


class AsyncIssuersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIssuersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIssuersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIssuersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return AsyncIssuersResourceWithStreamingResponse(self)

    async def get_id(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IssuerGetIDResponse:
        """
        To query the market data (market cap, volume, etc.) and tokens of an issuer
        based on a particular issuer ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/rwas/issuers/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IssuerGetIDResponse,
        )

    async def get_list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IssuerGetListResponse:
        """To query all the supported RWA issuers on CoinGecko"""
        return await self._get(
            "/rwas/issuers/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IssuerGetListResponse,
        )


class IssuersResourceWithRawResponse:
    def __init__(self, issuers: IssuersResource) -> None:
        self._issuers = issuers

        self.get_id = to_raw_response_wrapper(
            issuers.get_id,
        )
        self.get_list = to_raw_response_wrapper(
            issuers.get_list,
        )


class AsyncIssuersResourceWithRawResponse:
    def __init__(self, issuers: AsyncIssuersResource) -> None:
        self._issuers = issuers

        self.get_id = async_to_raw_response_wrapper(
            issuers.get_id,
        )
        self.get_list = async_to_raw_response_wrapper(
            issuers.get_list,
        )


class IssuersResourceWithStreamingResponse:
    def __init__(self, issuers: IssuersResource) -> None:
        self._issuers = issuers

        self.get_id = to_streamed_response_wrapper(
            issuers.get_id,
        )
        self.get_list = to_streamed_response_wrapper(
            issuers.get_list,
        )


class AsyncIssuersResourceWithStreamingResponse:
    def __init__(self, issuers: AsyncIssuersResource) -> None:
        self._issuers = issuers

        self.get_id = async_to_streamed_response_wrapper(
            issuers.get_id,
        )
        self.get_list = async_to_streamed_response_wrapper(
            issuers.get_list,
        )
