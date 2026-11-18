"""Parse HTML bytes with the explicit HTTP charset or the document's own encoding."""

from email.message import Message

from bs4 import BeautifulSoup


def parse_html(response):
    headers = Message()
    headers["Content-Type"] = response.headers.get("Content-Type", "")
    return BeautifulSoup(response.content, "lxml", from_encoding=headers.get_content_charset())
