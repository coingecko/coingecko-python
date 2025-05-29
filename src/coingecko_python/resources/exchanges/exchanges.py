# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...types import exchange_get_params, exchange_get_id_params, exchange_get_list_params
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
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .volume_chart import (
    VolumeChartResource,
    AsyncVolumeChartResource,
    VolumeChartResourceWithRawResponse,
    AsyncVolumeChartResourceWithRawResponse,
    VolumeChartResourceWithStreamingResponse,
    AsyncVolumeChartResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from ...types.exchange_get_response import ExchangeGetResponse
from ...types.exchange_get_id_response import ExchangeGetIDResponse
from ...types.exchange_get_list_response import ExchangeGetListResponse

__all__ = ["ExchangesResource", "AsyncExchangesResource"]


class ExchangesResource(SyncAPIResource):
    @cached_property
    def tickers(self) -> TickersResource:
        return TickersResource(self._client)

    @cached_property
    def volume_chart(self) -> VolumeChartResource:
        return VolumeChartResource(self._client)

    @cached_property
    def with_raw_response(self) -> ExchangesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return ExchangesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExchangesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return ExchangesResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExchangeGetResponse:
        """
        This endpoint allows you to **query all the supported exchanges with exchanges’
        data (ID, name, country, ...) that have active trading volumes on CoinGecko**

        Args:
          page: page through results, default: 1

          per_page: total results per page, default: 100 Valid values: 1...250

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/exchanges",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    exchange_get_params.ExchangeGetParams,
                ),
            ),
            cast_to=ExchangeGetResponse,
        )

    def get_id(
        self,
        id: str,
        *,
        dex_pair_format: Literal["contract_address", "symbol"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExchangeGetIDResponse:
        """
        This endpoint allows you to **query exchange’s data (name, year established,
        country, ...), exchange volume in BTC and top 100 tickers based on exchange’s
        ID**

        Args:
          dex_pair_format:
              set to `symbol` to display DEX pair base and target as symbols, default:
              `contract_address`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/exchanges/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"dex_pair_format": dex_pair_format}, exchange_get_id_params.ExchangeGetIDParams),
            ),
            cast_to=ExchangeGetIDResponse,
        )

    def get_list(
        self,
        *,
        status: Literal["active", "inactive"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExchangeGetListResponse:
        """
        This endpoint allows you to **query all the exchanges with ID and name**

        Args:
          status: filter by status of exchanges, default: active

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/exchanges/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"status": status}, exchange_get_list_params.ExchangeGetListParams),
            ),
            cast_to=ExchangeGetListResponse,
        )


class AsyncExchangesResource(AsyncAPIResource):
    @cached_property
    def tickers(self) -> AsyncTickersResource:
        return AsyncTickersResource(self._client)

    @cached_property
    def volume_chart(self) -> AsyncVolumeChartResource:
        return AsyncVolumeChartResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncExchangesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExchangesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExchangesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return AsyncExchangesResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExchangeGetResponse:
        """
        This endpoint allows you to **query all the supported exchanges with exchanges’
        data (ID, name, country, ...) that have active trading volumes on CoinGecko**

        Args:
          page: page through results, default: 1

          per_page: total results per page, default: 100 Valid values: 1...250

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/exchanges",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    exchange_get_params.ExchangeGetParams,
                ),
            ),
            cast_to=ExchangeGetResponse,
        )

    async def get_id(
        self,
        id: str,
        *,
        dex_pair_format: Literal["contract_address", "symbol"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExchangeGetIDResponse:
        """
        This endpoint allows you to **query exchange’s data (name, year established,
        country, ...), exchange volume in BTC and top 100 tickers based on exchange’s
        ID**

        Args:
          dex_pair_format:
              set to `symbol` to display DEX pair base and target as symbols, default:
              `contract_address`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/exchanges/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"dex_pair_format": dex_pair_format}, exchange_get_id_params.ExchangeGetIDParams
                ),
            ),
            cast_to=ExchangeGetIDResponse,
        )

    async def get_list(
        self,
        *,
        status: Literal["active", "inactive"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExchangeGetListResponse:
        """
        This endpoint allows you to **query all the exchanges with ID and name**

        Args:
          status: filter by status of exchanges, default: active

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/exchanges/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"status": status}, exchange_get_list_params.ExchangeGetListParams),
            ),
            cast_to=ExchangeGetListResponse,
        )


class ExchangesResourceWithRawResponse:
    def __init__(self, exchanges: ExchangesResource) -> None:
        self._exchanges = exchanges

        self.get = to_raw_response_wrapper(
            exchanges.get,
        )
        self.get_id = to_raw_response_wrapper(
            exchanges.get_id,
        )
        self.get_list = to_raw_response_wrapper(
            exchanges.get_list,
        )

    @cached_property
    def tickers(self) -> TickersResourceWithRawResponse:
        return TickersResourceWithRawResponse(self._exchanges.tickers)

    @cached_property
    def volume_chart(self) -> VolumeChartResourceWithRawResponse:
        return VolumeChartResourceWithRawResponse(self._exchanges.volume_chart)


class AsyncExchangesResourceWithRawResponse:
    def __init__(self, exchanges: AsyncExchangesResource) -> None:
        self._exchanges = exchanges

        self.get = async_to_raw_response_wrapper(
            exchanges.get,
        )
        self.get_id = async_to_raw_response_wrapper(
            exchanges.get_id,
        )
        self.get_list = async_to_raw_response_wrapper(
            exchanges.get_list,
        )

    @cached_property
    def tickers(self) -> AsyncTickersResourceWithRawResponse:
        return AsyncTickersResourceWithRawResponse(self._exchanges.tickers)

    @cached_property
    def volume_chart(self) -> AsyncVolumeChartResourceWithRawResponse:
        return AsyncVolumeChartResourceWithRawResponse(self._exchanges.volume_chart)


class ExchangesResourceWithStreamingResponse:
    def __init__(self, exchanges: ExchangesResource) -> None:
        self._exchanges = exchanges

        self.get = to_streamed_response_wrapper(
            exchanges.get,
        )
        self.get_id = to_streamed_response_wrapper(
            exchanges.get_id,
        )
        self.get_list = to_streamed_response_wrapper(
            exchanges.get_list,
        )

    @cached_property
    def tickers(self) -> TickersResourceWithStreamingResponse:
        return TickersResourceWithStreamingResponse(self._exchanges.tickers)

    @cached_property
    def volume_chart(self) -> VolumeChartResourceWithStreamingResponse:
        return VolumeChartResourceWithStreamingResponse(self._exchanges.volume_chart)


class AsyncExchangesResourceWithStreamingResponse:
    def __init__(self, exchanges: AsyncExchangesResource) -> None:
        self._exchanges = exchanges

        self.get = async_to_streamed_response_wrapper(
            exchanges.get,
        )
        self.get_id = async_to_streamed_response_wrapper(
            exchanges.get_id,
        )
        self.get_list = async_to_streamed_response_wrapper(
            exchanges.get_list,
        )

    @cached_property
    def tickers(self) -> AsyncTickersResourceWithStreamingResponse:
        return AsyncTickersResourceWithStreamingResponse(self._exchanges.tickers)

    @cached_property
    def volume_chart(self) -> AsyncVolumeChartResourceWithStreamingResponse:
        return AsyncVolumeChartResourceWithStreamingResponse(self._exchanges.volume_chart)
