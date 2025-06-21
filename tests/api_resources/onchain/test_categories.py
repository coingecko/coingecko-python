# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from coingecko_sdk import Coingecko, AsyncCoingecko
from coingecko_sdk.types.onchain import (
    CategoryGetResponse,
    CategoryGetPoolsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCategories:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Coingecko) -> None:
        category = client.onchain.categories.get()
        assert_matches_type(CategoryGetResponse, category, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_with_all_params(self, client: Coingecko) -> None:
        category = client.onchain.categories.get(
            page=0,
            sort="h1_volume_percentage_desc",
        )
        assert_matches_type(CategoryGetResponse, category, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Coingecko) -> None:
        response = client.onchain.categories.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = response.parse()
        assert_matches_type(CategoryGetResponse, category, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Coingecko) -> None:
        with client.onchain.categories.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = response.parse()
            assert_matches_type(CategoryGetResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_pools(self, client: Coingecko) -> None:
        category = client.onchain.categories.get_pools(
            category_id="pump-fun",
        )
        assert_matches_type(CategoryGetPoolsResponse, category, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_pools_with_all_params(self, client: Coingecko) -> None:
        category = client.onchain.categories.get_pools(
            category_id="pump-fun",
            include="include",
            page=0,
            sort="m5_trending",
        )
        assert_matches_type(CategoryGetPoolsResponse, category, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_pools(self, client: Coingecko) -> None:
        response = client.onchain.categories.with_raw_response.get_pools(
            category_id="pump-fun",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = response.parse()
        assert_matches_type(CategoryGetPoolsResponse, category, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_pools(self, client: Coingecko) -> None:
        with client.onchain.categories.with_streaming_response.get_pools(
            category_id="pump-fun",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = response.parse()
            assert_matches_type(CategoryGetPoolsResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get_pools(self, client: Coingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `category_id` but received ''"):
            client.onchain.categories.with_raw_response.get_pools(
                category_id="",
            )


class TestAsyncCategories:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCoingecko) -> None:
        category = await async_client.onchain.categories.get()
        assert_matches_type(CategoryGetResponse, category, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCoingecko) -> None:
        category = await async_client.onchain.categories.get(
            page=0,
            sort="h1_volume_percentage_desc",
        )
        assert_matches_type(CategoryGetResponse, category, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCoingecko) -> None:
        response = await async_client.onchain.categories.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = await response.parse()
        assert_matches_type(CategoryGetResponse, category, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCoingecko) -> None:
        async with async_client.onchain.categories.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = await response.parse()
            assert_matches_type(CategoryGetResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_pools(self, async_client: AsyncCoingecko) -> None:
        category = await async_client.onchain.categories.get_pools(
            category_id="pump-fun",
        )
        assert_matches_type(CategoryGetPoolsResponse, category, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_pools_with_all_params(self, async_client: AsyncCoingecko) -> None:
        category = await async_client.onchain.categories.get_pools(
            category_id="pump-fun",
            include="include",
            page=0,
            sort="m5_trending",
        )
        assert_matches_type(CategoryGetPoolsResponse, category, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_pools(self, async_client: AsyncCoingecko) -> None:
        response = await async_client.onchain.categories.with_raw_response.get_pools(
            category_id="pump-fun",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = await response.parse()
        assert_matches_type(CategoryGetPoolsResponse, category, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_pools(self, async_client: AsyncCoingecko) -> None:
        async with async_client.onchain.categories.with_streaming_response.get_pools(
            category_id="pump-fun",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = await response.parse()
            assert_matches_type(CategoryGetPoolsResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get_pools(self, async_client: AsyncCoingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `category_id` but received ''"):
            await async_client.onchain.categories.with_raw_response.get_pools(
                category_id="",
            )
