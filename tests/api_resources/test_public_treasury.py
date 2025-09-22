# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from coingecko_sdk import Coingecko, AsyncCoingecko
from coingecko_sdk.types import PublicTreasuryGetCoinIDResponse, PublicTreasuryGetEntityIDResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPublicTreasury:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_coin_id(self, client: Coingecko) -> None:
        public_treasury = client.public_treasury.get_coin_id(
            coin_id="bitcoin",
            entity="companies",
        )
        assert_matches_type(PublicTreasuryGetCoinIDResponse, public_treasury, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_coin_id(self, client: Coingecko) -> None:
        response = client.public_treasury.with_raw_response.get_coin_id(
            coin_id="bitcoin",
            entity="companies",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        public_treasury = response.parse()
        assert_matches_type(PublicTreasuryGetCoinIDResponse, public_treasury, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_coin_id(self, client: Coingecko) -> None:
        with client.public_treasury.with_streaming_response.get_coin_id(
            coin_id="bitcoin",
            entity="companies",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            public_treasury = response.parse()
            assert_matches_type(PublicTreasuryGetCoinIDResponse, public_treasury, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_coin_id(self, client: Coingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `coin_id` but received ''"):
            client.public_treasury.with_raw_response.get_coin_id(
                coin_id="",
                entity="companies",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_entity_id(self, client: Coingecko) -> None:
        public_treasury = client.public_treasury.get_entity_id(
            "strategy",
        )
        assert_matches_type(PublicTreasuryGetEntityIDResponse, public_treasury, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_entity_id(self, client: Coingecko) -> None:
        response = client.public_treasury.with_raw_response.get_entity_id(
            "strategy",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        public_treasury = response.parse()
        assert_matches_type(PublicTreasuryGetEntityIDResponse, public_treasury, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_entity_id(self, client: Coingecko) -> None:
        with client.public_treasury.with_streaming_response.get_entity_id(
            "strategy",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            public_treasury = response.parse()
            assert_matches_type(PublicTreasuryGetEntityIDResponse, public_treasury, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_entity_id(self, client: Coingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
            client.public_treasury.with_raw_response.get_entity_id(
                "",
            )


class TestAsyncPublicTreasury:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_coin_id(self, async_client: AsyncCoingecko) -> None:
        public_treasury = await async_client.public_treasury.get_coin_id(
            coin_id="bitcoin",
            entity="companies",
        )
        assert_matches_type(PublicTreasuryGetCoinIDResponse, public_treasury, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_coin_id(self, async_client: AsyncCoingecko) -> None:
        response = await async_client.public_treasury.with_raw_response.get_coin_id(
            coin_id="bitcoin",
            entity="companies",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        public_treasury = await response.parse()
        assert_matches_type(PublicTreasuryGetCoinIDResponse, public_treasury, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_coin_id(self, async_client: AsyncCoingecko) -> None:
        async with async_client.public_treasury.with_streaming_response.get_coin_id(
            coin_id="bitcoin",
            entity="companies",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            public_treasury = await response.parse()
            assert_matches_type(PublicTreasuryGetCoinIDResponse, public_treasury, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_coin_id(self, async_client: AsyncCoingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `coin_id` but received ''"):
            await async_client.public_treasury.with_raw_response.get_coin_id(
                coin_id="",
                entity="companies",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_entity_id(self, async_client: AsyncCoingecko) -> None:
        public_treasury = await async_client.public_treasury.get_entity_id(
            "strategy",
        )
        assert_matches_type(PublicTreasuryGetEntityIDResponse, public_treasury, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_entity_id(self, async_client: AsyncCoingecko) -> None:
        response = await async_client.public_treasury.with_raw_response.get_entity_id(
            "strategy",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        public_treasury = await response.parse()
        assert_matches_type(PublicTreasuryGetEntityIDResponse, public_treasury, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_entity_id(self, async_client: AsyncCoingecko) -> None:
        async with async_client.public_treasury.with_streaming_response.get_entity_id(
            "strategy",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            public_treasury = await response.parse()
            assert_matches_type(PublicTreasuryGetEntityIDResponse, public_treasury, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_entity_id(self, async_client: AsyncCoingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
            await async_client.public_treasury.with_raw_response.get_entity_id(
                "",
            )
