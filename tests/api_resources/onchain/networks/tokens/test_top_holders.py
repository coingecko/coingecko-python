# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from coingecko_sdk import Coingecko, AsyncCoingecko
from coingecko_sdk.types.onchain.networks.tokens import TopHolderGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTopHolders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Coingecko) -> None:
        top_holder = client.onchain.networks.tokens.top_holders.get(
            address="0x6921b130d297cc43754afba22e5eac0fbf8db75b",
            network="base",
        )
        assert_matches_type(TopHolderGetResponse, top_holder, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_with_all_params(self, client: Coingecko) -> None:
        top_holder = client.onchain.networks.tokens.top_holders.get(
            address="0x6921b130d297cc43754afba22e5eac0fbf8db75b",
            network="base",
            holders="holders",
        )
        assert_matches_type(TopHolderGetResponse, top_holder, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Coingecko) -> None:
        response = client.onchain.networks.tokens.top_holders.with_raw_response.get(
            address="0x6921b130d297cc43754afba22e5eac0fbf8db75b",
            network="base",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top_holder = response.parse()
        assert_matches_type(TopHolderGetResponse, top_holder, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Coingecko) -> None:
        with client.onchain.networks.tokens.top_holders.with_streaming_response.get(
            address="0x6921b130d297cc43754afba22e5eac0fbf8db75b",
            network="base",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top_holder = response.parse()
            assert_matches_type(TopHolderGetResponse, top_holder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Coingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `network` but received ''"):
            client.onchain.networks.tokens.top_holders.with_raw_response.get(
                address="0x6921b130d297cc43754afba22e5eac0fbf8db75b",
                network="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            client.onchain.networks.tokens.top_holders.with_raw_response.get(
                address="",
                network="base",
            )


class TestAsyncTopHolders:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCoingecko) -> None:
        top_holder = await async_client.onchain.networks.tokens.top_holders.get(
            address="0x6921b130d297cc43754afba22e5eac0fbf8db75b",
            network="base",
        )
        assert_matches_type(TopHolderGetResponse, top_holder, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCoingecko) -> None:
        top_holder = await async_client.onchain.networks.tokens.top_holders.get(
            address="0x6921b130d297cc43754afba22e5eac0fbf8db75b",
            network="base",
            holders="holders",
        )
        assert_matches_type(TopHolderGetResponse, top_holder, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCoingecko) -> None:
        response = await async_client.onchain.networks.tokens.top_holders.with_raw_response.get(
            address="0x6921b130d297cc43754afba22e5eac0fbf8db75b",
            network="base",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top_holder = await response.parse()
        assert_matches_type(TopHolderGetResponse, top_holder, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCoingecko) -> None:
        async with async_client.onchain.networks.tokens.top_holders.with_streaming_response.get(
            address="0x6921b130d297cc43754afba22e5eac0fbf8db75b",
            network="base",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top_holder = await response.parse()
            assert_matches_type(TopHolderGetResponse, top_holder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCoingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `network` but received ''"):
            await async_client.onchain.networks.tokens.top_holders.with_raw_response.get(
                address="0x6921b130d297cc43754afba22e5eac0fbf8db75b",
                network="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            await async_client.onchain.networks.tokens.top_holders.with_raw_response.get(
                address="",
                network="base",
            )
