# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["NewsGetParams"]


class NewsGetParams(TypedDict, total=False):
    coin_id: str
    """Filter news by coin ID. \\**refers to [`/coins/list`](/reference/coins-list)."""

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
    """Filter news by language. Default: `en`"""

    page: int
    """Page through results. Default value: 1 Valid values: 1...20"""

    per_page: int
    """Total results per page. Default value: 10 Valid values: 1...20"""

    type: Literal["all", "news", "guides"]
    """Filter news by type.

    Default: `all` Note: `guides` filter is only applicable if `coin_id` is
    specified and valid.
    """
