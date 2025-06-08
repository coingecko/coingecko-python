# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = [
    "InfoGetResponse",
    "Data",
    "DataAttributes",
    "DataAttributesGtScoreDetails",
    "DataAttributesHolders",
    "DataAttributesHoldersDistributionPercentage",
    "DataAttributesImage",
]


class DataAttributesGtScoreDetails(BaseModel):
    creation: Optional[float] = None

    holders: Optional[float] = None

    info: Optional[float] = None

    pool: Optional[float] = None

    transaction: Optional[float] = None


class DataAttributesHoldersDistributionPercentage(BaseModel):
    dist_11_30: Optional[float] = FieldInfo(alias="11_30", default=None)

    dist_31_50: Optional[float] = FieldInfo(alias="31_50", default=None)

    rest: Optional[float] = None

    top_10: Optional[float] = None


class DataAttributesHolders(BaseModel):
    count: Optional[int] = None

    distribution_percentage: Optional[DataAttributesHoldersDistributionPercentage] = None

    last_updated: Optional[str] = None


class DataAttributesImage(BaseModel):
    large: Optional[str] = None

    small: Optional[str] = None

    thumb: Optional[str] = None


class DataAttributes(BaseModel):
    address: Optional[str] = None

    categories: Optional[List[str]] = None

    coingecko_coin_id: Optional[str] = None

    description: Optional[str] = None

    discord_url: Optional[str] = None

    freeze_authority: Optional[str] = None

    gt_categories_id: Optional[List[str]] = None

    gt_score: Optional[float] = None

    gt_score_details: Optional[DataAttributesGtScoreDetails] = None

    holders: Optional[DataAttributesHolders] = None

    image: Optional[DataAttributesImage] = None

    image_url: Optional[str] = None

    mint_authority: Optional[str] = None

    name: Optional[str] = None

    symbol: Optional[str] = None

    telegram_handle: Optional[str] = None

    twitter_handle: Optional[str] = None

    websites: Optional[List[str]] = None


class Data(BaseModel):
    id: Optional[str] = None

    attributes: Optional[DataAttributes] = None

    type: Optional[str] = None


class InfoGetResponse(BaseModel):
    data: Optional[Data] = None
