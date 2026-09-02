# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["IssuerGetListResponse", "IssuerGetListResponseItem"]


class IssuerGetListResponseItem(BaseModel):
    id: str
    """Issuer ID"""

    name: str
    """Issuer name"""


IssuerGetListResponse: TypeAlias = List[IssuerGetListResponseItem]
