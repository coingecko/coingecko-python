# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from coingecko_sdk import Coingecko, AsyncCoingecko
from coingecko_sdk.types.coins import MarketGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMarkets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Coingecko) -> None:
        market = client.coins.markets.get(
            vs_currency="usd",
        )
        assert_matches_type(MarketGetResponse, market, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_with_all_params(self, client: Coingecko) -> None:
        market = client.coins.markets.get(
            vs_currency="usd",
            category="layer-1",
            ids="ids",
            include_tokens="top",
            locale="ar",
            names="names",
            order="market_cap_asc",
            page=0,
            per_page=0,
            precision="full",
            price_change_percentage="price_change_percentage",
            sparkline=True,
            symbols="symbols",
        )
        assert_matches_type(MarketGetResponse, market, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Coingecko) -> None:
        response = client.coins.markets.with_raw_response.get(
            vs_currency="usd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        market = response.parse()
        assert_matches_type(MarketGetResponse, market, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Coingecko) -> None:
        with client.coins.markets.with_streaming_response.get(
            vs_currency="usd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            market = response.parse()
            assert_matches_type(MarketGetResponse, market, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMarkets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCoingecko) -> None:
        market = await async_client.coins.markets.get(
            vs_currency="usd",
        )
        assert_matches_type(MarketGetResponse, market, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCoingecko) -> None:
        market = await async_client.coins.markets.get(
            vs_currency="usd",
            category="layer-1",
            ids="ids",
            include_tokens="top",
            locale="ar",
            names="names",
            order="market_cap_asc",
            page=0,
            per_page=0,
            precision="full",
            price_change_percentage="price_change_percentage",
            sparkline=True,
            symbols="symbols",
        )
        assert_matches_type(MarketGetResponse, market, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCoingecko) -> None:
        response = await async_client.coins.markets.with_raw_response.get(
            vs_currency="usd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        market = await response.parse()
        assert_matches_type(MarketGetResponse, market, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCoingecko) -> None:
        async with async_client.coins.markets.with_streaming_response.get(
            vs_currency="usd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            market = await response.parse()
            assert_matches_type(MarketGetResponse, market, path=["response"])

        assert cast(Any, response.is_closed) is True
