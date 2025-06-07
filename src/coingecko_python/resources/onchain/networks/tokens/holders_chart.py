# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.onchain.networks.tokens import holders_chart_get_params
from .....types.onchain.networks.tokens.holders_chart_get_response import HoldersChartGetResponse

__all__ = ["HoldersChartResource", "AsyncHoldersChartResource"]


class HoldersChartResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HoldersChartResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return HoldersChartResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HoldersChartResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return HoldersChartResourceWithStreamingResponse(self)

    def get(
        self,
        token_address: str,
        *,
        network: str,
        days: Literal["7", "30", "max"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HoldersChartGetResponse:
        """
        This endpoint allows you to **get the historical token holders chart based on
        the provided token contract address on a network**

        Args:
          days: number of days to return the historical token holders chart Default value: 7

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not network:
            raise ValueError(f"Expected a non-empty value for `network` but received {network!r}")
        if not token_address:
            raise ValueError(f"Expected a non-empty value for `token_address` but received {token_address!r}")
        return self._get(
            f"/onchain/networks/{network}/tokens/{token_address}/holders_chart",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"days": days}, holders_chart_get_params.HoldersChartGetParams),
            ),
            cast_to=HoldersChartGetResponse,
        )


class AsyncHoldersChartResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHoldersChartResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return AsyncHoldersChartResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHoldersChartResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return AsyncHoldersChartResourceWithStreamingResponse(self)

    async def get(
        self,
        token_address: str,
        *,
        network: str,
        days: Literal["7", "30", "max"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HoldersChartGetResponse:
        """
        This endpoint allows you to **get the historical token holders chart based on
        the provided token contract address on a network**

        Args:
          days: number of days to return the historical token holders chart Default value: 7

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not network:
            raise ValueError(f"Expected a non-empty value for `network` but received {network!r}")
        if not token_address:
            raise ValueError(f"Expected a non-empty value for `token_address` but received {token_address!r}")
        return await self._get(
            f"/onchain/networks/{network}/tokens/{token_address}/holders_chart",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"days": days}, holders_chart_get_params.HoldersChartGetParams),
            ),
            cast_to=HoldersChartGetResponse,
        )


class HoldersChartResourceWithRawResponse:
    def __init__(self, holders_chart: HoldersChartResource) -> None:
        self._holders_chart = holders_chart

        self.get = to_raw_response_wrapper(
            holders_chart.get,
        )


class AsyncHoldersChartResourceWithRawResponse:
    def __init__(self, holders_chart: AsyncHoldersChartResource) -> None:
        self._holders_chart = holders_chart

        self.get = async_to_raw_response_wrapper(
            holders_chart.get,
        )


class HoldersChartResourceWithStreamingResponse:
    def __init__(self, holders_chart: HoldersChartResource) -> None:
        self._holders_chart = holders_chart

        self.get = to_streamed_response_wrapper(
            holders_chart.get,
        )


class AsyncHoldersChartResourceWithStreamingResponse:
    def __init__(self, holders_chart: AsyncHoldersChartResource) -> None:
        self._holders_chart = holders_chart

        self.get = async_to_streamed_response_wrapper(
            holders_chart.get,
        )
