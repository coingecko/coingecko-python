# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
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
from ...._base_client import make_request_options
from ....types.coins.contract_get_response import ContractGetResponse

__all__ = ["ContractResource", "AsyncContractResource"]


class ContractResource(SyncAPIResource):
    @cached_property
    def market_chart(self) -> MarketChartResource:
        return MarketChartResource(self._client)

    @cached_property
    def with_raw_response(self) -> ContractResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return ContractResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContractResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return ContractResourceWithStreamingResponse(self)

    def get(
        self,
        contract_address: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContractGetResponse:
        """
        This endpoint allows you to **query all the metadata (image, websites, socials,
        description, contract address, etc.) and market data (price, ATH, exchange
        tickers, etc.) of a coin from the CoinGecko coin page based on an asset platform
        and a particular token contract address**

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not contract_address:
            raise ValueError(f"Expected a non-empty value for `contract_address` but received {contract_address!r}")
        return self._get(
            f"/coins/{id}/contract/{contract_address}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractGetResponse,
        )


class AsyncContractResource(AsyncAPIResource):
    @cached_property
    def market_chart(self) -> AsyncMarketChartResource:
        return AsyncMarketChartResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncContractResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return AsyncContractResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContractResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return AsyncContractResourceWithStreamingResponse(self)

    async def get(
        self,
        contract_address: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContractGetResponse:
        """
        This endpoint allows you to **query all the metadata (image, websites, socials,
        description, contract address, etc.) and market data (price, ATH, exchange
        tickers, etc.) of a coin from the CoinGecko coin page based on an asset platform
        and a particular token contract address**

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not contract_address:
            raise ValueError(f"Expected a non-empty value for `contract_address` but received {contract_address!r}")
        return await self._get(
            f"/coins/{id}/contract/{contract_address}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractGetResponse,
        )


class ContractResourceWithRawResponse:
    def __init__(self, contract: ContractResource) -> None:
        self._contract = contract

        self.get = to_raw_response_wrapper(
            contract.get,
        )

    @cached_property
    def market_chart(self) -> MarketChartResourceWithRawResponse:
        return MarketChartResourceWithRawResponse(self._contract.market_chart)


class AsyncContractResourceWithRawResponse:
    def __init__(self, contract: AsyncContractResource) -> None:
        self._contract = contract

        self.get = async_to_raw_response_wrapper(
            contract.get,
        )

    @cached_property
    def market_chart(self) -> AsyncMarketChartResourceWithRawResponse:
        return AsyncMarketChartResourceWithRawResponse(self._contract.market_chart)


class ContractResourceWithStreamingResponse:
    def __init__(self, contract: ContractResource) -> None:
        self._contract = contract

        self.get = to_streamed_response_wrapper(
            contract.get,
        )

    @cached_property
    def market_chart(self) -> MarketChartResourceWithStreamingResponse:
        return MarketChartResourceWithStreamingResponse(self._contract.market_chart)


class AsyncContractResourceWithStreamingResponse:
    def __init__(self, contract: AsyncContractResource) -> None:
        self._contract = contract

        self.get = async_to_streamed_response_wrapper(
            contract.get,
        )

    @cached_property
    def market_chart(self) -> AsyncMarketChartResourceWithStreamingResponse:
        return AsyncMarketChartResourceWithStreamingResponse(self._contract.market_chart)
