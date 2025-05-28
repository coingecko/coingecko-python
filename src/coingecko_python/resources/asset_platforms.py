# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import asset_platform_get_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ..types.asset_platform_get_response import AssetPlatformGetResponse

__all__ = ["AssetPlatformsResource", "AsyncAssetPlatformsResource"]


class AssetPlatformsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AssetPlatformsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return AssetPlatformsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AssetPlatformsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return AssetPlatformsResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        filter: Literal["nft"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssetPlatformGetResponse:
        """
        This endpoint allows you to **query all the asset platforms on CoinGecko**

        Args:
          filter: apply relevant filters to results

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/asset_platforms",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"filter": filter}, asset_platform_get_params.AssetPlatformGetParams),
            ),
            cast_to=AssetPlatformGetResponse,
        )


class AsyncAssetPlatformsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAssetPlatformsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAssetPlatformsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAssetPlatformsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return AsyncAssetPlatformsResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        filter: Literal["nft"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssetPlatformGetResponse:
        """
        This endpoint allows you to **query all the asset platforms on CoinGecko**

        Args:
          filter: apply relevant filters to results

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/asset_platforms",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"filter": filter}, asset_platform_get_params.AssetPlatformGetParams),
            ),
            cast_to=AssetPlatformGetResponse,
        )


class AssetPlatformsResourceWithRawResponse:
    def __init__(self, asset_platforms: AssetPlatformsResource) -> None:
        self._asset_platforms = asset_platforms

        self.get = to_raw_response_wrapper(
            asset_platforms.get,
        )


class AsyncAssetPlatformsResourceWithRawResponse:
    def __init__(self, asset_platforms: AsyncAssetPlatformsResource) -> None:
        self._asset_platforms = asset_platforms

        self.get = async_to_raw_response_wrapper(
            asset_platforms.get,
        )


class AssetPlatformsResourceWithStreamingResponse:
    def __init__(self, asset_platforms: AssetPlatformsResource) -> None:
        self._asset_platforms = asset_platforms

        self.get = to_streamed_response_wrapper(
            asset_platforms.get,
        )


class AsyncAssetPlatformsResourceWithStreamingResponse:
    def __init__(self, asset_platforms: AsyncAssetPlatformsResource) -> None:
        self._asset_platforms = asset_platforms

        self.get = async_to_streamed_response_wrapper(
            asset_platforms.get,
        )
