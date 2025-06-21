# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from coingecko_sdk import Coingecko, AsyncCoingecko
from coingecko_sdk.types.coins import ListGetResponse, ListGetNewResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestList:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Coingecko) -> None:
        list_ = client.coins.list.get()
        assert_matches_type(ListGetResponse, list_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_with_all_params(self, client: Coingecko) -> None:
        list_ = client.coins.list.get(
            include_platform=True,
            status="active",
        )
        assert_matches_type(ListGetResponse, list_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Coingecko) -> None:
        response = client.coins.list.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert_matches_type(ListGetResponse, list_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Coingecko) -> None:
        with client.coins.list.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert_matches_type(ListGetResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_new(self, client: Coingecko) -> None:
        list_ = client.coins.list.get_new()
        assert_matches_type(ListGetNewResponse, list_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_new(self, client: Coingecko) -> None:
        response = client.coins.list.with_raw_response.get_new()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert_matches_type(ListGetNewResponse, list_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_new(self, client: Coingecko) -> None:
        with client.coins.list.with_streaming_response.get_new() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert_matches_type(ListGetNewResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncList:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCoingecko) -> None:
        list_ = await async_client.coins.list.get()
        assert_matches_type(ListGetResponse, list_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCoingecko) -> None:
        list_ = await async_client.coins.list.get(
            include_platform=True,
            status="active",
        )
        assert_matches_type(ListGetResponse, list_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCoingecko) -> None:
        response = await async_client.coins.list.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert_matches_type(ListGetResponse, list_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCoingecko) -> None:
        async with async_client.coins.list.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert_matches_type(ListGetResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_new(self, async_client: AsyncCoingecko) -> None:
        list_ = await async_client.coins.list.get_new()
        assert_matches_type(ListGetNewResponse, list_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_new(self, async_client: AsyncCoingecko) -> None:
        response = await async_client.coins.list.with_raw_response.get_new()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert_matches_type(ListGetNewResponse, list_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_new(self, async_client: AsyncCoingecko) -> None:
        async with async_client.coins.list.with_streaming_response.get_new() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert_matches_type(ListGetNewResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True
