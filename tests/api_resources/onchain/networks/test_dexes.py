# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from coingecko_sdk import Coingecko, AsyncCoingecko
from coingecko_sdk.types.onchain.networks import (
    DexGetResponse,
    DexGetPoolsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDexes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Coingecko) -> None:
        dex = client.onchain.networks.dexes.get(
            network="eth",
        )
        assert_matches_type(DexGetResponse, dex, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_with_all_params(self, client: Coingecko) -> None:
        dex = client.onchain.networks.dexes.get(
            network="eth",
            page=0,
        )
        assert_matches_type(DexGetResponse, dex, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Coingecko) -> None:
        response = client.onchain.networks.dexes.with_raw_response.get(
            network="eth",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dex = response.parse()
        assert_matches_type(DexGetResponse, dex, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Coingecko) -> None:
        with client.onchain.networks.dexes.with_streaming_response.get(
            network="eth",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dex = response.parse()
            assert_matches_type(DexGetResponse, dex, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Coingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `network` but received ''"):
            client.onchain.networks.dexes.with_raw_response.get(
                network="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get_pools(self, client: Coingecko) -> None:
        dex = client.onchain.networks.dexes.get_pools(
            dex="sushiswap",
            network="eth",
        )
        assert_matches_type(DexGetPoolsResponse, dex, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_pools_with_all_params(self, client: Coingecko) -> None:
        dex = client.onchain.networks.dexes.get_pools(
            dex="sushiswap",
            network="eth",
            include="include",
            page=0,
            sort="h24_tx_count_desc",
        )
        assert_matches_type(DexGetPoolsResponse, dex, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_pools(self, client: Coingecko) -> None:
        response = client.onchain.networks.dexes.with_raw_response.get_pools(
            dex="sushiswap",
            network="eth",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dex = response.parse()
        assert_matches_type(DexGetPoolsResponse, dex, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_pools(self, client: Coingecko) -> None:
        with client.onchain.networks.dexes.with_streaming_response.get_pools(
            dex="sushiswap",
            network="eth",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dex = response.parse()
            assert_matches_type(DexGetPoolsResponse, dex, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get_pools(self, client: Coingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `network` but received ''"):
            client.onchain.networks.dexes.with_raw_response.get_pools(
                dex="sushiswap",
                network="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dex` but received ''"):
            client.onchain.networks.dexes.with_raw_response.get_pools(
                dex="",
                network="eth",
            )


class TestAsyncDexes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCoingecko) -> None:
        dex = await async_client.onchain.networks.dexes.get(
            network="eth",
        )
        assert_matches_type(DexGetResponse, dex, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCoingecko) -> None:
        dex = await async_client.onchain.networks.dexes.get(
            network="eth",
            page=0,
        )
        assert_matches_type(DexGetResponse, dex, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCoingecko) -> None:
        response = await async_client.onchain.networks.dexes.with_raw_response.get(
            network="eth",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dex = await response.parse()
        assert_matches_type(DexGetResponse, dex, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCoingecko) -> None:
        async with async_client.onchain.networks.dexes.with_streaming_response.get(
            network="eth",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dex = await response.parse()
            assert_matches_type(DexGetResponse, dex, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCoingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `network` but received ''"):
            await async_client.onchain.networks.dexes.with_raw_response.get(
                network="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_pools(self, async_client: AsyncCoingecko) -> None:
        dex = await async_client.onchain.networks.dexes.get_pools(
            dex="sushiswap",
            network="eth",
        )
        assert_matches_type(DexGetPoolsResponse, dex, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_pools_with_all_params(self, async_client: AsyncCoingecko) -> None:
        dex = await async_client.onchain.networks.dexes.get_pools(
            dex="sushiswap",
            network="eth",
            include="include",
            page=0,
            sort="h24_tx_count_desc",
        )
        assert_matches_type(DexGetPoolsResponse, dex, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_pools(self, async_client: AsyncCoingecko) -> None:
        response = await async_client.onchain.networks.dexes.with_raw_response.get_pools(
            dex="sushiswap",
            network="eth",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dex = await response.parse()
        assert_matches_type(DexGetPoolsResponse, dex, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_pools(self, async_client: AsyncCoingecko) -> None:
        async with async_client.onchain.networks.dexes.with_streaming_response.get_pools(
            dex="sushiswap",
            network="eth",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dex = await response.parse()
            assert_matches_type(DexGetPoolsResponse, dex, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get_pools(self, async_client: AsyncCoingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `network` but received ''"):
            await async_client.onchain.networks.dexes.with_raw_response.get_pools(
                dex="sushiswap",
                network="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dex` but received ''"):
            await async_client.onchain.networks.dexes.with_raw_response.get_pools(
                dex="",
                network="eth",
            )
