# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ....._models import BaseModel

__all__ = ["TradeGetResponse", "Data", "DataAttributes"]


class DataAttributes(BaseModel):
    block_number: int
    """Block number of the trade"""

    block_timestamp: str
    """Block timestamp"""

    from_token_address: str
    """From-token contract address"""

    from_token_amount: str
    """Amount of token sent"""

    kind: str
    """Trade kind (buy or sell)"""

    pool_address: str
    """Pool contract address where the trade occurred"""

    pool_dex: str
    """DEX identifier of the pool"""

    price_from_in_currency_token: str
    """Price of from-token in currency token"""

    price_from_in_usd: str
    """Price of from-token in USD"""

    price_to_in_currency_token: str
    """Price of to-token in currency token"""

    price_to_in_usd: str
    """Price of to-token in USD"""

    to_token_address: str
    """To-token contract address"""

    to_token_amount: str
    """Amount of token received"""

    tx_from_address: str
    """Transaction sender address"""

    tx_hash: str
    """Transaction hash"""

    volume_in_usd: str
    """Trade volume in USD"""


class Data(BaseModel):
    id: str
    """Trade identifier"""

    attributes: DataAttributes

    type: str
    """Resource type"""


class TradeGetResponse(BaseModel):
    data: List[Data]
