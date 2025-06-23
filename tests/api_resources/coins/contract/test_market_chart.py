# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from coingecko_sdk import Coingecko, AsyncCoingecko
from coingecko_sdk.types.coins.contract import (
    MarketChartGetResponse,
    MarketChartGetRangeResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMarketChart:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Coingecko) -> None:
        market_chart = client.coins.contract.market_chart.get(
            contract_address="0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
            id="ethereum",
            days="days",
            vs_currency="usd",
        )
        assert_matches_type(MarketChartGetResponse, market_chart, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_with_all_params(self, client: Coingecko) -> None:
        market_chart = client.coins.contract.market_chart.get(
            contract_address="0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
            id="ethereum",
            days="days",
            vs_currency="usd",
            interval="5m",
            precision="full",
        )
        assert_matches_type(MarketChartGetResponse, market_chart, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Coingecko) -> None:
        response = client.coins.contract.market_chart.with_raw_response.get(
            contract_address="0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
            id="ethereum",
            days="days",
            vs_currency="usd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        market_chart = response.parse()
        assert_matches_type(MarketChartGetResponse, market_chart, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Coingecko) -> None:
        with client.coins.contract.market_chart.with_streaming_response.get(
            contract_address="0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
            id="ethereum",
            days="days",
            vs_currency="usd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            market_chart = response.parse()
            assert_matches_type(MarketChartGetResponse, market_chart, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Coingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.coins.contract.market_chart.with_raw_response.get(
                contract_address="0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
                id="",
                days="days",
                vs_currency="usd",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_address` but received ''"):
            client.coins.contract.market_chart.with_raw_response.get(
                contract_address="",
                id="ethereum",
                days="days",
                vs_currency="usd",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get_range(self, client: Coingecko) -> None:
        market_chart = client.coins.contract.market_chart.get_range(
            contract_address="0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
            id="ethereum",
            from_=0,
            to=0,
            vs_currency="usd",
        )
        assert_matches_type(MarketChartGetRangeResponse, market_chart, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_range_with_all_params(self, client: Coingecko) -> None:
        market_chart = client.coins.contract.market_chart.get_range(
            contract_address="0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
            id="ethereum",
            from_=0,
            to=0,
            vs_currency="usd",
            interval="5m",
            precision="full",
        )
        assert_matches_type(MarketChartGetRangeResponse, market_chart, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_range(self, client: Coingecko) -> None:
        response = client.coins.contract.market_chart.with_raw_response.get_range(
            contract_address="0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
            id="ethereum",
            from_=0,
            to=0,
            vs_currency="usd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        market_chart = response.parse()
        assert_matches_type(MarketChartGetRangeResponse, market_chart, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_range(self, client: Coingecko) -> None:
        with client.coins.contract.market_chart.with_streaming_response.get_range(
            contract_address="0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
            id="ethereum",
            from_=0,
            to=0,
            vs_currency="usd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            market_chart = response.parse()
            assert_matches_type(MarketChartGetRangeResponse, market_chart, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get_range(self, client: Coingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.coins.contract.market_chart.with_raw_response.get_range(
                contract_address="0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
                id="",
                from_=0,
                to=0,
                vs_currency="usd",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_address` but received ''"):
            client.coins.contract.market_chart.with_raw_response.get_range(
                contract_address="",
                id="ethereum",
                from_=0,
                to=0,
                vs_currency="usd",
            )


class TestAsyncMarketChart:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCoingecko) -> None:
        market_chart = await async_client.coins.contract.market_chart.get(
            contract_address="0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
            id="ethereum",
            days="days",
            vs_currency="usd",
        )
        assert_matches_type(MarketChartGetResponse, market_chart, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCoingecko) -> None:
        market_chart = await async_client.coins.contract.market_chart.get(
            contract_address="0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
            id="ethereum",
            days="days",
            vs_currency="usd",
            interval="5m",
            precision="full",
        )
        assert_matches_type(MarketChartGetResponse, market_chart, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCoingecko) -> None:
        response = await async_client.coins.contract.market_chart.with_raw_response.get(
            contract_address="0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
            id="ethereum",
            days="days",
            vs_currency="usd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        market_chart = await response.parse()
        assert_matches_type(MarketChartGetResponse, market_chart, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCoingecko) -> None:
        async with async_client.coins.contract.market_chart.with_streaming_response.get(
            contract_address="0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
            id="ethereum",
            days="days",
            vs_currency="usd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            market_chart = await response.parse()
            assert_matches_type(MarketChartGetResponse, market_chart, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCoingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.coins.contract.market_chart.with_raw_response.get(
                contract_address="0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
                id="",
                days="days",
                vs_currency="usd",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_address` but received ''"):
            await async_client.coins.contract.market_chart.with_raw_response.get(
                contract_address="",
                id="ethereum",
                days="days",
                vs_currency="usd",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_range(self, async_client: AsyncCoingecko) -> None:
        market_chart = await async_client.coins.contract.market_chart.get_range(
            contract_address="0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
            id="ethereum",
            from_=0,
            to=0,
            vs_currency="usd",
        )
        assert_matches_type(MarketChartGetRangeResponse, market_chart, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_range_with_all_params(self, async_client: AsyncCoingecko) -> None:
        market_chart = await async_client.coins.contract.market_chart.get_range(
            contract_address="0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
            id="ethereum",
            from_=0,
            to=0,
            vs_currency="usd",
            interval="5m",
            precision="full",
        )
        assert_matches_type(MarketChartGetRangeResponse, market_chart, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_range(self, async_client: AsyncCoingecko) -> None:
        response = await async_client.coins.contract.market_chart.with_raw_response.get_range(
            contract_address="0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
            id="ethereum",
            from_=0,
            to=0,
            vs_currency="usd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        market_chart = await response.parse()
        assert_matches_type(MarketChartGetRangeResponse, market_chart, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_range(self, async_client: AsyncCoingecko) -> None:
        async with async_client.coins.contract.market_chart.with_streaming_response.get_range(
            contract_address="0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
            id="ethereum",
            from_=0,
            to=0,
            vs_currency="usd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            market_chart = await response.parse()
            assert_matches_type(MarketChartGetRangeResponse, market_chart, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get_range(self, async_client: AsyncCoingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.coins.contract.market_chart.with_raw_response.get_range(
                contract_address="0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
                id="",
                from_=0,
                to=0,
                vs_currency="usd",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_address` but received ''"):
            await async_client.coins.contract.market_chart.with_raw_response.get_range(
                contract_address="",
                id="ethereum",
                from_=0,
                to=0,
                vs_currency="usd",
            )
