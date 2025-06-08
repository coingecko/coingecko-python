# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ....._models import BaseModel

__all__ = ["HoldersChartGetResponse", "Data", "DataAttributes", "Meta", "MetaToken"]


class DataAttributes(BaseModel):
    token_holders_list: Optional[List[List[str]]] = None


class Data(BaseModel):
    id: Optional[str] = None

    attributes: Optional[DataAttributes] = None

    type: Optional[str] = None


class MetaToken(BaseModel):
    address: Optional[str] = None

    coingecko_coin_id: Optional[str] = None

    name: Optional[str] = None

    symbol: Optional[str] = None


class Meta(BaseModel):
    token: Optional[MetaToken] = None


class HoldersChartGetResponse(BaseModel):
    data: Optional[Data] = None

    meta: Optional[Meta] = None
