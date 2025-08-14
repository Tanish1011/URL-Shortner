from urllib.parse import urlparse

def normalize_url(url: str) -> str:
    url = url.strip()
    if not urlparse(url).scheme:
        url = "http://" + url
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https"):
        raise ValueError("Invalid scheme")
    return url
