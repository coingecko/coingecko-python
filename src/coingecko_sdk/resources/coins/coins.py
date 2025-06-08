# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .list import (
    ListResource,
    AsyncListResource,
    ListResourceWithRawResponse,
    AsyncListResourceWithRawResponse,
    ListResourceWithStreamingResponse,
    AsyncListResourceWithStreamingResponse,
)
from .ohlc import (
    OhlcResource,
    AsyncOhlcResource,
    OhlcResourceWithRawResponse,
    AsyncOhlcResourceWithRawResponse,
    OhlcResourceWithStreamingResponse,
    AsyncOhlcResourceWithStreamingResponse,
)
from ...types import coin_get_id_params
from .history import (
    HistoryResource,
    AsyncHistoryResource,
    HistoryResourceWithRawResponse,
    AsyncHistoryResourceWithRawResponse,
    HistoryResourceWithStreamingResponse,
    AsyncHistoryResourceWithStreamingResponse,
)
from .markets import (
    MarketsResource,
    AsyncMarketsResource,
    MarketsResourceWithRawResponse,
    AsyncMarketsResourceWithRawResponse,
    MarketsResourceWithStreamingResponse,
    AsyncMarketsResourceWithStreamingResponse,
)
from .tickers import (
    TickersResource,
    AsyncTickersResource,
    TickersResourceWithRawResponse,
    AsyncTickersResourceWithRawResponse,
    TickersResourceWithStreamingResponse,
    AsyncTickersResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .categories import (
    CategoriesResource,
    AsyncCategoriesResource,
    CategoriesResourceWithRawResponse,
    AsyncCategoriesResourceWithRawResponse,
    CategoriesResourceWithStreamingResponse,
    AsyncCategoriesResourceWithStreamingResponse,
)
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
from .contract.contract import (
    ContractResource,
    AsyncContractResource,
    ContractResourceWithRawResponse,
    AsyncContractResourceWithRawResponse,
    ContractResourceWithStreamingResponse,
    AsyncContractResourceWithStreamingResponse,
)
from .top_gainers_losers import (
    TopGainersLosersResource,
    AsyncTopGainersLosersResource,
    TopGainersLosersResourceWithRawResponse,
    AsyncTopGainersLosersResourceWithRawResponse,
    TopGainersLosersResourceWithStreamingResponse,
    AsyncTopGainersLosersResourceWithStreamingResponse,
)
from .total_supply_chart import (
    TotalSupplyChartResource,
    AsyncTotalSupplyChartResource,
    TotalSupplyChartResourceWithRawResponse,
    AsyncTotalSupplyChartResourceWithRawResponse,
    TotalSupplyChartResourceWithStreamingResponse,
    AsyncTotalSupplyChartResourceWithStreamingResponse,
)
from .circulating_supply_chart import (
    CirculatingSupplyChartResource,
    AsyncCirculatingSupplyChartResource,
    CirculatingSupplyChartResourceWithRawResponse,
    AsyncCirculatingSupplyChartResourceWithRawResponse,
    CirculatingSupplyChartResourceWithStreamingResponse,
    AsyncCirculatingSupplyChartResourceWithStreamingResponse,
)
from ...types.coin_get_id_response import CoinGetIDResponse

__all__ = ["CoinsResource", "AsyncCoinsResource"]


class CoinsResource(SyncAPIResource):
    @cached_property
    def categories(self) -> CategoriesResource:
        return CategoriesResource(self._client)

    @cached_property
    def list(self) -> ListResource:
        return ListResource(self._client)

    @cached_property
    def markets(self) -> MarketsResource:
        return MarketsResource(self._client)

    @cached_property
    def top_gainers_losers(self) -> TopGainersLosersResource:
        return TopGainersLosersResource(self._client)

    @cached_property
    def circulating_supply_chart(self) -> CirculatingSupplyChartResource:
        return CirculatingSupplyChartResource(self._client)

    @cached_property
    def contract(self) -> ContractResource:
        return ContractResource(self._client)

    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def market_chart(self) -> MarketChartResource:
        return MarketChartResource(self._client)

    @cached_property
    def ohlc(self) -> OhlcResource:
        return OhlcResource(self._client)

    @cached_property
    def tickers(self) -> TickersResource:
        return TickersResource(self._client)

    @cached_property
    def total_supply_chart(self) -> TotalSupplyChartResource:
        return TotalSupplyChartResource(self._client)

    @cached_property
    def with_raw_response(self) -> CoinsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return CoinsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CoinsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return CoinsResourceWithStreamingResponse(self)

    def get_id(
        self,
        id: str,
        *,
        community_data: bool | NotGiven = NOT_GIVEN,
        developer_data: bool | NotGiven = NOT_GIVEN,
        dex_pair_format: Literal["contract_address", "symbol"] | NotGiven = NOT_GIVEN,
        localization: bool | NotGiven = NOT_GIVEN,
        market_data: bool | NotGiven = NOT_GIVEN,
        sparkline: bool | NotGiven = NOT_GIVEN,
        tickers: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CoinGetIDResponse:
        """
        This endpoint allows you to **query all the metadata (image, websites, socials,
        description, contract address, etc.) and market data (price, ATH, exchange
        tickers, etc.) of a coin from the CoinGecko coin page based on a particular coin
        ID**

        Args:
          community_data: include community data, default: true

          developer_data: include developer data, default: true

          dex_pair_format:
              set to `symbol` to display DEX pair base and target as symbols, default:
              `contract_address`

          localization: include all the localized languages in the response, default: true

          market_data: include market data, default: true

          sparkline: include sparkline 7 days data, default: false

          tickers: include tickers data, default: true

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/coins/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "community_data": community_data,
                        "developer_data": developer_data,
                        "dex_pair_format": dex_pair_format,
                        "localization": localization,
                        "market_data": market_data,
                        "sparkline": sparkline,
                        "tickers": tickers,
                    },
                    coin_get_id_params.CoinGetIDParams,
                ),
            ),
            cast_to=CoinGetIDResponse,
        )


class AsyncCoinsResource(AsyncAPIResource):
    @cached_property
    def categories(self) -> AsyncCategoriesResource:
        return AsyncCategoriesResource(self._client)

    @cached_property
    def list(self) -> AsyncListResource:
        return AsyncListResource(self._client)

    @cached_property
    def markets(self) -> AsyncMarketsResource:
        return AsyncMarketsResource(self._client)

    @cached_property
    def top_gainers_losers(self) -> AsyncTopGainersLosersResource:
        return AsyncTopGainersLosersResource(self._client)

    @cached_property
    def circulating_supply_chart(self) -> AsyncCirculatingSupplyChartResource:
        return AsyncCirculatingSupplyChartResource(self._client)

    @cached_property
    def contract(self) -> AsyncContractResource:
        return AsyncContractResource(self._client)

    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def market_chart(self) -> AsyncMarketChartResource:
        return AsyncMarketChartResource(self._client)

    @cached_property
    def ohlc(self) -> AsyncOhlcResource:
        return AsyncOhlcResource(self._client)

    @cached_property
    def tickers(self) -> AsyncTickersResource:
        return AsyncTickersResource(self._client)

    @cached_property
    def total_supply_chart(self) -> AsyncTotalSupplyChartResource:
        return AsyncTotalSupplyChartResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCoinsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCoinsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCoinsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return AsyncCoinsResourceWithStreamingResponse(self)

    async def get_id(
        self,
        id: str,
        *,
        community_data: bool | NotGiven = NOT_GIVEN,
        developer_data: bool | NotGiven = NOT_GIVEN,
        dex_pair_format: Literal["contract_address", "symbol"] | NotGiven = NOT_GIVEN,
        localization: bool | NotGiven = NOT_GIVEN,
        market_data: bool | NotGiven = NOT_GIVEN,
        sparkline: bool | NotGiven = NOT_GIVEN,
        tickers: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CoinGetIDResponse:
        """
        This endpoint allows you to **query all the metadata (image, websites, socials,
        description, contract address, etc.) and market data (price, ATH, exchange
        tickers, etc.) of a coin from the CoinGecko coin page based on a particular coin
        ID**

        Args:
          community_data: include community data, default: true

          developer_data: include developer data, default: true

          dex_pair_format:
              set to `symbol` to display DEX pair base and target as symbols, default:
              `contract_address`

          localization: include all the localized languages in the response, default: true

          market_data: include market data, default: true

          sparkline: include sparkline 7 days data, default: false

          tickers: include tickers data, default: true

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/coins/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "community_data": community_data,
                        "developer_data": developer_data,
                        "dex_pair_format": dex_pair_format,
                        "localization": localization,
                        "market_data": market_data,
                        "sparkline": sparkline,
                        "tickers": tickers,
                    },
                    coin_get_id_params.CoinGetIDParams,
                ),
            ),
            cast_to=CoinGetIDResponse,
        )


class CoinsResourceWithRawResponse:
    def __init__(self, coins: CoinsResource) -> None:
        self._coins = coins

        self.get_id = to_raw_response_wrapper(
            coins.get_id,
        )

    @cached_property
    def categories(self) -> CategoriesResourceWithRawResponse:
        return CategoriesResourceWithRawResponse(self._coins.categories)

    @cached_property
    def list(self) -> ListResourceWithRawResponse:
        return ListResourceWithRawResponse(self._coins.list)

    @cached_property
    def markets(self) -> MarketsResourceWithRawResponse:
        return MarketsResourceWithRawResponse(self._coins.markets)

    @cached_property
    def top_gainers_losers(self) -> TopGainersLosersResourceWithRawResponse:
        return TopGainersLosersResourceWithRawResponse(self._coins.top_gainers_losers)

    @cached_property
    def circulating_supply_chart(self) -> CirculatingSupplyChartResourceWithRawResponse:
        return CirculatingSupplyChartResourceWithRawResponse(self._coins.circulating_supply_chart)

    @cached_property
    def contract(self) -> ContractResourceWithRawResponse:
        return ContractResourceWithRawResponse(self._coins.contract)

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._coins.history)

    @cached_property
    def market_chart(self) -> MarketChartResourceWithRawResponse:
        return MarketChartResourceWithRawResponse(self._coins.market_chart)

    @cached_property
    def ohlc(self) -> OhlcResourceWithRawResponse:
        return OhlcResourceWithRawResponse(self._coins.ohlc)

    @cached_property
    def tickers(self) -> TickersResourceWithRawResponse:
        return TickersResourceWithRawResponse(self._coins.tickers)

    @cached_property
    def total_supply_chart(self) -> TotalSupplyChartResourceWithRawResponse:
        return TotalSupplyChartResourceWithRawResponse(self._coins.total_supply_chart)


class AsyncCoinsResourceWithRawResponse:
    def __init__(self, coins: AsyncCoinsResource) -> None:
        self._coins = coins

        self.get_id = async_to_raw_response_wrapper(
            coins.get_id,
        )

    @cached_property
    def categories(self) -> AsyncCategoriesResourceWithRawResponse:
        return AsyncCategoriesResourceWithRawResponse(self._coins.categories)

    @cached_property
    def list(self) -> AsyncListResourceWithRawResponse:
        return AsyncListResourceWithRawResponse(self._coins.list)

    @cached_property
    def markets(self) -> AsyncMarketsResourceWithRawResponse:
        return AsyncMarketsResourceWithRawResponse(self._coins.markets)

    @cached_property
    def top_gainers_losers(self) -> AsyncTopGainersLosersResourceWithRawResponse:
        return AsyncTopGainersLosersResourceWithRawResponse(self._coins.top_gainers_losers)

    @cached_property
    def circulating_supply_chart(self) -> AsyncCirculatingSupplyChartResourceWithRawResponse:
        return AsyncCirculatingSupplyChartResourceWithRawResponse(self._coins.circulating_supply_chart)

    @cached_property
    def contract(self) -> AsyncContractResourceWithRawResponse:
        return AsyncContractResourceWithRawResponse(self._coins.contract)

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._coins.history)

    @cached_property
    def market_chart(self) -> AsyncMarketChartResourceWithRawResponse:
        return AsyncMarketChartResourceWithRawResponse(self._coins.market_chart)

    @cached_property
    def ohlc(self) -> AsyncOhlcResourceWithRawResponse:
        return AsyncOhlcResourceWithRawResponse(self._coins.ohlc)

    @cached_property
    def tickers(self) -> AsyncTickersResourceWithRawResponse:
        return AsyncTickersResourceWithRawResponse(self._coins.tickers)

    @cached_property
    def total_supply_chart(self) -> AsyncTotalSupplyChartResourceWithRawResponse:
        return AsyncTotalSupplyChartResourceWithRawResponse(self._coins.total_supply_chart)


class CoinsResourceWithStreamingResponse:
    def __init__(self, coins: CoinsResource) -> None:
        self._coins = coins

        self.get_id = to_streamed_response_wrapper(
            coins.get_id,
        )

    @cached_property
    def categories(self) -> CategoriesResourceWithStreamingResponse:
        return CategoriesResourceWithStreamingResponse(self._coins.categories)

    @cached_property
    def list(self) -> ListResourceWithStreamingResponse:
        return ListResourceWithStreamingResponse(self._coins.list)

    @cached_property
    def markets(self) -> MarketsResourceWithStreamingResponse:
        return MarketsResourceWithStreamingResponse(self._coins.markets)

    @cached_property
    def top_gainers_losers(self) -> TopGainersLosersResourceWithStreamingResponse:
        return TopGainersLosersResourceWithStreamingResponse(self._coins.top_gainers_losers)

    @cached_property
    def circulating_supply_chart(self) -> CirculatingSupplyChartResourceWithStreamingResponse:
        return CirculatingSupplyChartResourceWithStreamingResponse(self._coins.circulating_supply_chart)

    @cached_property
    def contract(self) -> ContractResourceWithStreamingResponse:
        return ContractResourceWithStreamingResponse(self._coins.contract)

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._coins.history)

    @cached_property
    def market_chart(self) -> MarketChartResourceWithStreamingResponse:
        return MarketChartResourceWithStreamingResponse(self._coins.market_chart)

    @cached_property
    def ohlc(self) -> OhlcResourceWithStreamingResponse:
        return OhlcResourceWithStreamingResponse(self._coins.ohlc)

    @cached_property
    def tickers(self) -> TickersResourceWithStreamingResponse:
        return TickersResourceWithStreamingResponse(self._coins.tickers)

    @cached_property
    def total_supply_chart(self) -> TotalSupplyChartResourceWithStreamingResponse:
        return TotalSupplyChartResourceWithStreamingResponse(self._coins.total_supply_chart)


class AsyncCoinsResourceWithStreamingResponse:
    def __init__(self, coins: AsyncCoinsResource) -> None:
        self._coins = coins

        self.get_id = async_to_streamed_response_wrapper(
            coins.get_id,
        )

    @cached_property
    def categories(self) -> AsyncCategoriesResourceWithStreamingResponse:
        return AsyncCategoriesResourceWithStreamingResponse(self._coins.categories)

    @cached_property
    def list(self) -> AsyncListResourceWithStreamingResponse:
        return AsyncListResourceWithStreamingResponse(self._coins.list)

    @cached_property
    def markets(self) -> AsyncMarketsResourceWithStreamingResponse:
        return AsyncMarketsResourceWithStreamingResponse(self._coins.markets)

    @cached_property
    def top_gainers_losers(self) -> AsyncTopGainersLosersResourceWithStreamingResponse:
        return AsyncTopGainersLosersResourceWithStreamingResponse(self._coins.top_gainers_losers)

    @cached_property
    def circulating_supply_chart(self) -> AsyncCirculatingSupplyChartResourceWithStreamingResponse:
        return AsyncCirculatingSupplyChartResourceWithStreamingResponse(self._coins.circulating_supply_chart)

    @cached_property
    def contract(self) -> AsyncContractResourceWithStreamingResponse:
        return AsyncContractResourceWithStreamingResponse(self._coins.contract)

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._coins.history)

    @cached_property
    def market_chart(self) -> AsyncMarketChartResourceWithStreamingResponse:
        return AsyncMarketChartResourceWithStreamingResponse(self._coins.market_chart)

    @cached_property
    def ohlc(self) -> AsyncOhlcResourceWithStreamingResponse:
        return AsyncOhlcResourceWithStreamingResponse(self._coins.ohlc)

    @cached_property
    def tickers(self) -> AsyncTickersResourceWithStreamingResponse:
        return AsyncTickersResourceWithStreamingResponse(self._coins.tickers)

    @cached_property
    def total_supply_chart(self) -> AsyncTotalSupplyChartResourceWithStreamingResponse:
        return AsyncTotalSupplyChartResourceWithStreamingResponse(self._coins.total_supply_chart)
