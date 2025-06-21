# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from coingecko_sdk import Coingecko, AsyncCoingecko
from coingecko_sdk.types.onchain.simple.networks import TokenPriceGetAddressesResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTokenPrice:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_addresses(self, client: Coingecko) -> None:
        token_price = client.onchain.simple.networks.token_price.get_addresses(
            addresses="addresses",
            network="eth",
        )
        assert_matches_type(TokenPriceGetAddressesResponse, token_price, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_addresses_with_all_params(self, client: Coingecko) -> None:
        token_price = client.onchain.simple.networks.token_price.get_addresses(
            addresses="addresses",
            network="eth",
            include_24hr_price_change=True,
            include_24hr_vol=True,
            include_market_cap=True,
            include_total_reserve_in_usd=True,
            mcap_fdv_fallback=True,
        )
        assert_matches_type(TokenPriceGetAddressesResponse, token_price, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_addresses(self, client: Coingecko) -> None:
        response = client.onchain.simple.networks.token_price.with_raw_response.get_addresses(
            addresses="addresses",
            network="eth",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token_price = response.parse()
        assert_matches_type(TokenPriceGetAddressesResponse, token_price, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_addresses(self, client: Coingecko) -> None:
        with client.onchain.simple.networks.token_price.with_streaming_response.get_addresses(
            addresses="addresses",
            network="eth",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token_price = response.parse()
            assert_matches_type(TokenPriceGetAddressesResponse, token_price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get_addresses(self, client: Coingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `network` but received ''"):
            client.onchain.simple.networks.token_price.with_raw_response.get_addresses(
                addresses="addresses",
                network="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `addresses` but received ''"):
            client.onchain.simple.networks.token_price.with_raw_response.get_addresses(
                addresses="",
                network="eth",
            )


class TestAsyncTokenPrice:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_addresses(self, async_client: AsyncCoingecko) -> None:
        token_price = await async_client.onchain.simple.networks.token_price.get_addresses(
            addresses="addresses",
            network="eth",
        )
        assert_matches_type(TokenPriceGetAddressesResponse, token_price, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_addresses_with_all_params(self, async_client: AsyncCoingecko) -> None:
        token_price = await async_client.onchain.simple.networks.token_price.get_addresses(
            addresses="addresses",
            network="eth",
            include_24hr_price_change=True,
            include_24hr_vol=True,
            include_market_cap=True,
            include_total_reserve_in_usd=True,
            mcap_fdv_fallback=True,
        )
        assert_matches_type(TokenPriceGetAddressesResponse, token_price, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_addresses(self, async_client: AsyncCoingecko) -> None:
        response = await async_client.onchain.simple.networks.token_price.with_raw_response.get_addresses(
            addresses="addresses",
            network="eth",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token_price = await response.parse()
        assert_matches_type(TokenPriceGetAddressesResponse, token_price, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_addresses(self, async_client: AsyncCoingecko) -> None:
        async with async_client.onchain.simple.networks.token_price.with_streaming_response.get_addresses(
            addresses="addresses",
            network="eth",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token_price = await response.parse()
            assert_matches_type(TokenPriceGetAddressesResponse, token_price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get_addresses(self, async_client: AsyncCoingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `network` but received ''"):
            await async_client.onchain.simple.networks.token_price.with_raw_response.get_addresses(
                addresses="addresses",
                network="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `addresses` but received ''"):
            await async_client.onchain.simple.networks.token_price.with_raw_response.get_addresses(
                addresses="",
                network="eth",
            )
