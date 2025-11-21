import requests
from bs4 import BeautifulSoup

def get_ebay_price(url):
    # Some pages require a user-agent to avoid bot blocking
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/124.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an error for bad responses

    soup = BeautifulSoup(response.text, "html.parser")

    # Try several common price selectors used by eBay
    selectors = [
        "#prcIsum",                   # regular price
        "#prcIsum_bidPrice",         # auction price
        ".notranslate#mm-saleDscPrc",# discounted price
        "#convbinPrice",             # converted BIN price
        ".x-price-primary span",     # newer layout price
    ]

    price = None
    for sel in selectors:
        tag = soup.select_one(sel)
        if tag:
            price = tag.get_text(strip=True)
            break

    return price


if __name__ == "__main__":
    url = "https://www.ebay.com/itm/388799045923"
    price = get_ebay_price(url)

    if price:
        print("Price found:", price)
    else:
        print("Price not found — the page layout may have changed.")
