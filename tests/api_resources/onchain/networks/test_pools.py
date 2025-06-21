# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from coingecko_sdk import Coingecko, AsyncCoingecko
from coingecko_sdk.types.onchain.networks import (
    PoolGetResponse,
    PoolGetAddressResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPools:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Coingecko) -> None:
        pool = client.onchain.networks.pools.get(
            network="eth",
        )
        assert_matches_type(PoolGetResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_with_all_params(self, client: Coingecko) -> None:
        pool = client.onchain.networks.pools.get(
            network="eth",
            include="include",
            page=0,
            sort="h24_tx_count_desc",
        )
        assert_matches_type(PoolGetResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Coingecko) -> None:
        response = client.onchain.networks.pools.with_raw_response.get(
            network="eth",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = response.parse()
        assert_matches_type(PoolGetResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Coingecko) -> None:
        with client.onchain.networks.pools.with_streaming_response.get(
            network="eth",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = response.parse()
            assert_matches_type(PoolGetResponse, pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Coingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `network` but received ''"):
            client.onchain.networks.pools.with_raw_response.get(
                network="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get_address(self, client: Coingecko) -> None:
        pool = client.onchain.networks.pools.get_address(
            address="0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640",
            network="eth",
        )
        assert_matches_type(PoolGetAddressResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_address_with_all_params(self, client: Coingecko) -> None:
        pool = client.onchain.networks.pools.get_address(
            address="0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640",
            network="eth",
            include="include",
            include_volume_breakdown=True,
        )
        assert_matches_type(PoolGetAddressResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_address(self, client: Coingecko) -> None:
        response = client.onchain.networks.pools.with_raw_response.get_address(
            address="0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640",
            network="eth",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = response.parse()
        assert_matches_type(PoolGetAddressResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_address(self, client: Coingecko) -> None:
        with client.onchain.networks.pools.with_streaming_response.get_address(
            address="0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640",
            network="eth",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = response.parse()
            assert_matches_type(PoolGetAddressResponse, pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get_address(self, client: Coingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `network` but received ''"):
            client.onchain.networks.pools.with_raw_response.get_address(
                address="0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640",
                network="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            client.onchain.networks.pools.with_raw_response.get_address(
                address="",
                network="eth",
            )


class TestAsyncPools:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCoingecko) -> None:
        pool = await async_client.onchain.networks.pools.get(
            network="eth",
        )
        assert_matches_type(PoolGetResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCoingecko) -> None:
        pool = await async_client.onchain.networks.pools.get(
            network="eth",
            include="include",
            page=0,
            sort="h24_tx_count_desc",
        )
        assert_matches_type(PoolGetResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCoingecko) -> None:
        response = await async_client.onchain.networks.pools.with_raw_response.get(
            network="eth",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = await response.parse()
        assert_matches_type(PoolGetResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCoingecko) -> None:
        async with async_client.onchain.networks.pools.with_streaming_response.get(
            network="eth",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = await response.parse()
            assert_matches_type(PoolGetResponse, pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCoingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `network` but received ''"):
            await async_client.onchain.networks.pools.with_raw_response.get(
                network="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_address(self, async_client: AsyncCoingecko) -> None:
        pool = await async_client.onchain.networks.pools.get_address(
            address="0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640",
            network="eth",
        )
        assert_matches_type(PoolGetAddressResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_address_with_all_params(self, async_client: AsyncCoingecko) -> None:
        pool = await async_client.onchain.networks.pools.get_address(
            address="0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640",
            network="eth",
            include="include",
            include_volume_breakdown=True,
        )
        assert_matches_type(PoolGetAddressResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_address(self, async_client: AsyncCoingecko) -> None:
        response = await async_client.onchain.networks.pools.with_raw_response.get_address(
            address="0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640",
            network="eth",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = await response.parse()
        assert_matches_type(PoolGetAddressResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_address(self, async_client: AsyncCoingecko) -> None:
        async with async_client.onchain.networks.pools.with_streaming_response.get_address(
            address="0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640",
            network="eth",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = await response.parse()
            assert_matches_type(PoolGetAddressResponse, pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get_address(self, async_client: AsyncCoingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `network` but received ''"):
            await async_client.onchain.networks.pools.with_raw_response.get_address(
                address="0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640",
                network="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            await async_client.onchain.networks.pools.with_raw_response.get_address(
                address="",
                network="eth",
            )
