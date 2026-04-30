# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import news_get_params
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
from ..types.news_get_response import NewsGetResponse

__all__ = ["NewsResource", "AsyncNewsResource"]


class NewsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NewsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return NewsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NewsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return NewsResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        coin_id: str | Omit = omit,
        language: Literal[
            "en",
            "ru",
            "de",
            "pl",
            "es",
            "vi",
            "fr",
            "pt-br",
            "ar",
            "bg",
            "cs",
            "da",
            "el",
            "fi",
            "he",
            "hi",
            "hr",
            "hu",
            "id",
            "it",
            "ja",
            "ko",
            "lt",
            "nl",
            "no",
            "ro",
            "sk",
            "sl",
            "sv",
            "th",
            "tr",
            "uk",
            "zh",
            "zh-tw",
        ]
        | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        type: Literal["all", "news", "guides"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewsGetResponse:
        """
        This endpoint allows you to **query the latest crypto news and guides on
        CoinGecko**

        Args:
          coin_id: filter news by coin ID \\**refers to [`/coins/list`](/reference/coins-list).

          language: filter news by language Default value: **en**

          page: page through results Default value: **1**

          per_page: total results per page Default value: **10**

          type: filter news by type Default value: **all** Note: `guides` filter is only
              applicable if `coin_id` is specified and valid

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/news",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "coin_id": coin_id,
                        "language": language,
                        "page": page,
                        "per_page": per_page,
                        "type": type,
                    },
                    news_get_params.NewsGetParams,
                ),
            ),
            cast_to=NewsGetResponse,
        )


class AsyncNewsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNewsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNewsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNewsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return AsyncNewsResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        coin_id: str | Omit = omit,
        language: Literal[
            "en",
            "ru",
            "de",
            "pl",
            "es",
            "vi",
            "fr",
            "pt-br",
            "ar",
            "bg",
            "cs",
            "da",
            "el",
            "fi",
            "he",
            "hi",
            "hr",
            "hu",
            "id",
            "it",
            "ja",
            "ko",
            "lt",
            "nl",
            "no",
            "ro",
            "sk",
            "sl",
            "sv",
            "th",
            "tr",
            "uk",
            "zh",
            "zh-tw",
        ]
        | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        type: Literal["all", "news", "guides"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewsGetResponse:
        """
        This endpoint allows you to **query the latest crypto news and guides on
        CoinGecko**

        Args:
          coin_id: filter news by coin ID \\**refers to [`/coins/list`](/reference/coins-list).

          language: filter news by language Default value: **en**

          page: page through results Default value: **1**

          per_page: total results per page Default value: **10**

          type: filter news by type Default value: **all** Note: `guides` filter is only
              applicable if `coin_id` is specified and valid

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/news",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "coin_id": coin_id,
                        "language": language,
                        "page": page,
                        "per_page": per_page,
                        "type": type,
                    },
                    news_get_params.NewsGetParams,
                ),
            ),
            cast_to=NewsGetResponse,
        )


class NewsResourceWithRawResponse:
    def __init__(self, news: NewsResource) -> None:
        self._news = news

        self.get = to_raw_response_wrapper(
            news.get,
        )


class AsyncNewsResourceWithRawResponse:
    def __init__(self, news: AsyncNewsResource) -> None:
        self._news = news

        self.get = async_to_raw_response_wrapper(
            news.get,
        )


class NewsResourceWithStreamingResponse:
    def __init__(self, news: NewsResource) -> None:
        self._news = news

        self.get = to_streamed_response_wrapper(
            news.get,
        )


class AsyncNewsResourceWithStreamingResponse:
    def __init__(self, news: AsyncNewsResource) -> None:
        self._news = news

        self.get = async_to_streamed_response_wrapper(
            news.get,
        )
