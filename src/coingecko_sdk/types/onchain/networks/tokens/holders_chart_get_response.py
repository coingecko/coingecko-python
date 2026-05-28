# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional

from ....._models import BaseModel

__all__ = ["HoldersChartGetResponse", "Data", "DataAttributes", "Meta", "MetaToken"]


class DataAttributes(BaseModel):
    token_holders_list: List[List[Union[str, int]]]
    """Historical token holders as [timestamp, holder_count] pairs"""


class Data(BaseModel):
    id: str
    """Request ID"""

    attributes: DataAttributes

    type: str
    """Resource type"""


class MetaToken(BaseModel):
    address: Optional[str] = None
    """Token contract address"""

    coingecko_coin_id: Optional[str] = None
    """CoinGecko coin ID"""

    name: Optional[str] = None
    """Token name"""

    symbol: Optional[str] = None
    """Token symbol"""


class Meta(BaseModel):
    token: Optional[MetaToken] = None


class HoldersChartGetResponse(BaseModel):
    data: Data

    meta: Meta
