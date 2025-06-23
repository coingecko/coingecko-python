# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from coingecko_sdk import Coingecko, AsyncCoingecko
from coingecko_sdk.types.onchain.networks.tokens import TradeGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTrades:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Coingecko) -> None:
        trade = client.onchain.networks.tokens.trades.get(
            token_address="0xdac17f958d2ee523a2206206994597c13d831ec7",
            network="eth",
        )
        assert_matches_type(TradeGetResponse, trade, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_with_all_params(self, client: Coingecko) -> None:
        trade = client.onchain.networks.tokens.trades.get(
            token_address="0xdac17f958d2ee523a2206206994597c13d831ec7",
            network="eth",
            trade_volume_in_usd_greater_than=0,
        )
        assert_matches_type(TradeGetResponse, trade, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Coingecko) -> None:
        response = client.onchain.networks.tokens.trades.with_raw_response.get(
            token_address="0xdac17f958d2ee523a2206206994597c13d831ec7",
            network="eth",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trade = response.parse()
        assert_matches_type(TradeGetResponse, trade, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Coingecko) -> None:
        with client.onchain.networks.tokens.trades.with_streaming_response.get(
            token_address="0xdac17f958d2ee523a2206206994597c13d831ec7",
            network="eth",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trade = response.parse()
            assert_matches_type(TradeGetResponse, trade, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Coingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `network` but received ''"):
            client.onchain.networks.tokens.trades.with_raw_response.get(
                token_address="0xdac17f958d2ee523a2206206994597c13d831ec7",
                network="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token_address` but received ''"):
            client.onchain.networks.tokens.trades.with_raw_response.get(
                token_address="",
                network="eth",
            )


class TestAsyncTrades:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCoingecko) -> None:
        trade = await async_client.onchain.networks.tokens.trades.get(
            token_address="0xdac17f958d2ee523a2206206994597c13d831ec7",
            network="eth",
        )
        assert_matches_type(TradeGetResponse, trade, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCoingecko) -> None:
        trade = await async_client.onchain.networks.tokens.trades.get(
            token_address="0xdac17f958d2ee523a2206206994597c13d831ec7",
            network="eth",
            trade_volume_in_usd_greater_than=0,
        )
        assert_matches_type(TradeGetResponse, trade, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCoingecko) -> None:
        response = await async_client.onchain.networks.tokens.trades.with_raw_response.get(
            token_address="0xdac17f958d2ee523a2206206994597c13d831ec7",
            network="eth",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trade = await response.parse()
        assert_matches_type(TradeGetResponse, trade, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCoingecko) -> None:
        async with async_client.onchain.networks.tokens.trades.with_streaming_response.get(
            token_address="0xdac17f958d2ee523a2206206994597c13d831ec7",
            network="eth",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trade = await response.parse()
            assert_matches_type(TradeGetResponse, trade, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCoingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `network` but received ''"):
            await async_client.onchain.networks.tokens.trades.with_raw_response.get(
                token_address="0xdac17f958d2ee523a2206206994597c13d831ec7",
                network="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token_address` but received ''"):
            await async_client.onchain.networks.tokens.trades.with_raw_response.get(
                token_address="",
                network="eth",
            )
