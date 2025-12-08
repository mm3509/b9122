# Prompt to chatGPT. The code fails to find the rate.

# Thank you. Now write a different version of the script without using
# BeautifulSoup at all.

import requests
import re


URL = "https://www.federalreserve.gov/releases/h15/"


def get_federal_funds_rate(url):
    """
    >>> get_federal_funds_rate(123)
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> get_federal_funds_rate("htt://")
    Traceback (most recent call last):
    ...
    AssertionError...
    """

    assert isinstance(url, str) and url.startswith("https://")

    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; my-scraper/1.0)"
    }

    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    html = resp.text

    text = re.sub(r"\s+", " ", html)

    # Regex pattern:
    # Look for "Federal funds (effective)" followed by any HTML,
    # then capture the next number-like string (e.g., 5.33)
    pattern = r"Federal funds \(effective\).*?>(\d+\.\d+)<"

    match = re.search(pattern, text, re.IGNORECASE)
    if not match:
        raise ValueError("Could not find the effective federal funds rate.")

    return match.group(1)


if __name__ == "__main__":
    rate = get_federal_funds_rate(URL)
    print("Effective Federal Funds Rate:", rate)
