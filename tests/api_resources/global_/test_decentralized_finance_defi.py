# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from coingecko_sdk import Coingecko, AsyncCoingecko
from coingecko_sdk.types.global_ import DecentralizedFinanceDefiGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDecentralizedFinanceDefi:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Coingecko) -> None:
        decentralized_finance_defi = client.global_.decentralized_finance_defi.get()
        assert_matches_type(DecentralizedFinanceDefiGetResponse, decentralized_finance_defi, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Coingecko) -> None:
        response = client.global_.decentralized_finance_defi.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        decentralized_finance_defi = response.parse()
        assert_matches_type(DecentralizedFinanceDefiGetResponse, decentralized_finance_defi, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Coingecko) -> None:
        with client.global_.decentralized_finance_defi.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            decentralized_finance_defi = response.parse()
            assert_matches_type(DecentralizedFinanceDefiGetResponse, decentralized_finance_defi, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDecentralizedFinanceDefi:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCoingecko) -> None:
        decentralized_finance_defi = await async_client.global_.decentralized_finance_defi.get()
        assert_matches_type(DecentralizedFinanceDefiGetResponse, decentralized_finance_defi, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCoingecko) -> None:
        response = await async_client.global_.decentralized_finance_defi.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        decentralized_finance_defi = await response.parse()
        assert_matches_type(DecentralizedFinanceDefiGetResponse, decentralized_finance_defi, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCoingecko) -> None:
        async with async_client.global_.decentralized_finance_defi.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            decentralized_finance_defi = await response.parse()
            assert_matches_type(DecentralizedFinanceDefiGetResponse, decentralized_finance_defi, path=["response"])

        assert cast(Any, response.is_closed) is True
