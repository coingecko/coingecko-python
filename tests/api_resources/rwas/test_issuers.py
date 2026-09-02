# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from coingecko_sdk import Coingecko, AsyncCoingecko
from coingecko_sdk.types.rwas import IssuerGetIDResponse, IssuerGetListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIssuers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_id(self, client: Coingecko) -> None:
        issuer = client.rwas.issuers.get_id(
            "id",
        )
        assert_matches_type(IssuerGetIDResponse, issuer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_id(self, client: Coingecko) -> None:
        response = client.rwas.issuers.with_raw_response.get_id(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        issuer = response.parse()
        assert_matches_type(IssuerGetIDResponse, issuer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_id(self, client: Coingecko) -> None:
        with client.rwas.issuers.with_streaming_response.get_id(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            issuer = response.parse()
            assert_matches_type(IssuerGetIDResponse, issuer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_id(self, client: Coingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.rwas.issuers.with_raw_response.get_id(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_list(self, client: Coingecko) -> None:
        issuer = client.rwas.issuers.get_list()
        assert_matches_type(IssuerGetListResponse, issuer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_list(self, client: Coingecko) -> None:
        response = client.rwas.issuers.with_raw_response.get_list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        issuer = response.parse()
        assert_matches_type(IssuerGetListResponse, issuer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_list(self, client: Coingecko) -> None:
        with client.rwas.issuers.with_streaming_response.get_list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            issuer = response.parse()
            assert_matches_type(IssuerGetListResponse, issuer, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncIssuers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_id(self, async_client: AsyncCoingecko) -> None:
        issuer = await async_client.rwas.issuers.get_id(
            "id",
        )
        assert_matches_type(IssuerGetIDResponse, issuer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_id(self, async_client: AsyncCoingecko) -> None:
        response = await async_client.rwas.issuers.with_raw_response.get_id(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        issuer = await response.parse()
        assert_matches_type(IssuerGetIDResponse, issuer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_id(self, async_client: AsyncCoingecko) -> None:
        async with async_client.rwas.issuers.with_streaming_response.get_id(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            issuer = await response.parse()
            assert_matches_type(IssuerGetIDResponse, issuer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_id(self, async_client: AsyncCoingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.rwas.issuers.with_raw_response.get_id(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_list(self, async_client: AsyncCoingecko) -> None:
        issuer = await async_client.rwas.issuers.get_list()
        assert_matches_type(IssuerGetListResponse, issuer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_list(self, async_client: AsyncCoingecko) -> None:
        response = await async_client.rwas.issuers.with_raw_response.get_list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        issuer = await response.parse()
        assert_matches_type(IssuerGetListResponse, issuer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_list(self, async_client: AsyncCoingecko) -> None:
        async with async_client.rwas.issuers.with_streaming_response.get_list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            issuer = await response.parse()
            assert_matches_type(IssuerGetListResponse, issuer, path=["response"])

        assert cast(Any, response.is_closed) is True
