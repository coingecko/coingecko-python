# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "RwaGetIDResponse",
    "Image",
    "TokenizedMarketData",
    "TokenizedMarketDataSparklineIn7d",
    "Token",
    "TokenIssuerDetails",
]


class Image(BaseModel):
    """Image URLs of the token with the largest market cap"""

    large: Optional[str] = None
    """Large image URL"""

    small: Optional[str] = None
    """Small image URL"""

    thumb: Optional[str] = None
    """Thumbnail image URL"""


class TokenizedMarketDataSparklineIn7d(BaseModel):
    """Sparkline price data for the last 7 days"""

    price: Optional[List[float]] = None
    """Array of price values"""


class TokenizedMarketData(BaseModel):
    """Aggregated tokenized market data"""

    current_price: Optional[float] = None
    """Current price in target currency"""

    high_24h: Optional[float] = None
    """24-hour price high in target currency"""

    last_updated: Optional[datetime] = None
    """Last updated timestamp"""

    low_24h: Optional[float] = None
    """24-hour price low in target currency"""

    market_cap: Optional[float] = None
    """Market cap in target currency"""

    market_cap_change_24h: Optional[float] = None
    """24-hour market cap change in target currency"""

    market_cap_change_percentage_24h: Optional[float] = None
    """24-hour market cap change percentage"""

    price_change_24h: Optional[float] = None
    """24-hour price change in target currency"""

    price_change_percentage_14d_in_currency: Optional[float] = None
    """14-day price change percentage in target currency"""

    price_change_percentage_1h_in_currency: Optional[float] = None
    """1-hour price change percentage in target currency"""

    price_change_percentage_1y_in_currency: Optional[float] = None
    """1-year price change percentage in target currency"""

    price_change_percentage_200d_in_currency: Optional[float] = None
    """200-day price change percentage in target currency"""

    price_change_percentage_24h: Optional[float] = None
    """24-hour price change percentage"""

    price_change_percentage_24h_in_currency: Optional[float] = None
    """24-hour price change percentage in target currency"""

    price_change_percentage_30d_in_currency: Optional[float] = None
    """30-day price change percentage in target currency"""

    price_change_percentage_7d_in_currency: Optional[float] = None
    """7-day price change percentage in target currency"""

    sparkline_in_7d: Optional[TokenizedMarketDataSparklineIn7d] = None
    """Sparkline price data for the last 7 days"""

    total_volume: Optional[float] = None
    """Total trading volume in target currency"""


class TokenIssuerDetails(BaseModel):
    """Token issuer details"""

    id: Optional[str] = None
    """Issuer ID"""

    name: Optional[str] = None
    """Issuer name"""


class Token(BaseModel):
    id: Optional[str] = None
    """Token ID"""

    issuer_details: Optional[TokenIssuerDetails] = None
    """Token issuer details"""

    name: Optional[str] = None
    """Token name"""

    platforms: Optional[Dict[str, str]] = None
    """Token asset platform and contract address"""

    symbol: Optional[str] = None
    """Token symbol"""


class RwaGetIDResponse(BaseModel):
    id: str
    """RWA ID"""

    asset_type: Literal["stock", "commodity", "etf"]
    """RWA asset type"""

    image: Image
    """Image URLs of the token with the largest market cap"""

    last_updated: datetime
    """Last updated timestamp"""

    name: str
    """RWA name"""

    symbol: str
    """RWA symbol"""

    web_slug: str
    """RWA web slug"""

    tokenized_market_data: Optional[TokenizedMarketData] = None
    """Aggregated tokenized market data"""

    tokens: Optional[List[Token]] = None
    """Tokens tracking this RWA"""
