# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = ["NewsGetResponse", "NewsGetResponseItem"]


class NewsGetResponseItem(BaseModel):
    author: Optional[str] = None
    """news article author"""

    image: Optional[str] = None
    """news article image URL"""

    posted_at: Optional[str] = None
    """news article published timestamp in ISO 8601 format"""

    related_coin_ids: Optional[List[str]] = None
    """related coin IDs"""

    source_name: Optional[str] = None
    """news article source name"""

    title: Optional[str] = None
    """news article title"""

    type: Optional[Literal["news", "guide"]] = None
    """news article type"""

    url: Optional[str] = None
    """news article URL"""


NewsGetResponse: TypeAlias = List[NewsGetResponseItem]
