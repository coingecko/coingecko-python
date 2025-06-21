# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from coingecko_sdk import Coingecko, AsyncCoingecko
from coingecko_sdk.types.onchain.pools import MegafilterGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMegafilter:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Coingecko) -> None:
        megafilter = client.onchain.pools.megafilter.get()
        assert_matches_type(MegafilterGetResponse, megafilter, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_with_all_params(self, client: Coingecko) -> None:
        megafilter = client.onchain.pools.megafilter.get(
            buy_tax_percentage_max=0,
            buy_tax_percentage_min=0,
            buys_duration="5m",
            buys_max=0,
            buys_min=0,
            checks="checks",
            dexes="dexes",
            fdv_usd_max=0,
            fdv_usd_min=0,
            h24_volume_usd_max=0,
            h24_volume_usd_min=0,
            include="include",
            networks="networks",
            page=0,
            pool_created_hour_max=0,
            pool_created_hour_min=0,
            reserve_in_usd_max=0,
            reserve_in_usd_min=0,
            sell_tax_percentage_max=0,
            sell_tax_percentage_min=0,
            sells_duration="5m",
            sells_max=0,
            sells_min=0,
            sort="m5_trending",
            tx_count_duration="5m",
            tx_count_max=0,
            tx_count_min=0,
        )
        assert_matches_type(MegafilterGetResponse, megafilter, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Coingecko) -> None:
        response = client.onchain.pools.megafilter.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        megafilter = response.parse()
        assert_matches_type(MegafilterGetResponse, megafilter, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Coingecko) -> None:
        with client.onchain.pools.megafilter.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            megafilter = response.parse()
            assert_matches_type(MegafilterGetResponse, megafilter, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMegafilter:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCoingecko) -> None:
        megafilter = await async_client.onchain.pools.megafilter.get()
        assert_matches_type(MegafilterGetResponse, megafilter, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCoingecko) -> None:
        megafilter = await async_client.onchain.pools.megafilter.get(
            buy_tax_percentage_max=0,
            buy_tax_percentage_min=0,
            buys_duration="5m",
            buys_max=0,
            buys_min=0,
            checks="checks",
            dexes="dexes",
            fdv_usd_max=0,
            fdv_usd_min=0,
            h24_volume_usd_max=0,
            h24_volume_usd_min=0,
            include="include",
            networks="networks",
            page=0,
            pool_created_hour_max=0,
            pool_created_hour_min=0,
            reserve_in_usd_max=0,
            reserve_in_usd_min=0,
            sell_tax_percentage_max=0,
            sell_tax_percentage_min=0,
            sells_duration="5m",
            sells_max=0,
            sells_min=0,
            sort="m5_trending",
            tx_count_duration="5m",
            tx_count_max=0,
            tx_count_min=0,
        )
        assert_matches_type(MegafilterGetResponse, megafilter, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCoingecko) -> None:
        response = await async_client.onchain.pools.megafilter.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        megafilter = await response.parse()
        assert_matches_type(MegafilterGetResponse, megafilter, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCoingecko) -> None:
        async with async_client.onchain.pools.megafilter.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            megafilter = await response.parse()
            assert_matches_type(MegafilterGetResponse, megafilter, path=["response"])

        assert cast(Any, response.is_closed) is True
