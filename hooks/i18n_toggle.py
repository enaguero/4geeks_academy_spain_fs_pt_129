"""Rewrite the in-content language-toggle link to a working mkdocs URL.

Source files contain a toggle like:
    🇪🇸 **Español** | [🇬🇧 English](README.en.md)
or (English variant):
    [🇪🇸 Español](README.md) | 🇬🇧 **English**

On GitHub, the *.en.md link works because the file exists on disk.
On the deployed mkdocs site, mkdocs-static-i18n consumes the .en.md as a
language variant, so the link target does not exist and the toggle 404s.

This hook detects the toggle line and rewrites the link target to a relative
URL pointing to the equivalent page in the other language tree.
"""

import re


_SPANISH_TOGGLE = re.compile(
    r"(🇪🇸 \*\*Español\*\* \| \[🇬🇧 English\]\()[^)]+(\))"
)
_ENGLISH_TOGGLE = re.compile(
    r"(\[🇪🇸 Español\]\()[^)]+(\) \| 🇬🇧 \*\*English\*\*)"
)


def _relative_url(from_url: str, to_url: str) -> str:
    """Return a relative URL going from `from_url` to `to_url`.

    Both URLs are directory-form mkdocs URLs (end with `/`, no leading `/`).
    The empty string represents the site root.
    """
    from_parts = [p for p in from_url.rstrip("/").split("/") if p]
    to_parts = [p for p in to_url.rstrip("/").split("/") if p]

    if not from_parts and not to_parts:
        return "./"
    if not from_parts:
        return "/".join(to_parts) + "/"
    if not to_parts:
        return "../" * len(from_parts)

    common = 0
    while (
        common < len(from_parts)
        and common < len(to_parts)
        and from_parts[common] == to_parts[common]
    ):
        common += 1

    up = len(from_parts) - common
    down = to_parts[common:]

    if up == 0 and not down:
        return "./"

    return "/".join([".."] * up + down) + "/"


def _sibling_url(page_url: str) -> str:
    """Return the URL of the equivalent page in the other language."""
    if page_url == "en/" or page_url.startswith("en/"):
        # English → Spanish: strip the leading "en/"
        return page_url[3:]
    # Spanish → English: prepend "en/"
    return "en/" + page_url


def on_page_markdown(markdown, page, config, files):
    page_url = page.url
    target = _relative_url(page_url, _sibling_url(page_url))

    markdown = _SPANISH_TOGGLE.sub(
        lambda m: m.group(1) + target + m.group(2), markdown, count=1
    )
    markdown = _ENGLISH_TOGGLE.sub(
        lambda m: m.group(1) + target + m.group(2), markdown, count=1
    )
    return markdown
