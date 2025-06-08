# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ....types.nfts.contract import market_chart_get_params
from ....types.nfts.contract.market_chart_get_response import MarketChartGetResponse

__all__ = ["MarketChartResource", "AsyncMarketChartResource"]


class MarketChartResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MarketChartResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return MarketChartResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MarketChartResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return MarketChartResourceWithStreamingResponse(self)

    def get(
        self,
        contract_address: str,
        *,
        asset_platform_id: str,
        days: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MarketChartGetResponse:
        """
        This endpoint allows you **query historical market data of a NFT collection,
        including floor price, market cap, and 24hr volume, by number of days away from
        now based on the provided contract address**

        Args:
          days: data up to number of days ago Valid values: any integer or max

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_platform_id:
            raise ValueError(f"Expected a non-empty value for `asset_platform_id` but received {asset_platform_id!r}")
        if not contract_address:
            raise ValueError(f"Expected a non-empty value for `contract_address` but received {contract_address!r}")
        return self._get(
            f"/nfts/{asset_platform_id}/contract/{contract_address}/market_chart",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"days": days}, market_chart_get_params.MarketChartGetParams),
            ),
            cast_to=MarketChartGetResponse,
        )


class AsyncMarketChartResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMarketChartResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMarketChartResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMarketChartResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return AsyncMarketChartResourceWithStreamingResponse(self)

    async def get(
        self,
        contract_address: str,
        *,
        asset_platform_id: str,
        days: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MarketChartGetResponse:
        """
        This endpoint allows you **query historical market data of a NFT collection,
        including floor price, market cap, and 24hr volume, by number of days away from
        now based on the provided contract address**

        Args:
          days: data up to number of days ago Valid values: any integer or max

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_platform_id:
            raise ValueError(f"Expected a non-empty value for `asset_platform_id` but received {asset_platform_id!r}")
        if not contract_address:
            raise ValueError(f"Expected a non-empty value for `contract_address` but received {contract_address!r}")
        return await self._get(
            f"/nfts/{asset_platform_id}/contract/{contract_address}/market_chart",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"days": days}, market_chart_get_params.MarketChartGetParams),
            ),
            cast_to=MarketChartGetResponse,
        )


class MarketChartResourceWithRawResponse:
    def __init__(self, market_chart: MarketChartResource) -> None:
        self._market_chart = market_chart

        self.get = to_raw_response_wrapper(
            market_chart.get,
        )


class AsyncMarketChartResourceWithRawResponse:
    def __init__(self, market_chart: AsyncMarketChartResource) -> None:
        self._market_chart = market_chart

        self.get = async_to_raw_response_wrapper(
            market_chart.get,
        )


class MarketChartResourceWithStreamingResponse:
    def __init__(self, market_chart: MarketChartResource) -> None:
        self._market_chart = market_chart

        self.get = to_streamed_response_wrapper(
            market_chart.get,
        )


class AsyncMarketChartResourceWithStreamingResponse:
    def __init__(self, market_chart: AsyncMarketChartResource) -> None:
        self._market_chart = market_chart

        self.get = async_to_streamed_response_wrapper(
            market_chart.get,
        )
