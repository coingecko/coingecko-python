# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from coingecko_sdk import Coingecko, AsyncCoingecko
from coingecko_sdk.types.onchain.tokens import InfoRecentlyUpdatedGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInfoRecentlyUpdated:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Coingecko) -> None:
        info_recently_updated = client.onchain.tokens.info_recently_updated.get()
        assert_matches_type(InfoRecentlyUpdatedGetResponse, info_recently_updated, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_with_all_params(self, client: Coingecko) -> None:
        info_recently_updated = client.onchain.tokens.info_recently_updated.get(
            include="network",
            network="eth",
        )
        assert_matches_type(InfoRecentlyUpdatedGetResponse, info_recently_updated, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Coingecko) -> None:
        response = client.onchain.tokens.info_recently_updated.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        info_recently_updated = response.parse()
        assert_matches_type(InfoRecentlyUpdatedGetResponse, info_recently_updated, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Coingecko) -> None:
        with client.onchain.tokens.info_recently_updated.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            info_recently_updated = response.parse()
            assert_matches_type(InfoRecentlyUpdatedGetResponse, info_recently_updated, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncInfoRecentlyUpdated:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCoingecko) -> None:
        info_recently_updated = await async_client.onchain.tokens.info_recently_updated.get()
        assert_matches_type(InfoRecentlyUpdatedGetResponse, info_recently_updated, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCoingecko) -> None:
        info_recently_updated = await async_client.onchain.tokens.info_recently_updated.get(
            include="network",
            network="eth",
        )
        assert_matches_type(InfoRecentlyUpdatedGetResponse, info_recently_updated, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCoingecko) -> None:
        response = await async_client.onchain.tokens.info_recently_updated.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        info_recently_updated = await response.parse()
        assert_matches_type(InfoRecentlyUpdatedGetResponse, info_recently_updated, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCoingecko) -> None:
        async with async_client.onchain.tokens.info_recently_updated.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            info_recently_updated = await response.parse()
            assert_matches_type(InfoRecentlyUpdatedGetResponse, info_recently_updated, path=["response"])

        assert cast(Any, response.is_closed) is True
