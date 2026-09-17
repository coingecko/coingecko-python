# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.onchain import token_get_multi_params
from .info_recently_updated import (
    InfoRecentlyUpdatedResource,
    AsyncInfoRecentlyUpdatedResource,
    InfoRecentlyUpdatedResourceWithRawResponse,
    AsyncInfoRecentlyUpdatedResourceWithRawResponse,
    InfoRecentlyUpdatedResourceWithStreamingResponse,
    AsyncInfoRecentlyUpdatedResourceWithStreamingResponse,
)
from ....types.onchain.token_get_multi_response import TokenGetMultiResponse

__all__ = ["TokensResource", "AsyncTokensResource"]


class TokensResource(SyncAPIResource):
    @cached_property
    def info_recently_updated(self) -> InfoRecentlyUpdatedResource:
        return InfoRecentlyUpdatedResource(self._client)

    @cached_property
    def with_raw_response(self) -> TokensResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return TokensResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TokensResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return TokensResourceWithStreamingResponse(self)

    def get_multi(
        self,
        *,
        tokens: str,
        include: Literal["top_pools"] | Omit = omit,
        include_composition: bool | Omit = omit,
        include_inactive_source: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TokenGetMultiResponse:
        """
        To query multiple tokens data based on the provided token contract addresses
        across multiple networks in a single request

        Args:
          tokens: Network ID and token contract address pairs in `network_id:token_address`
              format, comma-separated if more than one. Maximum: 50 \\**refers to
              [`/onchain/networks`](/reference/networks-list).

          include: Attributes to include.

          include_composition: Include pool composition. Default: `false`

          include_inactive_source: Include tokens from inactive pools using the most recent swap. Default: `false`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/onchain/tokens/multi",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "tokens": tokens,
                        "include": include,
                        "include_composition": include_composition,
                        "include_inactive_source": include_inactive_source,
                    },
                    token_get_multi_params.TokenGetMultiParams,
                ),
            ),
            cast_to=TokenGetMultiResponse,
        )


class AsyncTokensResource(AsyncAPIResource):
    @cached_property
    def info_recently_updated(self) -> AsyncInfoRecentlyUpdatedResource:
        return AsyncInfoRecentlyUpdatedResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTokensResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTokensResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTokensResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return AsyncTokensResourceWithStreamingResponse(self)

    async def get_multi(
        self,
        *,
        tokens: str,
        include: Literal["top_pools"] | Omit = omit,
        include_composition: bool | Omit = omit,
        include_inactive_source: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TokenGetMultiResponse:
        """
        To query multiple tokens data based on the provided token contract addresses
        across multiple networks in a single request

        Args:
          tokens: Network ID and token contract address pairs in `network_id:token_address`
              format, comma-separated if more than one. Maximum: 50 \\**refers to
              [`/onchain/networks`](/reference/networks-list).

          include: Attributes to include.

          include_composition: Include pool composition. Default: `false`

          include_inactive_source: Include tokens from inactive pools using the most recent swap. Default: `false`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/onchain/tokens/multi",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "tokens": tokens,
                        "include": include,
                        "include_composition": include_composition,
                        "include_inactive_source": include_inactive_source,
                    },
                    token_get_multi_params.TokenGetMultiParams,
                ),
            ),
            cast_to=TokenGetMultiResponse,
        )


class TokensResourceWithRawResponse:
    def __init__(self, tokens: TokensResource) -> None:
        self._tokens = tokens

        self.get_multi = to_raw_response_wrapper(
            tokens.get_multi,
        )

    @cached_property
    def info_recently_updated(self) -> InfoRecentlyUpdatedResourceWithRawResponse:
        return InfoRecentlyUpdatedResourceWithRawResponse(self._tokens.info_recently_updated)


class AsyncTokensResourceWithRawResponse:
    def __init__(self, tokens: AsyncTokensResource) -> None:
        self._tokens = tokens

        self.get_multi = async_to_raw_response_wrapper(
            tokens.get_multi,
        )

    @cached_property
    def info_recently_updated(self) -> AsyncInfoRecentlyUpdatedResourceWithRawResponse:
        return AsyncInfoRecentlyUpdatedResourceWithRawResponse(self._tokens.info_recently_updated)


class TokensResourceWithStreamingResponse:
    def __init__(self, tokens: TokensResource) -> None:
        self._tokens = tokens

        self.get_multi = to_streamed_response_wrapper(
            tokens.get_multi,
        )

    @cached_property
    def info_recently_updated(self) -> InfoRecentlyUpdatedResourceWithStreamingResponse:
        return InfoRecentlyUpdatedResourceWithStreamingResponse(self._tokens.info_recently_updated)


class AsyncTokensResourceWithStreamingResponse:
    def __init__(self, tokens: AsyncTokensResource) -> None:
        self._tokens = tokens

        self.get_multi = async_to_streamed_response_wrapper(
            tokens.get_multi,
        )

    @cached_property
    def info_recently_updated(self) -> AsyncInfoRecentlyUpdatedResourceWithStreamingResponse:
        return AsyncInfoRecentlyUpdatedResourceWithStreamingResponse(self._tokens.info_recently_updated)
