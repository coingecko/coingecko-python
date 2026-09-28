# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from coingecko_sdk import Coingecko, AsyncCoingecko
from coingecko_sdk.types.onchain.wallets import PnlGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPnl:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: Coingecko) -> None:
        pnl = client.onchain.wallets.pnl.get(
            address="address",
            networks="networks",
        )
        assert_matches_type(PnlGetResponse, pnl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: Coingecko) -> None:
        pnl = client.onchain.wallets.pnl.get(
            address="address",
            networks="networks",
            page=0,
            per_page=0,
            sort="realized_pnl_usd_desc",
        )
        assert_matches_type(PnlGetResponse, pnl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Coingecko) -> None:
        response = client.onchain.wallets.pnl.with_raw_response.get(
            address="address",
            networks="networks",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pnl = response.parse()
        assert_matches_type(PnlGetResponse, pnl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Coingecko) -> None:
        with client.onchain.wallets.pnl.with_streaming_response.get(
            address="address",
            networks="networks",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pnl = response.parse()
            assert_matches_type(PnlGetResponse, pnl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Coingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            client.onchain.wallets.pnl.with_raw_response.get(
                address="",
                networks="networks",
            )


class TestAsyncPnl:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncCoingecko) -> None:
        pnl = await async_client.onchain.wallets.pnl.get(
            address="address",
            networks="networks",
        )
        assert_matches_type(PnlGetResponse, pnl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCoingecko) -> None:
        pnl = await async_client.onchain.wallets.pnl.get(
            address="address",
            networks="networks",
            page=0,
            per_page=0,
            sort="realized_pnl_usd_desc",
        )
        assert_matches_type(PnlGetResponse, pnl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCoingecko) -> None:
        response = await async_client.onchain.wallets.pnl.with_raw_response.get(
            address="address",
            networks="networks",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pnl = await response.parse()
        assert_matches_type(PnlGetResponse, pnl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCoingecko) -> None:
        async with async_client.onchain.wallets.pnl.with_streaming_response.get(
            address="address",
            networks="networks",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pnl = await response.parse()
            assert_matches_type(PnlGetResponse, pnl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCoingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            await async_client.onchain.wallets.pnl.with_raw_response.get(
                address="",
                networks="networks",
            )
