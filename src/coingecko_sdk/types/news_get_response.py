# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = ["NewsGetResponse", "NewsGetResponseItem"]


class NewsGetResponseItem(BaseModel):
    author: str
    """News article author"""

    image: str
    """News article image URL"""

    posted_at: str
    """News article published timestamp in ISO 8601 format"""

    related_coin_ids: List[str]
    """Related coin IDs"""

    source_name: str
    """News article source name"""

    title: str
    """News article title"""

    type: Literal["news", "guide"]
    """News article type"""

    url: str
    """News article URL"""


NewsGetResponse: TypeAlias = List[NewsGetResponseItem]
