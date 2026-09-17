# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.onchain.wallets import balance_get_params
from ....types.onchain.wallets.balance_get_response import BalanceGetResponse

__all__ = ["BalancesResource", "AsyncBalancesResource"]


class BalancesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BalancesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return BalancesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BalancesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return BalancesResourceWithStreamingResponse(self)

    def get(
        self,
        address: str,
        *,
        networks: str,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        reserve_in_usd_min: float | Omit = omit,
        sort: Literal["value_usd_desc", "value_usd_asc"] | Omit = omit,
        token_type: Literal["native", "non_native"] | Omit = omit,
        value_usd_min: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BalanceGetResponse:
        """
        To query the token balances of a wallet address across networks

        Args:
          networks: Query balances by networks, comma-separated if more than one. \\**refers to
              [supported networks](/reference/wallet-token-balances#supported-networks).

          page: Page through results. Default value: 1

          per_page: Total results per page. Default value: 50 Valid values: 1...100

          reserve_in_usd_min: Minimum total reserve in USD of the holding's token.

          sort: Sort the holdings by field. Default: `value_usd_desc`

          token_type: Filter holdings by token type. Omit to return both.

          value_usd_min: Minimum holding value in USD.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not address:
            raise ValueError(f"Expected a non-empty value for `address` but received {address!r}")
        return self._get(
            path_template("/onchain/wallets/{address}/balances", address=address),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "networks": networks,
                        "page": page,
                        "per_page": per_page,
                        "reserve_in_usd_min": reserve_in_usd_min,
                        "sort": sort,
                        "token_type": token_type,
                        "value_usd_min": value_usd_min,
                    },
                    balance_get_params.BalanceGetParams,
                ),
            ),
            cast_to=BalanceGetResponse,
        )


class AsyncBalancesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBalancesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBalancesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBalancesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return AsyncBalancesResourceWithStreamingResponse(self)

    async def get(
        self,
        address: str,
        *,
        networks: str,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        reserve_in_usd_min: float | Omit = omit,
        sort: Literal["value_usd_desc", "value_usd_asc"] | Omit = omit,
        token_type: Literal["native", "non_native"] | Omit = omit,
        value_usd_min: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BalanceGetResponse:
        """
        To query the token balances of a wallet address across networks

        Args:
          networks: Query balances by networks, comma-separated if more than one. \\**refers to
              [supported networks](/reference/wallet-token-balances#supported-networks).

          page: Page through results. Default value: 1

          per_page: Total results per page. Default value: 50 Valid values: 1...100

          reserve_in_usd_min: Minimum total reserve in USD of the holding's token.

          sort: Sort the holdings by field. Default: `value_usd_desc`

          token_type: Filter holdings by token type. Omit to return both.

          value_usd_min: Minimum holding value in USD.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not address:
            raise ValueError(f"Expected a non-empty value for `address` but received {address!r}")
        return await self._get(
            path_template("/onchain/wallets/{address}/balances", address=address),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "networks": networks,
                        "page": page,
                        "per_page": per_page,
                        "reserve_in_usd_min": reserve_in_usd_min,
                        "sort": sort,
                        "token_type": token_type,
                        "value_usd_min": value_usd_min,
                    },
                    balance_get_params.BalanceGetParams,
                ),
            ),
            cast_to=BalanceGetResponse,
        )


class BalancesResourceWithRawResponse:
    def __init__(self, balances: BalancesResource) -> None:
        self._balances = balances

        self.get = to_raw_response_wrapper(
            balances.get,
        )


class AsyncBalancesResourceWithRawResponse:
    def __init__(self, balances: AsyncBalancesResource) -> None:
        self._balances = balances

        self.get = async_to_raw_response_wrapper(
            balances.get,
        )


class BalancesResourceWithStreamingResponse:
    def __init__(self, balances: BalancesResource) -> None:
        self._balances = balances

        self.get = to_streamed_response_wrapper(
            balances.get,
        )


class AsyncBalancesResourceWithStreamingResponse:
    def __init__(self, balances: AsyncBalancesResource) -> None:
        self._balances = balances

        self.get = async_to_streamed_response_wrapper(
            balances.get,
        )
