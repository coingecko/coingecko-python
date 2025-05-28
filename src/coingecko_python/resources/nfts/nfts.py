# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...types import nft_get_list_params, nft_get_markets_params
from .tickers import (
    TickersResource,
    AsyncTickersResource,
    TickersResourceWithRawResponse,
    AsyncTickersResourceWithRawResponse,
    TickersResourceWithStreamingResponse,
    AsyncTickersResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
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
from ..._base_client import make_request_options
from .contract.contract import (
    ContractResource,
    AsyncContractResource,
    ContractResourceWithRawResponse,
    AsyncContractResourceWithRawResponse,
    ContractResourceWithStreamingResponse,
    AsyncContractResourceWithStreamingResponse,
)
from ...types.nft_get_id_response import NFTGetIDResponse
from ...types.nft_get_list_response import NFTGetListResponse
from ...types.nft_get_markets_response import NFTGetMarketsResponse

__all__ = ["NFTsResource", "AsyncNFTsResource"]


class NFTsResource(SyncAPIResource):
    @cached_property
    def contract(self) -> ContractResource:
        return ContractResource(self._client)

    @cached_property
    def market_chart(self) -> MarketChartResource:
        return MarketChartResource(self._client)

    @cached_property
    def tickers(self) -> TickersResource:
        return TickersResource(self._client)

    @cached_property
    def with_raw_response(self) -> NFTsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return NFTsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NFTsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return NFTsResourceWithStreamingResponse(self)

    def get_id(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NFTGetIDResponse:
        """
        This endpoint allows you to **query all the NFT data (name, floor price, 24hr
        volume ...) based on the NFT collection ID**

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/nfts/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NFTGetIDResponse,
        )

    def get_list(
        self,
        *,
        order: Literal[
            "h24_volume_usd_asc",
            "h24_volume_usd_desc",
            "h24_volume_native_asc",
            "h24_volume_native_desc",
            "floor_price_native_asc",
            "floor_price_native_desc",
            "market_cap_native_asc",
            "market_cap_native_desc",
            "market_cap_usd_asc",
            "market_cap_usd_desc",
        ]
        | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NFTGetListResponse:
        """
        This endpoint allows you to **query all supported NFTs with ID, contract
        address, name, asset platform ID and symbol on CoinGecko**

        Args:
          order: use this to sort the order of responses

          page: page through results

          per_page: total results per page Valid values: 1...250

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/nfts/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                    },
                    nft_get_list_params.NFTGetListParams,
                ),
            ),
            cast_to=NFTGetListResponse,
        )

    def get_markets(
        self,
        *,
        asset_platform_id: str | NotGiven = NOT_GIVEN,
        order: Literal[
            "h24_volume_native_asc",
            "h24_volume_native_desc",
            "h24_volume_usd_asc",
            "h24_volume_usd_desc",
            "market_cap_usd_asc",
            "market_cap_usd_desc",
        ]
        | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NFTGetMarketsResponse:
        """
        This endpoint allows you to **query all the supported NFT collections with floor
        price, market cap, volume and market related data on CoinGecko**

        Args:
          asset_platform_id: filter result by asset platform (blockchain network) \\**refers to
              [`/asset_platforms`](/reference/asset-platforms-list) filter=`nft`

          order: sort results by field Default: `market_cap_usd_desc`

          page: page through results Default: `1`

          per_page:
              total results per page Valid values: any integer between 1 and 250 Default:
              `100`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/nfts/markets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "asset_platform_id": asset_platform_id,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                    },
                    nft_get_markets_params.NFTGetMarketsParams,
                ),
            ),
            cast_to=NFTGetMarketsResponse,
        )


class AsyncNFTsResource(AsyncAPIResource):
    @cached_property
    def contract(self) -> AsyncContractResource:
        return AsyncContractResource(self._client)

    @cached_property
    def market_chart(self) -> AsyncMarketChartResource:
        return AsyncMarketChartResource(self._client)

    @cached_property
    def tickers(self) -> AsyncTickersResource:
        return AsyncTickersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncNFTsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNFTsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNFTsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return AsyncNFTsResourceWithStreamingResponse(self)

    async def get_id(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NFTGetIDResponse:
        """
        This endpoint allows you to **query all the NFT data (name, floor price, 24hr
        volume ...) based on the NFT collection ID**

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/nfts/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NFTGetIDResponse,
        )

    async def get_list(
        self,
        *,
        order: Literal[
            "h24_volume_usd_asc",
            "h24_volume_usd_desc",
            "h24_volume_native_asc",
            "h24_volume_native_desc",
            "floor_price_native_asc",
            "floor_price_native_desc",
            "market_cap_native_asc",
            "market_cap_native_desc",
            "market_cap_usd_asc",
            "market_cap_usd_desc",
        ]
        | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NFTGetListResponse:
        """
        This endpoint allows you to **query all supported NFTs with ID, contract
        address, name, asset platform ID and symbol on CoinGecko**

        Args:
          order: use this to sort the order of responses

          page: page through results

          per_page: total results per page Valid values: 1...250

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/nfts/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                    },
                    nft_get_list_params.NFTGetListParams,
                ),
            ),
            cast_to=NFTGetListResponse,
        )

    async def get_markets(
        self,
        *,
        asset_platform_id: str | NotGiven = NOT_GIVEN,
        order: Literal[
            "h24_volume_native_asc",
            "h24_volume_native_desc",
            "h24_volume_usd_asc",
            "h24_volume_usd_desc",
            "market_cap_usd_asc",
            "market_cap_usd_desc",
        ]
        | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NFTGetMarketsResponse:
        """
        This endpoint allows you to **query all the supported NFT collections with floor
        price, market cap, volume and market related data on CoinGecko**

        Args:
          asset_platform_id: filter result by asset platform (blockchain network) \\**refers to
              [`/asset_platforms`](/reference/asset-platforms-list) filter=`nft`

          order: sort results by field Default: `market_cap_usd_desc`

          page: page through results Default: `1`

          per_page:
              total results per page Valid values: any integer between 1 and 250 Default:
              `100`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/nfts/markets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "asset_platform_id": asset_platform_id,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                    },
                    nft_get_markets_params.NFTGetMarketsParams,
                ),
            ),
            cast_to=NFTGetMarketsResponse,
        )


class NFTsResourceWithRawResponse:
    def __init__(self, nfts: NFTsResource) -> None:
        self._nfts = nfts

        self.get_id = to_raw_response_wrapper(
            nfts.get_id,
        )
        self.get_list = to_raw_response_wrapper(
            nfts.get_list,
        )
        self.get_markets = to_raw_response_wrapper(
            nfts.get_markets,
        )

    @cached_property
    def contract(self) -> ContractResourceWithRawResponse:
        return ContractResourceWithRawResponse(self._nfts.contract)

    @cached_property
    def market_chart(self) -> MarketChartResourceWithRawResponse:
        return MarketChartResourceWithRawResponse(self._nfts.market_chart)

    @cached_property
    def tickers(self) -> TickersResourceWithRawResponse:
        return TickersResourceWithRawResponse(self._nfts.tickers)


class AsyncNFTsResourceWithRawResponse:
    def __init__(self, nfts: AsyncNFTsResource) -> None:
        self._nfts = nfts

        self.get_id = async_to_raw_response_wrapper(
            nfts.get_id,
        )
        self.get_list = async_to_raw_response_wrapper(
            nfts.get_list,
        )
        self.get_markets = async_to_raw_response_wrapper(
            nfts.get_markets,
        )

    @cached_property
    def contract(self) -> AsyncContractResourceWithRawResponse:
        return AsyncContractResourceWithRawResponse(self._nfts.contract)

    @cached_property
    def market_chart(self) -> AsyncMarketChartResourceWithRawResponse:
        return AsyncMarketChartResourceWithRawResponse(self._nfts.market_chart)

    @cached_property
    def tickers(self) -> AsyncTickersResourceWithRawResponse:
        return AsyncTickersResourceWithRawResponse(self._nfts.tickers)


class NFTsResourceWithStreamingResponse:
    def __init__(self, nfts: NFTsResource) -> None:
        self._nfts = nfts

        self.get_id = to_streamed_response_wrapper(
            nfts.get_id,
        )
        self.get_list = to_streamed_response_wrapper(
            nfts.get_list,
        )
        self.get_markets = to_streamed_response_wrapper(
            nfts.get_markets,
        )

    @cached_property
    def contract(self) -> ContractResourceWithStreamingResponse:
        return ContractResourceWithStreamingResponse(self._nfts.contract)

    @cached_property
    def market_chart(self) -> MarketChartResourceWithStreamingResponse:
        return MarketChartResourceWithStreamingResponse(self._nfts.market_chart)

    @cached_property
    def tickers(self) -> TickersResourceWithStreamingResponse:
        return TickersResourceWithStreamingResponse(self._nfts.tickers)


class AsyncNFTsResourceWithStreamingResponse:
    def __init__(self, nfts: AsyncNFTsResource) -> None:
        self._nfts = nfts

        self.get_id = async_to_streamed_response_wrapper(
            nfts.get_id,
        )
        self.get_list = async_to_streamed_response_wrapper(
            nfts.get_list,
        )
        self.get_markets = async_to_streamed_response_wrapper(
            nfts.get_markets,
        )

    @cached_property
    def contract(self) -> AsyncContractResourceWithStreamingResponse:
        return AsyncContractResourceWithStreamingResponse(self._nfts.contract)

    @cached_property
    def market_chart(self) -> AsyncMarketChartResourceWithStreamingResponse:
        return AsyncMarketChartResourceWithStreamingResponse(self._nfts.market_chart)

    @cached_property
    def tickers(self) -> AsyncTickersResourceWithStreamingResponse:
        return AsyncTickersResourceWithStreamingResponse(self._nfts.tickers)
