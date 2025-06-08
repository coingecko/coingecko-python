# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["ListGetResponse", "ListGetResponseItem"]


class ListGetResponseItem(BaseModel):
    id: Optional[str] = None
    """coin ID"""

    name: Optional[str] = None
    """coin name"""

    platforms: Optional[Dict[str, str]] = None
    """coin asset platform and contract address"""

    symbol: Optional[str] = None
    """coin symbol"""


ListGetResponse: TypeAlias = List[ListGetResponseItem]
