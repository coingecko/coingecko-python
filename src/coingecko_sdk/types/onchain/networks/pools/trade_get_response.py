# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ....._models import BaseModel

__all__ = ["TradeGetResponse", "Data", "DataAttributes"]


class DataAttributes(BaseModel):
    block_number: Optional[int] = None

    block_timestamp: Optional[str] = None

    from_token_address: Optional[str] = None

    from_token_amount: Optional[str] = None

    kind: Optional[str] = None

    price_from_in_currency_token: Optional[str] = None

    price_from_in_usd: Optional[str] = None

    price_to_in_currency_token: Optional[str] = None

    price_to_in_usd: Optional[str] = None

    to_token_address: Optional[str] = None

    to_token_amount: Optional[str] = None

    tx_from_address: Optional[str] = None

    tx_hash: Optional[str] = None

    volume_in_usd: Optional[str] = None


class Data(BaseModel):
    id: Optional[str] = None

    attributes: Optional[DataAttributes] = None

    type: Optional[str] = None


class TradeGetResponse(BaseModel):
    data: Optional[List[Data]] = None
