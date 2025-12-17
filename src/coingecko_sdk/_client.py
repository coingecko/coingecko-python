# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Dict, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import (
        key,
        nfts,
        ping,
        coins,
        search,
        simple,
        global_,
        onchain,
        entities,
        exchanges,
        derivatives,
        token_lists,
        exchange_rates,
        asset_platforms,
        public_treasury,
    )
    from .resources.key import KeyResource, AsyncKeyResource
    from .resources.ping import PingResource, AsyncPingResource
    from .resources.entities import EntitiesResource, AsyncEntitiesResource
    from .resources.nfts.nfts import NFTsResource, AsyncNFTsResource
    from .resources.coins.coins import CoinsResource, AsyncCoinsResource
    from .resources.token_lists import TokenListsResource, AsyncTokenListsResource
    from .resources.search.search import SearchResource, AsyncSearchResource
    from .resources.simple.simple import SimpleResource, AsyncSimpleResource
    from .resources.exchange_rates import ExchangeRatesResource, AsyncExchangeRatesResource
    from .resources.asset_platforms import AssetPlatformsResource, AsyncAssetPlatformsResource
    from .resources.global_.global_ import GlobalResource, AsyncGlobalResource
    from .resources.onchain.onchain import OnchainResource, AsyncOnchainResource
    from .resources.public_treasury import PublicTreasuryResource, AsyncPublicTreasuryResource
    from .resources.exchanges.exchanges import ExchangesResource, AsyncExchangesResource
    from .resources.derivatives.derivatives import DerivativesResource, AsyncDerivativesResource

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
    # client options
    pro_api_key: str | None
    demo_api_key: str | None

    _environment: Literal["pro", "demo"] | NotGiven

    def __init__(
        self,
        *,
        pro_api_key: str | None = None,
        demo_api_key: str | None = None,
        environment: Literal["pro", "demo"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
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

    @cached_property
    def asset_platforms(self) -> AssetPlatformsResource:
        from .resources.asset_platforms import AssetPlatformsResource

        return AssetPlatformsResource(self)

    @cached_property
    def coins(self) -> CoinsResource:
        from .resources.coins import CoinsResource

        return CoinsResource(self)

    @cached_property
    def derivatives(self) -> DerivativesResource:
        from .resources.derivatives import DerivativesResource

        return DerivativesResource(self)

    @cached_property
    def entities(self) -> EntitiesResource:
        from .resources.entities import EntitiesResource

        return EntitiesResource(self)

    @cached_property
    def exchange_rates(self) -> ExchangeRatesResource:
        from .resources.exchange_rates import ExchangeRatesResource

        return ExchangeRatesResource(self)

    @cached_property
    def exchanges(self) -> ExchangesResource:
        from .resources.exchanges import ExchangesResource

        return ExchangesResource(self)

    @cached_property
    def global_(self) -> GlobalResource:
        from .resources.global_ import GlobalResource

        return GlobalResource(self)

    @cached_property
    def key(self) -> KeyResource:
        from .resources.key import KeyResource

        return KeyResource(self)

    @cached_property
    def nfts(self) -> NFTsResource:
        from .resources.nfts import NFTsResource

        return NFTsResource(self)

    @cached_property
    def onchain(self) -> OnchainResource:
        from .resources.onchain import OnchainResource

        return OnchainResource(self)

    @cached_property
    def ping(self) -> PingResource:
        from .resources.ping import PingResource

        return PingResource(self)

    @cached_property
    def public_treasury(self) -> PublicTreasuryResource:
        from .resources.public_treasury import PublicTreasuryResource

        return PublicTreasuryResource(self)

    @cached_property
    def search(self) -> SearchResource:
        from .resources.search import SearchResource

        return SearchResource(self)

    @cached_property
    def simple(self) -> SimpleResource:
        from .resources.simple import SimpleResource

        return SimpleResource(self)

    @cached_property
    def token_lists(self) -> TokenListsResource:
        from .resources.token_lists import TokenListsResource

        return TokenListsResource(self)

    @cached_property
    def with_raw_response(self) -> CoingeckoWithRawResponse:
        return CoingeckoWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CoingeckoWithStreamedResponse:
        return CoingeckoWithStreamedResponse(self)

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
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
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
    # client options
    pro_api_key: str | None
    demo_api_key: str | None

    _environment: Literal["pro", "demo"] | NotGiven

    def __init__(
        self,
        *,
        pro_api_key: str | None = None,
        demo_api_key: str | None = None,
        environment: Literal["pro", "demo"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
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

    @cached_property
    def asset_platforms(self) -> AsyncAssetPlatformsResource:
        from .resources.asset_platforms import AsyncAssetPlatformsResource

        return AsyncAssetPlatformsResource(self)

    @cached_property
    def coins(self) -> AsyncCoinsResource:
        from .resources.coins import AsyncCoinsResource

        return AsyncCoinsResource(self)

    @cached_property
    def derivatives(self) -> AsyncDerivativesResource:
        from .resources.derivatives import AsyncDerivativesResource

        return AsyncDerivativesResource(self)

    @cached_property
    def entities(self) -> AsyncEntitiesResource:
        from .resources.entities import AsyncEntitiesResource

        return AsyncEntitiesResource(self)

    @cached_property
    def exchange_rates(self) -> AsyncExchangeRatesResource:
        from .resources.exchange_rates import AsyncExchangeRatesResource

        return AsyncExchangeRatesResource(self)

    @cached_property
    def exchanges(self) -> AsyncExchangesResource:
        from .resources.exchanges import AsyncExchangesResource

        return AsyncExchangesResource(self)

    @cached_property
    def global_(self) -> AsyncGlobalResource:
        from .resources.global_ import AsyncGlobalResource

        return AsyncGlobalResource(self)

    @cached_property
    def key(self) -> AsyncKeyResource:
        from .resources.key import AsyncKeyResource

        return AsyncKeyResource(self)

    @cached_property
    def nfts(self) -> AsyncNFTsResource:
        from .resources.nfts import AsyncNFTsResource

        return AsyncNFTsResource(self)

    @cached_property
    def onchain(self) -> AsyncOnchainResource:
        from .resources.onchain import AsyncOnchainResource

        return AsyncOnchainResource(self)

    @cached_property
    def ping(self) -> AsyncPingResource:
        from .resources.ping import AsyncPingResource

        return AsyncPingResource(self)

    @cached_property
    def public_treasury(self) -> AsyncPublicTreasuryResource:
        from .resources.public_treasury import AsyncPublicTreasuryResource

        return AsyncPublicTreasuryResource(self)

    @cached_property
    def search(self) -> AsyncSearchResource:
        from .resources.search import AsyncSearchResource

        return AsyncSearchResource(self)

    @cached_property
    def simple(self) -> AsyncSimpleResource:
        from .resources.simple import AsyncSimpleResource

        return AsyncSimpleResource(self)

    @cached_property
    def token_lists(self) -> AsyncTokenListsResource:
        from .resources.token_lists import AsyncTokenListsResource

        return AsyncTokenListsResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncCoingeckoWithRawResponse:
        return AsyncCoingeckoWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCoingeckoWithStreamedResponse:
        return AsyncCoingeckoWithStreamedResponse(self)

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
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
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
    _client: Coingecko

    def __init__(self, client: Coingecko) -> None:
        self._client = client

    @cached_property
    def asset_platforms(self) -> asset_platforms.AssetPlatformsResourceWithRawResponse:
        from .resources.asset_platforms import AssetPlatformsResourceWithRawResponse

        return AssetPlatformsResourceWithRawResponse(self._client.asset_platforms)

    @cached_property
    def coins(self) -> coins.CoinsResourceWithRawResponse:
        from .resources.coins import CoinsResourceWithRawResponse

        return CoinsResourceWithRawResponse(self._client.coins)

    @cached_property
    def derivatives(self) -> derivatives.DerivativesResourceWithRawResponse:
        from .resources.derivatives import DerivativesResourceWithRawResponse

        return DerivativesResourceWithRawResponse(self._client.derivatives)

    @cached_property
    def entities(self) -> entities.EntitiesResourceWithRawResponse:
        from .resources.entities import EntitiesResourceWithRawResponse

        return EntitiesResourceWithRawResponse(self._client.entities)

    @cached_property
    def exchange_rates(self) -> exchange_rates.ExchangeRatesResourceWithRawResponse:
        from .resources.exchange_rates import ExchangeRatesResourceWithRawResponse

        return ExchangeRatesResourceWithRawResponse(self._client.exchange_rates)

    @cached_property
    def exchanges(self) -> exchanges.ExchangesResourceWithRawResponse:
        from .resources.exchanges import ExchangesResourceWithRawResponse

        return ExchangesResourceWithRawResponse(self._client.exchanges)

    @cached_property
    def global_(self) -> global_.GlobalResourceWithRawResponse:
        from .resources.global_ import GlobalResourceWithRawResponse

        return GlobalResourceWithRawResponse(self._client.global_)

    @cached_property
    def key(self) -> key.KeyResourceWithRawResponse:
        from .resources.key import KeyResourceWithRawResponse

        return KeyResourceWithRawResponse(self._client.key)

    @cached_property
    def nfts(self) -> nfts.NFTsResourceWithRawResponse:
        from .resources.nfts import NFTsResourceWithRawResponse

        return NFTsResourceWithRawResponse(self._client.nfts)

    @cached_property
    def onchain(self) -> onchain.OnchainResourceWithRawResponse:
        from .resources.onchain import OnchainResourceWithRawResponse

        return OnchainResourceWithRawResponse(self._client.onchain)

    @cached_property
    def ping(self) -> ping.PingResourceWithRawResponse:
        from .resources.ping import PingResourceWithRawResponse

        return PingResourceWithRawResponse(self._client.ping)

    @cached_property
    def public_treasury(self) -> public_treasury.PublicTreasuryResourceWithRawResponse:
        from .resources.public_treasury import PublicTreasuryResourceWithRawResponse

        return PublicTreasuryResourceWithRawResponse(self._client.public_treasury)

    @cached_property
    def search(self) -> search.SearchResourceWithRawResponse:
        from .resources.search import SearchResourceWithRawResponse

        return SearchResourceWithRawResponse(self._client.search)

    @cached_property
    def simple(self) -> simple.SimpleResourceWithRawResponse:
        from .resources.simple import SimpleResourceWithRawResponse

        return SimpleResourceWithRawResponse(self._client.simple)

    @cached_property
    def token_lists(self) -> token_lists.TokenListsResourceWithRawResponse:
        from .resources.token_lists import TokenListsResourceWithRawResponse

        return TokenListsResourceWithRawResponse(self._client.token_lists)


class AsyncCoingeckoWithRawResponse:
    _client: AsyncCoingecko

    def __init__(self, client: AsyncCoingecko) -> None:
        self._client = client

    @cached_property
    def asset_platforms(self) -> asset_platforms.AsyncAssetPlatformsResourceWithRawResponse:
        from .resources.asset_platforms import AsyncAssetPlatformsResourceWithRawResponse

        return AsyncAssetPlatformsResourceWithRawResponse(self._client.asset_platforms)

    @cached_property
    def coins(self) -> coins.AsyncCoinsResourceWithRawResponse:
        from .resources.coins import AsyncCoinsResourceWithRawResponse

        return AsyncCoinsResourceWithRawResponse(self._client.coins)

    @cached_property
    def derivatives(self) -> derivatives.AsyncDerivativesResourceWithRawResponse:
        from .resources.derivatives import AsyncDerivativesResourceWithRawResponse

        return AsyncDerivativesResourceWithRawResponse(self._client.derivatives)

    @cached_property
    def entities(self) -> entities.AsyncEntitiesResourceWithRawResponse:
        from .resources.entities import AsyncEntitiesResourceWithRawResponse

        return AsyncEntitiesResourceWithRawResponse(self._client.entities)

    @cached_property
    def exchange_rates(self) -> exchange_rates.AsyncExchangeRatesResourceWithRawResponse:
        from .resources.exchange_rates import AsyncExchangeRatesResourceWithRawResponse

        return AsyncExchangeRatesResourceWithRawResponse(self._client.exchange_rates)

    @cached_property
    def exchanges(self) -> exchanges.AsyncExchangesResourceWithRawResponse:
        from .resources.exchanges import AsyncExchangesResourceWithRawResponse

        return AsyncExchangesResourceWithRawResponse(self._client.exchanges)

    @cached_property
    def global_(self) -> global_.AsyncGlobalResourceWithRawResponse:
        from .resources.global_ import AsyncGlobalResourceWithRawResponse

        return AsyncGlobalResourceWithRawResponse(self._client.global_)

    @cached_property
    def key(self) -> key.AsyncKeyResourceWithRawResponse:
        from .resources.key import AsyncKeyResourceWithRawResponse

        return AsyncKeyResourceWithRawResponse(self._client.key)

    @cached_property
    def nfts(self) -> nfts.AsyncNFTsResourceWithRawResponse:
        from .resources.nfts import AsyncNFTsResourceWithRawResponse

        return AsyncNFTsResourceWithRawResponse(self._client.nfts)

    @cached_property
    def onchain(self) -> onchain.AsyncOnchainResourceWithRawResponse:
        from .resources.onchain import AsyncOnchainResourceWithRawResponse

        return AsyncOnchainResourceWithRawResponse(self._client.onchain)

    @cached_property
    def ping(self) -> ping.AsyncPingResourceWithRawResponse:
        from .resources.ping import AsyncPingResourceWithRawResponse

        return AsyncPingResourceWithRawResponse(self._client.ping)

    @cached_property
    def public_treasury(self) -> public_treasury.AsyncPublicTreasuryResourceWithRawResponse:
        from .resources.public_treasury import AsyncPublicTreasuryResourceWithRawResponse

        return AsyncPublicTreasuryResourceWithRawResponse(self._client.public_treasury)

    @cached_property
    def search(self) -> search.AsyncSearchResourceWithRawResponse:
        from .resources.search import AsyncSearchResourceWithRawResponse

        return AsyncSearchResourceWithRawResponse(self._client.search)

    @cached_property
    def simple(self) -> simple.AsyncSimpleResourceWithRawResponse:
        from .resources.simple import AsyncSimpleResourceWithRawResponse

        return AsyncSimpleResourceWithRawResponse(self._client.simple)

    @cached_property
    def token_lists(self) -> token_lists.AsyncTokenListsResourceWithRawResponse:
        from .resources.token_lists import AsyncTokenListsResourceWithRawResponse

        return AsyncTokenListsResourceWithRawResponse(self._client.token_lists)


class CoingeckoWithStreamedResponse:
    _client: Coingecko

    def __init__(self, client: Coingecko) -> None:
        self._client = client

    @cached_property
    def asset_platforms(self) -> asset_platforms.AssetPlatformsResourceWithStreamingResponse:
        from .resources.asset_platforms import AssetPlatformsResourceWithStreamingResponse

        return AssetPlatformsResourceWithStreamingResponse(self._client.asset_platforms)

    @cached_property
    def coins(self) -> coins.CoinsResourceWithStreamingResponse:
        from .resources.coins import CoinsResourceWithStreamingResponse

        return CoinsResourceWithStreamingResponse(self._client.coins)

    @cached_property
    def derivatives(self) -> derivatives.DerivativesResourceWithStreamingResponse:
        from .resources.derivatives import DerivativesResourceWithStreamingResponse

        return DerivativesResourceWithStreamingResponse(self._client.derivatives)

    @cached_property
    def entities(self) -> entities.EntitiesResourceWithStreamingResponse:
        from .resources.entities import EntitiesResourceWithStreamingResponse

        return EntitiesResourceWithStreamingResponse(self._client.entities)

    @cached_property
    def exchange_rates(self) -> exchange_rates.ExchangeRatesResourceWithStreamingResponse:
        from .resources.exchange_rates import ExchangeRatesResourceWithStreamingResponse

        return ExchangeRatesResourceWithStreamingResponse(self._client.exchange_rates)

    @cached_property
    def exchanges(self) -> exchanges.ExchangesResourceWithStreamingResponse:
        from .resources.exchanges import ExchangesResourceWithStreamingResponse

        return ExchangesResourceWithStreamingResponse(self._client.exchanges)

    @cached_property
    def global_(self) -> global_.GlobalResourceWithStreamingResponse:
        from .resources.global_ import GlobalResourceWithStreamingResponse

        return GlobalResourceWithStreamingResponse(self._client.global_)

    @cached_property
    def key(self) -> key.KeyResourceWithStreamingResponse:
        from .resources.key import KeyResourceWithStreamingResponse

        return KeyResourceWithStreamingResponse(self._client.key)

    @cached_property
    def nfts(self) -> nfts.NFTsResourceWithStreamingResponse:
        from .resources.nfts import NFTsResourceWithStreamingResponse

        return NFTsResourceWithStreamingResponse(self._client.nfts)

    @cached_property
    def onchain(self) -> onchain.OnchainResourceWithStreamingResponse:
        from .resources.onchain import OnchainResourceWithStreamingResponse

        return OnchainResourceWithStreamingResponse(self._client.onchain)

    @cached_property
    def ping(self) -> ping.PingResourceWithStreamingResponse:
        from .resources.ping import PingResourceWithStreamingResponse

        return PingResourceWithStreamingResponse(self._client.ping)

    @cached_property
    def public_treasury(self) -> public_treasury.PublicTreasuryResourceWithStreamingResponse:
        from .resources.public_treasury import PublicTreasuryResourceWithStreamingResponse

        return PublicTreasuryResourceWithStreamingResponse(self._client.public_treasury)

    @cached_property
    def search(self) -> search.SearchResourceWithStreamingResponse:
        from .resources.search import SearchResourceWithStreamingResponse

        return SearchResourceWithStreamingResponse(self._client.search)

    @cached_property
    def simple(self) -> simple.SimpleResourceWithStreamingResponse:
        from .resources.simple import SimpleResourceWithStreamingResponse

        return SimpleResourceWithStreamingResponse(self._client.simple)

    @cached_property
    def token_lists(self) -> token_lists.TokenListsResourceWithStreamingResponse:
        from .resources.token_lists import TokenListsResourceWithStreamingResponse

        return TokenListsResourceWithStreamingResponse(self._client.token_lists)


class AsyncCoingeckoWithStreamedResponse:
    _client: AsyncCoingecko

    def __init__(self, client: AsyncCoingecko) -> None:
        self._client = client

    @cached_property
    def asset_platforms(self) -> asset_platforms.AsyncAssetPlatformsResourceWithStreamingResponse:
        from .resources.asset_platforms import AsyncAssetPlatformsResourceWithStreamingResponse

        return AsyncAssetPlatformsResourceWithStreamingResponse(self._client.asset_platforms)

    @cached_property
    def coins(self) -> coins.AsyncCoinsResourceWithStreamingResponse:
        from .resources.coins import AsyncCoinsResourceWithStreamingResponse

        return AsyncCoinsResourceWithStreamingResponse(self._client.coins)

    @cached_property
    def derivatives(self) -> derivatives.AsyncDerivativesResourceWithStreamingResponse:
        from .resources.derivatives import AsyncDerivativesResourceWithStreamingResponse

        return AsyncDerivativesResourceWithStreamingResponse(self._client.derivatives)

    @cached_property
    def entities(self) -> entities.AsyncEntitiesResourceWithStreamingResponse:
        from .resources.entities import AsyncEntitiesResourceWithStreamingResponse

        return AsyncEntitiesResourceWithStreamingResponse(self._client.entities)

    @cached_property
    def exchange_rates(self) -> exchange_rates.AsyncExchangeRatesResourceWithStreamingResponse:
        from .resources.exchange_rates import AsyncExchangeRatesResourceWithStreamingResponse

        return AsyncExchangeRatesResourceWithStreamingResponse(self._client.exchange_rates)

    @cached_property
    def exchanges(self) -> exchanges.AsyncExchangesResourceWithStreamingResponse:
        from .resources.exchanges import AsyncExchangesResourceWithStreamingResponse

        return AsyncExchangesResourceWithStreamingResponse(self._client.exchanges)

    @cached_property
    def global_(self) -> global_.AsyncGlobalResourceWithStreamingResponse:
        from .resources.global_ import AsyncGlobalResourceWithStreamingResponse

        return AsyncGlobalResourceWithStreamingResponse(self._client.global_)

    @cached_property
    def key(self) -> key.AsyncKeyResourceWithStreamingResponse:
        from .resources.key import AsyncKeyResourceWithStreamingResponse

        return AsyncKeyResourceWithStreamingResponse(self._client.key)

    @cached_property
    def nfts(self) -> nfts.AsyncNFTsResourceWithStreamingResponse:
        from .resources.nfts import AsyncNFTsResourceWithStreamingResponse

        return AsyncNFTsResourceWithStreamingResponse(self._client.nfts)

    @cached_property
    def onchain(self) -> onchain.AsyncOnchainResourceWithStreamingResponse:
        from .resources.onchain import AsyncOnchainResourceWithStreamingResponse

        return AsyncOnchainResourceWithStreamingResponse(self._client.onchain)

    @cached_property
    def ping(self) -> ping.AsyncPingResourceWithStreamingResponse:
        from .resources.ping import AsyncPingResourceWithStreamingResponse

        return AsyncPingResourceWithStreamingResponse(self._client.ping)

    @cached_property
    def public_treasury(self) -> public_treasury.AsyncPublicTreasuryResourceWithStreamingResponse:
        from .resources.public_treasury import AsyncPublicTreasuryResourceWithStreamingResponse

        return AsyncPublicTreasuryResourceWithStreamingResponse(self._client.public_treasury)

    @cached_property
    def search(self) -> search.AsyncSearchResourceWithStreamingResponse:
        from .resources.search import AsyncSearchResourceWithStreamingResponse

        return AsyncSearchResourceWithStreamingResponse(self._client.search)

    @cached_property
    def simple(self) -> simple.AsyncSimpleResourceWithStreamingResponse:
        from .resources.simple import AsyncSimpleResourceWithStreamingResponse

        return AsyncSimpleResourceWithStreamingResponse(self._client.simple)

    @cached_property
    def token_lists(self) -> token_lists.AsyncTokenListsResourceWithStreamingResponse:
        from .resources.token_lists import AsyncTokenListsResourceWithStreamingResponse

        return AsyncTokenListsResourceWithStreamingResponse(self._client.token_lists)


Client = Coingecko

AsyncClient = AsyncCoingecko
