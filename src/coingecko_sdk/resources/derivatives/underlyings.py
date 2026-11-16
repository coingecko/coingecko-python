# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ...types.derivatives import underlying_get_params, underlying_get_list_params
from ...types.derivatives.underlying_get_response import UnderlyingGetResponse
from ...types.derivatives.underlying_get_list_response import UnderlyingGetListResponse

__all__ = ["UnderlyingsResource", "AsyncUnderlyingsResource"]


class UnderlyingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UnderlyingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return UnderlyingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UnderlyingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return UnderlyingsResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        coin_ids: str | Omit = omit,
        order: Literal["open_interest_desc", "open_interest_asc", "volume_desc", "volume_asc"] | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        rwa_ids: str | Omit = omit,
        underlying_type: Literal["coin", "rwa"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UnderlyingGetResponse:
        """
        To query all the supported derivatives underlying assets with price, open
        interest, funding rate and volume data

        Args:
          coin_ids: Coins' IDs, comma-separated if querying more than 1 coin. \\**refers to
              [`/coins/list`](/reference/coins-list)

          order: Sort result by field. Default: open_interest_desc

          page: Page through results. Default: 1

          per_page: Total results per page. Default: 100 Valid values: 1...250

          rwa_ids: RWAs' IDs, comma-separated if querying more than 1 RWA. \\**refers to
              [`/rwas/list`](/reference/rwas-list)

          underlying_type: Filter by underlying type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/derivatives/underlyings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "coin_ids": coin_ids,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                        "rwa_ids": rwa_ids,
                        "underlying_type": underlying_type,
                    },
                    underlying_get_params.UnderlyingGetParams,
                ),
            ),
            cast_to=UnderlyingGetResponse,
        )

    def get_list(
        self,
        *,
        underlying_type: Literal["coin", "rwa"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UnderlyingGetListResponse:
        """
        To query all the supported derivatives underlying assets with ID, name, symbol
        and underlying type

        Args:
          underlying_type: Filter by underlying type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/derivatives/underlyings/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"underlying_type": underlying_type}, underlying_get_list_params.UnderlyingGetListParams
                ),
            ),
            cast_to=UnderlyingGetListResponse,
        )


class AsyncUnderlyingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUnderlyingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUnderlyingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUnderlyingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return AsyncUnderlyingsResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        coin_ids: str | Omit = omit,
        order: Literal["open_interest_desc", "open_interest_asc", "volume_desc", "volume_asc"] | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        rwa_ids: str | Omit = omit,
        underlying_type: Literal["coin", "rwa"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UnderlyingGetResponse:
        """
        To query all the supported derivatives underlying assets with price, open
        interest, funding rate and volume data

        Args:
          coin_ids: Coins' IDs, comma-separated if querying more than 1 coin. \\**refers to
              [`/coins/list`](/reference/coins-list)

          order: Sort result by field. Default: open_interest_desc

          page: Page through results. Default: 1

          per_page: Total results per page. Default: 100 Valid values: 1...250

          rwa_ids: RWAs' IDs, comma-separated if querying more than 1 RWA. \\**refers to
              [`/rwas/list`](/reference/rwas-list)

          underlying_type: Filter by underlying type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/derivatives/underlyings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "coin_ids": coin_ids,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                        "rwa_ids": rwa_ids,
                        "underlying_type": underlying_type,
                    },
                    underlying_get_params.UnderlyingGetParams,
                ),
            ),
            cast_to=UnderlyingGetResponse,
        )

    async def get_list(
        self,
        *,
        underlying_type: Literal["coin", "rwa"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UnderlyingGetListResponse:
        """
        To query all the supported derivatives underlying assets with ID, name, symbol
        and underlying type

        Args:
          underlying_type: Filter by underlying type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/derivatives/underlyings/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"underlying_type": underlying_type}, underlying_get_list_params.UnderlyingGetListParams
                ),
            ),
            cast_to=UnderlyingGetListResponse,
        )


class UnderlyingsResourceWithRawResponse:
    def __init__(self, underlyings: UnderlyingsResource) -> None:
        self._underlyings = underlyings

        self.get = to_raw_response_wrapper(
            underlyings.get,
        )
        self.get_list = to_raw_response_wrapper(
            underlyings.get_list,
        )


class AsyncUnderlyingsResourceWithRawResponse:
    def __init__(self, underlyings: AsyncUnderlyingsResource) -> None:
        self._underlyings = underlyings

        self.get = async_to_raw_response_wrapper(
            underlyings.get,
        )
        self.get_list = async_to_raw_response_wrapper(
            underlyings.get_list,
        )


class UnderlyingsResourceWithStreamingResponse:
    def __init__(self, underlyings: UnderlyingsResource) -> None:
        self._underlyings = underlyings

        self.get = to_streamed_response_wrapper(
            underlyings.get,
        )
        self.get_list = to_streamed_response_wrapper(
            underlyings.get_list,
        )


class AsyncUnderlyingsResourceWithStreamingResponse:
    def __init__(self, underlyings: AsyncUnderlyingsResource) -> None:
        self._underlyings = underlyings

        self.get = async_to_streamed_response_wrapper(
            underlyings.get,
        )
        self.get_list = async_to_streamed_response_wrapper(
            underlyings.get_list,
        )
