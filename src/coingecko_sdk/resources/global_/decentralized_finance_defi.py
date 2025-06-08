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
from ...types.global_.decentralized_finance_defi_get_response import DecentralizedFinanceDefiGetResponse

__all__ = ["DecentralizedFinanceDefiResource", "AsyncDecentralizedFinanceDefiResource"]


class DecentralizedFinanceDefiResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DecentralizedFinanceDefiResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return DecentralizedFinanceDefiResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DecentralizedFinanceDefiResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return DecentralizedFinanceDefiResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DecentralizedFinanceDefiGetResponse:
        """
        This endpoint allows you **query top 100 cryptocurrency global decentralized
        finance (DeFi) data including DeFi market cap, trading volume**
        """
        return self._get(
            "/global/decentralized_finance_defi",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DecentralizedFinanceDefiGetResponse,
        )


class AsyncDecentralizedFinanceDefiResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDecentralizedFinanceDefiResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDecentralizedFinanceDefiResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDecentralizedFinanceDefiResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return AsyncDecentralizedFinanceDefiResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DecentralizedFinanceDefiGetResponse:
        """
        This endpoint allows you **query top 100 cryptocurrency global decentralized
        finance (DeFi) data including DeFi market cap, trading volume**
        """
        return await self._get(
            "/global/decentralized_finance_defi",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DecentralizedFinanceDefiGetResponse,
        )


class DecentralizedFinanceDefiResourceWithRawResponse:
    def __init__(self, decentralized_finance_defi: DecentralizedFinanceDefiResource) -> None:
        self._decentralized_finance_defi = decentralized_finance_defi

        self.get = to_raw_response_wrapper(
            decentralized_finance_defi.get,
        )


class AsyncDecentralizedFinanceDefiResourceWithRawResponse:
    def __init__(self, decentralized_finance_defi: AsyncDecentralizedFinanceDefiResource) -> None:
        self._decentralized_finance_defi = decentralized_finance_defi

        self.get = async_to_raw_response_wrapper(
            decentralized_finance_defi.get,
        )


class DecentralizedFinanceDefiResourceWithStreamingResponse:
    def __init__(self, decentralized_finance_defi: DecentralizedFinanceDefiResource) -> None:
        self._decentralized_finance_defi = decentralized_finance_defi

        self.get = to_streamed_response_wrapper(
            decentralized_finance_defi.get,
        )


class AsyncDecentralizedFinanceDefiResourceWithStreamingResponse:
    def __init__(self, decentralized_finance_defi: AsyncDecentralizedFinanceDefiResource) -> None:
        self._decentralized_finance_defi = decentralized_finance_defi

        self.get = async_to_streamed_response_wrapper(
            decentralized_finance_defi.get,
        )
