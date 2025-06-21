# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from coingecko_sdk import Coingecko, AsyncCoingecko
from coingecko_sdk.types.onchain.networks import (
    TrendingPoolGetResponse,
    TrendingPoolGetNetworkResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTrendingPools:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Coingecko) -> None:
        trending_pool = client.onchain.networks.trending_pools.get()
        assert_matches_type(TrendingPoolGetResponse, trending_pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_with_all_params(self, client: Coingecko) -> None:
        trending_pool = client.onchain.networks.trending_pools.get(
            duration="5m",
            include="include",
            page=0,
        )
        assert_matches_type(TrendingPoolGetResponse, trending_pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Coingecko) -> None:
        response = client.onchain.networks.trending_pools.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trending_pool = response.parse()
        assert_matches_type(TrendingPoolGetResponse, trending_pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Coingecko) -> None:
        with client.onchain.networks.trending_pools.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trending_pool = response.parse()
            assert_matches_type(TrendingPoolGetResponse, trending_pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_network(self, client: Coingecko) -> None:
        trending_pool = client.onchain.networks.trending_pools.get_network(
            network="eth",
        )
        assert_matches_type(TrendingPoolGetNetworkResponse, trending_pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_network_with_all_params(self, client: Coingecko) -> None:
        trending_pool = client.onchain.networks.trending_pools.get_network(
            network="eth",
            duration="5m",
            include="include",
            page=0,
        )
        assert_matches_type(TrendingPoolGetNetworkResponse, trending_pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_network(self, client: Coingecko) -> None:
        response = client.onchain.networks.trending_pools.with_raw_response.get_network(
            network="eth",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trending_pool = response.parse()
        assert_matches_type(TrendingPoolGetNetworkResponse, trending_pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_network(self, client: Coingecko) -> None:
        with client.onchain.networks.trending_pools.with_streaming_response.get_network(
            network="eth",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trending_pool = response.parse()
            assert_matches_type(TrendingPoolGetNetworkResponse, trending_pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get_network(self, client: Coingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `network` but received ''"):
            client.onchain.networks.trending_pools.with_raw_response.get_network(
                network="",
            )


class TestAsyncTrendingPools:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCoingecko) -> None:
        trending_pool = await async_client.onchain.networks.trending_pools.get()
        assert_matches_type(TrendingPoolGetResponse, trending_pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCoingecko) -> None:
        trending_pool = await async_client.onchain.networks.trending_pools.get(
            duration="5m",
            include="include",
            page=0,
        )
        assert_matches_type(TrendingPoolGetResponse, trending_pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCoingecko) -> None:
        response = await async_client.onchain.networks.trending_pools.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trending_pool = await response.parse()
        assert_matches_type(TrendingPoolGetResponse, trending_pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCoingecko) -> None:
        async with async_client.onchain.networks.trending_pools.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trending_pool = await response.parse()
            assert_matches_type(TrendingPoolGetResponse, trending_pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_network(self, async_client: AsyncCoingecko) -> None:
        trending_pool = await async_client.onchain.networks.trending_pools.get_network(
            network="eth",
        )
        assert_matches_type(TrendingPoolGetNetworkResponse, trending_pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_network_with_all_params(self, async_client: AsyncCoingecko) -> None:
        trending_pool = await async_client.onchain.networks.trending_pools.get_network(
            network="eth",
            duration="5m",
            include="include",
            page=0,
        )
        assert_matches_type(TrendingPoolGetNetworkResponse, trending_pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_network(self, async_client: AsyncCoingecko) -> None:
        response = await async_client.onchain.networks.trending_pools.with_raw_response.get_network(
            network="eth",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trending_pool = await response.parse()
        assert_matches_type(TrendingPoolGetNetworkResponse, trending_pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_network(self, async_client: AsyncCoingecko) -> None:
        async with async_client.onchain.networks.trending_pools.with_streaming_response.get_network(
            network="eth",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trending_pool = await response.parse()
            assert_matches_type(TrendingPoolGetNetworkResponse, trending_pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get_network(self, async_client: AsyncCoingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `network` but received ''"):
            await async_client.onchain.networks.trending_pools.with_raw_response.get_network(
                network="",
            )
