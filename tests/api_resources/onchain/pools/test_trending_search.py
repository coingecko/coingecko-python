# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from coingecko_sdk import Coingecko, AsyncCoingecko
from coingecko_sdk.types.onchain.pools import TrendingSearchGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTrendingSearch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Coingecko) -> None:
        trending_search = client.onchain.pools.trending_search.get()
        assert_matches_type(TrendingSearchGetResponse, trending_search, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_with_all_params(self, client: Coingecko) -> None:
        trending_search = client.onchain.pools.trending_search.get(
            include="include",
            pools=0,
        )
        assert_matches_type(TrendingSearchGetResponse, trending_search, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Coingecko) -> None:
        response = client.onchain.pools.trending_search.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trending_search = response.parse()
        assert_matches_type(TrendingSearchGetResponse, trending_search, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Coingecko) -> None:
        with client.onchain.pools.trending_search.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trending_search = response.parse()
            assert_matches_type(TrendingSearchGetResponse, trending_search, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTrendingSearch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCoingecko) -> None:
        trending_search = await async_client.onchain.pools.trending_search.get()
        assert_matches_type(TrendingSearchGetResponse, trending_search, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCoingecko) -> None:
        trending_search = await async_client.onchain.pools.trending_search.get(
            include="include",
            pools=0,
        )
        assert_matches_type(TrendingSearchGetResponse, trending_search, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCoingecko) -> None:
        response = await async_client.onchain.pools.trending_search.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trending_search = await response.parse()
        assert_matches_type(TrendingSearchGetResponse, trending_search, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCoingecko) -> None:
        async with async_client.onchain.pools.trending_search.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trending_search = await response.parse()
            assert_matches_type(TrendingSearchGetResponse, trending_search, path=["response"])

        assert cast(Any, response.is_closed) is True
