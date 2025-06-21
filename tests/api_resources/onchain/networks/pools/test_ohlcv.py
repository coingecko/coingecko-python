# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from coingecko_sdk import Coingecko, AsyncCoingecko
from coingecko_sdk.types.onchain.networks.pools import OhlcvGetTimeframeResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOhlcv:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_timeframe(self, client: Coingecko) -> None:
        ohlcv = client.onchain.networks.pools.ohlcv.get_timeframe(
            timeframe="day",
            network="eth",
            pool_address="0x06da0fd433c1a5d7a4faa01111c044910a184553",
        )
        assert_matches_type(OhlcvGetTimeframeResponse, ohlcv, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_timeframe_with_all_params(self, client: Coingecko) -> None:
        ohlcv = client.onchain.networks.pools.ohlcv.get_timeframe(
            timeframe="day",
            network="eth",
            pool_address="0x06da0fd433c1a5d7a4faa01111c044910a184553",
            token="token",
            aggregate="aggregate",
            before_timestamp=0,
            currency="usd",
            include_empty_intervals=True,
            limit=0,
        )
        assert_matches_type(OhlcvGetTimeframeResponse, ohlcv, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_timeframe(self, client: Coingecko) -> None:
        response = client.onchain.networks.pools.ohlcv.with_raw_response.get_timeframe(
            timeframe="day",
            network="eth",
            pool_address="0x06da0fd433c1a5d7a4faa01111c044910a184553",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ohlcv = response.parse()
        assert_matches_type(OhlcvGetTimeframeResponse, ohlcv, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_timeframe(self, client: Coingecko) -> None:
        with client.onchain.networks.pools.ohlcv.with_streaming_response.get_timeframe(
            timeframe="day",
            network="eth",
            pool_address="0x06da0fd433c1a5d7a4faa01111c044910a184553",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ohlcv = response.parse()
            assert_matches_type(OhlcvGetTimeframeResponse, ohlcv, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get_timeframe(self, client: Coingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `network` but received ''"):
            client.onchain.networks.pools.ohlcv.with_raw_response.get_timeframe(
                timeframe="day",
                network="",
                pool_address="0x06da0fd433c1a5d7a4faa01111c044910a184553",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pool_address` but received ''"):
            client.onchain.networks.pools.ohlcv.with_raw_response.get_timeframe(
                timeframe="day",
                network="eth",
                pool_address="",
            )


class TestAsyncOhlcv:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_timeframe(self, async_client: AsyncCoingecko) -> None:
        ohlcv = await async_client.onchain.networks.pools.ohlcv.get_timeframe(
            timeframe="day",
            network="eth",
            pool_address="0x06da0fd433c1a5d7a4faa01111c044910a184553",
        )
        assert_matches_type(OhlcvGetTimeframeResponse, ohlcv, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_timeframe_with_all_params(self, async_client: AsyncCoingecko) -> None:
        ohlcv = await async_client.onchain.networks.pools.ohlcv.get_timeframe(
            timeframe="day",
            network="eth",
            pool_address="0x06da0fd433c1a5d7a4faa01111c044910a184553",
            token="token",
            aggregate="aggregate",
            before_timestamp=0,
            currency="usd",
            include_empty_intervals=True,
            limit=0,
        )
        assert_matches_type(OhlcvGetTimeframeResponse, ohlcv, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_timeframe(self, async_client: AsyncCoingecko) -> None:
        response = await async_client.onchain.networks.pools.ohlcv.with_raw_response.get_timeframe(
            timeframe="day",
            network="eth",
            pool_address="0x06da0fd433c1a5d7a4faa01111c044910a184553",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ohlcv = await response.parse()
        assert_matches_type(OhlcvGetTimeframeResponse, ohlcv, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_timeframe(self, async_client: AsyncCoingecko) -> None:
        async with async_client.onchain.networks.pools.ohlcv.with_streaming_response.get_timeframe(
            timeframe="day",
            network="eth",
            pool_address="0x06da0fd433c1a5d7a4faa01111c044910a184553",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ohlcv = await response.parse()
            assert_matches_type(OhlcvGetTimeframeResponse, ohlcv, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get_timeframe(self, async_client: AsyncCoingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `network` but received ''"):
            await async_client.onchain.networks.pools.ohlcv.with_raw_response.get_timeframe(
                timeframe="day",
                network="",
                pool_address="0x06da0fd433c1a5d7a4faa01111c044910a184553",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pool_address` but received ''"):
            await async_client.onchain.networks.pools.ohlcv.with_raw_response.get_timeframe(
                timeframe="day",
                network="eth",
                pool_address="",
            )
