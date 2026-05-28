# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["CategoryGetResponse", "Data", "DataAttributes", "DataAttributesVolumeChangePercentage"]


class DataAttributesVolumeChangePercentage(BaseModel):
    """Volume change percentage over various timeframes"""

    h1: Optional[str] = None

    h12: Optional[str] = None

    h24: Optional[str] = None

    h6: Optional[str] = None


class DataAttributes(BaseModel):
    description: str
    """Category description"""

    fdv_usd: str
    """Fully diluted valuation in USD"""

    h24_tx_count: int
    """24hr transaction count"""

    h24_volume_usd: str
    """24hr volume in USD"""

    name: str
    """Category name"""

    reserve_in_usd: str
    """Total reserve in USD"""

    volume_change_percentage: DataAttributesVolumeChangePercentage
    """Volume change percentage over various timeframes"""


class Data(BaseModel):
    id: str
    """Category ID"""

    attributes: DataAttributes

    type: str
    """Resource type"""


class CategoryGetResponse(BaseModel):
    data: List[Data]
