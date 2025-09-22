# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = [
    "InfoGetResponse",
    "Data",
    "DataData",
    "DataDataAttributes",
    "DataDataAttributesGtScoreDetails",
    "DataDataAttributesHolders",
    "DataDataAttributesHoldersDistributionPercentage",
    "DataDataAttributesImage",
    "Included",
    "IncludedAttributes",
]


class DataDataAttributesGtScoreDetails(BaseModel):
    creation: Optional[float] = None

    holders: Optional[float] = None

    info: Optional[float] = None

    pool: Optional[float] = None

    transaction: Optional[float] = None


class DataDataAttributesHoldersDistributionPercentage(BaseModel):
    dist_11_30: Optional[float] = FieldInfo(alias="11_30", default=None)

    dist_31_50: Optional[float] = FieldInfo(alias="31_50", default=None)

    rest: Optional[float] = None

    top_10: Optional[float] = None


class DataDataAttributesHolders(BaseModel):
    count: Optional[int] = None

    distribution_percentage: Optional[DataDataAttributesHoldersDistributionPercentage] = None

    last_updated: Optional[str] = None


class DataDataAttributesImage(BaseModel):
    large: Optional[str] = None

    small: Optional[str] = None

    thumb: Optional[str] = None


class DataDataAttributes(BaseModel):
    address: Optional[str] = None

    categories: Optional[List[str]] = None

    coingecko_coin_id: Optional[str] = None

    description: Optional[str] = None

    discord_url: Optional[str] = None

    freeze_authority: Optional[str] = None

    gt_categories_id: Optional[List[str]] = None

    gt_score: Optional[float] = None

    gt_score_details: Optional[DataDataAttributesGtScoreDetails] = None

    holders: Optional[DataDataAttributesHolders] = None

    image: Optional[DataDataAttributesImage] = None

    image_url: Optional[str] = None

    is_honeypot: Union[bool, str, None] = None

    mint_authority: Optional[str] = None

    name: Optional[str] = None

    symbol: Optional[str] = None

    telegram_handle: Optional[str] = None

    twitter_handle: Optional[str] = None

    websites: Optional[List[str]] = None


class DataData(BaseModel):
    id: Optional[str] = None

    attributes: Optional[DataDataAttributes] = None

    type: Optional[str] = None


class Data(BaseModel):
    data: Optional[DataData] = None


class IncludedAttributes(BaseModel):
    base_token_address: Optional[str] = None

    community_sus_report: Optional[float] = None

    quote_token_address: Optional[str] = None

    sentiment_vote_negative_percentage: Optional[float] = None

    sentiment_vote_positive_percentage: Optional[float] = None


class Included(BaseModel):
    id: Optional[str] = None

    attributes: Optional[IncludedAttributes] = None

    type: Optional[str] = None


class InfoGetResponse(BaseModel):
    data: Optional[List[Data]] = None

    included: Optional[List[Included]] = None
