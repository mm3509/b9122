# Add your prompt here, as a comment in one line. If it has a link, it won't be
# flagged for going over 80 characters.

# Please write Python code using BeautifulSoup that returns the current value of the federal funds rate from this page: https://www.federalreserve.gov/releases/h15/

import requests
from bs4 import BeautifulSoup


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

    resp = requests.get(url)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    # On the H.15 page, the rate is in a table under the "Federal funds
    # (effective)" row.  Let's find the table row containing that.
    rate = None
    for tr in soup.select("table tr"):
        th = tr.find("th")
        if th and "Federal funds (effective)" in th.text:
            # find the last non-empty <td> in that row
            tds = tr.find_all("td")
            # strip whitespace and filter out weird/empty entries
            values = [td.get_text(strip=True)
                      for td in tds if td.get_text(strip=True)]
            if values:
                rate = values[-1]
            break

    return rate


if __name__ == "__main__":
    eff_rate = get_federal_funds_rate(URL)
    print("Effective Federal Funds Rate:", eff_rate)
