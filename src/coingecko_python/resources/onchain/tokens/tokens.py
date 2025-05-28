# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .info_recently_updated import (
    InfoRecentlyUpdatedResource,
    AsyncInfoRecentlyUpdatedResource,
    InfoRecentlyUpdatedResourceWithRawResponse,
    AsyncInfoRecentlyUpdatedResourceWithRawResponse,
    InfoRecentlyUpdatedResourceWithStreamingResponse,
    AsyncInfoRecentlyUpdatedResourceWithStreamingResponse,
)

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


class TokensResourceWithRawResponse:
    def __init__(self, tokens: TokensResource) -> None:
        self._tokens = tokens

    @cached_property
    def info_recently_updated(self) -> InfoRecentlyUpdatedResourceWithRawResponse:
        return InfoRecentlyUpdatedResourceWithRawResponse(self._tokens.info_recently_updated)


class AsyncTokensResourceWithRawResponse:
    def __init__(self, tokens: AsyncTokensResource) -> None:
        self._tokens = tokens

    @cached_property
    def info_recently_updated(self) -> AsyncInfoRecentlyUpdatedResourceWithRawResponse:
        return AsyncInfoRecentlyUpdatedResourceWithRawResponse(self._tokens.info_recently_updated)


class TokensResourceWithStreamingResponse:
    def __init__(self, tokens: TokensResource) -> None:
        self._tokens = tokens

    @cached_property
    def info_recently_updated(self) -> InfoRecentlyUpdatedResourceWithStreamingResponse:
        return InfoRecentlyUpdatedResourceWithStreamingResponse(self._tokens.info_recently_updated)


class AsyncTokensResourceWithStreamingResponse:
    def __init__(self, tokens: AsyncTokensResource) -> None:
        self._tokens = tokens

    @cached_property
    def info_recently_updated(self) -> AsyncInfoRecentlyUpdatedResourceWithStreamingResponse:
        return AsyncInfoRecentlyUpdatedResourceWithStreamingResponse(self._tokens.info_recently_updated)
