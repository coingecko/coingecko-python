# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["CategoryGetResponse", "Data", "DataAttributes", "DataAttributesVolumeChangePercentage"]


class DataAttributesVolumeChangePercentage(BaseModel):
    h1: Optional[str] = None

    h12: Optional[str] = None

    h24: Optional[str] = None

    h6: Optional[str] = None


class DataAttributes(BaseModel):
    description: Optional[str] = None

    fdv_usd: Optional[str] = None

    h24_tx_count: Optional[int] = None

    h24_volume_usd: Optional[str] = None

    name: Optional[str] = None

    reserve_in_usd: Optional[str] = None

    volume_change_percentage: Optional[DataAttributesVolumeChangePercentage] = None


class Data(BaseModel):
    id: Optional[str] = None

    attributes: Optional[DataAttributes] = None

    type: Optional[str] = None


class CategoryGetResponse(BaseModel):
    data: Optional[List[Data]] = None
