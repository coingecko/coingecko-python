# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.coins import list_get_params
from ..._base_client import make_request_options
from ...types.coins.list_get_response import ListGetResponse
from ...types.coins.list_get_new_response import ListGetNewResponse

__all__ = ["ListResource", "AsyncListResource"]


class ListResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ListResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return ListResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ListResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return ListResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        include_platform: bool | NotGiven = NOT_GIVEN,
        status: Literal["active", "inactive"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListGetResponse:
        """
        This endpoint allows you to **query all the supported coins on CoinGecko with
        coins ID, name and symbol**

        Args:
          include_platform: include platform and token's contract addresses, default: false

          status: filter by status of coins, default: active

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/coins/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_platform": include_platform,
                        "status": status,
                    },
                    list_get_params.ListGetParams,
                ),
            ),
            cast_to=ListGetResponse,
        )

    def get_new(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListGetNewResponse:
        """
        This endpoint allows you to **query the latest 200 coins that recently listed on
        CoinGecko**
        """
        return self._get(
            "/coins/list/new",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ListGetNewResponse,
        )


class AsyncListResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncListResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return AsyncListResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncListResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return AsyncListResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        include_platform: bool | NotGiven = NOT_GIVEN,
        status: Literal["active", "inactive"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListGetResponse:
        """
        This endpoint allows you to **query all the supported coins on CoinGecko with
        coins ID, name and symbol**

        Args:
          include_platform: include platform and token's contract addresses, default: false

          status: filter by status of coins, default: active

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/coins/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "include_platform": include_platform,
                        "status": status,
                    },
                    list_get_params.ListGetParams,
                ),
            ),
            cast_to=ListGetResponse,
        )

    async def get_new(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListGetNewResponse:
        """
        This endpoint allows you to **query the latest 200 coins that recently listed on
        CoinGecko**
        """
        return await self._get(
            "/coins/list/new",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ListGetNewResponse,
        )


class ListResourceWithRawResponse:
    def __init__(self, list: ListResource) -> None:
        self._list = list

        self.get = to_raw_response_wrapper(
            list.get,
        )
        self.get_new = to_raw_response_wrapper(
            list.get_new,
        )


class AsyncListResourceWithRawResponse:
    def __init__(self, list: AsyncListResource) -> None:
        self._list = list

        self.get = async_to_raw_response_wrapper(
            list.get,
        )
        self.get_new = async_to_raw_response_wrapper(
            list.get_new,
        )


class ListResourceWithStreamingResponse:
    def __init__(self, list: ListResource) -> None:
        self._list = list

        self.get = to_streamed_response_wrapper(
            list.get,
        )
        self.get_new = to_streamed_response_wrapper(
            list.get_new,
        )


class AsyncListResourceWithStreamingResponse:
    def __init__(self, list: AsyncListResource) -> None:
        self._list = list

        self.get = async_to_streamed_response_wrapper(
            list.get,
        )
        self.get_new = async_to_streamed_response_wrapper(
            list.get_new,
        )
