# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from coingecko_sdk import Coingecko, AsyncCoingecko
from coingecko_sdk.types.onchain.networks.tokens import TopTraderGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTopTraders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: Coingecko) -> None:
        top_trader = client.onchain.networks.tokens.top_traders.get(
            token_address="0x6921b130d297cc43754afba22e5eac0fbf8db75b",
            network_id="base",
        )
        assert_matches_type(TopTraderGetResponse, top_trader, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: Coingecko) -> None:
        top_trader = client.onchain.networks.tokens.top_traders.get(
            token_address="0x6921b130d297cc43754afba22e5eac0fbf8db75b",
            network_id="base",
            include_address_label=True,
            sort="realized_pnl_usd_desc",
            traders="traders",
        )
        assert_matches_type(TopTraderGetResponse, top_trader, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Coingecko) -> None:
        response = client.onchain.networks.tokens.top_traders.with_raw_response.get(
            token_address="0x6921b130d297cc43754afba22e5eac0fbf8db75b",
            network_id="base",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top_trader = response.parse()
        assert_matches_type(TopTraderGetResponse, top_trader, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Coingecko) -> None:
        with client.onchain.networks.tokens.top_traders.with_streaming_response.get(
            token_address="0x6921b130d297cc43754afba22e5eac0fbf8db75b",
            network_id="base",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top_trader = response.parse()
            assert_matches_type(TopTraderGetResponse, top_trader, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Coingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `network_id` but received ''"):
            client.onchain.networks.tokens.top_traders.with_raw_response.get(
                token_address="0x6921b130d297cc43754afba22e5eac0fbf8db75b",
                network_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token_address` but received ''"):
            client.onchain.networks.tokens.top_traders.with_raw_response.get(
                token_address="",
                network_id="base",
            )


class TestAsyncTopTraders:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncCoingecko) -> None:
        top_trader = await async_client.onchain.networks.tokens.top_traders.get(
            token_address="0x6921b130d297cc43754afba22e5eac0fbf8db75b",
            network_id="base",
        )
        assert_matches_type(TopTraderGetResponse, top_trader, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCoingecko) -> None:
        top_trader = await async_client.onchain.networks.tokens.top_traders.get(
            token_address="0x6921b130d297cc43754afba22e5eac0fbf8db75b",
            network_id="base",
            include_address_label=True,
            sort="realized_pnl_usd_desc",
            traders="traders",
        )
        assert_matches_type(TopTraderGetResponse, top_trader, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCoingecko) -> None:
        response = await async_client.onchain.networks.tokens.top_traders.with_raw_response.get(
            token_address="0x6921b130d297cc43754afba22e5eac0fbf8db75b",
            network_id="base",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top_trader = await response.parse()
        assert_matches_type(TopTraderGetResponse, top_trader, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCoingecko) -> None:
        async with async_client.onchain.networks.tokens.top_traders.with_streaming_response.get(
            token_address="0x6921b130d297cc43754afba22e5eac0fbf8db75b",
            network_id="base",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top_trader = await response.parse()
            assert_matches_type(TopTraderGetResponse, top_trader, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCoingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `network_id` but received ''"):
            await async_client.onchain.networks.tokens.top_traders.with_raw_response.get(
                token_address="0x6921b130d297cc43754afba22e5eac0fbf8db75b",
                network_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token_address` but received ''"):
            await async_client.onchain.networks.tokens.top_traders.with_raw_response.get(
                token_address="",
                network_id="base",
            )
