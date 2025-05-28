# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.token_list_get_all_json_response import TokenListGetAllJsonResponse

__all__ = ["TokenListsResource", "AsyncTokenListsResource"]


class TokenListsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TokenListsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return TokenListsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TokenListsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return TokenListsResourceWithStreamingResponse(self)

    def get_all_json(
        self,
        asset_platform_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TokenListGetAllJsonResponse:
        """
        This endpoint allows you to **get full list of tokens of a blockchain network
        (asset platform) that is supported by
        [Ethereum token list standard](https://tokenlists.org/)**

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_platform_id:
            raise ValueError(f"Expected a non-empty value for `asset_platform_id` but received {asset_platform_id!r}")
        return self._get(
            f"/token_lists/{asset_platform_id}/all.json",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TokenListGetAllJsonResponse,
        )


class AsyncTokenListsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTokenListsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTokenListsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTokenListsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return AsyncTokenListsResourceWithStreamingResponse(self)

    async def get_all_json(
        self,
        asset_platform_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TokenListGetAllJsonResponse:
        """
        This endpoint allows you to **get full list of tokens of a blockchain network
        (asset platform) that is supported by
        [Ethereum token list standard](https://tokenlists.org/)**

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_platform_id:
            raise ValueError(f"Expected a non-empty value for `asset_platform_id` but received {asset_platform_id!r}")
        return await self._get(
            f"/token_lists/{asset_platform_id}/all.json",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TokenListGetAllJsonResponse,
        )


class TokenListsResourceWithRawResponse:
    def __init__(self, token_lists: TokenListsResource) -> None:
        self._token_lists = token_lists

        self.get_all_json = to_raw_response_wrapper(
            token_lists.get_all_json,
        )


class AsyncTokenListsResourceWithRawResponse:
    def __init__(self, token_lists: AsyncTokenListsResource) -> None:
        self._token_lists = token_lists

        self.get_all_json = async_to_raw_response_wrapper(
            token_lists.get_all_json,
        )


class TokenListsResourceWithStreamingResponse:
    def __init__(self, token_lists: TokenListsResource) -> None:
        self._token_lists = token_lists

        self.get_all_json = to_streamed_response_wrapper(
            token_lists.get_all_json,
        )


class AsyncTokenListsResourceWithStreamingResponse:
    def __init__(self, token_lists: AsyncTokenListsResource) -> None:
        self._token_lists = token_lists

        self.get_all_json = async_to_streamed_response_wrapper(
            token_lists.get_all_json,
        )
