# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...types import rwa_get_id_params, rwa_get_list_params, rwa_get_markets_params
from .issuers import (
    IssuersResource,
    AsyncIssuersResource,
    IssuersResourceWithRawResponse,
    AsyncIssuersResourceWithRawResponse,
    IssuersResourceWithStreamingResponse,
    AsyncIssuersResourceWithStreamingResponse,
)
from .tickers import (
    TickersResource,
    AsyncTickersResource,
    TickersResourceWithRawResponse,
    AsyncTickersResourceWithRawResponse,
    TickersResourceWithStreamingResponse,
    AsyncTickersResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .market_chart import (
    MarketChartResource,
    AsyncMarketChartResource,
    MarketChartResourceWithRawResponse,
    AsyncMarketChartResourceWithRawResponse,
    MarketChartResourceWithStreamingResponse,
    AsyncMarketChartResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from ...types.rwa_get_id_response import RwaGetIDResponse
from ...types.rwa_get_list_response import RwaGetListResponse
from ...types.rwa_get_markets_response import RwaGetMarketsResponse

__all__ = ["RwasResource", "AsyncRwasResource"]


class RwasResource(SyncAPIResource):
    @cached_property
    def issuers(self) -> IssuersResource:
        return IssuersResource(self._client)

    @cached_property
    def market_chart(self) -> MarketChartResource:
        return MarketChartResource(self._client)

    @cached_property
    def tickers(self) -> TickersResource:
        return TickersResource(self._client)

    @cached_property
    def with_raw_response(self) -> RwasResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return RwasResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RwasResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return RwasResourceWithStreamingResponse(self)

    def get_id(
        self,
        id: str,
        *,
        sparkline: bool | Omit = omit,
        tokenized_market_data: bool | Omit = omit,
        tokens: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RwaGetIDResponse:
        """
        To query all the metadata, market data and tokens of a RWA based on a particular
        RWA ID

        Args:
          sparkline: Include sparkline 7-day data. Default: false

          tokenized_market_data: Include tokenized market data. Default: false

          tokens: Include tokens data. Default: false

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/rwas/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "sparkline": sparkline,
                        "tokenized_market_data": tokenized_market_data,
                        "tokens": tokens,
                    },
                    rwa_get_id_params.RwaGetIDParams,
                ),
            ),
            cast_to=RwaGetIDResponse,
        )

    def get_list(
        self,
        *,
        asset_type: Literal["stock", "commodity", "etf"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RwaGetListResponse:
        """
        To query all the supported tokenized real world assets (RWAs) on CoinGecko with
        RWA ID, name and symbol

        Args:
          asset_type: Filter by RWA asset type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/rwas/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"asset_type": asset_type}, rwa_get_list_params.RwaGetListParams),
            ),
            cast_to=RwaGetListResponse,
        )

    def get_markets(
        self,
        *,
        asset_type: Literal["stock", "commodity", "etf"] | Omit = omit,
        ids: str | Omit = omit,
        issuer: str | Omit = omit,
        names: str | Omit = omit,
        order: Literal["market_cap_asc", "market_cap_desc", "volume_asc", "volume_desc", "id_asc", "id_desc"]
        | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
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
        | Omit = omit,
        price_change_percentage: str | Omit = omit,
        sparkline: bool | Omit = omit,
        symbols: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RwaGetMarketsResponse:
        """
        To query all the supported RWAs with price, market cap, volume and market
        related data

        Args:
          asset_type: Filter by RWA asset type.

          ids: RWAs' IDs, comma-separated if querying more than 1 RWA. \\**refers to
              [`/rwas/list`](/reference/rwas-list)

          issuer: Filter based on RWAs' issuer. \\**refers to
              [`/rwas/issuers/list`](/reference/rwas-issuers-list)

          names: RWAs' names, comma-separated if querying more than 1 RWA.

          order: Sort result by field. Default: market_cap_desc

          page: Page through results. Default: 1

          per_page: Total results per page. Default: 100 Valid values: 1...250

          precision: Decimal places for currency price value

          price_change_percentage: Include price change percentage timeframe, comma-separated if querying more than
              1 timeframe. Valid values: `1h`, `24h`, `7d`, `14d`, `30d`, `200d`, `1y`

          sparkline: Include sparkline 7-day data. Default: false

          symbols: RWAs' symbols, comma-separated if querying more than 1 RWA.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/rwas/markets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "asset_type": asset_type,
                        "ids": ids,
                        "issuer": issuer,
                        "names": names,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                        "precision": precision,
                        "price_change_percentage": price_change_percentage,
                        "sparkline": sparkline,
                        "symbols": symbols,
                    },
                    rwa_get_markets_params.RwaGetMarketsParams,
                ),
            ),
            cast_to=RwaGetMarketsResponse,
        )


class AsyncRwasResource(AsyncAPIResource):
    @cached_property
    def issuers(self) -> AsyncIssuersResource:
        return AsyncIssuersResource(self._client)

    @cached_property
    def market_chart(self) -> AsyncMarketChartResource:
        return AsyncMarketChartResource(self._client)

    @cached_property
    def tickers(self) -> AsyncTickersResource:
        return AsyncTickersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRwasResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRwasResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRwasResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return AsyncRwasResourceWithStreamingResponse(self)

    async def get_id(
        self,
        id: str,
        *,
        sparkline: bool | Omit = omit,
        tokenized_market_data: bool | Omit = omit,
        tokens: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RwaGetIDResponse:
        """
        To query all the metadata, market data and tokens of a RWA based on a particular
        RWA ID

        Args:
          sparkline: Include sparkline 7-day data. Default: false

          tokenized_market_data: Include tokenized market data. Default: false

          tokens: Include tokens data. Default: false

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/rwas/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "sparkline": sparkline,
                        "tokenized_market_data": tokenized_market_data,
                        "tokens": tokens,
                    },
                    rwa_get_id_params.RwaGetIDParams,
                ),
            ),
            cast_to=RwaGetIDResponse,
        )

    async def get_list(
        self,
        *,
        asset_type: Literal["stock", "commodity", "etf"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RwaGetListResponse:
        """
        To query all the supported tokenized real world assets (RWAs) on CoinGecko with
        RWA ID, name and symbol

        Args:
          asset_type: Filter by RWA asset type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/rwas/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"asset_type": asset_type}, rwa_get_list_params.RwaGetListParams),
            ),
            cast_to=RwaGetListResponse,
        )

    async def get_markets(
        self,
        *,
        asset_type: Literal["stock", "commodity", "etf"] | Omit = omit,
        ids: str | Omit = omit,
        issuer: str | Omit = omit,
        names: str | Omit = omit,
        order: Literal["market_cap_asc", "market_cap_desc", "volume_asc", "volume_desc", "id_asc", "id_desc"]
        | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
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
        | Omit = omit,
        price_change_percentage: str | Omit = omit,
        sparkline: bool | Omit = omit,
        symbols: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RwaGetMarketsResponse:
        """
        To query all the supported RWAs with price, market cap, volume and market
        related data

        Args:
          asset_type: Filter by RWA asset type.

          ids: RWAs' IDs, comma-separated if querying more than 1 RWA. \\**refers to
              [`/rwas/list`](/reference/rwas-list)

          issuer: Filter based on RWAs' issuer. \\**refers to
              [`/rwas/issuers/list`](/reference/rwas-issuers-list)

          names: RWAs' names, comma-separated if querying more than 1 RWA.

          order: Sort result by field. Default: market_cap_desc

          page: Page through results. Default: 1

          per_page: Total results per page. Default: 100 Valid values: 1...250

          precision: Decimal places for currency price value

          price_change_percentage: Include price change percentage timeframe, comma-separated if querying more than
              1 timeframe. Valid values: `1h`, `24h`, `7d`, `14d`, `30d`, `200d`, `1y`

          sparkline: Include sparkline 7-day data. Default: false

          symbols: RWAs' symbols, comma-separated if querying more than 1 RWA.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/rwas/markets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "asset_type": asset_type,
                        "ids": ids,
                        "issuer": issuer,
                        "names": names,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                        "precision": precision,
                        "price_change_percentage": price_change_percentage,
                        "sparkline": sparkline,
                        "symbols": symbols,
                    },
                    rwa_get_markets_params.RwaGetMarketsParams,
                ),
            ),
            cast_to=RwaGetMarketsResponse,
        )


class RwasResourceWithRawResponse:
    def __init__(self, rwas: RwasResource) -> None:
        self._rwas = rwas

        self.get_id = to_raw_response_wrapper(
            rwas.get_id,
        )
        self.get_list = to_raw_response_wrapper(
            rwas.get_list,
        )
        self.get_markets = to_raw_response_wrapper(
            rwas.get_markets,
        )

    @cached_property
    def issuers(self) -> IssuersResourceWithRawResponse:
        return IssuersResourceWithRawResponse(self._rwas.issuers)

    @cached_property
    def market_chart(self) -> MarketChartResourceWithRawResponse:
        return MarketChartResourceWithRawResponse(self._rwas.market_chart)

    @cached_property
    def tickers(self) -> TickersResourceWithRawResponse:
        return TickersResourceWithRawResponse(self._rwas.tickers)


class AsyncRwasResourceWithRawResponse:
    def __init__(self, rwas: AsyncRwasResource) -> None:
        self._rwas = rwas

        self.get_id = async_to_raw_response_wrapper(
            rwas.get_id,
        )
        self.get_list = async_to_raw_response_wrapper(
            rwas.get_list,
        )
        self.get_markets = async_to_raw_response_wrapper(
            rwas.get_markets,
        )

    @cached_property
    def issuers(self) -> AsyncIssuersResourceWithRawResponse:
        return AsyncIssuersResourceWithRawResponse(self._rwas.issuers)

    @cached_property
    def market_chart(self) -> AsyncMarketChartResourceWithRawResponse:
        return AsyncMarketChartResourceWithRawResponse(self._rwas.market_chart)

    @cached_property
    def tickers(self) -> AsyncTickersResourceWithRawResponse:
        return AsyncTickersResourceWithRawResponse(self._rwas.tickers)


class RwasResourceWithStreamingResponse:
    def __init__(self, rwas: RwasResource) -> None:
        self._rwas = rwas

        self.get_id = to_streamed_response_wrapper(
            rwas.get_id,
        )
        self.get_list = to_streamed_response_wrapper(
            rwas.get_list,
        )
        self.get_markets = to_streamed_response_wrapper(
            rwas.get_markets,
        )

    @cached_property
    def issuers(self) -> IssuersResourceWithStreamingResponse:
        return IssuersResourceWithStreamingResponse(self._rwas.issuers)

    @cached_property
    def market_chart(self) -> MarketChartResourceWithStreamingResponse:
        return MarketChartResourceWithStreamingResponse(self._rwas.market_chart)

    @cached_property
    def tickers(self) -> TickersResourceWithStreamingResponse:
        return TickersResourceWithStreamingResponse(self._rwas.tickers)


class AsyncRwasResourceWithStreamingResponse:
    def __init__(self, rwas: AsyncRwasResource) -> None:
        self._rwas = rwas

        self.get_id = async_to_streamed_response_wrapper(
            rwas.get_id,
        )
        self.get_list = async_to_streamed_response_wrapper(
            rwas.get_list,
        )
        self.get_markets = async_to_streamed_response_wrapper(
            rwas.get_markets,
        )

    @cached_property
    def issuers(self) -> AsyncIssuersResourceWithStreamingResponse:
        return AsyncIssuersResourceWithStreamingResponse(self._rwas.issuers)

    @cached_property
    def market_chart(self) -> AsyncMarketChartResourceWithStreamingResponse:
        return AsyncMarketChartResourceWithStreamingResponse(self._rwas.market_chart)

    @cached_property
    def tickers(self) -> AsyncTickersResourceWithStreamingResponse:
        return AsyncTickersResourceWithStreamingResponse(self._rwas.tickers)
