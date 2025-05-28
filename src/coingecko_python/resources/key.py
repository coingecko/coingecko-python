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
from ..types.key_get_response import KeyGetResponse

__all__ = ["KeyResource", "AsyncKeyResource"]


class KeyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> KeyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return KeyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KeyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return KeyResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KeyGetResponse:
        """
        This endpoint allows you to **monitor your account's API usage, including rate
        limits, monthly total credits, remaining credits, and more**
        """
        return self._get(
            "/key",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeyGetResponse,
        )


class AsyncKeyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncKeyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return AsyncKeyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKeyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return AsyncKeyResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KeyGetResponse:
        """
        This endpoint allows you to **monitor your account's API usage, including rate
        limits, monthly total credits, remaining credits, and more**
        """
        return await self._get(
            "/key",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeyGetResponse,
        )


class KeyResourceWithRawResponse:
    def __init__(self, key: KeyResource) -> None:
        self._key = key

        self.get = to_raw_response_wrapper(
            key.get,
        )


class AsyncKeyResourceWithRawResponse:
    def __init__(self, key: AsyncKeyResource) -> None:
        self._key = key

        self.get = async_to_raw_response_wrapper(
            key.get,
        )


class KeyResourceWithStreamingResponse:
    def __init__(self, key: KeyResource) -> None:
        self._key = key

        self.get = to_streamed_response_wrapper(
            key.get,
        )


class AsyncKeyResourceWithStreamingResponse:
    def __init__(self, key: AsyncKeyResource) -> None:
        self._key = key

        self.get = async_to_streamed_response_wrapper(
            key.get,
        )
