# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from coingecko_sdk import Coingecko, AsyncCoingecko
from coingecko_sdk.types.exchanges import (
    VolumeChartGetResponse,
    VolumeChartGetRangeResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVolumeChart:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Coingecko) -> None:
        volume_chart = client.exchanges.volume_chart.get(
            id="id",
            days="1",
        )
        assert_matches_type(VolumeChartGetResponse, volume_chart, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Coingecko) -> None:
        response = client.exchanges.volume_chart.with_raw_response.get(
            id="id",
            days="1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume_chart = response.parse()
        assert_matches_type(VolumeChartGetResponse, volume_chart, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Coingecko) -> None:
        with client.exchanges.volume_chart.with_streaming_response.get(
            id="id",
            days="1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume_chart = response.parse()
            assert_matches_type(VolumeChartGetResponse, volume_chart, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Coingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.exchanges.volume_chart.with_raw_response.get(
                id="",
                days="1",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get_range(self, client: Coingecko) -> None:
        volume_chart = client.exchanges.volume_chart.get_range(
            id="id",
            from_=0,
            to=0,
        )
        assert_matches_type(VolumeChartGetRangeResponse, volume_chart, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_range(self, client: Coingecko) -> None:
        response = client.exchanges.volume_chart.with_raw_response.get_range(
            id="id",
            from_=0,
            to=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume_chart = response.parse()
        assert_matches_type(VolumeChartGetRangeResponse, volume_chart, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_range(self, client: Coingecko) -> None:
        with client.exchanges.volume_chart.with_streaming_response.get_range(
            id="id",
            from_=0,
            to=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume_chart = response.parse()
            assert_matches_type(VolumeChartGetRangeResponse, volume_chart, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get_range(self, client: Coingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.exchanges.volume_chart.with_raw_response.get_range(
                id="",
                from_=0,
                to=0,
            )


class TestAsyncVolumeChart:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCoingecko) -> None:
        volume_chart = await async_client.exchanges.volume_chart.get(
            id="id",
            days="1",
        )
        assert_matches_type(VolumeChartGetResponse, volume_chart, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCoingecko) -> None:
        response = await async_client.exchanges.volume_chart.with_raw_response.get(
            id="id",
            days="1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume_chart = await response.parse()
        assert_matches_type(VolumeChartGetResponse, volume_chart, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCoingecko) -> None:
        async with async_client.exchanges.volume_chart.with_streaming_response.get(
            id="id",
            days="1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume_chart = await response.parse()
            assert_matches_type(VolumeChartGetResponse, volume_chart, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCoingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.exchanges.volume_chart.with_raw_response.get(
                id="",
                days="1",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_range(self, async_client: AsyncCoingecko) -> None:
        volume_chart = await async_client.exchanges.volume_chart.get_range(
            id="id",
            from_=0,
            to=0,
        )
        assert_matches_type(VolumeChartGetRangeResponse, volume_chart, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_range(self, async_client: AsyncCoingecko) -> None:
        response = await async_client.exchanges.volume_chart.with_raw_response.get_range(
            id="id",
            from_=0,
            to=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume_chart = await response.parse()
        assert_matches_type(VolumeChartGetRangeResponse, volume_chart, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_range(self, async_client: AsyncCoingecko) -> None:
        async with async_client.exchanges.volume_chart.with_streaming_response.get_range(
            id="id",
            from_=0,
            to=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume_chart = await response.parse()
            assert_matches_type(VolumeChartGetRangeResponse, volume_chart, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get_range(self, async_client: AsyncCoingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.exchanges.volume_chart.with_raw_response.get_range(
                id="",
                from_=0,
                to=0,
            )
