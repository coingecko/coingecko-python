# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["PingGetResponse"]


class PingGetResponse(BaseModel):
    gecko_says: str
    """API server status message"""
