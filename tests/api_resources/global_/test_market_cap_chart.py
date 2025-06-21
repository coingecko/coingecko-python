# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from coingecko_sdk import Coingecko, AsyncCoingecko
from coingecko_sdk.types.global_ import MarketCapChartGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMarketCapChart:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Coingecko) -> None:
        market_cap_chart = client.global_.market_cap_chart.get(
            days="1",
        )
        assert_matches_type(MarketCapChartGetResponse, market_cap_chart, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_with_all_params(self, client: Coingecko) -> None:
        market_cap_chart = client.global_.market_cap_chart.get(
            days="1",
            vs_currency="usd",
        )
        assert_matches_type(MarketCapChartGetResponse, market_cap_chart, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Coingecko) -> None:
        response = client.global_.market_cap_chart.with_raw_response.get(
            days="1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        market_cap_chart = response.parse()
        assert_matches_type(MarketCapChartGetResponse, market_cap_chart, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Coingecko) -> None:
        with client.global_.market_cap_chart.with_streaming_response.get(
            days="1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            market_cap_chart = response.parse()
            assert_matches_type(MarketCapChartGetResponse, market_cap_chart, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMarketCapChart:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCoingecko) -> None:
        market_cap_chart = await async_client.global_.market_cap_chart.get(
            days="1",
        )
        assert_matches_type(MarketCapChartGetResponse, market_cap_chart, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCoingecko) -> None:
        market_cap_chart = await async_client.global_.market_cap_chart.get(
            days="1",
            vs_currency="usd",
        )
        assert_matches_type(MarketCapChartGetResponse, market_cap_chart, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCoingecko) -> None:
        response = await async_client.global_.market_cap_chart.with_raw_response.get(
            days="1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        market_cap_chart = await response.parse()
        assert_matches_type(MarketCapChartGetResponse, market_cap_chart, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCoingecko) -> None:
        async with async_client.global_.market_cap_chart.with_streaming_response.get(
            days="1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            market_cap_chart = await response.parse()
            assert_matches_type(MarketCapChartGetResponse, market_cap_chart, path=["response"])

        assert cast(Any, response.is_closed) is True
