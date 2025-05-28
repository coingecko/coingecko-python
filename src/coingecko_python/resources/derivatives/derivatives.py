# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from .exchanges import (
    ExchangesResource,
    AsyncExchangesResource,
    ExchangesResourceWithRawResponse,
    AsyncExchangesResourceWithRawResponse,
    ExchangesResourceWithStreamingResponse,
    AsyncExchangesResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.derivative_get_response import DerivativeGetResponse

__all__ = ["DerivativesResource", "AsyncDerivativesResource"]


class DerivativesResource(SyncAPIResource):
    @cached_property
    def exchanges(self) -> ExchangesResource:
        return ExchangesResource(self._client)

    @cached_property
    def with_raw_response(self) -> DerivativesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return DerivativesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DerivativesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return DerivativesResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DerivativeGetResponse:
        """
        This endpoint allows you to **query all the tickers from derivatives exchanges
        on CoinGecko**
        """
        return self._get(
            "/derivatives",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DerivativeGetResponse,
        )


class AsyncDerivativesResource(AsyncAPIResource):
    @cached_property
    def exchanges(self) -> AsyncExchangesResource:
        return AsyncExchangesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDerivativesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDerivativesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDerivativesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return AsyncDerivativesResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DerivativeGetResponse:
        """
        This endpoint allows you to **query all the tickers from derivatives exchanges
        on CoinGecko**
        """
        return await self._get(
            "/derivatives",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DerivativeGetResponse,
        )


class DerivativesResourceWithRawResponse:
    def __init__(self, derivatives: DerivativesResource) -> None:
        self._derivatives = derivatives

        self.get = to_raw_response_wrapper(
            derivatives.get,
        )

    @cached_property
    def exchanges(self) -> ExchangesResourceWithRawResponse:
        return ExchangesResourceWithRawResponse(self._derivatives.exchanges)


class AsyncDerivativesResourceWithRawResponse:
    def __init__(self, derivatives: AsyncDerivativesResource) -> None:
        self._derivatives = derivatives

        self.get = async_to_raw_response_wrapper(
            derivatives.get,
        )

    @cached_property
    def exchanges(self) -> AsyncExchangesResourceWithRawResponse:
        return AsyncExchangesResourceWithRawResponse(self._derivatives.exchanges)


class DerivativesResourceWithStreamingResponse:
    def __init__(self, derivatives: DerivativesResource) -> None:
        self._derivatives = derivatives

        self.get = to_streamed_response_wrapper(
            derivatives.get,
        )

    @cached_property
    def exchanges(self) -> ExchangesResourceWithStreamingResponse:
        return ExchangesResourceWithStreamingResponse(self._derivatives.exchanges)


class AsyncDerivativesResourceWithStreamingResponse:
    def __init__(self, derivatives: AsyncDerivativesResource) -> None:
        self._derivatives = derivatives

        self.get = async_to_streamed_response_wrapper(
            derivatives.get,
        )

    @cached_property
    def exchanges(self) -> AsyncExchangesResourceWithStreamingResponse:
        return AsyncExchangesResourceWithStreamingResponse(self._derivatives.exchanges)
