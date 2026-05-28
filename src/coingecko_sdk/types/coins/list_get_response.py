# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["ListGetResponse", "ListGetResponseItem"]


class ListGetResponseItem(BaseModel):
    id: str
    """Coin ID"""

    name: str
    """Coin name"""

    symbol: str
    """Coin symbol"""

    platforms: Optional[Dict[str, Optional[str]]] = None
    """Asset platform and contract address"""


ListGetResponse: TypeAlias = List[ListGetResponseItem]
