# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from coingecko_sdk import Coingecko, AsyncCoingecko
from coingecko_sdk.types.coins import OhlcGetResponse, OhlcGetRangeResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOhlc:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Coingecko) -> None:
        ohlc = client.coins.ohlc.get(
            id="bitcoin",
            days="1",
            vs_currency="usd",
        )
        assert_matches_type(OhlcGetResponse, ohlc, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_with_all_params(self, client: Coingecko) -> None:
        ohlc = client.coins.ohlc.get(
            id="bitcoin",
            days="1",
            vs_currency="usd",
            interval="daily",
            precision="full",
        )
        assert_matches_type(OhlcGetResponse, ohlc, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Coingecko) -> None:
        response = client.coins.ohlc.with_raw_response.get(
            id="bitcoin",
            days="1",
            vs_currency="usd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ohlc = response.parse()
        assert_matches_type(OhlcGetResponse, ohlc, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Coingecko) -> None:
        with client.coins.ohlc.with_streaming_response.get(
            id="bitcoin",
            days="1",
            vs_currency="usd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ohlc = response.parse()
            assert_matches_type(OhlcGetResponse, ohlc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Coingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.coins.ohlc.with_raw_response.get(
                id="",
                days="1",
                vs_currency="usd",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get_range(self, client: Coingecko) -> None:
        ohlc = client.coins.ohlc.get_range(
            id="bitcoin",
            from_=0,
            interval="daily",
            to=0,
            vs_currency="usd",
        )
        assert_matches_type(OhlcGetRangeResponse, ohlc, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_range(self, client: Coingecko) -> None:
        response = client.coins.ohlc.with_raw_response.get_range(
            id="bitcoin",
            from_=0,
            interval="daily",
            to=0,
            vs_currency="usd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ohlc = response.parse()
        assert_matches_type(OhlcGetRangeResponse, ohlc, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_range(self, client: Coingecko) -> None:
        with client.coins.ohlc.with_streaming_response.get_range(
            id="bitcoin",
            from_=0,
            interval="daily",
            to=0,
            vs_currency="usd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ohlc = response.parse()
            assert_matches_type(OhlcGetRangeResponse, ohlc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get_range(self, client: Coingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.coins.ohlc.with_raw_response.get_range(
                id="",
                from_=0,
                interval="daily",
                to=0,
                vs_currency="usd",
            )


class TestAsyncOhlc:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCoingecko) -> None:
        ohlc = await async_client.coins.ohlc.get(
            id="bitcoin",
            days="1",
            vs_currency="usd",
        )
        assert_matches_type(OhlcGetResponse, ohlc, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCoingecko) -> None:
        ohlc = await async_client.coins.ohlc.get(
            id="bitcoin",
            days="1",
            vs_currency="usd",
            interval="daily",
            precision="full",
        )
        assert_matches_type(OhlcGetResponse, ohlc, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCoingecko) -> None:
        response = await async_client.coins.ohlc.with_raw_response.get(
            id="bitcoin",
            days="1",
            vs_currency="usd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ohlc = await response.parse()
        assert_matches_type(OhlcGetResponse, ohlc, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCoingecko) -> None:
        async with async_client.coins.ohlc.with_streaming_response.get(
            id="bitcoin",
            days="1",
            vs_currency="usd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ohlc = await response.parse()
            assert_matches_type(OhlcGetResponse, ohlc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCoingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.coins.ohlc.with_raw_response.get(
                id="",
                days="1",
                vs_currency="usd",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_range(self, async_client: AsyncCoingecko) -> None:
        ohlc = await async_client.coins.ohlc.get_range(
            id="bitcoin",
            from_=0,
            interval="daily",
            to=0,
            vs_currency="usd",
        )
        assert_matches_type(OhlcGetRangeResponse, ohlc, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_range(self, async_client: AsyncCoingecko) -> None:
        response = await async_client.coins.ohlc.with_raw_response.get_range(
            id="bitcoin",
            from_=0,
            interval="daily",
            to=0,
            vs_currency="usd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ohlc = await response.parse()
        assert_matches_type(OhlcGetRangeResponse, ohlc, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_range(self, async_client: AsyncCoingecko) -> None:
        async with async_client.coins.ohlc.with_streaming_response.get_range(
            id="bitcoin",
            from_=0,
            interval="daily",
            to=0,
            vs_currency="usd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ohlc = await response.parse()
            assert_matches_type(OhlcGetRangeResponse, ohlc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get_range(self, async_client: AsyncCoingecko) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.coins.ohlc.with_raw_response.get_range(
                id="",
                from_=0,
                interval="daily",
                to=0,
                vs_currency="usd",
            )
