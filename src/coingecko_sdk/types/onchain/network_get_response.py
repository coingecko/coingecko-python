# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["NetworkGetResponse", "Data", "DataAttributes"]


class DataAttributes(BaseModel):
    coingecko_asset_platform_id: str
    """Corresponding CoinGecko asset platform ID"""

    name: str
    """Network name"""


class Data(BaseModel):
    id: str
    """Network identifier"""

    attributes: DataAttributes

    type: str
    """Resource type"""


class NetworkGetResponse(BaseModel):
    data: List[Data]
