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
from ...types.coins import market_get_params
from ..._base_client import make_request_options
from ...types.coins.market_get_response import MarketGetResponse

__all__ = ["MarketsResource", "AsyncMarketsResource"]


class MarketsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MarketsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return MarketsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MarketsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return MarketsResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        vs_currency: str,
        category: str | NotGiven = NOT_GIVEN,
        ids: str | NotGiven = NOT_GIVEN,
        include_tokens: Literal["top", "all"] | NotGiven = NOT_GIVEN,
        locale: Literal[
            "ar",
            "bg",
            "cs",
            "da",
            "de",
            "el",
            "en",
            "es",
            "fi",
            "fr",
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
            "pl",
            "pt",
            "ro",
            "ru",
            "sk",
            "sl",
            "sv",
            "th",
            "tr",
            "uk",
            "vi",
            "zh",
            "zh-tw",
        ]
        | NotGiven = NOT_GIVEN,
        names: str | NotGiven = NOT_GIVEN,
        order: Literal["market_cap_asc", "market_cap_desc", "volume_asc", "volume_desc", "id_asc", "id_desc"]
        | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        precision: Literal[
            "full",
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "11",
            "12",
            "13",
            "14",
            "15",
            "16",
            "17",
            "18",
        ]
        | NotGiven = NOT_GIVEN,
        price_change_percentage: str | NotGiven = NOT_GIVEN,
        sparkline: bool | NotGiven = NOT_GIVEN,
        symbols: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MarketGetResponse:
        """
        This endpoint allows you to **query all the supported coins with price, market
        cap, volume and market related data**

        Args:
          vs_currency: target currency of coins and market data \\**refers to
              [`/simple/supported_vs_currencies`](/reference/simple-supported-currencies).

          category: filter based on coins' category \\**refers to
              [`/coins/categories/list`](/reference/coins-categories-list).

          ids: coins' IDs, comma-separated if querying more than 1 coin. \\**refers to
              [`/coins/list`](/reference/coins-list).

          include_tokens: for `symbols` lookups, specify `all` to include all matching tokens Default
              `top` returns top-ranked tokens (by market cap or volume)

          locale: language background, default: en

          names: coins' names, comma-separated if querying more than 1 coin.

          order: sort result by field, default: market_cap_desc

          page: page through results, default: 1

          per_page: total results per page, default: 100 Valid values: 1...250

          precision: decimal place for currency price value

          price_change_percentage: include price change percentage timeframe, comma-separated if query more than 1
              price change percentage timeframe Valid values: 1h, 24h, 7d, 14d, 30d, 200d, 1y

          sparkline: include sparkline 7 days data, default: false

          symbols: coins' symbols, comma-separated if querying more than 1 coin.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/coins/markets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "vs_currency": vs_currency,
                        "category": category,
                        "ids": ids,
                        "include_tokens": include_tokens,
                        "locale": locale,
                        "names": names,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                        "precision": precision,
                        "price_change_percentage": price_change_percentage,
                        "sparkline": sparkline,
                        "symbols": symbols,
                    },
                    market_get_params.MarketGetParams,
                ),
            ),
            cast_to=MarketGetResponse,
        )


class AsyncMarketsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMarketsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMarketsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMarketsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return AsyncMarketsResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        vs_currency: str,
        category: str | NotGiven = NOT_GIVEN,
        ids: str | NotGiven = NOT_GIVEN,
        include_tokens: Literal["top", "all"] | NotGiven = NOT_GIVEN,
        locale: Literal[
            "ar",
            "bg",
            "cs",
            "da",
            "de",
            "el",
            "en",
            "es",
            "fi",
            "fr",
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
            "pl",
            "pt",
            "ro",
            "ru",
            "sk",
            "sl",
            "sv",
            "th",
            "tr",
            "uk",
            "vi",
            "zh",
            "zh-tw",
        ]
        | NotGiven = NOT_GIVEN,
        names: str | NotGiven = NOT_GIVEN,
        order: Literal["market_cap_asc", "market_cap_desc", "volume_asc", "volume_desc", "id_asc", "id_desc"]
        | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        precision: Literal[
            "full",
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "11",
            "12",
            "13",
            "14",
            "15",
            "16",
            "17",
            "18",
        ]
        | NotGiven = NOT_GIVEN,
        price_change_percentage: str | NotGiven = NOT_GIVEN,
        sparkline: bool | NotGiven = NOT_GIVEN,
        symbols: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MarketGetResponse:
        """
        This endpoint allows you to **query all the supported coins with price, market
        cap, volume and market related data**

        Args:
          vs_currency: target currency of coins and market data \\**refers to
              [`/simple/supported_vs_currencies`](/reference/simple-supported-currencies).

          category: filter based on coins' category \\**refers to
              [`/coins/categories/list`](/reference/coins-categories-list).

          ids: coins' IDs, comma-separated if querying more than 1 coin. \\**refers to
              [`/coins/list`](/reference/coins-list).

          include_tokens: for `symbols` lookups, specify `all` to include all matching tokens Default
              `top` returns top-ranked tokens (by market cap or volume)

          locale: language background, default: en

          names: coins' names, comma-separated if querying more than 1 coin.

          order: sort result by field, default: market_cap_desc

          page: page through results, default: 1

          per_page: total results per page, default: 100 Valid values: 1...250

          precision: decimal place for currency price value

          price_change_percentage: include price change percentage timeframe, comma-separated if query more than 1
              price change percentage timeframe Valid values: 1h, 24h, 7d, 14d, 30d, 200d, 1y

          sparkline: include sparkline 7 days data, default: false

          symbols: coins' symbols, comma-separated if querying more than 1 coin.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/coins/markets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "vs_currency": vs_currency,
                        "category": category,
                        "ids": ids,
                        "include_tokens": include_tokens,
                        "locale": locale,
                        "names": names,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                        "precision": precision,
                        "price_change_percentage": price_change_percentage,
                        "sparkline": sparkline,
                        "symbols": symbols,
                    },
                    market_get_params.MarketGetParams,
                ),
            ),
            cast_to=MarketGetResponse,
        )


class MarketsResourceWithRawResponse:
    def __init__(self, markets: MarketsResource) -> None:
        self._markets = markets

        self.get = to_raw_response_wrapper(
            markets.get,
        )


class AsyncMarketsResourceWithRawResponse:
    def __init__(self, markets: AsyncMarketsResource) -> None:
        self._markets = markets

        self.get = async_to_raw_response_wrapper(
            markets.get,
        )


class MarketsResourceWithStreamingResponse:
    def __init__(self, markets: MarketsResource) -> None:
        self._markets = markets

        self.get = to_streamed_response_wrapper(
            markets.get,
        )


class AsyncMarketsResourceWithStreamingResponse:
    def __init__(self, markets: AsyncMarketsResource) -> None:
        self._markets = markets

        self.get = async_to_streamed_response_wrapper(
            markets.get,
        )
