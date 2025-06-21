# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from coingecko_sdk import Coingecko, AsyncCoingecko
from coingecko_sdk.types.simple import TokenPriceGetIDResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTokenPrice:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_id(self, client: Coingecko) -> None:
        token_price = client.simple.token_price.get_id(
            id="ethereum",
            contract_addresses="contract_addresses",
            vs_currencies="vs_currencies",
        )
        assert_matches_type(TokenPriceGetIDResponse, token_price, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_id_with_all_params(self, client: Coingecko) -> None:
        token_price = client.simple.token_price.get_id(
            id="ethereum",
            contract_addresses="contract_addresses",
            vs_currencies="vs_currencies",
            include_24hr_change=True,
            include_24hr_vol=True,
            include_last_updated_at=True,
            include_market_cap=True,
            precision="full",
        )
        assert_matches_type(TokenPriceGetIDResponse, token_price, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_id(self, client: Coingecko) -> None:
        response = client.simple.token_price.with_raw_response.get_id(
            id="ethereum",
            contract_addresses="contract_addresses",
            vs_currencies="vs_currencies",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token_price = response.parse()
        assert_matches_type(TokenPriceGetIDResponse, token_price, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_id(self, client: Coingecko) -> None:
        with client.simple.token_price.with_streaming_response.get_id(
            id="ethereum",
            contract_addresses="contract_addresses",
            vs_currencies="vs_currencies",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token_price = response.parse()
            assert_matches_type(TokenPriceGetIDResponse, token_price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get_id(self, client: Coingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.simple.token_price.with_raw_response.get_id(
                id="",
                contract_addresses="contract_addresses",
                vs_currencies="vs_currencies",
            )


class TestAsyncTokenPrice:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_id(self, async_client: AsyncCoingecko) -> None:
        token_price = await async_client.simple.token_price.get_id(
            id="ethereum",
            contract_addresses="contract_addresses",
            vs_currencies="vs_currencies",
        )
        assert_matches_type(TokenPriceGetIDResponse, token_price, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_id_with_all_params(self, async_client: AsyncCoingecko) -> None:
        token_price = await async_client.simple.token_price.get_id(
            id="ethereum",
            contract_addresses="contract_addresses",
            vs_currencies="vs_currencies",
            include_24hr_change=True,
            include_24hr_vol=True,
            include_last_updated_at=True,
            include_market_cap=True,
            precision="full",
        )
        assert_matches_type(TokenPriceGetIDResponse, token_price, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_id(self, async_client: AsyncCoingecko) -> None:
        response = await async_client.simple.token_price.with_raw_response.get_id(
            id="ethereum",
            contract_addresses="contract_addresses",
            vs_currencies="vs_currencies",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token_price = await response.parse()
        assert_matches_type(TokenPriceGetIDResponse, token_price, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_id(self, async_client: AsyncCoingecko) -> None:
        async with async_client.simple.token_price.with_streaming_response.get_id(
            id="ethereum",
            contract_addresses="contract_addresses",
            vs_currencies="vs_currencies",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token_price = await response.parse()
            assert_matches_type(TokenPriceGetIDResponse, token_price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get_id(self, async_client: AsyncCoingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.simple.token_price.with_raw_response.get_id(
                id="",
                contract_addresses="contract_addresses",
                vs_currencies="vs_currencies",
            )
