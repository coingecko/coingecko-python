# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ....types.onchain.tokens import info_recently_updated_get_params
from ....types.onchain.tokens.info_recently_updated_get_response import InfoRecentlyUpdatedGetResponse

__all__ = ["InfoRecentlyUpdatedResource", "AsyncInfoRecentlyUpdatedResource"]


class InfoRecentlyUpdatedResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InfoRecentlyUpdatedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return InfoRecentlyUpdatedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InfoRecentlyUpdatedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return InfoRecentlyUpdatedResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        include: Literal["network"] | NotGiven = NOT_GIVEN,
        network: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InfoRecentlyUpdatedGetResponse:
        """
        This endpoint allows you to **query 100 most recently updated tokens info of a
        specific network or across all networks on GeckoTerminal**

        Args:
          include: Attributes for related resources to include, which will be returned under the
              top-level 'included' key

          network: filter tokens by provided network \\**refers to
              [/networks](/reference/networks-list)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/onchain/tokens/info_recently_updated",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include": include,
                        "network": network,
                    },
                    info_recently_updated_get_params.InfoRecentlyUpdatedGetParams,
                ),
            ),
            cast_to=InfoRecentlyUpdatedGetResponse,
        )


class AsyncInfoRecentlyUpdatedResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInfoRecentlyUpdatedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInfoRecentlyUpdatedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInfoRecentlyUpdatedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return AsyncInfoRecentlyUpdatedResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        include: Literal["network"] | NotGiven = NOT_GIVEN,
        network: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InfoRecentlyUpdatedGetResponse:
        """
        This endpoint allows you to **query 100 most recently updated tokens info of a
        specific network or across all networks on GeckoTerminal**

        Args:
          include: Attributes for related resources to include, which will be returned under the
              top-level 'included' key

          network: filter tokens by provided network \\**refers to
              [/networks](/reference/networks-list)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/onchain/tokens/info_recently_updated",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "include": include,
                        "network": network,
                    },
                    info_recently_updated_get_params.InfoRecentlyUpdatedGetParams,
                ),
            ),
            cast_to=InfoRecentlyUpdatedGetResponse,
        )


class InfoRecentlyUpdatedResourceWithRawResponse:
    def __init__(self, info_recently_updated: InfoRecentlyUpdatedResource) -> None:
        self._info_recently_updated = info_recently_updated

        self.get = to_raw_response_wrapper(
            info_recently_updated.get,
        )


class AsyncInfoRecentlyUpdatedResourceWithRawResponse:
    def __init__(self, info_recently_updated: AsyncInfoRecentlyUpdatedResource) -> None:
        self._info_recently_updated = info_recently_updated

        self.get = async_to_raw_response_wrapper(
            info_recently_updated.get,
        )


class InfoRecentlyUpdatedResourceWithStreamingResponse:
    def __init__(self, info_recently_updated: InfoRecentlyUpdatedResource) -> None:
        self._info_recently_updated = info_recently_updated

        self.get = to_streamed_response_wrapper(
            info_recently_updated.get,
        )


class AsyncInfoRecentlyUpdatedResourceWithStreamingResponse:
    def __init__(self, info_recently_updated: AsyncInfoRecentlyUpdatedResource) -> None:
        self._info_recently_updated = info_recently_updated

        self.get = async_to_streamed_response_wrapper(
            info_recently_updated.get,
        )
