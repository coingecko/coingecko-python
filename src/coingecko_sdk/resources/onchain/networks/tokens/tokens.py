# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .info import (
    InfoResource,
    AsyncInfoResource,
    InfoResourceWithRawResponse,
    AsyncInfoResourceWithRawResponse,
    InfoResourceWithStreamingResponse,
    AsyncInfoResourceWithStreamingResponse,
)
from .multi import (
    MultiResource,
    AsyncMultiResource,
    MultiResourceWithRawResponse,
    AsyncMultiResourceWithRawResponse,
    MultiResourceWithStreamingResponse,
    AsyncMultiResourceWithStreamingResponse,
)
from .ohlcv import (
    OhlcvResource,
    AsyncOhlcvResource,
    OhlcvResourceWithRawResponse,
    AsyncOhlcvResourceWithRawResponse,
    OhlcvResourceWithStreamingResponse,
    AsyncOhlcvResourceWithStreamingResponse,
)
from .pools import (
    PoolsResource,
    AsyncPoolsResource,
    PoolsResourceWithRawResponse,
    AsyncPoolsResourceWithRawResponse,
    PoolsResourceWithStreamingResponse,
    AsyncPoolsResourceWithStreamingResponse,
)
from .trades import (
    TradesResource,
    AsyncTradesResource,
    TradesResourceWithRawResponse,
    AsyncTradesResourceWithRawResponse,
    TradesResourceWithStreamingResponse,
    AsyncTradesResourceWithStreamingResponse,
)
from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from .top_holders import (
    TopHoldersResource,
    AsyncTopHoldersResource,
    TopHoldersResourceWithRawResponse,
    AsyncTopHoldersResourceWithRawResponse,
    TopHoldersResourceWithStreamingResponse,
    AsyncTopHoldersResourceWithStreamingResponse,
)
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .holders_chart import (
    HoldersChartResource,
    AsyncHoldersChartResource,
    HoldersChartResourceWithRawResponse,
    AsyncHoldersChartResourceWithRawResponse,
    HoldersChartResourceWithStreamingResponse,
    AsyncHoldersChartResourceWithStreamingResponse,
)
from ....._base_client import make_request_options
from .....types.onchain.networks import token_get_address_params
from .....types.onchain.networks.token_get_address_response import TokenGetAddressResponse

__all__ = ["TokensResource", "AsyncTokensResource"]


class TokensResource(SyncAPIResource):
    @cached_property
    def multi(self) -> MultiResource:
        return MultiResource(self._client)

    @cached_property
    def info(self) -> InfoResource:
        return InfoResource(self._client)

    @cached_property
    def top_holders(self) -> TopHoldersResource:
        return TopHoldersResource(self._client)

    @cached_property
    def holders_chart(self) -> HoldersChartResource:
        return HoldersChartResource(self._client)

    @cached_property
    def ohlcv(self) -> OhlcvResource:
        return OhlcvResource(self._client)

    @cached_property
    def pools(self) -> PoolsResource:
        return PoolsResource(self._client)

    @cached_property
    def trades(self) -> TradesResource:
        return TradesResource(self._client)

    @cached_property
    def with_raw_response(self) -> TokensResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return TokensResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TokensResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return TokensResourceWithStreamingResponse(self)

    def get_address(
        self,
        address: str,
        *,
        network: str,
        include: Literal["top_pools"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TokenGetAddressResponse:
        """
        This endpoint allows you to **query specific token data based on the provided
        token contract address on a network**

        Args:
          include: attributes to include

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not network:
            raise ValueError(f"Expected a non-empty value for `network` but received {network!r}")
        if not address:
            raise ValueError(f"Expected a non-empty value for `address` but received {address!r}")
        return self._get(
            f"/onchain/networks/{network}/tokens/{address}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"include": include}, token_get_address_params.TokenGetAddressParams),
            ),
            cast_to=TokenGetAddressResponse,
        )


class AsyncTokensResource(AsyncAPIResource):
    @cached_property
    def multi(self) -> AsyncMultiResource:
        return AsyncMultiResource(self._client)

    @cached_property
    def info(self) -> AsyncInfoResource:
        return AsyncInfoResource(self._client)

    @cached_property
    def top_holders(self) -> AsyncTopHoldersResource:
        return AsyncTopHoldersResource(self._client)

    @cached_property
    def holders_chart(self) -> AsyncHoldersChartResource:
        return AsyncHoldersChartResource(self._client)

    @cached_property
    def ohlcv(self) -> AsyncOhlcvResource:
        return AsyncOhlcvResource(self._client)

    @cached_property
    def pools(self) -> AsyncPoolsResource:
        return AsyncPoolsResource(self._client)

    @cached_property
    def trades(self) -> AsyncTradesResource:
        return AsyncTradesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTokensResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTokensResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTokensResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return AsyncTokensResourceWithStreamingResponse(self)

    async def get_address(
        self,
        address: str,
        *,
        network: str,
        include: Literal["top_pools"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TokenGetAddressResponse:
        """
        This endpoint allows you to **query specific token data based on the provided
        token contract address on a network**

        Args:
          include: attributes to include

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not network:
            raise ValueError(f"Expected a non-empty value for `network` but received {network!r}")
        if not address:
            raise ValueError(f"Expected a non-empty value for `address` but received {address!r}")
        return await self._get(
            f"/onchain/networks/{network}/tokens/{address}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"include": include}, token_get_address_params.TokenGetAddressParams),
            ),
            cast_to=TokenGetAddressResponse,
        )


class TokensResourceWithRawResponse:
    def __init__(self, tokens: TokensResource) -> None:
        self._tokens = tokens

        self.get_address = to_raw_response_wrapper(
            tokens.get_address,
        )

    @cached_property
    def multi(self) -> MultiResourceWithRawResponse:
        return MultiResourceWithRawResponse(self._tokens.multi)

    @cached_property
    def info(self) -> InfoResourceWithRawResponse:
        return InfoResourceWithRawResponse(self._tokens.info)

    @cached_property
    def top_holders(self) -> TopHoldersResourceWithRawResponse:
        return TopHoldersResourceWithRawResponse(self._tokens.top_holders)

    @cached_property
    def holders_chart(self) -> HoldersChartResourceWithRawResponse:
        return HoldersChartResourceWithRawResponse(self._tokens.holders_chart)

    @cached_property
    def ohlcv(self) -> OhlcvResourceWithRawResponse:
        return OhlcvResourceWithRawResponse(self._tokens.ohlcv)

    @cached_property
    def pools(self) -> PoolsResourceWithRawResponse:
        return PoolsResourceWithRawResponse(self._tokens.pools)

    @cached_property
    def trades(self) -> TradesResourceWithRawResponse:
        return TradesResourceWithRawResponse(self._tokens.trades)


class AsyncTokensResourceWithRawResponse:
    def __init__(self, tokens: AsyncTokensResource) -> None:
        self._tokens = tokens

        self.get_address = async_to_raw_response_wrapper(
            tokens.get_address,
        )

    @cached_property
    def multi(self) -> AsyncMultiResourceWithRawResponse:
        return AsyncMultiResourceWithRawResponse(self._tokens.multi)

    @cached_property
    def info(self) -> AsyncInfoResourceWithRawResponse:
        return AsyncInfoResourceWithRawResponse(self._tokens.info)

    @cached_property
    def top_holders(self) -> AsyncTopHoldersResourceWithRawResponse:
        return AsyncTopHoldersResourceWithRawResponse(self._tokens.top_holders)

    @cached_property
    def holders_chart(self) -> AsyncHoldersChartResourceWithRawResponse:
        return AsyncHoldersChartResourceWithRawResponse(self._tokens.holders_chart)

    @cached_property
    def ohlcv(self) -> AsyncOhlcvResourceWithRawResponse:
        return AsyncOhlcvResourceWithRawResponse(self._tokens.ohlcv)

    @cached_property
    def pools(self) -> AsyncPoolsResourceWithRawResponse:
        return AsyncPoolsResourceWithRawResponse(self._tokens.pools)

    @cached_property
    def trades(self) -> AsyncTradesResourceWithRawResponse:
        return AsyncTradesResourceWithRawResponse(self._tokens.trades)


class TokensResourceWithStreamingResponse:
    def __init__(self, tokens: TokensResource) -> None:
        self._tokens = tokens

        self.get_address = to_streamed_response_wrapper(
            tokens.get_address,
        )

    @cached_property
    def multi(self) -> MultiResourceWithStreamingResponse:
        return MultiResourceWithStreamingResponse(self._tokens.multi)

    @cached_property
    def info(self) -> InfoResourceWithStreamingResponse:
        return InfoResourceWithStreamingResponse(self._tokens.info)

    @cached_property
    def top_holders(self) -> TopHoldersResourceWithStreamingResponse:
        return TopHoldersResourceWithStreamingResponse(self._tokens.top_holders)

    @cached_property
    def holders_chart(self) -> HoldersChartResourceWithStreamingResponse:
        return HoldersChartResourceWithStreamingResponse(self._tokens.holders_chart)

    @cached_property
    def ohlcv(self) -> OhlcvResourceWithStreamingResponse:
        return OhlcvResourceWithStreamingResponse(self._tokens.ohlcv)

    @cached_property
    def pools(self) -> PoolsResourceWithStreamingResponse:
        return PoolsResourceWithStreamingResponse(self._tokens.pools)

    @cached_property
    def trades(self) -> TradesResourceWithStreamingResponse:
        return TradesResourceWithStreamingResponse(self._tokens.trades)


class AsyncTokensResourceWithStreamingResponse:
    def __init__(self, tokens: AsyncTokensResource) -> None:
        self._tokens = tokens

        self.get_address = async_to_streamed_response_wrapper(
            tokens.get_address,
        )

    @cached_property
    def multi(self) -> AsyncMultiResourceWithStreamingResponse:
        return AsyncMultiResourceWithStreamingResponse(self._tokens.multi)

    @cached_property
    def info(self) -> AsyncInfoResourceWithStreamingResponse:
        return AsyncInfoResourceWithStreamingResponse(self._tokens.info)

    @cached_property
    def top_holders(self) -> AsyncTopHoldersResourceWithStreamingResponse:
        return AsyncTopHoldersResourceWithStreamingResponse(self._tokens.top_holders)

    @cached_property
    def holders_chart(self) -> AsyncHoldersChartResourceWithStreamingResponse:
        return AsyncHoldersChartResourceWithStreamingResponse(self._tokens.holders_chart)

    @cached_property
    def ohlcv(self) -> AsyncOhlcvResourceWithStreamingResponse:
        return AsyncOhlcvResourceWithStreamingResponse(self._tokens.ohlcv)

    @cached_property
    def pools(self) -> AsyncPoolsResourceWithStreamingResponse:
        return AsyncPoolsResourceWithStreamingResponse(self._tokens.pools)

    @cached_property
    def trades(self) -> AsyncTradesResourceWithStreamingResponse:
        return AsyncTradesResourceWithStreamingResponse(self._tokens.trades)
