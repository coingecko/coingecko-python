# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from coingecko_sdk import Coingecko, AsyncCoingecko
from coingecko_sdk.types.simple import PriceGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPrice:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Coingecko) -> None:
        price = client.simple.price.get(
            vs_currencies="vs_currencies",
        )
        assert_matches_type(PriceGetResponse, price, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_with_all_params(self, client: Coingecko) -> None:
        price = client.simple.price.get(
            vs_currencies="vs_currencies",
            ids="ids",
            include_24hr_change=True,
            include_24hr_vol=True,
            include_last_updated_at=True,
            include_market_cap=True,
            include_tokens="top",
            names="names",
            precision="full",
            symbols="symbols",
        )
        assert_matches_type(PriceGetResponse, price, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Coingecko) -> None:
        response = client.simple.price.with_raw_response.get(
            vs_currencies="vs_currencies",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(PriceGetResponse, price, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Coingecko) -> None:
        with client.simple.price.with_streaming_response.get(
            vs_currencies="vs_currencies",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = response.parse()
            assert_matches_type(PriceGetResponse, price, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPrice:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCoingecko) -> None:
        price = await async_client.simple.price.get(
            vs_currencies="vs_currencies",
        )
        assert_matches_type(PriceGetResponse, price, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCoingecko) -> None:
        price = await async_client.simple.price.get(
            vs_currencies="vs_currencies",
            ids="ids",
            include_24hr_change=True,
            include_24hr_vol=True,
            include_last_updated_at=True,
            include_market_cap=True,
            include_tokens="top",
            names="names",
            precision="full",
            symbols="symbols",
        )
        assert_matches_type(PriceGetResponse, price, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCoingecko) -> None:
        response = await async_client.simple.price.with_raw_response.get(
            vs_currencies="vs_currencies",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = await response.parse()
        assert_matches_type(PriceGetResponse, price, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCoingecko) -> None:
        async with async_client.simple.price.with_streaming_response.get(
            vs_currencies="vs_currencies",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = await response.parse()
            assert_matches_type(PriceGetResponse, price, path=["response"])

        assert cast(Any, response.is_closed) is True
