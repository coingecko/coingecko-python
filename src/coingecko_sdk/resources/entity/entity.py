# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .public_treasury import (
    PublicTreasuryResource,
    AsyncPublicTreasuryResource,
    PublicTreasuryResourceWithRawResponse,
    AsyncPublicTreasuryResourceWithRawResponse,
    PublicTreasuryResourceWithStreamingResponse,
    AsyncPublicTreasuryResourceWithStreamingResponse,
)

__all__ = ["EntityResource", "AsyncEntityResource"]


class EntityResource(SyncAPIResource):
    @cached_property
    def public_treasury(self) -> PublicTreasuryResource:
        return PublicTreasuryResource(self._client)

    @cached_property
    def with_raw_response(self) -> EntityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return EntityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EntityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return EntityResourceWithStreamingResponse(self)


class AsyncEntityResource(AsyncAPIResource):
    @cached_property
    def public_treasury(self) -> AsyncPublicTreasuryResource:
        return AsyncPublicTreasuryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEntityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEntityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEntityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return AsyncEntityResourceWithStreamingResponse(self)


class EntityResourceWithRawResponse:
    def __init__(self, entity: EntityResource) -> None:
        self._entity = entity

    @cached_property
    def public_treasury(self) -> PublicTreasuryResourceWithRawResponse:
        return PublicTreasuryResourceWithRawResponse(self._entity.public_treasury)


class AsyncEntityResourceWithRawResponse:
    def __init__(self, entity: AsyncEntityResource) -> None:
        self._entity = entity

    @cached_property
    def public_treasury(self) -> AsyncPublicTreasuryResourceWithRawResponse:
        return AsyncPublicTreasuryResourceWithRawResponse(self._entity.public_treasury)


class EntityResourceWithStreamingResponse:
    def __init__(self, entity: EntityResource) -> None:
        self._entity = entity

    @cached_property
    def public_treasury(self) -> PublicTreasuryResourceWithStreamingResponse:
        return PublicTreasuryResourceWithStreamingResponse(self._entity.public_treasury)


class AsyncEntityResourceWithStreamingResponse:
    def __init__(self, entity: AsyncEntityResource) -> None:
        self._entity = entity

    @cached_property
    def public_treasury(self) -> AsyncPublicTreasuryResourceWithStreamingResponse:
        return AsyncPublicTreasuryResourceWithStreamingResponse(self._entity.public_treasury)
