# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from .market_cap_chart import (
    MarketCapChartResource,
    AsyncMarketCapChartResource,
    MarketCapChartResourceWithRawResponse,
    AsyncMarketCapChartResourceWithRawResponse,
    MarketCapChartResourceWithStreamingResponse,
    AsyncMarketCapChartResourceWithStreamingResponse,
)
from .decentralized_finance_defi import (
    DecentralizedFinanceDefiResource,
    AsyncDecentralizedFinanceDefiResource,
    DecentralizedFinanceDefiResourceWithRawResponse,
    AsyncDecentralizedFinanceDefiResourceWithRawResponse,
    DecentralizedFinanceDefiResourceWithStreamingResponse,
    AsyncDecentralizedFinanceDefiResourceWithStreamingResponse,
)
from ...types.global_get_response import GlobalGetResponse

__all__ = ["GlobalResource", "AsyncGlobalResource"]


class GlobalResource(SyncAPIResource):
    @cached_property
    def decentralized_finance_defi(self) -> DecentralizedFinanceDefiResource:
        return DecentralizedFinanceDefiResource(self._client)

    @cached_property
    def market_cap_chart(self) -> MarketCapChartResource:
        return MarketCapChartResource(self._client)

    @cached_property
    def with_raw_response(self) -> GlobalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return GlobalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GlobalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return GlobalResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GlobalGetResponse:
        """
        This endpoint allows you **query cryptocurrency global data including active
        cryptocurrencies, markets, total crypto market cap and etc**
        """
        return self._get(
            "/global",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GlobalGetResponse,
        )


class AsyncGlobalResource(AsyncAPIResource):
    @cached_property
    def decentralized_finance_defi(self) -> AsyncDecentralizedFinanceDefiResource:
        return AsyncDecentralizedFinanceDefiResource(self._client)

    @cached_property
    def market_cap_chart(self) -> AsyncMarketCapChartResource:
        return AsyncMarketCapChartResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncGlobalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGlobalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGlobalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return AsyncGlobalResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GlobalGetResponse:
        """
        This endpoint allows you **query cryptocurrency global data including active
        cryptocurrencies, markets, total crypto market cap and etc**
        """
        return await self._get(
            "/global",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GlobalGetResponse,
        )


class GlobalResourceWithRawResponse:
    def __init__(self, global_: GlobalResource) -> None:
        self._global_ = global_

        self.get = to_raw_response_wrapper(
            global_.get,
        )

    @cached_property
    def decentralized_finance_defi(self) -> DecentralizedFinanceDefiResourceWithRawResponse:
        return DecentralizedFinanceDefiResourceWithRawResponse(self._global_.decentralized_finance_defi)

    @cached_property
    def market_cap_chart(self) -> MarketCapChartResourceWithRawResponse:
        return MarketCapChartResourceWithRawResponse(self._global_.market_cap_chart)


class AsyncGlobalResourceWithRawResponse:
    def __init__(self, global_: AsyncGlobalResource) -> None:
        self._global_ = global_

        self.get = async_to_raw_response_wrapper(
            global_.get,
        )

    @cached_property
    def decentralized_finance_defi(self) -> AsyncDecentralizedFinanceDefiResourceWithRawResponse:
        return AsyncDecentralizedFinanceDefiResourceWithRawResponse(self._global_.decentralized_finance_defi)

    @cached_property
    def market_cap_chart(self) -> AsyncMarketCapChartResourceWithRawResponse:
        return AsyncMarketCapChartResourceWithRawResponse(self._global_.market_cap_chart)


class GlobalResourceWithStreamingResponse:
    def __init__(self, global_: GlobalResource) -> None:
        self._global_ = global_

        self.get = to_streamed_response_wrapper(
            global_.get,
        )

    @cached_property
    def decentralized_finance_defi(self) -> DecentralizedFinanceDefiResourceWithStreamingResponse:
        return DecentralizedFinanceDefiResourceWithStreamingResponse(self._global_.decentralized_finance_defi)

    @cached_property
    def market_cap_chart(self) -> MarketCapChartResourceWithStreamingResponse:
        return MarketCapChartResourceWithStreamingResponse(self._global_.market_cap_chart)


class AsyncGlobalResourceWithStreamingResponse:
    def __init__(self, global_: AsyncGlobalResource) -> None:
        self._global_ = global_

        self.get = async_to_streamed_response_wrapper(
            global_.get,
        )

    @cached_property
    def decentralized_finance_defi(self) -> AsyncDecentralizedFinanceDefiResourceWithStreamingResponse:
        return AsyncDecentralizedFinanceDefiResourceWithStreamingResponse(self._global_.decentralized_finance_defi)

    @cached_property
    def market_cap_chart(self) -> AsyncMarketCapChartResourceWithStreamingResponse:
        return AsyncMarketCapChartResourceWithStreamingResponse(self._global_.market_cap_chart)
