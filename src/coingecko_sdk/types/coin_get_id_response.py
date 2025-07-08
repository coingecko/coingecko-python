# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = [
    "CoinGetIDResponse",
    "CommunityData",
    "DetailPlatforms",
    "DeveloperData",
    "DeveloperDataCodeAdditionsDeletions4Weeks",
    "Image",
    "Links",
    "LinksReposURL",
    "MarketData",
    "MarketDataAth",
    "MarketDataAthChangePercentage",
    "MarketDataAthDate",
    "MarketDataAtl",
    "MarketDataAtlChangePercentage",
    "MarketDataAtlDate",
    "MarketDataCurrentPrice",
    "MarketDataFullyDilutedValuation",
    "MarketDataHigh24h",
    "MarketDataLow24h",
    "MarketDataMarketCap",
    "MarketDataMarketCapChange24hInCurrency",
    "MarketDataMarketCapChangePercentage24hInCurrency",
    "MarketDataPriceChangePercentage14dInCurrency",
    "MarketDataPriceChangePercentage1hInCurrency",
    "MarketDataPriceChangePercentage1yInCurrency",
    "MarketDataPriceChangePercentage200dInCurrency",
    "MarketDataPriceChangePercentage24hInCurrency",
    "MarketDataPriceChangePercentage30dInCurrency",
    "MarketDataPriceChangePercentage60dInCurrency",
    "MarketDataPriceChangePercentage7dInCurrency",
    "MarketDataTotalVolume",
    "Ticker",
    "TickerConvertedLast",
    "TickerConvertedVolume",
    "TickerMarket",
]


class CommunityData(BaseModel):
    facebook_likes: Optional[float] = None
    """coin facebook likes"""

    reddit_accounts_active_48h: Optional[float] = None
    """coin reddit active accounts in 48 hours"""

    reddit_average_comments_48h: Optional[float] = None
    """coin reddit average comments in 48 hours"""

    reddit_average_posts_48h: Optional[float] = None
    """coin reddit average posts in 48 hours"""

    reddit_subscribers: Optional[float] = None
    """coin reddit subscribers"""

    telegram_channel_user_count: Optional[float] = None
    """coin telegram channel user count"""


class DetailPlatforms(BaseModel):
    contract_address: Optional[str] = None
    """contract address on the platform"""

    decimal_place: Optional[float] = None
    """decimal places for the token"""


class DeveloperDataCodeAdditionsDeletions4Weeks(BaseModel):
    additions: Optional[float] = None

    deletions: Optional[float] = None


class DeveloperData(BaseModel):
    closed_issues: Optional[float] = None
    """coin repository closed issues"""

    code_additions_deletions_4_weeks: Optional[DeveloperDataCodeAdditionsDeletions4Weeks] = None
    """coin code additions and deletions in 4 weeks"""

    commit_count_4_weeks: Optional[float] = None
    """coin repository commit count in 4 weeks"""

    forks: Optional[float] = None
    """coin repository forks"""

    last_4_weeks_commit_activity_series: Optional[List[float]] = None
    """coin repository last 4 weeks commit activity series"""

    pull_request_contributors: Optional[float] = None
    """coin repository pull request contributors"""

    pull_requests_merged: Optional[float] = None
    """coin repository pull requests merged"""

    stars: Optional[float] = None
    """coin repository stars"""

    subscribers: Optional[float] = None
    """coin repository subscribers"""

    total_issues: Optional[float] = None
    """coin repository total issues"""


class Image(BaseModel):
    large: Optional[str] = None

    small: Optional[str] = None

    thumb: Optional[str] = None


class LinksReposURL(BaseModel):
    bitbucket: Optional[List[str]] = None
    """coin bitbucket repository url"""

    github: Optional[List[str]] = None
    """coin github repository url"""


class Links(BaseModel):
    announcement_url: Optional[List[str]] = None
    """coin announcement url"""

    bitcointalk_thread_identifier: Optional[str] = None
    """coin bitcointalk thread identifier"""

    blockchain_site: Optional[List[str]] = None
    """coin block explorer url"""

    chat_url: Optional[List[str]] = None
    """coin chat url"""

    facebook_username: Optional[str] = None
    """coin facebook username"""

    homepage: Optional[List[str]] = None
    """coin website url"""

    official_forum_url: Optional[List[str]] = None
    """coin official forum url"""

    repos_url: Optional[LinksReposURL] = None
    """coin repository url"""

    snapshot_url: Optional[str] = None
    """coin snapshot url"""

    subreddit_url: Optional[str] = None
    """coin subreddit url"""

    telegram_channel_identifier: Optional[str] = None
    """coin telegram channel identifier"""

    twitter_screen_name: Optional[str] = None
    """coin twitter handle"""

    whitepaper: Optional[List[str]] = None
    """coin whitepaper url"""


class MarketDataAth(BaseModel):
    btc: Optional[float] = None

    eur: Optional[float] = None

    usd: Optional[float] = None


class MarketDataAthChangePercentage(BaseModel):
    btc: Optional[float] = None

    eur: Optional[float] = None

    usd: Optional[float] = None


class MarketDataAthDate(BaseModel):
    btc: Optional[str] = None

    eur: Optional[str] = None

    usd: Optional[str] = None


class MarketDataAtl(BaseModel):
    btc: Optional[float] = None

    eur: Optional[float] = None

    usd: Optional[float] = None


class MarketDataAtlChangePercentage(BaseModel):
    btc: Optional[float] = None

    eur: Optional[float] = None

    usd: Optional[float] = None


class MarketDataAtlDate(BaseModel):
    btc: Optional[str] = None

    eur: Optional[str] = None

    usd: Optional[str] = None


class MarketDataCurrentPrice(BaseModel):
    btc: Optional[float] = None

    eur: Optional[float] = None

    usd: Optional[float] = None


class MarketDataFullyDilutedValuation(BaseModel):
    btc: Optional[float] = None

    eur: Optional[float] = None

    usd: Optional[float] = None


class MarketDataHigh24h(BaseModel):
    btc: Optional[float] = None

    eur: Optional[float] = None

    usd: Optional[float] = None


class MarketDataLow24h(BaseModel):
    btc: Optional[float] = None

    eur: Optional[float] = None

    usd: Optional[float] = None


class MarketDataMarketCap(BaseModel):
    btc: Optional[float] = None

    eur: Optional[float] = None

    usd: Optional[float] = None


class MarketDataMarketCapChange24hInCurrency(BaseModel):
    btc: Optional[float] = None

    eur: Optional[float] = None

    usd: Optional[float] = None


class MarketDataMarketCapChangePercentage24hInCurrency(BaseModel):
    btc: Optional[float] = None

    eur: Optional[float] = None

    usd: Optional[float] = None


class MarketDataPriceChangePercentage14dInCurrency(BaseModel):
    btc: Optional[float] = None

    eur: Optional[float] = None

    usd: Optional[float] = None


class MarketDataPriceChangePercentage1hInCurrency(BaseModel):
    btc: Optional[float] = None

    eur: Optional[float] = None

    usd: Optional[float] = None


class MarketDataPriceChangePercentage1yInCurrency(BaseModel):
    btc: Optional[float] = None

    eur: Optional[float] = None

    usd: Optional[float] = None


class MarketDataPriceChangePercentage200dInCurrency(BaseModel):
    btc: Optional[float] = None

    eur: Optional[float] = None

    usd: Optional[float] = None


class MarketDataPriceChangePercentage24hInCurrency(BaseModel):
    btc: Optional[float] = None

    eur: Optional[float] = None

    usd: Optional[float] = None


class MarketDataPriceChangePercentage30dInCurrency(BaseModel):
    btc: Optional[float] = None

    eur: Optional[float] = None

    usd: Optional[float] = None


class MarketDataPriceChangePercentage60dInCurrency(BaseModel):
    btc: Optional[float] = None

    eur: Optional[float] = None

    usd: Optional[float] = None


class MarketDataPriceChangePercentage7dInCurrency(BaseModel):
    btc: Optional[float] = None

    eur: Optional[float] = None

    usd: Optional[float] = None


class MarketDataTotalVolume(BaseModel):
    btc: Optional[float] = None

    eur: Optional[float] = None

    usd: Optional[float] = None


class MarketData(BaseModel):
    ath: Optional[MarketDataAth] = None
    """coin all time high (ATH) in currency"""

    ath_change_percentage: Optional[MarketDataAthChangePercentage] = None
    """coin all time high (ATH) change in percentage"""

    ath_date: Optional[MarketDataAthDate] = None
    """coin all time high (ATH) date"""

    atl: Optional[MarketDataAtl] = None
    """coin all time low (atl) in currency"""

    atl_change_percentage: Optional[MarketDataAtlChangePercentage] = None
    """coin all time low (atl) change in percentage"""

    atl_date: Optional[MarketDataAtlDate] = None
    """coin all time low (atl) date"""

    circulating_supply: Optional[float] = None
    """coin circulating supply"""

    current_price: Optional[MarketDataCurrentPrice] = None
    """coin current price in currency"""

    fdv_to_tvl_ratio: Optional[float] = None
    """fully diluted valuation to total value locked ratio"""

    fully_diluted_valuation: Optional[MarketDataFullyDilutedValuation] = None
    """coin fully diluted valuation (fdv) in currency"""

    high_24h: Optional[MarketDataHigh24h] = None
    """coin 24hr price high in currency"""

    last_updated: Optional[datetime] = None
    """coin market data last updated timestamp"""

    low_24h: Optional[MarketDataLow24h] = None
    """coin 24hr price low in currency"""

    market_cap: Optional[MarketDataMarketCap] = None
    """coin market cap in currency"""

    market_cap_change_24h: Optional[float] = None
    """coin 24hr market cap change in currency"""

    market_cap_change_24h_in_currency: Optional[MarketDataMarketCapChange24hInCurrency] = None
    """coin 24hr market cap change in currency"""

    market_cap_change_percentage_24h: Optional[float] = None
    """coin 24hr market cap change in percentage"""

    market_cap_change_percentage_24h_in_currency: Optional[MarketDataMarketCapChangePercentage24hInCurrency] = None
    """coin 24hr market cap change in percentage"""

    market_cap_fdv_ratio: Optional[float] = None
    """market cap to fully diluted valuation ratio"""

    market_cap_rank: Optional[float] = None
    """coin rank by market cap"""

    max_supply: Optional[float] = None
    """coin max supply"""

    mcap_to_tvl_ratio: Optional[float] = None
    """market cap to total value locked ratio"""

    price_change_24h: Optional[float] = None
    """coin 24hr price change in currency"""

    price_change_percentage_14d: Optional[float] = None
    """coin 14d price change in percentage"""

    price_change_percentage_14d_in_currency: Optional[MarketDataPriceChangePercentage14dInCurrency] = None
    """coin 14d price change in currency"""

    price_change_percentage_1h_in_currency: Optional[MarketDataPriceChangePercentage1hInCurrency] = None
    """coin 1h price change in currency"""

    price_change_percentage_1y: Optional[float] = None
    """coin 1y price change in percentage"""

    price_change_percentage_1y_in_currency: Optional[MarketDataPriceChangePercentage1yInCurrency] = None
    """coin 1y price change in currency"""

    price_change_percentage_200d: Optional[float] = None
    """coin 200d price change in percentage"""

    price_change_percentage_200d_in_currency: Optional[MarketDataPriceChangePercentage200dInCurrency] = None
    """coin 200d price change in currency"""

    price_change_percentage_24h: Optional[float] = None
    """coin 24hr price change in percentage"""

    price_change_percentage_24h_in_currency: Optional[MarketDataPriceChangePercentage24hInCurrency] = None
    """coin 24hr price change in currency"""

    price_change_percentage_30d: Optional[float] = None
    """coin 30d price change in percentage"""

    price_change_percentage_30d_in_currency: Optional[MarketDataPriceChangePercentage30dInCurrency] = None
    """coin 30d price change in currency"""

    price_change_percentage_60d: Optional[float] = None
    """coin 60d price change in percentage"""

    price_change_percentage_60d_in_currency: Optional[MarketDataPriceChangePercentage60dInCurrency] = None
    """coin 60d price change in currency"""

    price_change_percentage_7d: Optional[float] = None
    """coin 7d price change in percentage"""

    price_change_percentage_7d_in_currency: Optional[MarketDataPriceChangePercentage7dInCurrency] = None
    """coin 7d price change in currency"""

    roi: Optional[float] = None
    """coin return on investment"""

    total_supply: Optional[float] = None
    """coin total supply"""

    total_value_locked: Optional[float] = None
    """total value locked"""

    total_volume: Optional[MarketDataTotalVolume] = None
    """coin total trading volume in currency"""


class TickerConvertedLast(BaseModel):
    btc: Optional[float] = None

    eth: Optional[float] = None

    usd: Optional[float] = None


class TickerConvertedVolume(BaseModel):
    btc: Optional[float] = None

    eth: Optional[float] = None

    usd: Optional[float] = None


class TickerMarket(BaseModel):
    has_trading_incentive: Optional[bool] = None
    """coin ticker exchange trading incentive"""

    identifier: Optional[str] = None
    """coin ticker exchange identifier"""

    name: Optional[str] = None
    """coin ticker exchange name"""


class Ticker(BaseModel):
    base: Optional[str] = None
    """coin ticker base currency"""

    bid_ask_spread_percentage: Optional[float] = None
    """coin ticker bid ask spread percentage"""

    coin_id: Optional[str] = None
    """coin ticker base currency coin ID"""

    converted_last: Optional[TickerConvertedLast] = None
    """coin ticker converted last price"""

    converted_volume: Optional[TickerConvertedVolume] = None
    """coin ticker converted volume"""

    is_anomaly: Optional[bool] = None
    """coin ticker anomaly"""

    is_stale: Optional[bool] = None
    """coin ticker stale"""

    last: Optional[float] = None
    """coin ticker last price"""

    last_fetch_at: Optional[datetime] = None
    """coin ticker last fetch timestamp"""

    last_traded_at: Optional[datetime] = None
    """coin ticker last traded timestamp"""

    market: Optional[TickerMarket] = None
    """coin ticker exchange"""

    target: Optional[str] = None
    """coin ticker target currency"""

    target_coin_id: Optional[str] = None
    """coin ticker target currency coin ID"""

    timestamp: Optional[datetime] = None
    """coin ticker timestamp"""

    token_info_url: Optional[str] = None
    """coin ticker token info url"""

    trade_url: Optional[str] = None
    """coin ticker trade url"""

    trust_score: Optional[str] = None
    """coin ticker trust score"""

    volume: Optional[float] = None
    """coin ticker volume"""


class CoinGetIDResponse(BaseModel):
    id: Optional[str] = None
    """coin ID"""

    additional_notices: Optional[List[str]] = None
    """additional notices"""

    asset_platform_id: Optional[str] = None
    """coin asset platform ID"""

    block_time_in_minutes: Optional[float] = None
    """blockchain block time in minutes"""

    categories: Optional[List[str]] = None
    """coin categories"""

    community_data: Optional[CommunityData] = None
    """coin community data"""

    country_origin: Optional[str] = None
    """coin country of origin"""

    description: Optional[Dict[str, str]] = None
    """coin description"""

    detail_platforms: Optional[Dict[str, DetailPlatforms]] = None
    """detailed coin asset platform and contract address"""

    developer_data: Optional[DeveloperData] = None
    """coin developer data"""

    genesis_date: Optional[datetime] = None
    """coin genesis date"""

    hashing_algorithm: Optional[str] = None
    """blockchain hashing algorithm"""

    image: Optional[Image] = None
    """coin image url"""

    last_updated: Optional[datetime] = None
    """coin last updated timestamp"""

    links: Optional[Links] = None
    """links"""

    localization: Optional[Dict[str, str]] = None
    """coin name localization"""

    market_cap_rank: Optional[float] = None
    """coin rank by market cap"""

    market_data: Optional[MarketData] = None
    """coin market data"""

    name: Optional[str] = None
    """coin name"""

    platforms: Optional[Dict[str, str]] = None
    """coin asset platform and contract address"""

    preview_listing: Optional[bool] = None
    """preview listing coin"""

    public_notice: Optional[str] = None
    """public notice"""

    sentiment_votes_down_percentage: Optional[float] = None
    """coin sentiment votes down percentage"""

    sentiment_votes_up_percentage: Optional[float] = None
    """coin sentiment votes up percentage"""

    status_updates: Optional[List[str]] = None
    """coin status updates"""

    symbol: Optional[str] = None
    """coin symbol"""

    tickers: Optional[List[Ticker]] = None
    """coin tickers"""

    web_slug: Optional[str] = None
    """coin web slug"""
