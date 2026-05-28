# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["TokenListGetAllJsonResponse", "Token", "Version"]


class Token(BaseModel):
    address: str
    """Token contract address"""

    chain_id: float = FieldInfo(alias="chainId")
    """Chainlist's chain ID"""

    decimals: float
    """Token decimals"""

    logo_uri: str = FieldInfo(alias="logoURI")
    """Token image URL"""

    name: str
    """Token name"""

    symbol: str
    """Token symbol"""


class Version(BaseModel):
    """Token list version"""

    major: Optional[float] = None
    """Major version"""

    minor: Optional[float] = None
    """Minor version"""

    patch: Optional[float] = None
    """Patch version"""


class TokenListGetAllJsonResponse(BaseModel):
    keywords: List[str]
    """Token list keywords"""

    logo_uri: str = FieldInfo(alias="logoURI")
    """Token list logo URL"""

    name: str
    """Token list name"""

    timestamp: datetime
    """Token list generation timestamp"""

    tokens: List[Token]
    """List of tokens"""

    version: Version
    """Token list version"""
