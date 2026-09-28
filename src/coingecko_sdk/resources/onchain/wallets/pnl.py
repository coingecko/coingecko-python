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
from ....types.onchain.wallets import pnl_get_params
from ....types.onchain.wallets.pnl_get_response import PnlGetResponse

__all__ = ["PnlResource", "AsyncPnlResource"]


class PnlResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PnlResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return PnlResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PnlResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return PnlResourceWithStreamingResponse(self)

    def get(
        self,
        address: str,
        *,
        networks: str,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        sort: Literal["realized_pnl_usd_desc", "unrealized_pnl_usd_desc", "total_buy_usd_desc", "total_sell_usd_desc"]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PnlGetResponse:
        """
        To query the PnL of a wallet address across networks

        Args:
          networks: Query PnL by networks, comma-separated if more than one. \\**refers to
              [`/onchain/networks`](/reference/networks-list).

          page: Page through results. Default value: 1

          per_page: Total results per page. Default value: 100 Valid values: 1...300

          sort: Sort the token stats by field. Default: `realized_pnl_usd_desc`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not address:
            raise ValueError(f"Expected a non-empty value for `address` but received {address!r}")
        return self._get(
            path_template("/onchain/wallets/{address}/pnl", address=address),
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
                        "sort": sort,
                    },
                    pnl_get_params.PnlGetParams,
                ),
            ),
            cast_to=PnlGetResponse,
        )


class AsyncPnlResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPnlResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPnlResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPnlResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return AsyncPnlResourceWithStreamingResponse(self)

    async def get(
        self,
        address: str,
        *,
        networks: str,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        sort: Literal["realized_pnl_usd_desc", "unrealized_pnl_usd_desc", "total_buy_usd_desc", "total_sell_usd_desc"]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PnlGetResponse:
        """
        To query the PnL of a wallet address across networks

        Args:
          networks: Query PnL by networks, comma-separated if more than one. \\**refers to
              [`/onchain/networks`](/reference/networks-list).

          page: Page through results. Default value: 1

          per_page: Total results per page. Default value: 100 Valid values: 1...300

          sort: Sort the token stats by field. Default: `realized_pnl_usd_desc`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not address:
            raise ValueError(f"Expected a non-empty value for `address` but received {address!r}")
        return await self._get(
            path_template("/onchain/wallets/{address}/pnl", address=address),
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
                        "sort": sort,
                    },
                    pnl_get_params.PnlGetParams,
                ),
            ),
            cast_to=PnlGetResponse,
        )


class PnlResourceWithRawResponse:
    def __init__(self, pnl: PnlResource) -> None:
        self._pnl = pnl

        self.get = to_raw_response_wrapper(
            pnl.get,
        )


class AsyncPnlResourceWithRawResponse:
    def __init__(self, pnl: AsyncPnlResource) -> None:
        self._pnl = pnl

        self.get = async_to_raw_response_wrapper(
            pnl.get,
        )


class PnlResourceWithStreamingResponse:
    def __init__(self, pnl: PnlResource) -> None:
        self._pnl = pnl

        self.get = to_streamed_response_wrapper(
            pnl.get,
        )


class AsyncPnlResourceWithStreamingResponse:
    def __init__(self, pnl: AsyncPnlResource) -> None:
        self._pnl = pnl

        self.get = async_to_streamed_response_wrapper(
            pnl.get,
        )
