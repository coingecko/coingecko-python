# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from coingecko_sdk import Coingecko, AsyncCoingecko
from coingecko_sdk.types import CoinGetIDResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCoins:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_id(self, client: Coingecko) -> None:
        coin = client.coins.get_id(
            id="bitcoin",
        )
        assert_matches_type(CoinGetIDResponse, coin, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_id_with_all_params(self, client: Coingecko) -> None:
        coin = client.coins.get_id(
            id="bitcoin",
            community_data=True,
            developer_data=True,
            dex_pair_format="contract_address",
            localization=True,
            market_data=True,
            sparkline=True,
            tickers=True,
        )
        assert_matches_type(CoinGetIDResponse, coin, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_id(self, client: Coingecko) -> None:
        response = client.coins.with_raw_response.get_id(
            id="bitcoin",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        coin = response.parse()
        assert_matches_type(CoinGetIDResponse, coin, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_id(self, client: Coingecko) -> None:
        with client.coins.with_streaming_response.get_id(
            id="bitcoin",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            coin = response.parse()
            assert_matches_type(CoinGetIDResponse, coin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get_id(self, client: Coingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.coins.with_raw_response.get_id(
                id="",
            )


class TestAsyncCoins:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_id(self, async_client: AsyncCoingecko) -> None:
        coin = await async_client.coins.get_id(
            id="bitcoin",
        )
        assert_matches_type(CoinGetIDResponse, coin, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_id_with_all_params(self, async_client: AsyncCoingecko) -> None:
        coin = await async_client.coins.get_id(
            id="bitcoin",
            community_data=True,
            developer_data=True,
            dex_pair_format="contract_address",
            localization=True,
            market_data=True,
            sparkline=True,
            tickers=True,
        )
        assert_matches_type(CoinGetIDResponse, coin, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_id(self, async_client: AsyncCoingecko) -> None:
        response = await async_client.coins.with_raw_response.get_id(
            id="bitcoin",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        coin = await response.parse()
        assert_matches_type(CoinGetIDResponse, coin, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_id(self, async_client: AsyncCoingecko) -> None:
        async with async_client.coins.with_streaming_response.get_id(
            id="bitcoin",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            coin = await response.parse()
            assert_matches_type(CoinGetIDResponse, coin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get_id(self, async_client: AsyncCoingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.coins.with_raw_response.get_id(
                id="",
            )
