# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from coingecko_sdk import Coingecko, AsyncCoingecko
from coingecko_sdk.types.coins import (
    TotalSupplyChartGetResponse,
    TotalSupplyChartGetRangeResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTotalSupplyChart:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Coingecko) -> None:
        total_supply_chart = client.coins.total_supply_chart.get(
            id="bitcoin",
            days="days",
        )
        assert_matches_type(TotalSupplyChartGetResponse, total_supply_chart, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_with_all_params(self, client: Coingecko) -> None:
        total_supply_chart = client.coins.total_supply_chart.get(
            id="bitcoin",
            days="days",
            interval="daily",
        )
        assert_matches_type(TotalSupplyChartGetResponse, total_supply_chart, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Coingecko) -> None:
        response = client.coins.total_supply_chart.with_raw_response.get(
            id="bitcoin",
            days="days",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        total_supply_chart = response.parse()
        assert_matches_type(TotalSupplyChartGetResponse, total_supply_chart, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Coingecko) -> None:
        with client.coins.total_supply_chart.with_streaming_response.get(
            id="bitcoin",
            days="days",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            total_supply_chart = response.parse()
            assert_matches_type(TotalSupplyChartGetResponse, total_supply_chart, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Coingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.coins.total_supply_chart.with_raw_response.get(
                id="",
                days="days",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get_range(self, client: Coingecko) -> None:
        total_supply_chart = client.coins.total_supply_chart.get_range(
            id="bitcoin",
            from_=0,
            to=0,
        )
        assert_matches_type(TotalSupplyChartGetRangeResponse, total_supply_chart, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_range(self, client: Coingecko) -> None:
        response = client.coins.total_supply_chart.with_raw_response.get_range(
            id="bitcoin",
            from_=0,
            to=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        total_supply_chart = response.parse()
        assert_matches_type(TotalSupplyChartGetRangeResponse, total_supply_chart, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_range(self, client: Coingecko) -> None:
        with client.coins.total_supply_chart.with_streaming_response.get_range(
            id="bitcoin",
            from_=0,
            to=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            total_supply_chart = response.parse()
            assert_matches_type(TotalSupplyChartGetRangeResponse, total_supply_chart, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get_range(self, client: Coingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.coins.total_supply_chart.with_raw_response.get_range(
                id="",
                from_=0,
                to=0,
            )


class TestAsyncTotalSupplyChart:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCoingecko) -> None:
        total_supply_chart = await async_client.coins.total_supply_chart.get(
            id="bitcoin",
            days="days",
        )
        assert_matches_type(TotalSupplyChartGetResponse, total_supply_chart, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCoingecko) -> None:
        total_supply_chart = await async_client.coins.total_supply_chart.get(
            id="bitcoin",
            days="days",
            interval="daily",
        )
        assert_matches_type(TotalSupplyChartGetResponse, total_supply_chart, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCoingecko) -> None:
        response = await async_client.coins.total_supply_chart.with_raw_response.get(
            id="bitcoin",
            days="days",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        total_supply_chart = await response.parse()
        assert_matches_type(TotalSupplyChartGetResponse, total_supply_chart, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCoingecko) -> None:
        async with async_client.coins.total_supply_chart.with_streaming_response.get(
            id="bitcoin",
            days="days",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            total_supply_chart = await response.parse()
            assert_matches_type(TotalSupplyChartGetResponse, total_supply_chart, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCoingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.coins.total_supply_chart.with_raw_response.get(
                id="",
                days="days",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_range(self, async_client: AsyncCoingecko) -> None:
        total_supply_chart = await async_client.coins.total_supply_chart.get_range(
            id="bitcoin",
            from_=0,
            to=0,
        )
        assert_matches_type(TotalSupplyChartGetRangeResponse, total_supply_chart, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_range(self, async_client: AsyncCoingecko) -> None:
        response = await async_client.coins.total_supply_chart.with_raw_response.get_range(
            id="bitcoin",
            from_=0,
            to=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        total_supply_chart = await response.parse()
        assert_matches_type(TotalSupplyChartGetRangeResponse, total_supply_chart, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_range(self, async_client: AsyncCoingecko) -> None:
        async with async_client.coins.total_supply_chart.with_streaming_response.get_range(
            id="bitcoin",
            from_=0,
            to=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            total_supply_chart = await response.parse()
            assert_matches_type(TotalSupplyChartGetRangeResponse, total_supply_chart, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get_range(self, async_client: AsyncCoingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.coins.total_supply_chart.with_raw_response.get_range(
                id="",
                from_=0,
                to=0,
            )
