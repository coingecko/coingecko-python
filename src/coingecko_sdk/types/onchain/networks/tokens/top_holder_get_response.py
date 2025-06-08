# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ....._models import BaseModel

__all__ = ["TopHolderGetResponse", "Data", "DataAttributes", "DataAttributesHolder"]


class DataAttributesHolder(BaseModel):
    address: Optional[str] = None

    amount: Optional[str] = None

    label: Optional[str] = None

    percentage: Optional[str] = None

    rank: Optional[float] = None

    value: Optional[str] = None


class DataAttributes(BaseModel):
    holders: Optional[List[DataAttributesHolder]] = None

    last_updated_at: Optional[str] = None


class Data(BaseModel):
    id: Optional[str] = None

    attributes: Optional[DataAttributes] = None

    type: Optional[str] = None


class TopHolderGetResponse(BaseModel):
    data: Optional[Data] = None
