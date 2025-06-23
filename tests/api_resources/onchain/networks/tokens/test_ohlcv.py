# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from coingecko_sdk import Coingecko, AsyncCoingecko
from coingecko_sdk.types.onchain.networks.tokens import OhlcvGetTimeframeResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOhlcv:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_timeframe(self, client: Coingecko) -> None:
        ohlcv = client.onchain.networks.tokens.ohlcv.get_timeframe(
            timeframe="day",
            network="solana",
            token_address="So11111111111111111111111111111111111111112",
        )
        assert_matches_type(OhlcvGetTimeframeResponse, ohlcv, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_timeframe_with_all_params(self, client: Coingecko) -> None:
        ohlcv = client.onchain.networks.tokens.ohlcv.get_timeframe(
            timeframe="day",
            network="solana",
            token_address="So11111111111111111111111111111111111111112",
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
        response = client.onchain.networks.tokens.ohlcv.with_raw_response.get_timeframe(
            timeframe="day",
            network="solana",
            token_address="So11111111111111111111111111111111111111112",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ohlcv = response.parse()
        assert_matches_type(OhlcvGetTimeframeResponse, ohlcv, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_timeframe(self, client: Coingecko) -> None:
        with client.onchain.networks.tokens.ohlcv.with_streaming_response.get_timeframe(
            timeframe="day",
            network="solana",
            token_address="So11111111111111111111111111111111111111112",
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
            client.onchain.networks.tokens.ohlcv.with_raw_response.get_timeframe(
                timeframe="day",
                network="",
                token_address="So11111111111111111111111111111111111111112",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token_address` but received ''"):
            client.onchain.networks.tokens.ohlcv.with_raw_response.get_timeframe(
                timeframe="day",
                network="solana",
                token_address="",
            )


class TestAsyncOhlcv:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_timeframe(self, async_client: AsyncCoingecko) -> None:
        ohlcv = await async_client.onchain.networks.tokens.ohlcv.get_timeframe(
            timeframe="day",
            network="solana",
            token_address="So11111111111111111111111111111111111111112",
        )
        assert_matches_type(OhlcvGetTimeframeResponse, ohlcv, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_timeframe_with_all_params(self, async_client: AsyncCoingecko) -> None:
        ohlcv = await async_client.onchain.networks.tokens.ohlcv.get_timeframe(
            timeframe="day",
            network="solana",
            token_address="So11111111111111111111111111111111111111112",
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
        response = await async_client.onchain.networks.tokens.ohlcv.with_raw_response.get_timeframe(
            timeframe="day",
            network="solana",
            token_address="So11111111111111111111111111111111111111112",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ohlcv = await response.parse()
        assert_matches_type(OhlcvGetTimeframeResponse, ohlcv, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_timeframe(self, async_client: AsyncCoingecko) -> None:
        async with async_client.onchain.networks.tokens.ohlcv.with_streaming_response.get_timeframe(
            timeframe="day",
            network="solana",
            token_address="So11111111111111111111111111111111111111112",
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
            await async_client.onchain.networks.tokens.ohlcv.with_raw_response.get_timeframe(
                timeframe="day",
                network="",
                token_address="So11111111111111111111111111111111111111112",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token_address` but received ''"):
            await async_client.onchain.networks.tokens.ohlcv.with_raw_response.get_timeframe(
                timeframe="day",
                network="solana",
                token_address="",
            )
