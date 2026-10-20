# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from coingecko_sdk import Coingecko, AsyncCoingecko
from coingecko_sdk.types.onchain.networks.pools import LiquidityEventGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLiquidityEvents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: Coingecko) -> None:
        liquidity_event = client.onchain.networks.pools.liquidity_events.get(
            pool_address="pool_address",
            network="network",
        )
        assert_matches_type(LiquidityEventGetResponse, liquidity_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: Coingecko) -> None:
        liquidity_event = client.onchain.networks.pools.liquidity_events.get(
            pool_address="pool_address",
            network="network",
            cursor="cursor",
            kind="add",
            per_page=0,
            volume_in_usd_greater_than=0,
        )
        assert_matches_type(LiquidityEventGetResponse, liquidity_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Coingecko) -> None:
        response = client.onchain.networks.pools.liquidity_events.with_raw_response.get(
            pool_address="pool_address",
            network="network",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        liquidity_event = response.parse()
        assert_matches_type(LiquidityEventGetResponse, liquidity_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Coingecko) -> None:
        with client.onchain.networks.pools.liquidity_events.with_streaming_response.get(
            pool_address="pool_address",
            network="network",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            liquidity_event = response.parse()
            assert_matches_type(LiquidityEventGetResponse, liquidity_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Coingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `network` but received ''"):
            client.onchain.networks.pools.liquidity_events.with_raw_response.get(
                pool_address="pool_address",
                network="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pool_address` but received ''"):
            client.onchain.networks.pools.liquidity_events.with_raw_response.get(
                pool_address="",
                network="network",
            )


class TestAsyncLiquidityEvents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncCoingecko) -> None:
        liquidity_event = await async_client.onchain.networks.pools.liquidity_events.get(
            pool_address="pool_address",
            network="network",
        )
        assert_matches_type(LiquidityEventGetResponse, liquidity_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCoingecko) -> None:
        liquidity_event = await async_client.onchain.networks.pools.liquidity_events.get(
            pool_address="pool_address",
            network="network",
            cursor="cursor",
            kind="add",
            per_page=0,
            volume_in_usd_greater_than=0,
        )
        assert_matches_type(LiquidityEventGetResponse, liquidity_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCoingecko) -> None:
        response = await async_client.onchain.networks.pools.liquidity_events.with_raw_response.get(
            pool_address="pool_address",
            network="network",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        liquidity_event = await response.parse()
        assert_matches_type(LiquidityEventGetResponse, liquidity_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCoingecko) -> None:
        async with async_client.onchain.networks.pools.liquidity_events.with_streaming_response.get(
            pool_address="pool_address",
            network="network",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            liquidity_event = await response.parse()
            assert_matches_type(LiquidityEventGetResponse, liquidity_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCoingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `network` but received ''"):
            await async_client.onchain.networks.pools.liquidity_events.with_raw_response.get(
                pool_address="pool_address",
                network="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pool_address` but received ''"):
            await async_client.onchain.networks.pools.liquidity_events.with_raw_response.get(
                pool_address="",
                network="network",
            )
