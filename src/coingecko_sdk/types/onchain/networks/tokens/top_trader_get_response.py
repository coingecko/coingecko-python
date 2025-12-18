# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ....._models import BaseModel

__all__ = ["TopTraderGetResponse", "Data", "DataAttributes", "DataAttributesTrader"]


class DataAttributesTrader(BaseModel):
    address: Optional[str] = None

    average_buy_price_usd: Optional[str] = None

    average_sell_price_usd: Optional[str] = None

    explorer_url: Optional[str] = None

    label: Optional[str] = None

    name: Optional[str] = None

    realized_pnl_usd: Optional[str] = None

    token_balance: Optional[str] = None

    total_buy_count: Optional[int] = None

    total_buy_token_amount: Optional[str] = None

    total_buy_usd: Optional[str] = None

    total_sell_count: Optional[int] = None

    total_sell_token_amount: Optional[str] = None

    total_sell_usd: Optional[str] = None

    type: Optional[str] = None

    unrealized_pnl_usd: Optional[str] = None


class DataAttributes(BaseModel):
    traders: Optional[List[DataAttributesTrader]] = None


class Data(BaseModel):
    id: Optional[str] = None

    attributes: Optional[DataAttributes] = None

    type: Optional[str] = None


class TopTraderGetResponse(BaseModel):
    data: Optional[Data] = None
