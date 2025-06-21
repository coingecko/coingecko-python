# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from coingecko_sdk import Coingecko, AsyncCoingecko
from coingecko_sdk.types.derivatives import (
    ExchangeGetResponse,
    ExchangeGetIDResponse,
    ExchangeGetListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExchanges:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Coingecko) -> None:
        exchange = client.derivatives.exchanges.get()
        assert_matches_type(ExchangeGetResponse, exchange, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_with_all_params(self, client: Coingecko) -> None:
        exchange = client.derivatives.exchanges.get(
            order="name_asc",
            page=0,
            per_page=0,
        )
        assert_matches_type(ExchangeGetResponse, exchange, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Coingecko) -> None:
        response = client.derivatives.exchanges.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exchange = response.parse()
        assert_matches_type(ExchangeGetResponse, exchange, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Coingecko) -> None:
        with client.derivatives.exchanges.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exchange = response.parse()
            assert_matches_type(ExchangeGetResponse, exchange, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_id(self, client: Coingecko) -> None:
        exchange = client.derivatives.exchanges.get_id(
            id="binance_futures",
        )
        assert_matches_type(ExchangeGetIDResponse, exchange, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_id_with_all_params(self, client: Coingecko) -> None:
        exchange = client.derivatives.exchanges.get_id(
            id="binance_futures",
            include_tickers="all",
        )
        assert_matches_type(ExchangeGetIDResponse, exchange, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_id(self, client: Coingecko) -> None:
        response = client.derivatives.exchanges.with_raw_response.get_id(
            id="binance_futures",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exchange = response.parse()
        assert_matches_type(ExchangeGetIDResponse, exchange, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_id(self, client: Coingecko) -> None:
        with client.derivatives.exchanges.with_streaming_response.get_id(
            id="binance_futures",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exchange = response.parse()
            assert_matches_type(ExchangeGetIDResponse, exchange, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get_id(self, client: Coingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.derivatives.exchanges.with_raw_response.get_id(
                id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get_list(self, client: Coingecko) -> None:
        exchange = client.derivatives.exchanges.get_list()
        assert_matches_type(ExchangeGetListResponse, exchange, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_list(self, client: Coingecko) -> None:
        response = client.derivatives.exchanges.with_raw_response.get_list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exchange = response.parse()
        assert_matches_type(ExchangeGetListResponse, exchange, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_list(self, client: Coingecko) -> None:
        with client.derivatives.exchanges.with_streaming_response.get_list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exchange = response.parse()
            assert_matches_type(ExchangeGetListResponse, exchange, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncExchanges:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCoingecko) -> None:
        exchange = await async_client.derivatives.exchanges.get()
        assert_matches_type(ExchangeGetResponse, exchange, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCoingecko) -> None:
        exchange = await async_client.derivatives.exchanges.get(
            order="name_asc",
            page=0,
            per_page=0,
        )
        assert_matches_type(ExchangeGetResponse, exchange, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCoingecko) -> None:
        response = await async_client.derivatives.exchanges.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exchange = await response.parse()
        assert_matches_type(ExchangeGetResponse, exchange, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCoingecko) -> None:
        async with async_client.derivatives.exchanges.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exchange = await response.parse()
            assert_matches_type(ExchangeGetResponse, exchange, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_id(self, async_client: AsyncCoingecko) -> None:
        exchange = await async_client.derivatives.exchanges.get_id(
            id="binance_futures",
        )
        assert_matches_type(ExchangeGetIDResponse, exchange, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_id_with_all_params(self, async_client: AsyncCoingecko) -> None:
        exchange = await async_client.derivatives.exchanges.get_id(
            id="binance_futures",
            include_tickers="all",
        )
        assert_matches_type(ExchangeGetIDResponse, exchange, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_id(self, async_client: AsyncCoingecko) -> None:
        response = await async_client.derivatives.exchanges.with_raw_response.get_id(
            id="binance_futures",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exchange = await response.parse()
        assert_matches_type(ExchangeGetIDResponse, exchange, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_id(self, async_client: AsyncCoingecko) -> None:
        async with async_client.derivatives.exchanges.with_streaming_response.get_id(
            id="binance_futures",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exchange = await response.parse()
            assert_matches_type(ExchangeGetIDResponse, exchange, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get_id(self, async_client: AsyncCoingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.derivatives.exchanges.with_raw_response.get_id(
                id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_list(self, async_client: AsyncCoingecko) -> None:
        exchange = await async_client.derivatives.exchanges.get_list()
        assert_matches_type(ExchangeGetListResponse, exchange, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_list(self, async_client: AsyncCoingecko) -> None:
        response = await async_client.derivatives.exchanges.with_raw_response.get_list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exchange = await response.parse()
        assert_matches_type(ExchangeGetListResponse, exchange, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_list(self, async_client: AsyncCoingecko) -> None:
        async with async_client.derivatives.exchanges.with_streaming_response.get_list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exchange = await response.parse()
            assert_matches_type(ExchangeGetListResponse, exchange, path=["response"])

        assert cast(Any, response.is_closed) is True
