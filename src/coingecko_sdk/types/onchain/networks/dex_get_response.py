# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["DexGetResponse", "Data", "DataAttributes"]


class DataAttributes(BaseModel):
    name: Optional[str] = None


class Data(BaseModel):
    id: Optional[str] = None

    attributes: Optional[DataAttributes] = None

    type: Optional[str] = None


class DexGetResponse(BaseModel):
    data: Optional[List[Data]] = None
