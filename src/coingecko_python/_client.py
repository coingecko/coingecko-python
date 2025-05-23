# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Dict, Union, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import is_given, get_async_library
from ._version import __version__
from .resources import key, ping, token_lists, exchange_rates, asset_platforms
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.nfts import nfts
from .resources.coins import coins
from .resources.search import search
from .resources.simple import simple
from .resources.global_ import global_
from .resources.onchain import onchain
from .resources.companies import companies
from .resources.exchanges import exchanges
from .resources.derivatives import derivatives

__all__ = [
    "ENVIRONMENTS",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Coingecko",
    "AsyncCoingecko",
    "Client",
    "AsyncClient",
]

ENVIRONMENTS: Dict[str, str] = {
    "pro": "https://pro-api.coingecko.com/api/v3",
    "demo": "https://api.coingecko.com/api/v3",
}


class Coingecko(SyncAPIClient):
    asset_platforms: asset_platforms.AssetPlatformsResource
    coins: coins.CoinsResource
    companies: companies.CompaniesResource
    derivatives: derivatives.DerivativesResource
    exchange_rates: exchange_rates.ExchangeRatesResource
    exchanges: exchanges.ExchangesResource
    global_: global_.GlobalResource
    key: key.KeyResource
    nfts: nfts.NFTsResource
    onchain: onchain.OnchainResource
    ping: ping.PingResource
    search: search.SearchResource
    simple: simple.SimpleResource
    token_lists: token_lists.TokenListsResource
    with_raw_response: CoingeckoWithRawResponse
    with_streaming_response: CoingeckoWithStreamedResponse

    # client options
    pro_api_key: str | None
    demo_api_key: str | None

    _environment: Literal["pro", "demo"] | NotGiven

    def __init__(
        self,
        *,
        pro_api_key: str | None = None,
        demo_api_key: str | None = None,
        environment: Literal["pro", "demo"] | NotGiven = NOT_GIVEN,
        base_url: str | httpx.URL | None | NotGiven = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Coingecko client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `pro_api_key` from `COINGECKO_PRO_API_KEY`
        - `demo_api_key` from `COINGECKO_DEMO_API_KEY`
        """
        if pro_api_key is None:
            pro_api_key = os.environ.get("COINGECKO_PRO_API_KEY")
        self.pro_api_key = pro_api_key

        if demo_api_key is None:
            demo_api_key = os.environ.get("COINGECKO_DEMO_API_KEY")
        self.demo_api_key = demo_api_key

        self._environment = environment

        base_url_env = os.environ.get("COINGECKO_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `COINGECKO_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "pro"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.asset_platforms = asset_platforms.AssetPlatformsResource(self)
        self.coins = coins.CoinsResource(self)
        self.companies = companies.CompaniesResource(self)
        self.derivatives = derivatives.DerivativesResource(self)
        self.exchange_rates = exchange_rates.ExchangeRatesResource(self)
        self.exchanges = exchanges.ExchangesResource(self)
        self.global_ = global_.GlobalResource(self)
        self.key = key.KeyResource(self)
        self.nfts = nfts.NFTsResource(self)
        self.onchain = onchain.OnchainResource(self)
        self.ping = ping.PingResource(self)
        self.search = search.SearchResource(self)
        self.simple = simple.SimpleResource(self)
        self.token_lists = token_lists.TokenListsResource(self)
        self.with_raw_response = CoingeckoWithRawResponse(self)
        self.with_streaming_response = CoingeckoWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        return {**self._pro_key_auth, **self._demo_key_auth}

    @property
    def _pro_key_auth(self) -> dict[str, str]:
        pro_api_key = self.pro_api_key
        if pro_api_key is None:
            return {}
        return {"x-cg-pro-api-key": pro_api_key}

    @property
    def _demo_key_auth(self) -> dict[str, str]:
        demo_api_key = self.demo_api_key
        if demo_api_key is None:
            return {}
        return {"x-cg-demo-api-key": demo_api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if self.pro_api_key and headers.get("x-cg-pro-api-key"):
            return
        if isinstance(custom_headers.get("x-cg-pro-api-key"), Omit):
            return

        if self.demo_api_key and headers.get("x-cg-demo-api-key"):
            return
        if isinstance(custom_headers.get("x-cg-demo-api-key"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected either pro_api_key or demo_api_key to be set. Or for one of the `x-cg-pro-api-key` or `x-cg-demo-api-key` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        pro_api_key: str | None = None,
        demo_api_key: str | None = None,
        environment: Literal["pro", "demo"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            pro_api_key=pro_api_key or self.pro_api_key,
            demo_api_key=demo_api_key or self.demo_api_key,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncCoingecko(AsyncAPIClient):
    asset_platforms: asset_platforms.AsyncAssetPlatformsResource
    coins: coins.AsyncCoinsResource
    companies: companies.AsyncCompaniesResource
    derivatives: derivatives.AsyncDerivativesResource
    exchange_rates: exchange_rates.AsyncExchangeRatesResource
    exchanges: exchanges.AsyncExchangesResource
    global_: global_.AsyncGlobalResource
    key: key.AsyncKeyResource
    nfts: nfts.AsyncNFTsResource
    onchain: onchain.AsyncOnchainResource
    ping: ping.AsyncPingResource
    search: search.AsyncSearchResource
    simple: simple.AsyncSimpleResource
    token_lists: token_lists.AsyncTokenListsResource
    with_raw_response: AsyncCoingeckoWithRawResponse
    with_streaming_response: AsyncCoingeckoWithStreamedResponse

    # client options
    pro_api_key: str | None
    demo_api_key: str | None

    _environment: Literal["pro", "demo"] | NotGiven

    def __init__(
        self,
        *,
        pro_api_key: str | None = None,
        demo_api_key: str | None = None,
        environment: Literal["pro", "demo"] | NotGiven = NOT_GIVEN,
        base_url: str | httpx.URL | None | NotGiven = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncCoingecko client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `pro_api_key` from `COINGECKO_PRO_API_KEY`
        - `demo_api_key` from `COINGECKO_DEMO_API_KEY`
        """
        if pro_api_key is None:
            pro_api_key = os.environ.get("COINGECKO_PRO_API_KEY")
        self.pro_api_key = pro_api_key

        if demo_api_key is None:
            demo_api_key = os.environ.get("COINGECKO_DEMO_API_KEY")
        self.demo_api_key = demo_api_key

        self._environment = environment

        base_url_env = os.environ.get("COINGECKO_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `COINGECKO_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "pro"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.asset_platforms = asset_platforms.AsyncAssetPlatformsResource(self)
        self.coins = coins.AsyncCoinsResource(self)
        self.companies = companies.AsyncCompaniesResource(self)
        self.derivatives = derivatives.AsyncDerivativesResource(self)
        self.exchange_rates = exchange_rates.AsyncExchangeRatesResource(self)
        self.exchanges = exchanges.AsyncExchangesResource(self)
        self.global_ = global_.AsyncGlobalResource(self)
        self.key = key.AsyncKeyResource(self)
        self.nfts = nfts.AsyncNFTsResource(self)
        self.onchain = onchain.AsyncOnchainResource(self)
        self.ping = ping.AsyncPingResource(self)
        self.search = search.AsyncSearchResource(self)
        self.simple = simple.AsyncSimpleResource(self)
        self.token_lists = token_lists.AsyncTokenListsResource(self)
        self.with_raw_response = AsyncCoingeckoWithRawResponse(self)
        self.with_streaming_response = AsyncCoingeckoWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        return {**self._pro_key_auth, **self._demo_key_auth}

    @property
    def _pro_key_auth(self) -> dict[str, str]:
        pro_api_key = self.pro_api_key
        if pro_api_key is None:
            return {}
        return {"x-cg-pro-api-key": pro_api_key}

    @property
    def _demo_key_auth(self) -> dict[str, str]:
        demo_api_key = self.demo_api_key
        if demo_api_key is None:
            return {}
        return {"x-cg-demo-api-key": demo_api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if self.pro_api_key and headers.get("x-cg-pro-api-key"):
            return
        if isinstance(custom_headers.get("x-cg-pro-api-key"), Omit):
            return

        if self.demo_api_key and headers.get("x-cg-demo-api-key"):
            return
        if isinstance(custom_headers.get("x-cg-demo-api-key"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected either pro_api_key or demo_api_key to be set. Or for one of the `x-cg-pro-api-key` or `x-cg-demo-api-key` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        pro_api_key: str | None = None,
        demo_api_key: str | None = None,
        environment: Literal["pro", "demo"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            pro_api_key=pro_api_key or self.pro_api_key,
            demo_api_key=demo_api_key or self.demo_api_key,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class CoingeckoWithRawResponse:
    def __init__(self, client: Coingecko) -> None:
        self.asset_platforms = asset_platforms.AssetPlatformsResourceWithRawResponse(client.asset_platforms)
        self.coins = coins.CoinsResourceWithRawResponse(client.coins)
        self.companies = companies.CompaniesResourceWithRawResponse(client.companies)
        self.derivatives = derivatives.DerivativesResourceWithRawResponse(client.derivatives)
        self.exchange_rates = exchange_rates.ExchangeRatesResourceWithRawResponse(client.exchange_rates)
        self.exchanges = exchanges.ExchangesResourceWithRawResponse(client.exchanges)
        self.global_ = global_.GlobalResourceWithRawResponse(client.global_)
        self.key = key.KeyResourceWithRawResponse(client.key)
        self.nfts = nfts.NFTsResourceWithRawResponse(client.nfts)
        self.onchain = onchain.OnchainResourceWithRawResponse(client.onchain)
        self.ping = ping.PingResourceWithRawResponse(client.ping)
        self.search = search.SearchResourceWithRawResponse(client.search)
        self.simple = simple.SimpleResourceWithRawResponse(client.simple)
        self.token_lists = token_lists.TokenListsResourceWithRawResponse(client.token_lists)


class AsyncCoingeckoWithRawResponse:
    def __init__(self, client: AsyncCoingecko) -> None:
        self.asset_platforms = asset_platforms.AsyncAssetPlatformsResourceWithRawResponse(client.asset_platforms)
        self.coins = coins.AsyncCoinsResourceWithRawResponse(client.coins)
        self.companies = companies.AsyncCompaniesResourceWithRawResponse(client.companies)
        self.derivatives = derivatives.AsyncDerivativesResourceWithRawResponse(client.derivatives)
        self.exchange_rates = exchange_rates.AsyncExchangeRatesResourceWithRawResponse(client.exchange_rates)
        self.exchanges = exchanges.AsyncExchangesResourceWithRawResponse(client.exchanges)
        self.global_ = global_.AsyncGlobalResourceWithRawResponse(client.global_)
        self.key = key.AsyncKeyResourceWithRawResponse(client.key)
        self.nfts = nfts.AsyncNFTsResourceWithRawResponse(client.nfts)
        self.onchain = onchain.AsyncOnchainResourceWithRawResponse(client.onchain)
        self.ping = ping.AsyncPingResourceWithRawResponse(client.ping)
        self.search = search.AsyncSearchResourceWithRawResponse(client.search)
        self.simple = simple.AsyncSimpleResourceWithRawResponse(client.simple)
        self.token_lists = token_lists.AsyncTokenListsResourceWithRawResponse(client.token_lists)


class CoingeckoWithStreamedResponse:
    def __init__(self, client: Coingecko) -> None:
        self.asset_platforms = asset_platforms.AssetPlatformsResourceWithStreamingResponse(client.asset_platforms)
        self.coins = coins.CoinsResourceWithStreamingResponse(client.coins)
        self.companies = companies.CompaniesResourceWithStreamingResponse(client.companies)
        self.derivatives = derivatives.DerivativesResourceWithStreamingResponse(client.derivatives)
        self.exchange_rates = exchange_rates.ExchangeRatesResourceWithStreamingResponse(client.exchange_rates)
        self.exchanges = exchanges.ExchangesResourceWithStreamingResponse(client.exchanges)
        self.global_ = global_.GlobalResourceWithStreamingResponse(client.global_)
        self.key = key.KeyResourceWithStreamingResponse(client.key)
        self.nfts = nfts.NFTsResourceWithStreamingResponse(client.nfts)
        self.onchain = onchain.OnchainResourceWithStreamingResponse(client.onchain)
        self.ping = ping.PingResourceWithStreamingResponse(client.ping)
        self.search = search.SearchResourceWithStreamingResponse(client.search)
        self.simple = simple.SimpleResourceWithStreamingResponse(client.simple)
        self.token_lists = token_lists.TokenListsResourceWithStreamingResponse(client.token_lists)


class AsyncCoingeckoWithStreamedResponse:
    def __init__(self, client: AsyncCoingecko) -> None:
        self.asset_platforms = asset_platforms.AsyncAssetPlatformsResourceWithStreamingResponse(client.asset_platforms)
        self.coins = coins.AsyncCoinsResourceWithStreamingResponse(client.coins)
        self.companies = companies.AsyncCompaniesResourceWithStreamingResponse(client.companies)
        self.derivatives = derivatives.AsyncDerivativesResourceWithStreamingResponse(client.derivatives)
        self.exchange_rates = exchange_rates.AsyncExchangeRatesResourceWithStreamingResponse(client.exchange_rates)
        self.exchanges = exchanges.AsyncExchangesResourceWithStreamingResponse(client.exchanges)
        self.global_ = global_.AsyncGlobalResourceWithStreamingResponse(client.global_)
        self.key = key.AsyncKeyResourceWithStreamingResponse(client.key)
        self.nfts = nfts.AsyncNFTsResourceWithStreamingResponse(client.nfts)
        self.onchain = onchain.AsyncOnchainResourceWithStreamingResponse(client.onchain)
        self.ping = ping.AsyncPingResourceWithStreamingResponse(client.ping)
        self.search = search.AsyncSearchResourceWithStreamingResponse(client.search)
        self.simple = simple.AsyncSimpleResourceWithStreamingResponse(client.simple)
        self.token_lists = token_lists.AsyncTokenListsResourceWithStreamingResponse(client.token_lists)


Client = Coingecko

AsyncClient = AsyncCoingecko
