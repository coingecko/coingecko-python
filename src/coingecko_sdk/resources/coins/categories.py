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
from ...types.coins import category_get_params
from ..._base_client import make_request_options
from ...types.coins.category_get_response import CategoryGetResponse
from ...types.coins.category_get_list_response import CategoryGetListResponse

__all__ = ["CategoriesResource", "AsyncCategoriesResource"]


class CategoriesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CategoriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return CategoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CategoriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return CategoriesResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        order: Literal[
            "market_cap_desc",
            "market_cap_asc",
            "name_desc",
            "name_asc",
            "market_cap_change_24h_desc",
            "market_cap_change_24h_asc",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CategoryGetResponse:
        """
        This endpoint allows you to **query all the coins categories with market data
        (market cap, volume, ...) on CoinGecko**

        Args:
          order: sort results by field, default: market_cap_desc

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/coins/categories",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"order": order}, category_get_params.CategoryGetParams),
            ),
            cast_to=CategoryGetResponse,
        )

    def get_list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CategoryGetListResponse:
        """This endpoint allows you to **query all the coins categories on CoinGecko**"""
        return self._get(
            "/coins/categories/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CategoryGetListResponse,
        )


class AsyncCategoriesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCategoriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCategoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCategoriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return AsyncCategoriesResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        order: Literal[
            "market_cap_desc",
            "market_cap_asc",
            "name_desc",
            "name_asc",
            "market_cap_change_24h_desc",
            "market_cap_change_24h_asc",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CategoryGetResponse:
        """
        This endpoint allows you to **query all the coins categories with market data
        (market cap, volume, ...) on CoinGecko**

        Args:
          order: sort results by field, default: market_cap_desc

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/coins/categories",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"order": order}, category_get_params.CategoryGetParams),
            ),
            cast_to=CategoryGetResponse,
        )

    async def get_list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CategoryGetListResponse:
        """This endpoint allows you to **query all the coins categories on CoinGecko**"""
        return await self._get(
            "/coins/categories/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CategoryGetListResponse,
        )


class CategoriesResourceWithRawResponse:
    def __init__(self, categories: CategoriesResource) -> None:
        self._categories = categories

        self.get = to_raw_response_wrapper(
            categories.get,
        )
        self.get_list = to_raw_response_wrapper(
            categories.get_list,
        )


class AsyncCategoriesResourceWithRawResponse:
    def __init__(self, categories: AsyncCategoriesResource) -> None:
        self._categories = categories

        self.get = async_to_raw_response_wrapper(
            categories.get,
        )
        self.get_list = async_to_raw_response_wrapper(
            categories.get_list,
        )


class CategoriesResourceWithStreamingResponse:
    def __init__(self, categories: CategoriesResource) -> None:
        self._categories = categories

        self.get = to_streamed_response_wrapper(
            categories.get,
        )
        self.get_list = to_streamed_response_wrapper(
            categories.get_list,
        )


class AsyncCategoriesResourceWithStreamingResponse:
    def __init__(self, categories: AsyncCategoriesResource) -> None:
        self._categories = categories

        self.get = async_to_streamed_response_wrapper(
            categories.get,
        )
        self.get_list = async_to_streamed_response_wrapper(
            categories.get_list,
        )
