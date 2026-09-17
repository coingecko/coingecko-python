# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["IssuerGetIDResponse", "Image", "Token"]


class Image(BaseModel):
    """Issuer image URLs"""

    large: Optional[str] = None
    """Large image URL"""

    small: Optional[str] = None
    """Small image URL"""

    thumb: Optional[str] = None
    """Thumbnail image URL"""


class Token(BaseModel):
    id: Optional[str] = None
    """Token ID"""

    name: Optional[str] = None
    """Token name"""

    platforms: Optional[Dict[str, str]] = None
    """Token asset platform and contract address"""

    symbol: Optional[str] = None
    """Token symbol"""


class IssuerGetIDResponse(BaseModel):
    id: str
    """Issuer ID"""

    market_cap: Optional[float] = None
    """Issuer market cap in USD"""

    market_cap_change_24h: Optional[float] = None
    """24-hour issuer market cap change in USD"""

    name: str
    """Issuer name"""

    updated_at: datetime
    """Issuer last updated timestamp"""

    volume_24h: Optional[float] = None
    """24-hour issuer trading volume in USD"""

    image: Optional[Image] = None
    """Issuer image URLs"""

    tokens: Optional[List[Token]] = None
    """Tokens issued by this issuer"""
