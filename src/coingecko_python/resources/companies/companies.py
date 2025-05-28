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

__all__ = ["CompaniesResource", "AsyncCompaniesResource"]


class CompaniesResource(SyncAPIResource):
    @cached_property
    def public_treasury(self) -> PublicTreasuryResource:
        return PublicTreasuryResource(self._client)

    @cached_property
    def with_raw_response(self) -> CompaniesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return CompaniesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CompaniesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return CompaniesResourceWithStreamingResponse(self)


class AsyncCompaniesResource(AsyncAPIResource):
    @cached_property
    def public_treasury(self) -> AsyncPublicTreasuryResource:
        return AsyncPublicTreasuryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCompaniesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/coingecko/coingecko-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCompaniesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCompaniesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/coingecko/coingecko-python#with_streaming_response
        """
        return AsyncCompaniesResourceWithStreamingResponse(self)


class CompaniesResourceWithRawResponse:
    def __init__(self, companies: CompaniesResource) -> None:
        self._companies = companies

    @cached_property
    def public_treasury(self) -> PublicTreasuryResourceWithRawResponse:
        return PublicTreasuryResourceWithRawResponse(self._companies.public_treasury)


class AsyncCompaniesResourceWithRawResponse:
    def __init__(self, companies: AsyncCompaniesResource) -> None:
        self._companies = companies

    @cached_property
    def public_treasury(self) -> AsyncPublicTreasuryResourceWithRawResponse:
        return AsyncPublicTreasuryResourceWithRawResponse(self._companies.public_treasury)


class CompaniesResourceWithStreamingResponse:
    def __init__(self, companies: CompaniesResource) -> None:
        self._companies = companies

    @cached_property
    def public_treasury(self) -> PublicTreasuryResourceWithStreamingResponse:
        return PublicTreasuryResourceWithStreamingResponse(self._companies.public_treasury)


class AsyncCompaniesResourceWithStreamingResponse:
    def __init__(self, companies: AsyncCompaniesResource) -> None:
        self._companies = companies

    @cached_property
    def public_treasury(self) -> AsyncPublicTreasuryResourceWithStreamingResponse:
        return AsyncPublicTreasuryResourceWithStreamingResponse(self._companies.public_treasury)
