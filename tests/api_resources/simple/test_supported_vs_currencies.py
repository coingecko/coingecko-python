# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from coingecko_sdk import Coingecko, AsyncCoingecko
from coingecko_sdk.types.simple import SupportedVsCurrencyGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSupportedVsCurrencies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Coingecko) -> None:
        supported_vs_currency = client.simple.supported_vs_currencies.get()
        assert_matches_type(SupportedVsCurrencyGetResponse, supported_vs_currency, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Coingecko) -> None:
        response = client.simple.supported_vs_currencies.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        supported_vs_currency = response.parse()
        assert_matches_type(SupportedVsCurrencyGetResponse, supported_vs_currency, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Coingecko) -> None:
        with client.simple.supported_vs_currencies.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            supported_vs_currency = response.parse()
            assert_matches_type(SupportedVsCurrencyGetResponse, supported_vs_currency, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSupportedVsCurrencies:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCoingecko) -> None:
        supported_vs_currency = await async_client.simple.supported_vs_currencies.get()
        assert_matches_type(SupportedVsCurrencyGetResponse, supported_vs_currency, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCoingecko) -> None:
        response = await async_client.simple.supported_vs_currencies.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        supported_vs_currency = await response.parse()
        assert_matches_type(SupportedVsCurrencyGetResponse, supported_vs_currency, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCoingecko) -> None:
        async with async_client.simple.supported_vs_currencies.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            supported_vs_currency = await response.parse()
            assert_matches_type(SupportedVsCurrencyGetResponse, supported_vs_currency, path=["response"])

        assert cast(Any, response.is_closed) is True
