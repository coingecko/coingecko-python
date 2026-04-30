# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["TokenListGetAllJsonResponse", "Token", "Version"]


class Token(BaseModel):
    address: Optional[str] = None
    """token contract address"""

    chain_id: Optional[float] = FieldInfo(alias="chainId", default=None)
    """chainlist's chain ID"""

    decimals: Optional[float] = None
    """token decimals"""

    logo_uri: Optional[str] = FieldInfo(alias="logoURI", default=None)
    """token image url"""

    name: Optional[str] = None
    """token name"""

    symbol: Optional[str] = None
    """token symbol"""


class Version(BaseModel):
    """token list version"""

    major: Optional[float] = None

    minor: Optional[float] = None

    patch: Optional[float] = None


class TokenListGetAllJsonResponse(BaseModel):
    keywords: Optional[List[str]] = None

    logo_uri: Optional[str] = FieldInfo(alias="logoURI", default=None)

    name: Optional[str] = None

    timestamp: Optional[datetime] = None

    tokens: Optional[List[Token]] = None

    version: Optional[Version] = None
    """token list version"""
