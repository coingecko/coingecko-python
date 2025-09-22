# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from coingecko_sdk import Coingecko, AsyncCoingecko
from coingecko_sdk.types import EntityGetListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEntities:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_list(self, client: Coingecko) -> None:
        entity = client.entities.get_list()
        assert_matches_type(EntityGetListResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_list_with_all_params(self, client: Coingecko) -> None:
        entity = client.entities.get_list(
            entity_type="company",
            page=0,
            per_page=0,
        )
        assert_matches_type(EntityGetListResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_list(self, client: Coingecko) -> None:
        response = client.entities.with_raw_response.get_list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(EntityGetListResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_list(self, client: Coingecko) -> None:
        with client.entities.with_streaming_response.get_list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(EntityGetListResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEntities:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_list(self, async_client: AsyncCoingecko) -> None:
        entity = await async_client.entities.get_list()
        assert_matches_type(EntityGetListResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_list_with_all_params(self, async_client: AsyncCoingecko) -> None:
        entity = await async_client.entities.get_list(
            entity_type="company",
            page=0,
            per_page=0,
        )
        assert_matches_type(EntityGetListResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_list(self, async_client: AsyncCoingecko) -> None:
        response = await async_client.entities.with_raw_response.get_list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(EntityGetListResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_list(self, async_client: AsyncCoingecko) -> None:
        async with async_client.entities.with_streaming_response.get_list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(EntityGetListResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True
