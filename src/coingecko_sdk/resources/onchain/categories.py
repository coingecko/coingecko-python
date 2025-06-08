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
from ..._base_client import make_request_options
from ...types.onchain import category_get_params, category_get_pools_params
from ...types.onchain.category_get_response import CategoryGetResponse
from ...types.onchain.category_get_pools_response import CategoryGetPoolsResponse

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
        page: int | NotGiven = NOT_GIVEN,
        sort: Literal[
            "h1_volume_percentage_desc",
            "h6_volume_percentage_desc",
            "h12_volume_percentage_desc",
            "h24_tx_count_desc",
            "h24_volume_usd_desc",
            "fdv_usd_desc",
            "reserve_in_usd_desc",
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
        This endpoint allows you to **query all the supported categories on
        GeckoTerminal**

        Args:
          page: page through results Default value: `1`

          sort: sort the categories by field Default value: `h6_volume_percentage_desc`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/onchain/categories",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "sort": sort,
                    },
                    category_get_params.CategoryGetParams,
                ),
            ),
            cast_to=CategoryGetResponse,
        )

    def get_pools(
        self,
        category_id: str,
        *,
        include: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        sort: Literal[
            "m5_trending",
            "h1_trending",
            "h6_trending",
            "h24_trending",
            "h24_tx_count_desc",
            "h24_volume_usd_desc",
            "pool_created_at_desc",
            "h24_price_change_percentage_desc",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CategoryGetPoolsResponse:
        """
        This endpoint allows you to **query all the pools based on the provided category
        ID**

        Args:
          include: attributes to include, comma-separated if more than one to include Available
              values: `base_token`, `quote_token`, `dex`, `network`. Example: `base_token` or
              `base_token,dex`

          page: page through results Default value: `1`

          sort: sort the pools by field Default value: `pool_created_at_desc`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not category_id:
            raise ValueError(f"Expected a non-empty value for `category_id` but received {category_id!r}")
        return self._get(
            f"/onchain/categories/{category_id}/pools",
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
                    category_get_pools_params.CategoryGetPoolsParams,
                ),
            ),
            cast_to=CategoryGetPoolsResponse,
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
        page: int | NotGiven = NOT_GIVEN,
        sort: Literal[
            "h1_volume_percentage_desc",
            "h6_volume_percentage_desc",
            "h12_volume_percentage_desc",
            "h24_tx_count_desc",
            "h24_volume_usd_desc",
            "fdv_usd_desc",
            "reserve_in_usd_desc",
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
        This endpoint allows you to **query all the supported categories on
        GeckoTerminal**

        Args:
          page: page through results Default value: `1`

          sort: sort the categories by field Default value: `h6_volume_percentage_desc`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/onchain/categories",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "sort": sort,
                    },
                    category_get_params.CategoryGetParams,
                ),
            ),
            cast_to=CategoryGetResponse,
        )

    async def get_pools(
        self,
        category_id: str,
        *,
        include: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        sort: Literal[
            "m5_trending",
            "h1_trending",
            "h6_trending",
            "h24_trending",
            "h24_tx_count_desc",
            "h24_volume_usd_desc",
            "pool_created_at_desc",
            "h24_price_change_percentage_desc",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CategoryGetPoolsResponse:
        """
        This endpoint allows you to **query all the pools based on the provided category
        ID**

        Args:
          include: attributes to include, comma-separated if more than one to include Available
              values: `base_token`, `quote_token`, `dex`, `network`. Example: `base_token` or
              `base_token,dex`

          page: page through results Default value: `1`

          sort: sort the pools by field Default value: `pool_created_at_desc`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not category_id:
            raise ValueError(f"Expected a non-empty value for `category_id` but received {category_id!r}")
        return await self._get(
            f"/onchain/categories/{category_id}/pools",
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
                    category_get_pools_params.CategoryGetPoolsParams,
                ),
            ),
            cast_to=CategoryGetPoolsResponse,
        )


class CategoriesResourceWithRawResponse:
    def __init__(self, categories: CategoriesResource) -> None:
        self._categories = categories

        self.get = to_raw_response_wrapper(
            categories.get,
        )
        self.get_pools = to_raw_response_wrapper(
            categories.get_pools,
        )


class AsyncCategoriesResourceWithRawResponse:
    def __init__(self, categories: AsyncCategoriesResource) -> None:
        self._categories = categories

        self.get = async_to_raw_response_wrapper(
            categories.get,
        )
        self.get_pools = async_to_raw_response_wrapper(
            categories.get_pools,
        )


class CategoriesResourceWithStreamingResponse:
    def __init__(self, categories: CategoriesResource) -> None:
        self._categories = categories

        self.get = to_streamed_response_wrapper(
            categories.get,
        )
        self.get_pools = to_streamed_response_wrapper(
            categories.get_pools,
        )


class AsyncCategoriesResourceWithStreamingResponse:
    def __init__(self, categories: AsyncCategoriesResource) -> None:
        self._categories = categories

        self.get = async_to_streamed_response_wrapper(
            categories.get,
        )
        self.get_pools = async_to_streamed_response_wrapper(
            categories.get_pools,
        )
