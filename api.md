# AssetPlatforms

Types:

```python
from coingecko_sdk.types import AssetPlatformGetResponse
```

Methods:

- <code title="get /asset_platforms">client.asset_platforms.<a href="./src/coingecko_sdk/resources/asset_platforms.py">get</a>(\*\*<a href="src/coingecko_sdk/types/asset_platform_get_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/asset_platform_get_response.py">AssetPlatformGetResponse</a></code>

# Coins

Types:

```python
from coingecko_sdk.types import CoinGetIDResponse
```

Methods:

- <code title="get /coins/{id}">client.coins.<a href="./src/coingecko_sdk/resources/coins/coins.py">get_id</a>(id, \*\*<a href="src/coingecko_sdk/types/coin_get_id_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/coin_get_id_response.py">CoinGetIDResponse</a></code>

## Categories

Types:

```python
from coingecko_sdk.types.coins import CategoryGetResponse, CategoryGetListResponse
```

Methods:

- <code title="get /coins/categories">client.coins.categories.<a href="./src/coingecko_sdk/resources/coins/categories.py">get</a>(\*\*<a href="src/coingecko_sdk/types/coins/category_get_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/coins/category_get_response.py">CategoryGetResponse</a></code>
- <code title="get /coins/categories/list">client.coins.categories.<a href="./src/coingecko_sdk/resources/coins/categories.py">get_list</a>() -> <a href="./src/coingecko_sdk/types/coins/category_get_list_response.py">CategoryGetListResponse</a></code>

## List

Types:

```python
from coingecko_sdk.types.coins import ListGetResponse, ListGetNewResponse
```

Methods:

- <code title="get /coins/list">client.coins.list.<a href="./src/coingecko_sdk/resources/coins/list.py">get</a>(\*\*<a href="src/coingecko_sdk/types/coins/list_get_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/coins/list_get_response.py">ListGetResponse</a></code>
- <code title="get /coins/list/new">client.coins.list.<a href="./src/coingecko_sdk/resources/coins/list.py">get_new</a>() -> <a href="./src/coingecko_sdk/types/coins/list_get_new_response.py">ListGetNewResponse</a></code>

## Markets

Types:

```python
from coingecko_sdk.types.coins import MarketGetResponse
```

Methods:

- <code title="get /coins/markets">client.coins.markets.<a href="./src/coingecko_sdk/resources/coins/markets.py">get</a>(\*\*<a href="src/coingecko_sdk/types/coins/market_get_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/coins/market_get_response.py">MarketGetResponse</a></code>

## TopGainersLosers

Types:

```python
from coingecko_sdk.types.coins import TopGainersLoserGetResponse
```

Methods:

- <code title="get /coins/top_gainers_losers">client.coins.top_gainers_losers.<a href="./src/coingecko_sdk/resources/coins/top_gainers_losers.py">get</a>(\*\*<a href="src/coingecko_sdk/types/coins/top_gainers_loser_get_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/coins/top_gainers_loser_get_response.py">TopGainersLoserGetResponse</a></code>

## CirculatingSupplyChart

Types:

```python
from coingecko_sdk.types.coins import (
    CirculatingSupplyChartGetResponse,
    CirculatingSupplyChartGetRangeResponse,
)
```

Methods:

- <code title="get /coins/{id}/circulating_supply_chart">client.coins.circulating_supply_chart.<a href="./src/coingecko_sdk/resources/coins/circulating_supply_chart.py">get</a>(id, \*\*<a href="src/coingecko_sdk/types/coins/circulating_supply_chart_get_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/coins/circulating_supply_chart_get_response.py">CirculatingSupplyChartGetResponse</a></code>
- <code title="get /coins/{id}/circulating_supply_chart/range">client.coins.circulating_supply_chart.<a href="./src/coingecko_sdk/resources/coins/circulating_supply_chart.py">get_range</a>(id, \*\*<a href="src/coingecko_sdk/types/coins/circulating_supply_chart_get_range_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/coins/circulating_supply_chart_get_range_response.py">CirculatingSupplyChartGetRangeResponse</a></code>

## Contract

Types:

```python
from coingecko_sdk.types.coins import ContractGetResponse
```

Methods:

- <code title="get /coins/{id}/contract/{contract_address}">client.coins.contract.<a href="./src/coingecko_sdk/resources/coins/contract/contract.py">get</a>(contract_address, \*, id) -> <a href="./src/coingecko_sdk/types/coins/contract_get_response.py">ContractGetResponse</a></code>

### MarketChart

Types:

```python
from coingecko_sdk.types.coins.contract import MarketChartGetResponse, MarketChartGetRangeResponse
```

Methods:

- <code title="get /coins/{id}/contract/{contract_address}/market_chart">client.coins.contract.market_chart.<a href="./src/coingecko_sdk/resources/coins/contract/market_chart.py">get</a>(contract_address, \*, id, \*\*<a href="src/coingecko_sdk/types/coins/contract/market_chart_get_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/coins/contract/market_chart_get_response.py">MarketChartGetResponse</a></code>
- <code title="get /coins/{id}/contract/{contract_address}/market_chart/range">client.coins.contract.market_chart.<a href="./src/coingecko_sdk/resources/coins/contract/market_chart.py">get_range</a>(contract_address, \*, id, \*\*<a href="src/coingecko_sdk/types/coins/contract/market_chart_get_range_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/coins/contract/market_chart_get_range_response.py">MarketChartGetRangeResponse</a></code>

## History

Types:

```python
from coingecko_sdk.types.coins import HistoryGetResponse
```

Methods:

- <code title="get /coins/{id}/history">client.coins.history.<a href="./src/coingecko_sdk/resources/coins/history.py">get</a>(id, \*\*<a href="src/coingecko_sdk/types/coins/history_get_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/coins/history_get_response.py">HistoryGetResponse</a></code>

## MarketChart

Types:

```python
from coingecko_sdk.types.coins import MarketChartGetResponse, MarketChartGetRangeResponse
```

Methods:

- <code title="get /coins/{id}/market_chart">client.coins.market_chart.<a href="./src/coingecko_sdk/resources/coins/market_chart.py">get</a>(id, \*\*<a href="src/coingecko_sdk/types/coins/market_chart_get_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/coins/market_chart_get_response.py">MarketChartGetResponse</a></code>
- <code title="get /coins/{id}/market_chart/range">client.coins.market_chart.<a href="./src/coingecko_sdk/resources/coins/market_chart.py">get_range</a>(id, \*\*<a href="src/coingecko_sdk/types/coins/market_chart_get_range_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/coins/market_chart_get_range_response.py">MarketChartGetRangeResponse</a></code>

## Ohlc

Types:

```python
from coingecko_sdk.types.coins import OhlcGetResponse, OhlcGetRangeResponse
```

Methods:

- <code title="get /coins/{id}/ohlc">client.coins.ohlc.<a href="./src/coingecko_sdk/resources/coins/ohlc.py">get</a>(id, \*\*<a href="src/coingecko_sdk/types/coins/ohlc_get_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/coins/ohlc_get_response.py">OhlcGetResponse</a></code>
- <code title="get /coins/{id}/ohlc/range">client.coins.ohlc.<a href="./src/coingecko_sdk/resources/coins/ohlc.py">get_range</a>(id, \*\*<a href="src/coingecko_sdk/types/coins/ohlc_get_range_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/coins/ohlc_get_range_response.py">OhlcGetRangeResponse</a></code>

## Tickers

Types:

```python
from coingecko_sdk.types.coins import TickerGetResponse
```

Methods:

- <code title="get /coins/{id}/tickers">client.coins.tickers.<a href="./src/coingecko_sdk/resources/coins/tickers.py">get</a>(id, \*\*<a href="src/coingecko_sdk/types/coins/ticker_get_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/coins/ticker_get_response.py">TickerGetResponse</a></code>

## TotalSupplyChart

Types:

```python
from coingecko_sdk.types.coins import TotalSupplyChartGetResponse, TotalSupplyChartGetRangeResponse
```

Methods:

- <code title="get /coins/{id}/total_supply_chart">client.coins.total_supply_chart.<a href="./src/coingecko_sdk/resources/coins/total_supply_chart.py">get</a>(id, \*\*<a href="src/coingecko_sdk/types/coins/total_supply_chart_get_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/coins/total_supply_chart_get_response.py">TotalSupplyChartGetResponse</a></code>
- <code title="get /coins/{id}/total_supply_chart/range">client.coins.total_supply_chart.<a href="./src/coingecko_sdk/resources/coins/total_supply_chart.py">get_range</a>(id, \*\*<a href="src/coingecko_sdk/types/coins/total_supply_chart_get_range_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/coins/total_supply_chart_get_range_response.py">TotalSupplyChartGetRangeResponse</a></code>

# Companies

## PublicTreasury

Types:

```python
from coingecko_sdk.types.companies import PublicTreasuryGetCoinIDResponse
```

Methods:

- <code title="get /companies/public_treasury/{coin_id}">client.companies.public_treasury.<a href="./src/coingecko_sdk/resources/companies/public_treasury.py">get_coin_id</a>(coin_id) -> <a href="./src/coingecko_sdk/types/companies/public_treasury_get_coin_id_response.py">PublicTreasuryGetCoinIDResponse</a></code>

# Derivatives

Types:

```python
from coingecko_sdk.types import DerivativeGetResponse
```

Methods:

- <code title="get /derivatives">client.derivatives.<a href="./src/coingecko_sdk/resources/derivatives/derivatives.py">get</a>() -> <a href="./src/coingecko_sdk/types/derivative_get_response.py">DerivativeGetResponse</a></code>

## Exchanges

Types:

```python
from coingecko_sdk.types.derivatives import (
    ExchangeGetResponse,
    ExchangeGetIDResponse,
    ExchangeGetListResponse,
)
```

Methods:

- <code title="get /derivatives/exchanges">client.derivatives.exchanges.<a href="./src/coingecko_sdk/resources/derivatives/exchanges.py">get</a>(\*\*<a href="src/coingecko_sdk/types/derivatives/exchange_get_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/derivatives/exchange_get_response.py">ExchangeGetResponse</a></code>
- <code title="get /derivatives/exchanges/{id}">client.derivatives.exchanges.<a href="./src/coingecko_sdk/resources/derivatives/exchanges.py">get_id</a>(id, \*\*<a href="src/coingecko_sdk/types/derivatives/exchange_get_id_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/derivatives/exchange_get_id_response.py">ExchangeGetIDResponse</a></code>
- <code title="get /derivatives/exchanges/list">client.derivatives.exchanges.<a href="./src/coingecko_sdk/resources/derivatives/exchanges.py">get_list</a>() -> <a href="./src/coingecko_sdk/types/derivatives/exchange_get_list_response.py">ExchangeGetListResponse</a></code>

# ExchangeRates

Types:

```python
from coingecko_sdk.types import ExchangeRateGetResponse
```

Methods:

- <code title="get /exchange_rates">client.exchange_rates.<a href="./src/coingecko_sdk/resources/exchange_rates.py">get</a>() -> <a href="./src/coingecko_sdk/types/exchange_rate_get_response.py">ExchangeRateGetResponse</a></code>

# Exchanges

Types:

```python
from coingecko_sdk.types import ExchangeGetResponse, ExchangeGetIDResponse, ExchangeGetListResponse
```

Methods:

- <code title="get /exchanges">client.exchanges.<a href="./src/coingecko_sdk/resources/exchanges/exchanges.py">get</a>(\*\*<a href="src/coingecko_sdk/types/exchange_get_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/exchange_get_response.py">ExchangeGetResponse</a></code>
- <code title="get /exchanges/{id}">client.exchanges.<a href="./src/coingecko_sdk/resources/exchanges/exchanges.py">get_id</a>(id, \*\*<a href="src/coingecko_sdk/types/exchange_get_id_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/exchange_get_id_response.py">ExchangeGetIDResponse</a></code>
- <code title="get /exchanges/list">client.exchanges.<a href="./src/coingecko_sdk/resources/exchanges/exchanges.py">get_list</a>(\*\*<a href="src/coingecko_sdk/types/exchange_get_list_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/exchange_get_list_response.py">ExchangeGetListResponse</a></code>

## Tickers

Types:

```python
from coingecko_sdk.types.exchanges import TickerGetResponse
```

Methods:

- <code title="get /exchanges/{id}/tickers">client.exchanges.tickers.<a href="./src/coingecko_sdk/resources/exchanges/tickers.py">get</a>(id, \*\*<a href="src/coingecko_sdk/types/exchanges/ticker_get_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/exchanges/ticker_get_response.py">TickerGetResponse</a></code>

## VolumeChart

Types:

```python
from coingecko_sdk.types.exchanges import VolumeChartGetResponse, VolumeChartGetRangeResponse
```

Methods:

- <code title="get /exchanges/{id}/volume_chart">client.exchanges.volume_chart.<a href="./src/coingecko_sdk/resources/exchanges/volume_chart.py">get</a>(id, \*\*<a href="src/coingecko_sdk/types/exchanges/volume_chart_get_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/exchanges/volume_chart_get_response.py">VolumeChartGetResponse</a></code>
- <code title="get /exchanges/{id}/volume_chart/range">client.exchanges.volume_chart.<a href="./src/coingecko_sdk/resources/exchanges/volume_chart.py">get_range</a>(id, \*\*<a href="src/coingecko_sdk/types/exchanges/volume_chart_get_range_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/exchanges/volume_chart_get_range_response.py">VolumeChartGetRangeResponse</a></code>

# Global

Types:

```python
from coingecko_sdk.types import GlobalGetResponse
```

Methods:

- <code title="get /global">client.global*.<a href="./src/coingecko_sdk/resources/global*/global\_.py">get</a>() -> <a href="./src/coingecko_sdk/types/global_get_response.py">GlobalGetResponse</a></code>

## DecentralizedFinanceDefi

Types:

```python
from coingecko_sdk.types.global_ import DecentralizedFinanceDefiGetResponse
```

Methods:

- <code title="get /global/decentralized_finance_defi">client.global*.decentralized_finance_defi.<a href="./src/coingecko_sdk/resources/global*/decentralized*finance_defi.py">get</a>() -> <a href="./src/coingecko_sdk/types/global*/decentralized_finance_defi_get_response.py">DecentralizedFinanceDefiGetResponse</a></code>

## MarketCapChart

Types:

```python
from coingecko_sdk.types.global_ import MarketCapChartGetResponse
```

Methods:

- <code title="get /global/market_cap_chart">client.global*.market_cap_chart.<a href="./src/coingecko_sdk/resources/global*/market*cap_chart.py">get</a>(\*\*<a href="src/coingecko_sdk/types/global*/market*cap_chart_get_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/global*/market_cap_chart_get_response.py">MarketCapChartGetResponse</a></code>

# Key

Types:

```python
from coingecko_sdk.types import KeyGetResponse
```

Methods:

- <code title="get /key">client.key.<a href="./src/coingecko_sdk/resources/key.py">get</a>() -> <a href="./src/coingecko_sdk/types/key_get_response.py">KeyGetResponse</a></code>

# NFTs

Types:

```python
from coingecko_sdk.types import NFTGetIDResponse, NFTGetListResponse, NFTGetMarketsResponse
```

Methods:

- <code title="get /nfts/{id}">client.nfts.<a href="./src/coingecko_sdk/resources/nfts/nfts.py">get_id</a>(id) -> <a href="./src/coingecko_sdk/types/nft_get_id_response.py">NFTGetIDResponse</a></code>
- <code title="get /nfts/list">client.nfts.<a href="./src/coingecko_sdk/resources/nfts/nfts.py">get_list</a>(\*\*<a href="src/coingecko_sdk/types/nft_get_list_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/nft_get_list_response.py">NFTGetListResponse</a></code>
- <code title="get /nfts/markets">client.nfts.<a href="./src/coingecko_sdk/resources/nfts/nfts.py">get_markets</a>(\*\*<a href="src/coingecko_sdk/types/nft_get_markets_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/nft_get_markets_response.py">NFTGetMarketsResponse</a></code>

## Contract

Types:

```python
from coingecko_sdk.types.nfts import ContractGetContractAddressResponse
```

Methods:

- <code title="get /nfts/{asset_platform_id}/contract/{contract_address}">client.nfts.contract.<a href="./src/coingecko_sdk/resources/nfts/contract/contract.py">get_contract_address</a>(contract_address, \*, asset_platform_id) -> <a href="./src/coingecko_sdk/types/nfts/contract_get_contract_address_response.py">ContractGetContractAddressResponse</a></code>

### MarketChart

Types:

```python
from coingecko_sdk.types.nfts.contract import MarketChartGetResponse
```

Methods:

- <code title="get /nfts/{asset_platform_id}/contract/{contract_address}/market_chart">client.nfts.contract.market_chart.<a href="./src/coingecko_sdk/resources/nfts/contract/market_chart.py">get</a>(contract_address, \*, asset_platform_id, \*\*<a href="src/coingecko_sdk/types/nfts/contract/market_chart_get_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/nfts/contract/market_chart_get_response.py">MarketChartGetResponse</a></code>

## MarketChart

Types:

```python
from coingecko_sdk.types.nfts import MarketChartGetResponse
```

Methods:

- <code title="get /nfts/{id}/market_chart">client.nfts.market_chart.<a href="./src/coingecko_sdk/resources/nfts/market_chart.py">get</a>(id, \*\*<a href="src/coingecko_sdk/types/nfts/market_chart_get_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/nfts/market_chart_get_response.py">MarketChartGetResponse</a></code>

## Tickers

Types:

```python
from coingecko_sdk.types.nfts import TickerGetResponse
```

Methods:

- <code title="get /nfts/{id}/tickers">client.nfts.tickers.<a href="./src/coingecko_sdk/resources/nfts/tickers.py">get</a>(id) -> <a href="./src/coingecko_sdk/types/nfts/ticker_get_response.py">TickerGetResponse</a></code>

# Onchain

## Categories

Types:

```python
from coingecko_sdk.types.onchain import CategoryGetResponse, CategoryGetPoolsResponse
```

Methods:

- <code title="get /onchain/categories">client.onchain.categories.<a href="./src/coingecko_sdk/resources/onchain/categories.py">get</a>(\*\*<a href="src/coingecko_sdk/types/onchain/category_get_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/onchain/category_get_response.py">CategoryGetResponse</a></code>
- <code title="get /onchain/categories/{category_id}/pools">client.onchain.categories.<a href="./src/coingecko_sdk/resources/onchain/categories.py">get_pools</a>(category_id, \*\*<a href="src/coingecko_sdk/types/onchain/category_get_pools_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/onchain/category_get_pools_response.py">CategoryGetPoolsResponse</a></code>

## Networks

Types:

```python
from coingecko_sdk.types.onchain import NetworkGetResponse
```

Methods:

- <code title="get /onchain/networks">client.onchain.networks.<a href="./src/coingecko_sdk/resources/onchain/networks/networks.py">get</a>(\*\*<a href="src/coingecko_sdk/types/onchain/network_get_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/onchain/network_get_response.py">NetworkGetResponse</a></code>

### NewPools

Types:

```python
from coingecko_sdk.types.onchain.networks import NewPoolGetResponse, NewPoolGetNetworkResponse
```

Methods:

- <code title="get /onchain/networks/new_pools">client.onchain.networks.new_pools.<a href="./src/coingecko_sdk/resources/onchain/networks/new_pools.py">get</a>(\*\*<a href="src/coingecko_sdk/types/onchain/networks/new_pool_get_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/onchain/networks/new_pool_get_response.py">NewPoolGetResponse</a></code>
- <code title="get /onchain/networks/{network}/new_pools">client.onchain.networks.new_pools.<a href="./src/coingecko_sdk/resources/onchain/networks/new_pools.py">get_network</a>(network, \*\*<a href="src/coingecko_sdk/types/onchain/networks/new_pool_get_network_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/onchain/networks/new_pool_get_network_response.py">NewPoolGetNetworkResponse</a></code>

### TrendingPools

Types:

```python
from coingecko_sdk.types.onchain.networks import (
    TrendingPoolGetResponse,
    TrendingPoolGetNetworkResponse,
)
```

Methods:

- <code title="get /onchain/networks/trending_pools">client.onchain.networks.trending_pools.<a href="./src/coingecko_sdk/resources/onchain/networks/trending_pools.py">get</a>(\*\*<a href="src/coingecko_sdk/types/onchain/networks/trending_pool_get_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/onchain/networks/trending_pool_get_response.py">TrendingPoolGetResponse</a></code>
- <code title="get /onchain/networks/{network}/trending_pools">client.onchain.networks.trending_pools.<a href="./src/coingecko_sdk/resources/onchain/networks/trending_pools.py">get_network</a>(network, \*\*<a href="src/coingecko_sdk/types/onchain/networks/trending_pool_get_network_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/onchain/networks/trending_pool_get_network_response.py">TrendingPoolGetNetworkResponse</a></code>

### Dexes

Types:

```python
from coingecko_sdk.types.onchain.networks import DexGetResponse, DexGetPoolsResponse
```

Methods:

- <code title="get /onchain/networks/{network}/dexes">client.onchain.networks.dexes.<a href="./src/coingecko_sdk/resources/onchain/networks/dexes.py">get</a>(network, \*\*<a href="src/coingecko_sdk/types/onchain/networks/dex_get_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/onchain/networks/dex_get_response.py">DexGetResponse</a></code>
- <code title="get /onchain/networks/{network}/dexes/{dex}/pools">client.onchain.networks.dexes.<a href="./src/coingecko_sdk/resources/onchain/networks/dexes.py">get_pools</a>(dex, \*, network, \*\*<a href="src/coingecko_sdk/types/onchain/networks/dex_get_pools_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/onchain/networks/dex_get_pools_response.py">DexGetPoolsResponse</a></code>

### Pools

Types:

```python
from coingecko_sdk.types.onchain.networks import PoolGetResponse, PoolGetAddressResponse
```

Methods:

- <code title="get /onchain/networks/{network}/pools">client.onchain.networks.pools.<a href="./src/coingecko_sdk/resources/onchain/networks/pools/pools.py">get</a>(network, \*\*<a href="src/coingecko_sdk/types/onchain/networks/pool_get_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/onchain/networks/pool_get_response.py">PoolGetResponse</a></code>
- <code title="get /onchain/networks/{network}/pools/{address}">client.onchain.networks.pools.<a href="./src/coingecko_sdk/resources/onchain/networks/pools/pools.py">get_address</a>(address, \*, network, \*\*<a href="src/coingecko_sdk/types/onchain/networks/pool_get_address_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/onchain/networks/pool_get_address_response.py">PoolGetAddressResponse</a></code>

#### Multi

Types:

```python
from coingecko_sdk.types.onchain.networks.pools import MultiGetAddressesResponse
```

Methods:

- <code title="get /onchain/networks/{network}/pools/multi/{addresses}">client.onchain.networks.pools.multi.<a href="./src/coingecko_sdk/resources/onchain/networks/pools/multi.py">get_addresses</a>(addresses, \*, network, \*\*<a href="src/coingecko_sdk/types/onchain/networks/pools/multi_get_addresses_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/onchain/networks/pools/multi_get_addresses_response.py">MultiGetAddressesResponse</a></code>

#### Info

Types:

```python
from coingecko_sdk.types.onchain.networks.pools import InfoGetResponse
```

Methods:

- <code title="get /onchain/networks/{network}/pools/{pool_address}/info">client.onchain.networks.pools.info.<a href="./src/coingecko_sdk/resources/onchain/networks/pools/info.py">get</a>(pool_address, \*, network) -> <a href="./src/coingecko_sdk/types/onchain/networks/pools/info_get_response.py">InfoGetResponse</a></code>

#### Ohlcv

Types:

```python
from coingecko_sdk.types.onchain.networks.pools import OhlcvGetTimeframeResponse
```

Methods:

- <code title="get /onchain/networks/{network}/pools/{pool_address}/ohlcv/{timeframe}">client.onchain.networks.pools.ohlcv.<a href="./src/coingecko_sdk/resources/onchain/networks/pools/ohlcv.py">get_timeframe</a>(timeframe, \*, network, pool_address, \*\*<a href="src/coingecko_sdk/types/onchain/networks/pools/ohlcv_get_timeframe_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/onchain/networks/pools/ohlcv_get_timeframe_response.py">OhlcvGetTimeframeResponse</a></code>

#### Trades

Types:

```python
from coingecko_sdk.types.onchain.networks.pools import TradeGetResponse
```

Methods:

- <code title="get /onchain/networks/{network}/pools/{pool_address}/trades">client.onchain.networks.pools.trades.<a href="./src/coingecko_sdk/resources/onchain/networks/pools/trades.py">get</a>(pool_address, \*, network, \*\*<a href="src/coingecko_sdk/types/onchain/networks/pools/trade_get_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/onchain/networks/pools/trade_get_response.py">TradeGetResponse</a></code>

### Tokens

Types:

```python
from coingecko_sdk.types.onchain.networks import TokenGetAddressResponse
```

Methods:

- <code title="get /onchain/networks/{network}/tokens/{address}">client.onchain.networks.tokens.<a href="./src/coingecko_sdk/resources/onchain/networks/tokens/tokens.py">get_address</a>(address, \*, network, \*\*<a href="src/coingecko_sdk/types/onchain/networks/token_get_address_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/onchain/networks/token_get_address_response.py">TokenGetAddressResponse</a></code>

#### Multi

Types:

```python
from coingecko_sdk.types.onchain.networks.tokens import MultiGetAddressesResponse
```

Methods:

- <code title="get /onchain/networks/{network}/tokens/multi/{addresses}">client.onchain.networks.tokens.multi.<a href="./src/coingecko_sdk/resources/onchain/networks/tokens/multi.py">get_addresses</a>(addresses, \*, network, \*\*<a href="src/coingecko_sdk/types/onchain/networks/tokens/multi_get_addresses_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/onchain/networks/tokens/multi_get_addresses_response.py">MultiGetAddressesResponse</a></code>

#### Info

Types:

```python
from coingecko_sdk.types.onchain.networks.tokens import InfoGetResponse
```

Methods:

- <code title="get /onchain/networks/{network}/tokens/{address}/info">client.onchain.networks.tokens.info.<a href="./src/coingecko_sdk/resources/onchain/networks/tokens/info.py">get</a>(address, \*, network) -> <a href="./src/coingecko_sdk/types/onchain/networks/tokens/info_get_response.py">InfoGetResponse</a></code>

#### TopHolders

Types:

```python
from coingecko_sdk.types.onchain.networks.tokens import TopHolderGetResponse
```

Methods:

- <code title="get /onchain/networks/{network}/tokens/{address}/top_holders">client.onchain.networks.tokens.top_holders.<a href="./src/coingecko_sdk/resources/onchain/networks/tokens/top_holders.py">get</a>(address, \*, network, \*\*<a href="src/coingecko_sdk/types/onchain/networks/tokens/top_holder_get_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/onchain/networks/tokens/top_holder_get_response.py">TopHolderGetResponse</a></code>

#### HoldersChart

Types:

```python
from coingecko_sdk.types.onchain.networks.tokens import HoldersChartGetResponse
```

Methods:

- <code title="get /onchain/networks/{network}/tokens/{token_address}/holders_chart">client.onchain.networks.tokens.holders_chart.<a href="./src/coingecko_sdk/resources/onchain/networks/tokens/holders_chart.py">get</a>(token_address, \*, network, \*\*<a href="src/coingecko_sdk/types/onchain/networks/tokens/holders_chart_get_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/onchain/networks/tokens/holders_chart_get_response.py">HoldersChartGetResponse</a></code>

#### Ohlcv

Types:

```python
from coingecko_sdk.types.onchain.networks.tokens import OhlcvGetTimeframeResponse
```

Methods:

- <code title="get /onchain/networks/{network}/tokens/{token_address}/ohlcv/{timeframe}">client.onchain.networks.tokens.ohlcv.<a href="./src/coingecko_sdk/resources/onchain/networks/tokens/ohlcv.py">get_timeframe</a>(timeframe, \*, network, token_address, \*\*<a href="src/coingecko_sdk/types/onchain/networks/tokens/ohlcv_get_timeframe_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/onchain/networks/tokens/ohlcv_get_timeframe_response.py">OhlcvGetTimeframeResponse</a></code>

#### Pools

Types:

```python
from coingecko_sdk.types.onchain.networks.tokens import PoolGetResponse
```

Methods:

- <code title="get /onchain/networks/{network}/tokens/{token_address}/pools">client.onchain.networks.tokens.pools.<a href="./src/coingecko_sdk/resources/onchain/networks/tokens/pools.py">get</a>(token_address, \*, network, \*\*<a href="src/coingecko_sdk/types/onchain/networks/tokens/pool_get_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/onchain/networks/tokens/pool_get_response.py">PoolGetResponse</a></code>

#### Trades

Types:

```python
from coingecko_sdk.types.onchain.networks.tokens import TradeGetResponse
```

Methods:

- <code title="get /onchain/networks/{network}/tokens/{token_address}/trades">client.onchain.networks.tokens.trades.<a href="./src/coingecko_sdk/resources/onchain/networks/tokens/trades.py">get</a>(token_address, \*, network, \*\*<a href="src/coingecko_sdk/types/onchain/networks/tokens/trade_get_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/onchain/networks/tokens/trade_get_response.py">TradeGetResponse</a></code>

## Pools

### Megafilter

Types:

```python
from coingecko_sdk.types.onchain.pools import MegafilterGetResponse
```

Methods:

- <code title="get /onchain/pools/megafilter">client.onchain.pools.megafilter.<a href="./src/coingecko_sdk/resources/onchain/pools/megafilter.py">get</a>(\*\*<a href="src/coingecko_sdk/types/onchain/pools/megafilter_get_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/onchain/pools/megafilter_get_response.py">MegafilterGetResponse</a></code>

### TrendingSearch

Types:

```python
from coingecko_sdk.types.onchain.pools import TrendingSearchGetResponse
```

Methods:

- <code title="get /onchain/pools/trending_search">client.onchain.pools.trending_search.<a href="./src/coingecko_sdk/resources/onchain/pools/trending_search.py">get</a>(\*\*<a href="src/coingecko_sdk/types/onchain/pools/trending_search_get_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/onchain/pools/trending_search_get_response.py">TrendingSearchGetResponse</a></code>

## Search

### Pools

Types:

```python
from coingecko_sdk.types.onchain.search import PoolGetResponse
```

Methods:

- <code title="get /onchain/search/pools">client.onchain.search.pools.<a href="./src/coingecko_sdk/resources/onchain/search/pools.py">get</a>(\*\*<a href="src/coingecko_sdk/types/onchain/search/pool_get_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/onchain/search/pool_get_response.py">PoolGetResponse</a></code>

## Simple

### Networks

#### TokenPrice

Types:

```python
from coingecko_sdk.types.onchain.simple.networks import TokenPriceGetAddressesResponse
```

Methods:

- <code title="get /onchain/simple/networks/{network}/token_price/{addresses}">client.onchain.simple.networks.token_price.<a href="./src/coingecko_sdk/resources/onchain/simple/networks/token_price.py">get_addresses</a>(addresses, \*, network, \*\*<a href="src/coingecko_sdk/types/onchain/simple/networks/token_price_get_addresses_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/onchain/simple/networks/token_price_get_addresses_response.py">TokenPriceGetAddressesResponse</a></code>

## Tokens

### InfoRecentlyUpdated

Types:

```python
from coingecko_sdk.types.onchain.tokens import InfoRecentlyUpdatedGetResponse
```

Methods:

- <code title="get /onchain/tokens/info_recently_updated">client.onchain.tokens.info_recently_updated.<a href="./src/coingecko_sdk/resources/onchain/tokens/info_recently_updated.py">get</a>(\*\*<a href="src/coingecko_sdk/types/onchain/tokens/info_recently_updated_get_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/onchain/tokens/info_recently_updated_get_response.py">InfoRecentlyUpdatedGetResponse</a></code>

# Ping

Types:

```python
from coingecko_sdk.types import PingGetResponse
```

Methods:

- <code title="get /ping">client.ping.<a href="./src/coingecko_sdk/resources/ping.py">get</a>() -> <a href="./src/coingecko_sdk/types/ping_get_response.py">PingGetResponse</a></code>

# Search

Types:

```python
from coingecko_sdk.types import SearchGetResponse
```

Methods:

- <code title="get /search">client.search.<a href="./src/coingecko_sdk/resources/search/search.py">get</a>(\*\*<a href="src/coingecko_sdk/types/search_get_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/search_get_response.py">SearchGetResponse</a></code>

## Trending

Types:

```python
from coingecko_sdk.types.search import TrendingGetResponse
```

Methods:

- <code title="get /search/trending">client.search.trending.<a href="./src/coingecko_sdk/resources/search/trending.py">get</a>(\*\*<a href="src/coingecko_sdk/types/search/trending_get_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/search/trending_get_response.py">TrendingGetResponse</a></code>

# Simple

## Price

Types:

```python
from coingecko_sdk.types.simple import PriceGetResponse
```

Methods:

- <code title="get /simple/price">client.simple.price.<a href="./src/coingecko_sdk/resources/simple/price.py">get</a>(\*\*<a href="src/coingecko_sdk/types/simple/price_get_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/simple/price_get_response.py">PriceGetResponse</a></code>

## SupportedVsCurrencies

Types:

```python
from coingecko_sdk.types.simple import SupportedVsCurrencyGetResponse
```

Methods:

- <code title="get /simple/supported_vs_currencies">client.simple.supported_vs_currencies.<a href="./src/coingecko_sdk/resources/simple/supported_vs_currencies.py">get</a>() -> <a href="./src/coingecko_sdk/types/simple/supported_vs_currency_get_response.py">SupportedVsCurrencyGetResponse</a></code>

## TokenPrice

Types:

```python
from coingecko_sdk.types.simple import TokenPriceGetIDResponse
```

Methods:

- <code title="get /simple/token_price/{id}">client.simple.token_price.<a href="./src/coingecko_sdk/resources/simple/token_price.py">get_id</a>(id, \*\*<a href="src/coingecko_sdk/types/simple/token_price_get_id_params.py">params</a>) -> <a href="./src/coingecko_sdk/types/simple/token_price_get_id_response.py">TokenPriceGetIDResponse</a></code>

# TokenLists

Types:

```python
from coingecko_sdk.types import TokenListGetAllJsonResponse
```

Methods:

- <code title="get /token_lists/{asset_platform_id}/all.json">client.token_lists.<a href="./src/coingecko_sdk/resources/token_lists.py">get_all_json</a>(asset_platform_id) -> <a href="./src/coingecko_sdk/types/token_list_get_all_json_response.py">TokenListGetAllJsonResponse</a></code>
