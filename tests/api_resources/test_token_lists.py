# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from coingecko_sdk import Coingecko, AsyncCoingecko
from coingecko_sdk.types import TokenListGetAllJsonResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTokenLists:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_all_json(self, client: Coingecko) -> None:
        token_list = client.token_lists.get_all_json(
            "ethereum",
        )
        assert_matches_type(TokenListGetAllJsonResponse, token_list, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_all_json(self, client: Coingecko) -> None:
        response = client.token_lists.with_raw_response.get_all_json(
            "ethereum",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token_list = response.parse()
        assert_matches_type(TokenListGetAllJsonResponse, token_list, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_all_json(self, client: Coingecko) -> None:
        with client.token_lists.with_streaming_response.get_all_json(
            "ethereum",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token_list = response.parse()
            assert_matches_type(TokenListGetAllJsonResponse, token_list, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get_all_json(self, client: Coingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_platform_id` but received ''"):
            client.token_lists.with_raw_response.get_all_json(
                "",
            )


class TestAsyncTokenLists:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_all_json(self, async_client: AsyncCoingecko) -> None:
        token_list = await async_client.token_lists.get_all_json(
            "ethereum",
        )
        assert_matches_type(TokenListGetAllJsonResponse, token_list, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_all_json(self, async_client: AsyncCoingecko) -> None:
        response = await async_client.token_lists.with_raw_response.get_all_json(
            "ethereum",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token_list = await response.parse()
        assert_matches_type(TokenListGetAllJsonResponse, token_list, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_all_json(self, async_client: AsyncCoingecko) -> None:
        async with async_client.token_lists.with_streaming_response.get_all_json(
            "ethereum",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token_list = await response.parse()
            assert_matches_type(TokenListGetAllJsonResponse, token_list, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get_all_json(self, async_client: AsyncCoingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_platform_id` but received ''"):
            await async_client.token_lists.with_raw_response.get_all_json(
                "",
            )
