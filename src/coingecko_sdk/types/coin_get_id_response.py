# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = [
    "CoinGetIDResponse",
    "DetailPlatforms",
    "Image",
    "Links",
    "LinksReposURL",
    "StatusUpdate",
    "CategoriesDetail",
    "CommunityData",
    "DeveloperData",
    "DeveloperDataCodeAdditionsDeletions4Weeks",
    "IcoData",
    "MarketData",
    "MarketDataRoi",
    "Ticker",
    "TickerConvertedLast",
    "TickerConvertedVolume",
    "TickerMarket",
]


class DetailPlatforms(BaseModel):
    contract_address: Optional[str] = None
    """Token contract address"""

    decimal_place: Optional[int] = None
    """Token decimal place"""


class Image(BaseModel):
    """Coin image URL"""

    large: Optional[str] = None

    small: Optional[str] = None

    thumb: Optional[str] = None


class LinksReposURL(BaseModel):
    """Repository URL"""

    bitbucket: Optional[List[str]] = None
    """Bitbucket repository URL"""

    github: Optional[List[str]] = None
    """GitHub repository URL"""


class Links(BaseModel):
    """Links"""

    announcement_url: Optional[List[str]] = None
    """Announcement URL"""

    bitcointalk_thread_identifier: Optional[int] = None
    """Bitcointalk thread identifier"""

    blockchain_site: Optional[List[str]] = None
    """Block explorer URL"""

    chat_url: Optional[List[str]] = None
    """Chat URL"""

    facebook_username: Optional[str] = None
    """Facebook username"""

    homepage: Optional[List[str]] = None
    """Website URL"""

    official_forum_url: Optional[List[str]] = None
    """Official forum URL"""

    repos_url: Optional[LinksReposURL] = None
    """Repository URL"""

    snapshot_url: Optional[str] = None
    """Snapshot URL"""

    subreddit_url: Optional[str] = None
    """Subreddit URL"""

    telegram_channel_identifier: Optional[str] = None
    """Telegram channel identifier"""

    twitter_screen_name: Optional[str] = None
    """Twitter handle"""

    whitepaper: Optional[str] = None
    """Whitepaper URL"""


class StatusUpdate(BaseModel):
    category: Optional[str] = None
    """Status update category"""

    created_at: Optional[str] = None
    """Status update creation time"""

    description: Optional[str] = None
    """Status update description"""

    user: Optional[str] = None
    """Status update user"""

    user_title: Optional[str] = None
    """Status update user title"""


class CategoriesDetail(BaseModel):
    id: Optional[str] = None
    """Category ID"""

    name: Optional[str] = None
    """Category name"""


class CommunityData(BaseModel):
    """Community data"""

    facebook_likes: Optional[float] = None
    """Facebook likes"""

    reddit_accounts_active_48h: Optional[float] = None
    """Reddit active accounts in 48 hours"""

    reddit_average_comments_48h: Optional[float] = None
    """Reddit average comments in 48 hours"""

    reddit_average_posts_48h: Optional[float] = None
    """Reddit average posts in 48 hours"""

    reddit_subscribers: Optional[float] = None
    """Reddit subscribers"""

    telegram_channel_user_count: Optional[float] = None
    """Telegram channel user count"""


class DeveloperDataCodeAdditionsDeletions4Weeks(BaseModel):
    """Code additions and deletions in 4 weeks"""

    additions: Optional[float] = None

    deletions: Optional[float] = None


class DeveloperData(BaseModel):
    """Developer data"""

    closed_issues: Optional[float] = None
    """Repository closed issues"""

    code_additions_deletions_4_weeks: Optional[DeveloperDataCodeAdditionsDeletions4Weeks] = None
    """Code additions and deletions in 4 weeks"""

    commit_count_4_weeks: Optional[float] = None
    """Repository commit count in 4 weeks"""

    forks: Optional[float] = None
    """Repository forks"""

    last_4_weeks_commit_activity_series: Optional[List[float]] = None
    """Repository last 4 weeks commit activity series"""

    pull_request_contributors: Optional[float] = None
    """Repository pull request contributors"""

    pull_requests_merged: Optional[float] = None
    """Repository pull requests merged"""

    stars: Optional[float] = None
    """Repository stars"""

    subscribers: Optional[float] = None
    """Repository subscribers"""

    total_issues: Optional[float] = None
    """Repository total issues"""


class IcoData(BaseModel):
    """ICO data"""

    accepting_currencies: Optional[str] = None
    """Accepting currencies"""

    amount_for_sale: Optional[float] = None
    """Amount for sale"""

    base_pre_sale_amount: Optional[float] = None
    """Base pre-sale amount"""

    base_public_sale_amount: Optional[float] = None
    """Base public sale amount"""

    bounty_detail_url: Optional[str] = None
    """Bounty detail URL"""

    country_origin: Optional[str] = None
    """Country of origin"""

    description: Optional[str] = None
    """Detailed description"""

    hardcap_amount: Optional[float] = None
    """Hardcap amount"""

    hardcap_currency: Optional[str] = None
    """Hardcap currency"""

    ico_end_date: Optional[str] = None
    """ICO end date"""

    ico_start_date: Optional[str] = None
    """ICO start date"""

    kyc_required: Optional[bool] = None
    """KYC required"""

    links: Optional[Dict[str, str]] = None
    """ICO related links"""

    pre_sale_available: Optional[bool] = None
    """Pre-sale available"""

    pre_sale_end_date: Optional[str] = None
    """Pre-sale end date"""

    pre_sale_ended: Optional[bool] = None
    """Pre-sale ended"""

    pre_sale_start_date: Optional[str] = None
    """Pre-sale start date"""

    quote_pre_sale_amount: Optional[float] = None
    """Quote pre-sale amount"""

    quote_pre_sale_currency: Optional[str] = None
    """Quote pre-sale currency"""

    quote_public_sale_amount: Optional[float] = None
    """Quote public sale amount"""

    quote_public_sale_currency: Optional[str] = None
    """Quote public sale currency"""

    short_desc: Optional[str] = None
    """Short description"""

    softcap_amount: Optional[float] = None
    """Softcap amount"""

    softcap_currency: Optional[str] = None
    """Softcap currency"""

    total_raised: Optional[float] = None
    """Total raised amount"""

    total_raised_currency: Optional[str] = None
    """Total raised currency"""

    whitelist_available: Optional[bool] = None
    """Whitelist available"""

    whitelist_end_date: Optional[str] = None
    """Whitelist end date"""

    whitelist_start_date: Optional[str] = None
    """Whitelist start date"""

    whitelist_url: Optional[str] = None
    """Whitelist URL"""


class MarketDataRoi(BaseModel):
    """Return on investment"""

    currency: Optional[str] = None
    """ROI currency"""

    percentage: Optional[float] = None
    """ROI percentage"""

    times: Optional[float] = None
    """ROI multiplier"""


class MarketData(BaseModel):
    """Market data"""

    ath: Optional[Dict[str, float]] = None
    """All-time high in target currency"""

    ath_change_percentage: Optional[Dict[str, float]] = None
    """All-time high change percentage"""

    ath_date: Optional[Dict[str, str]] = None
    """All-time high date"""

    atl: Optional[Dict[str, float]] = None
    """All-time low in target currency"""

    atl_change_percentage: Optional[Dict[str, float]] = None
    """All-time low change percentage"""

    atl_date: Optional[Dict[str, str]] = None
    """All-time low date"""

    circulating_supply: Optional[float] = None
    """Circulating supply"""

    current_price: Optional[Dict[str, float]] = None
    """Current price in target currency"""

    fdv_to_tvl_ratio: Optional[float] = None
    """FDV to TVL ratio"""

    fully_diluted_valuation: Optional[Dict[str, float]] = None
    """Fully diluted valuation in target currency"""

    high_24h: Optional[Dict[str, float]] = None
    """24h price high in target currency"""

    last_updated: Optional[str] = None
    """Market data last updated timestamp"""

    low_24h: Optional[Dict[str, float]] = None
    """24h price low in target currency"""

    market_cap: Optional[Dict[str, float]] = None
    """Market cap in target currency"""

    market_cap_change_24h: Optional[float] = None
    """24h market cap change in target currency"""

    market_cap_change_24h_in_currency: Optional[Dict[str, float]] = None
    """24h market cap change in target currency"""

    market_cap_change_percentage_24h: Optional[float] = None
    """24h market cap change percentage"""

    market_cap_change_percentage_24h_in_currency: Optional[Dict[str, float]] = None
    """24h market cap change percentage per currency"""

    market_cap_fdv_ratio: Optional[float] = None
    """Market cap to FDV ratio"""

    market_cap_rank: Optional[int] = None
    """Market cap rank"""

    market_cap_rank_with_rehypothecated: Optional[int] = None
    """Market cap rank including rehypothecated tokens"""

    max_supply: Optional[float] = None
    """Max supply"""

    max_supply_infinite: Optional[bool] = None
    """Max supply infinite"""

    mcap_to_tvl_ratio: Optional[float] = None
    """Market cap to TVL ratio"""

    outstanding_supply: Optional[float] = None
    """Tokens outstanding in the market"""

    outstanding_token_value_usd: Optional[float] = None
    """Outstanding token value in USD"""

    price_change_24h: Optional[float] = None
    """24h price change in target currency"""

    price_change_24h_in_currency: Optional[Dict[str, float]] = None
    """24h price change in target currency"""

    price_change_percentage_14d: Optional[float] = None
    """14d price change percentage"""

    price_change_percentage_14d_in_currency: Optional[Dict[str, float]] = None
    """14d price change percentage per currency"""

    price_change_percentage_1h_in_currency: Optional[Dict[str, float]] = None
    """1h price change percentage per currency"""

    price_change_percentage_1y: Optional[float] = None
    """1y price change percentage"""

    price_change_percentage_1y_in_currency: Optional[Dict[str, float]] = None
    """1y price change percentage per currency"""

    price_change_percentage_200d: Optional[float] = None
    """200d price change percentage"""

    price_change_percentage_200d_in_currency: Optional[Dict[str, float]] = None
    """200d price change percentage per currency"""

    price_change_percentage_24h: Optional[float] = None
    """24h price change percentage"""

    price_change_percentage_24h_in_currency: Optional[Dict[str, float]] = None
    """24h price change percentage per currency"""

    price_change_percentage_30d: Optional[float] = None
    """30d price change percentage"""

    price_change_percentage_30d_in_currency: Optional[Dict[str, float]] = None
    """30d price change percentage per currency"""

    price_change_percentage_60d: Optional[float] = None
    """60d price change percentage"""

    price_change_percentage_60d_in_currency: Optional[Dict[str, float]] = None
    """60d price change percentage per currency"""

    price_change_percentage_7d: Optional[float] = None
    """7d price change percentage"""

    price_change_percentage_7d_in_currency: Optional[Dict[str, float]] = None
    """7d price change percentage per currency"""

    roi: Optional[MarketDataRoi] = None
    """Return on investment"""

    sparkline_7d: Optional[List[float]] = None
    """Sparkline 7-day price data"""

    total_supply: Optional[float] = None
    """Total supply"""

    total_value_locked: Optional[float] = None
    """Total value locked"""

    total_volume: Optional[Dict[str, float]] = None
    """Total trading volume in target currency"""


class TickerConvertedLast(BaseModel):
    """Ticker converted last price"""

    btc: Optional[float] = None

    eth: Optional[float] = None

    usd: Optional[float] = None


class TickerConvertedVolume(BaseModel):
    """Ticker converted volume"""

    btc: Optional[float] = None

    eth: Optional[float] = None

    usd: Optional[float] = None


class TickerMarket(BaseModel):
    """Ticker exchange"""

    has_trading_incentive: Optional[bool] = None
    """Exchange trading incentive"""

    identifier: Optional[str] = None
    """Exchange identifier"""

    name: Optional[str] = None
    """Exchange name"""


class Ticker(BaseModel):
    base: Optional[str] = None
    """Ticker base currency"""

    bid_ask_spread_percentage: Optional[float] = None
    """Ticker bid-ask spread percentage"""

    coin_id: Optional[str] = None
    """Ticker base currency coin ID"""

    coin_mcap_usd: Optional[float] = None
    """Market cap in USD"""

    converted_last: Optional[TickerConvertedLast] = None
    """Ticker converted last price"""

    converted_volume: Optional[TickerConvertedVolume] = None
    """Ticker converted volume"""

    is_anomaly: Optional[bool] = None
    """Ticker anomaly"""

    is_stale: Optional[bool] = None
    """Ticker stale"""

    last: Optional[float] = None
    """Ticker last price"""

    last_fetch_at: Optional[str] = None
    """Ticker last fetch timestamp"""

    last_traded_at: Optional[str] = None
    """Ticker last traded timestamp"""

    market: Optional[TickerMarket] = None
    """Ticker exchange"""

    target: Optional[str] = None
    """Ticker target currency"""

    target_coin_id: Optional[str] = None
    """Ticker target currency coin ID"""

    timestamp: Optional[str] = None
    """Ticker timestamp"""

    token_info_url: Optional[str] = None
    """Ticker token info URL"""

    trade_url: Optional[str] = None
    """Ticker trade URL"""

    trust_score: Optional[str] = None
    """Ticker trust score"""

    volume: Optional[float] = None
    """Ticker volume"""


class CoinGetIDResponse(BaseModel):
    id: str
    """Coin ID"""

    additional_notices: List[str]
    """Additional notices"""

    asset_platform_id: Optional[str] = None
    """Coin asset platform ID"""

    block_time_in_minutes: float
    """Blockchain block time in minutes"""

    categories: List[str]
    """Coin categories"""

    country_origin: str
    """Country of origin"""

    description: Dict[str, str]
    """Coin description"""

    detail_platforms: Dict[str, DetailPlatforms]
    """Detailed coin asset platform and contract address"""

    genesis_date: Optional[str] = None
    """Genesis date"""

    has_supply_breakdown: bool
    """Whether detailed supply breakdown data is available via /coins/supply_breakdown"""

    hashing_algorithm: Optional[str] = None
    """Blockchain hashing algorithm"""

    image: Image
    """Coin image URL"""

    last_updated: str
    """Last updated timestamp"""

    links: Links
    """Links"""

    market_cap_rank: Optional[int] = None
    """Market cap rank"""

    market_cap_rank_with_rehypothecated: Optional[int] = None
    """Market cap rank including rehypothecated tokens"""

    name: str
    """Coin name"""

    platforms: Dict[str, str]
    """Coin asset platform and contract address"""

    preview_listing: bool
    """Preview listing coin"""

    public_notice: Optional[str] = None
    """Public notice"""

    sentiment_votes_down_percentage: Optional[float] = None
    """Sentiment votes down percentage"""

    sentiment_votes_up_percentage: Optional[float] = None
    """Sentiment votes up percentage"""

    status_updates: List[StatusUpdate]
    """Status updates"""

    symbol: str
    """Coin symbol"""

    watchlist_portfolio_users: float
    """Number of users watching this coin in portfolio"""

    web_slug: str
    """Coin web slug"""

    categories_details: Optional[List[CategoriesDetail]] = None
    """Detailed coin categories"""

    community_data: Optional[CommunityData] = None
    """Community data"""

    developer_data: Optional[DeveloperData] = None
    """Developer data"""

    ico_data: Optional[IcoData] = None
    """ICO data"""

    localization: Optional[Dict[str, str]] = None
    """Coin name localization"""

    market_data: Optional[MarketData] = None
    """Market data"""

    tickers: Optional[List[Ticker]] = None
    """Tickers"""
