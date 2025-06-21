# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from coingecko_sdk import Coingecko, AsyncCoingecko
from coingecko_sdk.types.coins import TopGainersLoserGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTopGainersLosers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Coingecko) -> None:
        top_gainers_loser = client.coins.top_gainers_losers.get(
            vs_currency="usd",
        )
        assert_matches_type(TopGainersLoserGetResponse, top_gainers_loser, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_with_all_params(self, client: Coingecko) -> None:
        top_gainers_loser = client.coins.top_gainers_losers.get(
            vs_currency="usd",
            duration="1h",
            top_coins="300",
        )
        assert_matches_type(TopGainersLoserGetResponse, top_gainers_loser, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Coingecko) -> None:
        response = client.coins.top_gainers_losers.with_raw_response.get(
            vs_currency="usd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top_gainers_loser = response.parse()
        assert_matches_type(TopGainersLoserGetResponse, top_gainers_loser, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Coingecko) -> None:
        with client.coins.top_gainers_losers.with_streaming_response.get(
            vs_currency="usd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top_gainers_loser = response.parse()
            assert_matches_type(TopGainersLoserGetResponse, top_gainers_loser, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTopGainersLosers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCoingecko) -> None:
        top_gainers_loser = await async_client.coins.top_gainers_losers.get(
            vs_currency="usd",
        )
        assert_matches_type(TopGainersLoserGetResponse, top_gainers_loser, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCoingecko) -> None:
        top_gainers_loser = await async_client.coins.top_gainers_losers.get(
            vs_currency="usd",
            duration="1h",
            top_coins="300",
        )
        assert_matches_type(TopGainersLoserGetResponse, top_gainers_loser, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCoingecko) -> None:
        response = await async_client.coins.top_gainers_losers.with_raw_response.get(
            vs_currency="usd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top_gainers_loser = await response.parse()
        assert_matches_type(TopGainersLoserGetResponse, top_gainers_loser, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCoingecko) -> None:
        async with async_client.coins.top_gainers_losers.with_streaming_response.get(
            vs_currency="usd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top_gainers_loser = await response.parse()
            assert_matches_type(TopGainersLoserGetResponse, top_gainers_loser, path=["response"])

        assert cast(Any, response.is_closed) is True
