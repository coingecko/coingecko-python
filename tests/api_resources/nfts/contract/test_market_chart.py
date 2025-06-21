# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from coingecko_sdk import Coingecko, AsyncCoingecko
from coingecko_sdk.types.nfts.contract import MarketChartGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMarketChart:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Coingecko) -> None:
        market_chart = client.nfts.contract.market_chart.get(
            contract_address="0xBd3531dA5CF5857e7CfAA92426877b022e612cf8",
            asset_platform_id="ethereum",
            days="days",
        )
        assert_matches_type(MarketChartGetResponse, market_chart, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Coingecko) -> None:
        response = client.nfts.contract.market_chart.with_raw_response.get(
            contract_address="0xBd3531dA5CF5857e7CfAA92426877b022e612cf8",
            asset_platform_id="ethereum",
            days="days",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        market_chart = response.parse()
        assert_matches_type(MarketChartGetResponse, market_chart, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Coingecko) -> None:
        with client.nfts.contract.market_chart.with_streaming_response.get(
            contract_address="0xBd3531dA5CF5857e7CfAA92426877b022e612cf8",
            asset_platform_id="ethereum",
            days="days",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            market_chart = response.parse()
            assert_matches_type(MarketChartGetResponse, market_chart, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Coingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_platform_id` but received ''"):
            client.nfts.contract.market_chart.with_raw_response.get(
                contract_address="0xBd3531dA5CF5857e7CfAA92426877b022e612cf8",
                asset_platform_id="",
                days="days",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_address` but received ''"):
            client.nfts.contract.market_chart.with_raw_response.get(
                contract_address="",
                asset_platform_id="ethereum",
                days="days",
            )


class TestAsyncMarketChart:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCoingecko) -> None:
        market_chart = await async_client.nfts.contract.market_chart.get(
            contract_address="0xBd3531dA5CF5857e7CfAA92426877b022e612cf8",
            asset_platform_id="ethereum",
            days="days",
        )
        assert_matches_type(MarketChartGetResponse, market_chart, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCoingecko) -> None:
        response = await async_client.nfts.contract.market_chart.with_raw_response.get(
            contract_address="0xBd3531dA5CF5857e7CfAA92426877b022e612cf8",
            asset_platform_id="ethereum",
            days="days",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        market_chart = await response.parse()
        assert_matches_type(MarketChartGetResponse, market_chart, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCoingecko) -> None:
        async with async_client.nfts.contract.market_chart.with_streaming_response.get(
            contract_address="0xBd3531dA5CF5857e7CfAA92426877b022e612cf8",
            asset_platform_id="ethereum",
            days="days",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            market_chart = await response.parse()
            assert_matches_type(MarketChartGetResponse, market_chart, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCoingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_platform_id` but received ''"):
            await async_client.nfts.contract.market_chart.with_raw_response.get(
                contract_address="0xBd3531dA5CF5857e7CfAA92426877b022e612cf8",
                asset_platform_id="",
                days="days",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_address` but received ''"):
            await async_client.nfts.contract.market_chart.with_raw_response.get(
                contract_address="",
                asset_platform_id="ethereum",
                days="days",
            )
