# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import public_treasury_get_holding_chart_params, public_treasury_get_transaction_history_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.public_treasury_get_coin_id_response import PublicTreasuryGetCoinIDResponse
from ..types.public_treasury_get_entity_id_response import PublicTreasuryGetEntityIDResponse
from ..types.public_treasury_get_holding_chart_response import PublicTreasuryGetHoldingChartResponse
from ..types.public_treasury_get_transaction_history_response import PublicTreasuryGetTransactionHistoryResponse

__all__ = ["PublicTreasuryResource", "AsyncPublicTreasuryResource"]


class PublicTreasuryResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PublicTreasuryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return PublicTreasuryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PublicTreasuryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return PublicTreasuryResourceWithStreamingResponse(self)

    def get_coin_id(
        self,
        coin_id: str,
        *,
        entity: Literal["companies", "governments"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicTreasuryGetCoinIDResponse:
        """
        This endpoint allows you **query public companies & governments' cryptocurrency
        holdings** by Coin ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity:
            raise ValueError(f"Expected a non-empty value for `entity` but received {entity!r}")
        if not coin_id:
            raise ValueError(f"Expected a non-empty value for `coin_id` but received {coin_id!r}")
        return self._get(
            f"/{entity}/public_treasury/{coin_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicTreasuryGetCoinIDResponse,
        )

    def get_entity_id(
        self,
        entity_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicTreasuryGetEntityIDResponse:
        """
        This endpoint allows you **query public companies & governments' cryptocurrency
        holdings** by Entity ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return self._get(
            f"/public_treasury/{entity_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicTreasuryGetEntityIDResponse,
        )

    def get_holding_chart(
        self,
        coin_id: str,
        *,
        entity_id: str,
        days: str,
        include_empty_intervals: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicTreasuryGetHoldingChartResponse:
        """
        This endpoint allows you to **query historical cryptocurrency holdings chart of
        public companies & governments** by Entity ID and Coin ID

        Args:
          days: data up to number of days ago Valid values: `7, 14, 30, 90, 180, 365, 730, max`

          include_empty_intervals: include empty intervals with no transaction data, default: false

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        if not coin_id:
            raise ValueError(f"Expected a non-empty value for `coin_id` but received {coin_id!r}")
        return self._get(
            f"/public_treasury/{entity_id}/{coin_id}/holding_chart",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "days": days,
                        "include_empty_intervals": include_empty_intervals,
                    },
                    public_treasury_get_holding_chart_params.PublicTreasuryGetHoldingChartParams,
                ),
            ),
            cast_to=PublicTreasuryGetHoldingChartResponse,
        )

    def get_transaction_history(
        self,
        entity_id: str,
        *,
        coin_ids: str | Omit = omit,
        order: Literal[
            "date_desc",
            "date_asc",
            "holding_net_change_desc",
            "holding_net_change_asc",
            "transaction_value_usd_desc",
            "transaction_value_usd_asc",
            "average_cost_desc",
            "average_cost_asc",
        ]
        | Omit = omit,
        page: float | Omit = omit,
        per_page: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicTreasuryGetTransactionHistoryResponse:
        """
        This endpoint allows you **query public companies & governments' cryptocurrency
        transaction history** by Entity ID

        Args:
          coin_ids: filter transactions by coin IDs, comma-separated if querying more than 1 coin
              \\**refers to [`/coins/list`](/reference/coins-list).

          order: use this to sort the order of transactions, default: `date_desc`

          page: page through results, default: `1`

          per_page: total results per page, default: `100` Valid values: 1...250

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return self._get(
            f"/public_treasury/{entity_id}/transaction_history",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "coin_ids": coin_ids,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                    },
                    public_treasury_get_transaction_history_params.PublicTreasuryGetTransactionHistoryParams,
                ),
            ),
            cast_to=PublicTreasuryGetTransactionHistoryResponse,
        )


class AsyncPublicTreasuryResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPublicTreasuryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPublicTreasuryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPublicTreasuryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return AsyncPublicTreasuryResourceWithStreamingResponse(self)

    async def get_coin_id(
        self,
        coin_id: str,
        *,
        entity: Literal["companies", "governments"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicTreasuryGetCoinIDResponse:
        """
        This endpoint allows you **query public companies & governments' cryptocurrency
        holdings** by Coin ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity:
            raise ValueError(f"Expected a non-empty value for `entity` but received {entity!r}")
        if not coin_id:
            raise ValueError(f"Expected a non-empty value for `coin_id` but received {coin_id!r}")
        return await self._get(
            f"/{entity}/public_treasury/{coin_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicTreasuryGetCoinIDResponse,
        )

    async def get_entity_id(
        self,
        entity_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicTreasuryGetEntityIDResponse:
        """
        This endpoint allows you **query public companies & governments' cryptocurrency
        holdings** by Entity ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return await self._get(
            f"/public_treasury/{entity_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicTreasuryGetEntityIDResponse,
        )

    async def get_holding_chart(
        self,
        coin_id: str,
        *,
        entity_id: str,
        days: str,
        include_empty_intervals: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicTreasuryGetHoldingChartResponse:
        """
        This endpoint allows you to **query historical cryptocurrency holdings chart of
        public companies & governments** by Entity ID and Coin ID

        Args:
          days: data up to number of days ago Valid values: `7, 14, 30, 90, 180, 365, 730, max`

          include_empty_intervals: include empty intervals with no transaction data, default: false

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        if not coin_id:
            raise ValueError(f"Expected a non-empty value for `coin_id` but received {coin_id!r}")
        return await self._get(
            f"/public_treasury/{entity_id}/{coin_id}/holding_chart",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "days": days,
                        "include_empty_intervals": include_empty_intervals,
                    },
                    public_treasury_get_holding_chart_params.PublicTreasuryGetHoldingChartParams,
                ),
            ),
            cast_to=PublicTreasuryGetHoldingChartResponse,
        )

    async def get_transaction_history(
        self,
        entity_id: str,
        *,
        coin_ids: str | Omit = omit,
        order: Literal[
            "date_desc",
            "date_asc",
            "holding_net_change_desc",
            "holding_net_change_asc",
            "transaction_value_usd_desc",
            "transaction_value_usd_asc",
            "average_cost_desc",
            "average_cost_asc",
        ]
        | Omit = omit,
        page: float | Omit = omit,
        per_page: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicTreasuryGetTransactionHistoryResponse:
        """
        This endpoint allows you **query public companies & governments' cryptocurrency
        transaction history** by Entity ID

        Args:
          coin_ids: filter transactions by coin IDs, comma-separated if querying more than 1 coin
              \\**refers to [`/coins/list`](/reference/coins-list).

          order: use this to sort the order of transactions, default: `date_desc`

          page: page through results, default: `1`

          per_page: total results per page, default: `100` Valid values: 1...250

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return await self._get(
            f"/public_treasury/{entity_id}/transaction_history",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "coin_ids": coin_ids,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                    },
                    public_treasury_get_transaction_history_params.PublicTreasuryGetTransactionHistoryParams,
                ),
            ),
            cast_to=PublicTreasuryGetTransactionHistoryResponse,
        )


class PublicTreasuryResourceWithRawResponse:
    def __init__(self, public_treasury: PublicTreasuryResource) -> None:
        self._public_treasury = public_treasury

        self.get_coin_id = to_raw_response_wrapper(
            public_treasury.get_coin_id,
        )
        self.get_entity_id = to_raw_response_wrapper(
            public_treasury.get_entity_id,
        )
        self.get_holding_chart = to_raw_response_wrapper(
            public_treasury.get_holding_chart,
        )
        self.get_transaction_history = to_raw_response_wrapper(
            public_treasury.get_transaction_history,
        )


class AsyncPublicTreasuryResourceWithRawResponse:
    def __init__(self, public_treasury: AsyncPublicTreasuryResource) -> None:
        self._public_treasury = public_treasury

        self.get_coin_id = async_to_raw_response_wrapper(
            public_treasury.get_coin_id,
        )
        self.get_entity_id = async_to_raw_response_wrapper(
            public_treasury.get_entity_id,
        )
        self.get_holding_chart = async_to_raw_response_wrapper(
            public_treasury.get_holding_chart,
        )
        self.get_transaction_history = async_to_raw_response_wrapper(
            public_treasury.get_transaction_history,
        )


class PublicTreasuryResourceWithStreamingResponse:
    def __init__(self, public_treasury: PublicTreasuryResource) -> None:
        self._public_treasury = public_treasury

        self.get_coin_id = to_streamed_response_wrapper(
            public_treasury.get_coin_id,
        )
        self.get_entity_id = to_streamed_response_wrapper(
            public_treasury.get_entity_id,
        )
        self.get_holding_chart = to_streamed_response_wrapper(
            public_treasury.get_holding_chart,
        )
        self.get_transaction_history = to_streamed_response_wrapper(
            public_treasury.get_transaction_history,
        )


class AsyncPublicTreasuryResourceWithStreamingResponse:
    def __init__(self, public_treasury: AsyncPublicTreasuryResource) -> None:
        self._public_treasury = public_treasury

        self.get_coin_id = async_to_streamed_response_wrapper(
            public_treasury.get_coin_id,
        )
        self.get_entity_id = async_to_streamed_response_wrapper(
            public_treasury.get_entity_id,
        )
        self.get_holding_chart = async_to_streamed_response_wrapper(
            public_treasury.get_holding_chart,
        )
        self.get_transaction_history = async_to_streamed_response_wrapper(
            public_treasury.get_transaction_history,
        )
