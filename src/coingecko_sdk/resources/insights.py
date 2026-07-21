# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import insight_get_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.insight_get_response import InsightGetResponse

__all__ = ["InsightsResource", "AsyncInsightsResource"]


class InsightsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InsightsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return InsightsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InsightsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return InsightsResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        coin_id: str | Omit = omit,
        from_: str | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        to: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InsightGetResponse:
        """
        To query the latest coin insights on CoinGecko

        Args:
          coin_id: Filter insights by coin ID. \\**refers to [`/coins/list`](/reference/coins-list).

          from_: Starting date in ISO date string (`YYYY-MM-DD`).

          page: Page through results. Default value: 1 Valid values: 1...20

          per_page: Total results per page. Default value: 10 Valid values: 1...20

          to: Ending date in ISO date string (`YYYY-MM-DD`).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/insights",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "coin_id": coin_id,
                        "from_": from_,
                        "page": page,
                        "per_page": per_page,
                        "to": to,
                    },
                    insight_get_params.InsightGetParams,
                ),
            ),
            cast_to=InsightGetResponse,
        )


class AsyncInsightsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInsightsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInsightsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInsightsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return AsyncInsightsResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        coin_id: str | Omit = omit,
        from_: str | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        to: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InsightGetResponse:
        """
        To query the latest coin insights on CoinGecko

        Args:
          coin_id: Filter insights by coin ID. \\**refers to [`/coins/list`](/reference/coins-list).

          from_: Starting date in ISO date string (`YYYY-MM-DD`).

          page: Page through results. Default value: 1 Valid values: 1...20

          per_page: Total results per page. Default value: 10 Valid values: 1...20

          to: Ending date in ISO date string (`YYYY-MM-DD`).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/insights",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "coin_id": coin_id,
                        "from_": from_,
                        "page": page,
                        "per_page": per_page,
                        "to": to,
                    },
                    insight_get_params.InsightGetParams,
                ),
            ),
            cast_to=InsightGetResponse,
        )


class InsightsResourceWithRawResponse:
    def __init__(self, insights: InsightsResource) -> None:
        self._insights = insights

        self.get = to_raw_response_wrapper(
            insights.get,
        )


class AsyncInsightsResourceWithRawResponse:
    def __init__(self, insights: AsyncInsightsResource) -> None:
        self._insights = insights

        self.get = async_to_raw_response_wrapper(
            insights.get,
        )


class InsightsResourceWithStreamingResponse:
    def __init__(self, insights: InsightsResource) -> None:
        self._insights = insights

        self.get = to_streamed_response_wrapper(
            insights.get,
        )


class AsyncInsightsResourceWithStreamingResponse:
    def __init__(self, insights: AsyncInsightsResource) -> None:
        self._insights = insights

        self.get = async_to_streamed_response_wrapper(
            insights.get,
        )
