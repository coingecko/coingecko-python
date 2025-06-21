# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from coingecko_sdk import Coingecko, AsyncCoingecko
from coingecko_sdk.types import (
    NFTGetIDResponse,
    NFTGetListResponse,
    NFTGetMarketsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNFTs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_id(self, client: Coingecko) -> None:
        nft = client.nfts.get_id(
            "pudgy-penguins",
        )
        assert_matches_type(NFTGetIDResponse, nft, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_id(self, client: Coingecko) -> None:
        response = client.nfts.with_raw_response.get_id(
            "pudgy-penguins",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        nft = response.parse()
        assert_matches_type(NFTGetIDResponse, nft, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_id(self, client: Coingecko) -> None:
        with client.nfts.with_streaming_response.get_id(
            "pudgy-penguins",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            nft = response.parse()
            assert_matches_type(NFTGetIDResponse, nft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get_id(self, client: Coingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.nfts.with_raw_response.get_id(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get_list(self, client: Coingecko) -> None:
        nft = client.nfts.get_list()
        assert_matches_type(NFTGetListResponse, nft, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_list_with_all_params(self, client: Coingecko) -> None:
        nft = client.nfts.get_list(
            order="h24_volume_usd_asc",
            page=0,
            per_page=0,
        )
        assert_matches_type(NFTGetListResponse, nft, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_list(self, client: Coingecko) -> None:
        response = client.nfts.with_raw_response.get_list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        nft = response.parse()
        assert_matches_type(NFTGetListResponse, nft, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_list(self, client: Coingecko) -> None:
        with client.nfts.with_streaming_response.get_list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            nft = response.parse()
            assert_matches_type(NFTGetListResponse, nft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_markets(self, client: Coingecko) -> None:
        nft = client.nfts.get_markets()
        assert_matches_type(NFTGetMarketsResponse, nft, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_markets_with_all_params(self, client: Coingecko) -> None:
        nft = client.nfts.get_markets(
            asset_platform_id="ethereum",
            order="h24_volume_native_asc",
            page=0,
            per_page=0,
        )
        assert_matches_type(NFTGetMarketsResponse, nft, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_markets(self, client: Coingecko) -> None:
        response = client.nfts.with_raw_response.get_markets()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        nft = response.parse()
        assert_matches_type(NFTGetMarketsResponse, nft, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_markets(self, client: Coingecko) -> None:
        with client.nfts.with_streaming_response.get_markets() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            nft = response.parse()
            assert_matches_type(NFTGetMarketsResponse, nft, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncNFTs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_id(self, async_client: AsyncCoingecko) -> None:
        nft = await async_client.nfts.get_id(
            "pudgy-penguins",
        )
        assert_matches_type(NFTGetIDResponse, nft, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_id(self, async_client: AsyncCoingecko) -> None:
        response = await async_client.nfts.with_raw_response.get_id(
            "pudgy-penguins",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        nft = await response.parse()
        assert_matches_type(NFTGetIDResponse, nft, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_id(self, async_client: AsyncCoingecko) -> None:
        async with async_client.nfts.with_streaming_response.get_id(
            "pudgy-penguins",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            nft = await response.parse()
            assert_matches_type(NFTGetIDResponse, nft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get_id(self, async_client: AsyncCoingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.nfts.with_raw_response.get_id(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_list(self, async_client: AsyncCoingecko) -> None:
        nft = await async_client.nfts.get_list()
        assert_matches_type(NFTGetListResponse, nft, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_list_with_all_params(self, async_client: AsyncCoingecko) -> None:
        nft = await async_client.nfts.get_list(
            order="h24_volume_usd_asc",
            page=0,
            per_page=0,
        )
        assert_matches_type(NFTGetListResponse, nft, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_list(self, async_client: AsyncCoingecko) -> None:
        response = await async_client.nfts.with_raw_response.get_list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        nft = await response.parse()
        assert_matches_type(NFTGetListResponse, nft, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_list(self, async_client: AsyncCoingecko) -> None:
        async with async_client.nfts.with_streaming_response.get_list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            nft = await response.parse()
            assert_matches_type(NFTGetListResponse, nft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_markets(self, async_client: AsyncCoingecko) -> None:
        nft = await async_client.nfts.get_markets()
        assert_matches_type(NFTGetMarketsResponse, nft, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_markets_with_all_params(self, async_client: AsyncCoingecko) -> None:
        nft = await async_client.nfts.get_markets(
            asset_platform_id="ethereum",
            order="h24_volume_native_asc",
            page=0,
            per_page=0,
        )
        assert_matches_type(NFTGetMarketsResponse, nft, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_markets(self, async_client: AsyncCoingecko) -> None:
        response = await async_client.nfts.with_raw_response.get_markets()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        nft = await response.parse()
        assert_matches_type(NFTGetMarketsResponse, nft, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_markets(self, async_client: AsyncCoingecko) -> None:
        async with async_client.nfts.with_streaming_response.get_markets() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            nft = await response.parse()
            assert_matches_type(NFTGetMarketsResponse, nft, path=["response"])

        assert cast(Any, response.is_closed) is True
