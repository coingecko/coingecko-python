# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["InsightGetResponse", "InsightGetResponseItem"]


class InsightGetResponseItem(BaseModel):
    description: str
    """Insight description"""

    posted_at: str
    """Insight posted timestamp in ISO 8601 format"""

    related_coin_ids: List[str]
    """Related coin IDs"""

    title: str
    """Insight title"""


InsightGetResponse: TypeAlias = List[InsightGetResponseItem]
