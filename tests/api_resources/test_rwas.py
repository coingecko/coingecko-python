# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from coingecko_sdk import Coingecko, AsyncCoingecko
from coingecko_sdk.types import (
    RwaGetIDResponse,
    RwaGetListResponse,
    RwaGetMarketsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRwas:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_id(self, client: Coingecko) -> None:
        rwa = client.rwas.get_id(
            id="id",
        )
        assert_matches_type(RwaGetIDResponse, rwa, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_id_with_all_params(self, client: Coingecko) -> None:
        rwa = client.rwas.get_id(
            id="id",
            sparkline=True,
            tokenized_market_data=True,
            tokens=True,
        )
        assert_matches_type(RwaGetIDResponse, rwa, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_id(self, client: Coingecko) -> None:
        response = client.rwas.with_raw_response.get_id(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rwa = response.parse()
        assert_matches_type(RwaGetIDResponse, rwa, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_id(self, client: Coingecko) -> None:
        with client.rwas.with_streaming_response.get_id(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rwa = response.parse()
            assert_matches_type(RwaGetIDResponse, rwa, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_id(self, client: Coingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.rwas.with_raw_response.get_id(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_list(self, client: Coingecko) -> None:
        rwa = client.rwas.get_list()
        assert_matches_type(RwaGetListResponse, rwa, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_list_with_all_params(self, client: Coingecko) -> None:
        rwa = client.rwas.get_list(
            asset_type="stock",
        )
        assert_matches_type(RwaGetListResponse, rwa, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_list(self, client: Coingecko) -> None:
        response = client.rwas.with_raw_response.get_list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rwa = response.parse()
        assert_matches_type(RwaGetListResponse, rwa, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_list(self, client: Coingecko) -> None:
        with client.rwas.with_streaming_response.get_list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rwa = response.parse()
            assert_matches_type(RwaGetListResponse, rwa, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_markets(self, client: Coingecko) -> None:
        rwa = client.rwas.get_markets()
        assert_matches_type(RwaGetMarketsResponse, rwa, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_markets_with_all_params(self, client: Coingecko) -> None:
        rwa = client.rwas.get_markets(
            asset_type="stock",
            ids="ids",
            issuer="issuer",
            names="names",
            order="market_cap_asc",
            page=0,
            per_page=0,
            precision="full",
            price_change_percentage="price_change_percentage",
            sparkline=True,
            symbols="symbols",
        )
        assert_matches_type(RwaGetMarketsResponse, rwa, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_markets(self, client: Coingecko) -> None:
        response = client.rwas.with_raw_response.get_markets()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rwa = response.parse()
        assert_matches_type(RwaGetMarketsResponse, rwa, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_markets(self, client: Coingecko) -> None:
        with client.rwas.with_streaming_response.get_markets() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rwa = response.parse()
            assert_matches_type(RwaGetMarketsResponse, rwa, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRwas:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_id(self, async_client: AsyncCoingecko) -> None:
        rwa = await async_client.rwas.get_id(
            id="id",
        )
        assert_matches_type(RwaGetIDResponse, rwa, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_id_with_all_params(self, async_client: AsyncCoingecko) -> None:
        rwa = await async_client.rwas.get_id(
            id="id",
            sparkline=True,
            tokenized_market_data=True,
            tokens=True,
        )
        assert_matches_type(RwaGetIDResponse, rwa, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_id(self, async_client: AsyncCoingecko) -> None:
        response = await async_client.rwas.with_raw_response.get_id(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rwa = await response.parse()
        assert_matches_type(RwaGetIDResponse, rwa, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_id(self, async_client: AsyncCoingecko) -> None:
        async with async_client.rwas.with_streaming_response.get_id(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rwa = await response.parse()
            assert_matches_type(RwaGetIDResponse, rwa, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_id(self, async_client: AsyncCoingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.rwas.with_raw_response.get_id(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_list(self, async_client: AsyncCoingecko) -> None:
        rwa = await async_client.rwas.get_list()
        assert_matches_type(RwaGetListResponse, rwa, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_list_with_all_params(self, async_client: AsyncCoingecko) -> None:
        rwa = await async_client.rwas.get_list(
            asset_type="stock",
        )
        assert_matches_type(RwaGetListResponse, rwa, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_list(self, async_client: AsyncCoingecko) -> None:
        response = await async_client.rwas.with_raw_response.get_list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rwa = await response.parse()
        assert_matches_type(RwaGetListResponse, rwa, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_list(self, async_client: AsyncCoingecko) -> None:
        async with async_client.rwas.with_streaming_response.get_list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rwa = await response.parse()
            assert_matches_type(RwaGetListResponse, rwa, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_markets(self, async_client: AsyncCoingecko) -> None:
        rwa = await async_client.rwas.get_markets()
        assert_matches_type(RwaGetMarketsResponse, rwa, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_markets_with_all_params(self, async_client: AsyncCoingecko) -> None:
        rwa = await async_client.rwas.get_markets(
            asset_type="stock",
            ids="ids",
            issuer="issuer",
            names="names",
            order="market_cap_asc",
            page=0,
            per_page=0,
            precision="full",
            price_change_percentage="price_change_percentage",
            sparkline=True,
            symbols="symbols",
        )
        assert_matches_type(RwaGetMarketsResponse, rwa, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_markets(self, async_client: AsyncCoingecko) -> None:
        response = await async_client.rwas.with_raw_response.get_markets()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rwa = await response.parse()
        assert_matches_type(RwaGetMarketsResponse, rwa, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_markets(self, async_client: AsyncCoingecko) -> None:
        async with async_client.rwas.with_streaming_response.get_markets() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rwa = await response.parse()
            assert_matches_type(RwaGetMarketsResponse, rwa, path=["response"])

        assert cast(Any, response.is_closed) is True
