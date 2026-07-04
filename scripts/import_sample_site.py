from __future__ import annotations

import html
import os
import re
import textwrap
import time
import urllib.parse
import urllib.request
from html.parser import HTMLParser
from pathlib import Path


BASE_URL = "https://workshop-sample.awsfcaj.com/"
ROOT = Path(__file__).resolve().parents[1]
CONTENT_DIR = ROOT / "content"
STATIC_DIR = ROOT / "static"
USER_AGENT = "intership-report-importer/1.0"


def fetch_text(url: str) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=45) as response:
        charset = response.headers.get_content_charset() or "utf-8"
        return response.read().decode(charset, errors="replace")


def fetch_bytes(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=45) as response:
        return response.read()


def clean_url(url: str) -> str:
    parsed = urllib.parse.urlsplit(url)
    return urllib.parse.urlunsplit((parsed.scheme, parsed.netloc, parsed.path, "", ""))


def local_asset_path(url: str) -> Path:
    parsed = urllib.parse.urlsplit(url)
    path = urllib.parse.unquote(parsed.path).lstrip("/")
    return STATIC_DIR / path


def download_asset(url: str, seen: set[str]) -> None:
    absolute = urllib.parse.urljoin(BASE_URL, url)
    absolute = clean_url(absolute)
    parsed = urllib.parse.urlsplit(absolute)
    if parsed.netloc and parsed.netloc != urllib.parse.urlsplit(BASE_URL).netloc:
        return
    if absolute in seen:
        return
    seen.add(absolute)

    target = local_asset_path(absolute)
    if target.exists():
        return
    target.parent.mkdir(parents=True, exist_ok=True)
    try:
        data = fetch_bytes(absolute)
        target.write_bytes(data)
        if target.suffix.lower() == ".css":
            css = data.decode("utf-8", errors="replace")
            for match in re.findall(r"url\\(([^)]+)\\)", css):
                nested = match.strip("'\" ")
                if nested.startswith("data:"):
                    continue
                download_asset(urllib.parse.urljoin(absolute, nested), seen)
    except Exception as exc:
        print(f"warn: could not download {absolute}: {exc}")


class BodyInnerExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=False)
        self.collecting = False
        self.depth = 0
        self.parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = dict(attrs)
        if tag == "div" and attrs_dict.get("id") == "body-inner" and not self.collecting:
            self.collecting = True
            self.depth = 1
            return
        if self.collecting:
            if tag == "div":
                self.depth += 1
            self.parts.append(self.get_starttag_text() or "")

    def handle_endtag(self, tag: str) -> None:
        if not self.collecting:
            return
        if tag == "div":
            self.depth -= 1
            if self.depth == 0:
                self.collecting = False
                return
        self.parts.append(f"</{tag}>")

    def handle_data(self, data: str) -> None:
        if self.collecting:
            self.parts.append(data)

    def handle_entityref(self, name: str) -> None:
        if self.collecting:
            self.parts.append(f"&{name};")

    def handle_charref(self, name: str) -> None:
        if self.collecting:
            self.parts.append(f"&#{name};")


class MarkdownConverter(HTMLParser):
    def __init__(self, asset_seen: set[str]) -> None:
        super().__init__(convert_charrefs=True)
        self.asset_seen = asset_seen
        self.parts: list[str] = []
        self.list_stack: list[str] = []
        self.link_stack: list[str] = []
        self.skip_depth = 0
        self.pre_depth = 0

    def append(self, value: str) -> None:
        self.parts.append(value)

    def newline(self, count: int = 1) -> None:
        self.append("\n" * count)

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = dict(attrs)
        if tag in {"script", "style", "svg"}:
            self.skip_depth += 1
            return
        if self.skip_depth:
            return

        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self.newline(2)
            self.append("#" * int(tag[1]) + " ")
        elif tag == "p":
            self.newline(2)
        elif tag == "br":
            self.newline()
        elif tag == "ul":
            self.list_stack.append("ul")
            self.newline()
        elif tag == "ol":
            self.list_stack.append("ol")
            self.newline()
        elif tag == "li":
            self.newline()
            self.append("  " * max(0, len(self.list_stack) - 1) + "- ")
        elif tag in {"strong", "b"}:
            self.append("**")
        elif tag in {"em", "i"}:
            self.append("*")
        elif tag == "code" and not self.pre_depth:
            self.append("`")
        elif tag == "pre":
            self.pre_depth += 1
            self.newline(2)
            self.append("```text\n")
        elif tag == "a":
            href = attrs_dict.get("href") or ""
            self.link_stack.append(href)
            self.append("[")
        elif tag == "img":
            src = attrs_dict.get("src") or ""
            alt = attrs_dict.get("alt") or "Image"
            if src:
                download_asset(src, self.asset_seen)
                destination = urllib.parse.urlsplit(src).path
                self.newline(2)
                self.append(f"![{escape_markdown(alt)}]({destination})")
                self.newline()
        elif tag == "blockquote":
            self.newline(2)
            self.append("> ")
        elif tag in {"table", "tr"}:
            self.newline()
        elif tag in {"td", "th"}:
            self.append(" | ")

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "svg"} and self.skip_depth:
            self.skip_depth -= 1
            return
        if self.skip_depth:
            return

        if tag in {"h1", "h2", "h3", "h4", "h5", "h6", "p", "blockquote"}:
            self.newline(2)
        elif tag in {"ul", "ol"} and self.list_stack:
            self.list_stack.pop()
            self.newline()
        elif tag in {"strong", "b"}:
            self.append("**")
        elif tag in {"em", "i"}:
            self.append("*")
        elif tag == "code" and not self.pre_depth:
            self.append("`")
        elif tag == "pre" and self.pre_depth:
            self.append("\n```")
            self.pre_depth -= 1
            self.newline(2)
        elif tag == "a" and self.link_stack:
            href = self.link_stack.pop()
            self.append(f"]({href})")
        elif tag in {"tr", "table"}:
            self.newline()

    def handle_data(self, data: str) -> None:
        if self.skip_depth:
            return
        if self.pre_depth:
            self.append(data)
            return
        normalized = re.sub(r"\s+", " ", data)
        self.append(normalized)

    def markdown(self) -> str:
        text = "".join(self.parts)
        text = html.unescape(text)
        text = re.sub(r"[ \t]+\n", "\n", text)
        text = re.sub(r"\n{3,}", "\n\n", text)
        text = re.sub(r" +", " ", text)
        return text.strip() + "\n"


def escape_markdown(value: str) -> str:
    return value.replace("[", "\\[").replace("]", "\\]")


def toml_string(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"')


def page_title(page_html: str, body_html: str) -> str:
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", body_html, re.I | re.S)
    if h1:
        return re.sub(r"\s+", " ", strip_tags(h1.group(1))).strip()
    title = re.search(r"<title>(.*?)</title>", page_html, re.I | re.S)
    if title:
        return html.unescape(title.group(1).split("::")[0]).strip()
    return "Untitled"


def strip_tags(value: str) -> str:
    return re.sub(r"<[^>]+>", "", value)


def content_path_for(url: str) -> Path:
    relative = urllib.parse.urlsplit(url).path.strip("/")
    lang_suffix = ".md"
    if relative == "vi":
        relative = ""
        lang_suffix = ".vi.md"
    elif relative.startswith("vi/"):
        relative = relative[3:]
        lang_suffix = ".vi.md"

    if not relative:
        return CONTENT_DIR / f"_index{lang_suffix}"
    return CONTENT_DIR / relative / f"_index{lang_suffix}"


def weight_for(path: Path) -> int:
    stem = path.parent.name if path.name.startswith("_index") else path.stem
    match = re.match(r"(\d+)(?:[.-](\d+))?(?:[.-](\d+))?", stem)
    if not match:
        return 10
    parts = [int(part) for part in match.groups() if part is not None]
    weight = 0
    for part in parts:
        weight = weight * 100 + part
    return weight


def front_matter(title: str, weight: int) -> str:
    return textwrap.dedent(
        f"""\
        +++
        title = "{toml_string(title)}"
        weight = {weight}
        +++

        """
    )


def sitemap_urls() -> list[str]:
    urls: list[str] = []
    for sitemap in ("en/sitemap.xml", "vi/sitemap.xml"):
        xml = fetch_text(urllib.parse.urljoin(BASE_URL, sitemap))
        urls.extend(re.findall(r"<loc>(.*?)</loc>", xml))
    unique = []
    seen = set()
    for url in urls:
        clean = html.unescape(url)
        if clean not in seen:
            seen.add(clean)
            unique.append(clean)
    return unique


def download_shell_assets(page_html: str, seen: set[str]) -> None:
    for attr in re.findall(r"""(?:href|src)=["']?([^"' >]+)""", page_html, re.I):
        path = urllib.parse.urlsplit(attr).path
        if path.startswith(("/css/", "/js/", "/images/", "/fonts/", "/webfonts/", "/mermaid/")):
            download_asset(attr, seen)


def import_page(url: str, asset_seen: set[str]) -> None:
    page_html = fetch_text(url)
    download_shell_assets(page_html, asset_seen)

    extractor = BodyInnerExtractor()
    extractor.feed(page_html)
    body_html = "".join(extractor.parts)
    if not body_html:
        body_html = page_html

    title = page_title(page_html, body_html)
    converter = MarkdownConverter(asset_seen)
    converter.feed(body_html)
    markdown = converter.markdown()

    destination = content_path_for(url)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(front_matter(title, weight_for(destination)) + markdown, encoding="utf-8")
    print(f"imported {url} -> {destination.relative_to(ROOT)}", flush=True)


def main() -> None:
    CONTENT_DIR.mkdir(parents=True, exist_ok=True)
    STATIC_DIR.mkdir(parents=True, exist_ok=True)
    asset_seen: set[str] = set()

    for url in sitemap_urls():
        import_page(url, asset_seen)
        time.sleep(0.05)


if __name__ == "__main__":
    main()
