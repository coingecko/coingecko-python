# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import path_template, maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.onchain.networks.wallets import transfer_get_params
from .....types.onchain.networks.wallets.transfer_get_response import TransferGetResponse

__all__ = ["TransfersResource", "AsyncTransfersResource"]


class TransfersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TransfersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return TransfersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TransfersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return TransfersResourceWithStreamingResponse(self)

    def get(
        self,
        address: str,
        *,
        network: str,
        token: str | Omit = omit,
        cursor: str | Omit = omit,
        direction: Literal["in", "out"] | Omit = omit,
        from_: str | Omit = omit,
        per_page: int | Omit = omit,
        to: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransferGetResponse:
        """
        To query the token transfers of a wallet address on a network

        Args:
          token: Filter transfers by token contract address.

          cursor: Cursor from the previous response, passed back unchanged to fetch the next page.

          direction: Filter transfers by direction, relative to the queried wallet. Omit to return
              both.

          from_: Starting date in ISO date string (`YYYY-MM-DD` or `YYYY-MM-DDTHH:MM`) or UNIX
              timestamp. **Use ISO date string for best compatibility.** Must be provided
              together with `to`.

          per_page: Total results per page. Default value: 100 Valid values: 1...300

          to: Ending date in ISO date string (`YYYY-MM-DD` or `YYYY-MM-DDTHH:MM`) or UNIX
              timestamp. **Use ISO date string for best compatibility.** Must be provided
              together with `from`.

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
            path_template("/onchain/networks/{network}/wallets/{address}/transfers", network=network, address=address),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "token": token,
                        "cursor": cursor,
                        "direction": direction,
                        "from_": from_,
                        "per_page": per_page,
                        "to": to,
                    },
                    transfer_get_params.TransferGetParams,
                ),
            ),
            cast_to=TransferGetResponse,
        )


class AsyncTransfersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTransfersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTransfersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTransfersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return AsyncTransfersResourceWithStreamingResponse(self)

    async def get(
        self,
        address: str,
        *,
        network: str,
        token: str | Omit = omit,
        cursor: str | Omit = omit,
        direction: Literal["in", "out"] | Omit = omit,
        from_: str | Omit = omit,
        per_page: int | Omit = omit,
        to: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransferGetResponse:
        """
        To query the token transfers of a wallet address on a network

        Args:
          token: Filter transfers by token contract address.

          cursor: Cursor from the previous response, passed back unchanged to fetch the next page.

          direction: Filter transfers by direction, relative to the queried wallet. Omit to return
              both.

          from_: Starting date in ISO date string (`YYYY-MM-DD` or `YYYY-MM-DDTHH:MM`) or UNIX
              timestamp. **Use ISO date string for best compatibility.** Must be provided
              together with `to`.

          per_page: Total results per page. Default value: 100 Valid values: 1...300

          to: Ending date in ISO date string (`YYYY-MM-DD` or `YYYY-MM-DDTHH:MM`) or UNIX
              timestamp. **Use ISO date string for best compatibility.** Must be provided
              together with `from`.

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
            path_template("/onchain/networks/{network}/wallets/{address}/transfers", network=network, address=address),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "token": token,
                        "cursor": cursor,
                        "direction": direction,
                        "from_": from_,
                        "per_page": per_page,
                        "to": to,
                    },
                    transfer_get_params.TransferGetParams,
                ),
            ),
            cast_to=TransferGetResponse,
        )


class TransfersResourceWithRawResponse:
    def __init__(self, transfers: TransfersResource) -> None:
        self._transfers = transfers

        self.get = to_raw_response_wrapper(
            transfers.get,
        )


class AsyncTransfersResourceWithRawResponse:
    def __init__(self, transfers: AsyncTransfersResource) -> None:
        self._transfers = transfers

        self.get = async_to_raw_response_wrapper(
            transfers.get,
        )


class TransfersResourceWithStreamingResponse:
    def __init__(self, transfers: TransfersResource) -> None:
        self._transfers = transfers

        self.get = to_streamed_response_wrapper(
            transfers.get,
        )


class AsyncTransfersResourceWithStreamingResponse:
    def __init__(self, transfers: AsyncTransfersResource) -> None:
        self._transfers = transfers

        self.get = async_to_streamed_response_wrapper(
            transfers.get,
        )
