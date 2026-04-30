# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["NewsGetParams"]


class NewsGetParams(TypedDict, total=False):
    coin_id: str
    """filter news by coin ID \\**refers to [`/coins/list`](/reference/coins-list)."""

    language: Literal[
        "en",
        "ru",
        "de",
        "pl",
        "es",
        "vi",
        "fr",
        "pt-br",
        "ar",
        "bg",
        "cs",
        "da",
        "el",
        "fi",
        "he",
        "hi",
        "hr",
        "hu",
        "id",
        "it",
        "ja",
        "ko",
        "lt",
        "nl",
        "no",
        "ro",
        "sk",
        "sl",
        "sv",
        "th",
        "tr",
        "uk",
        "zh",
        "zh-tw",
    ]
    """filter news by language Default value: **en**"""

    page: int
    """page through results Default value: **1**"""

    per_page: int
    """total results per page Default value: **10**"""

    type: Literal["all", "news", "guides"]
    """
    filter news by type Default value: **all** Note: `guides` filter is only
    applicable if `coin_id` is specified and valid
    """
