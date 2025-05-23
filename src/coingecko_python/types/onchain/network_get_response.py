# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["NetworkGetResponse", "Data", "DataAttributes"]


class DataAttributes(BaseModel):
    coingecko_asset_platform_id: Optional[str] = None

    name: Optional[str] = None


class Data(BaseModel):
    id: Optional[str] = None

    attributes: Optional[DataAttributes] = None

    type: Optional[str] = None


class NetworkGetResponse(BaseModel):
    data: Optional[List[Data]] = None
