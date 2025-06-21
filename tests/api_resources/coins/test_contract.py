# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from coingecko_sdk import Coingecko, AsyncCoingecko
from coingecko_sdk.types.coins import ContractGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContract:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Coingecko) -> None:
        contract = client.coins.contract.get(
            contract_address="0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
            id="ethereum",
        )
        assert_matches_type(ContractGetResponse, contract, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Coingecko) -> None:
        response = client.coins.contract.with_raw_response.get(
            contract_address="0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
            id="ethereum",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(ContractGetResponse, contract, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Coingecko) -> None:
        with client.coins.contract.with_streaming_response.get(
            contract_address="0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
            id="ethereum",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(ContractGetResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Coingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.coins.contract.with_raw_response.get(
                contract_address="0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_address` but received ''"):
            client.coins.contract.with_raw_response.get(
                contract_address="",
                id="ethereum",
            )


class TestAsyncContract:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCoingecko) -> None:
        contract = await async_client.coins.contract.get(
            contract_address="0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
            id="ethereum",
        )
        assert_matches_type(ContractGetResponse, contract, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCoingecko) -> None:
        response = await async_client.coins.contract.with_raw_response.get(
            contract_address="0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
            id="ethereum",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(ContractGetResponse, contract, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCoingecko) -> None:
        async with async_client.coins.contract.with_streaming_response.get(
            contract_address="0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
            id="ethereum",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(ContractGetResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCoingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.coins.contract.with_raw_response.get(
                contract_address="0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_address` but received ''"):
            await async_client.coins.contract.with_raw_response.get(
                contract_address="",
                id="ethereum",
            )
