# Prompt to Claude (from Anthropic). The code also fails to find the rate.

# Please write Python code without using BeautifulSoup that returns the current value of the federal funds rate from this page: https://www.federalreserve.gov/releases/h15/

import urllib.request
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

    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req)
    html = resp.read().decode("ascii")

    url = "https://www.federalreserve.gov/releases/h15/"

    # Fetch the page
    with urllib.request.urlopen(url) as response:
        html = response.read().decode('utf-8')

    # Look for the Federal funds (effective) row in the table
    # The pattern looks for the rate value in the table cells
    pattern = r'Federal funds \(effective\)[^<]*</td>\s*<td[^>]*>\s*([\d.]+)'

    match = re.search(pattern, html)

    if match:
        rate = float(match.group(1))
        return rate
    else:
        # Alternative pattern: look for data in the table more broadly
        # Sometimes the rate appears in various formats
        alt_pattern = r'Federal funds[^<]*effective[^<]*</td>(?:\s*<td[^>]*>.*?)*?<td[^>]*>\s*([\d.]+)'  # noqa: E501

        alt_match = re.search(alt_pattern, html, re.DOTALL)

        if alt_match:
            rate = float(alt_match.group(1))
            return rate
        else:
            raise ValueError("Could not find federal funds rate on the page")


if __name__ == "__main__":
    try:
        rate = get_federal_funds_rate(URL)
        print(f"Current Federal Funds Rate (Effective): {rate}%")
    except Exception as e:
        print(f"Error: {e}")
