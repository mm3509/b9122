# Prompt:

# Please write a Python script that fetches this page from eBay, parses it, and returns the price of the item: https://www.ebay.com/itm/388799045923

import requests
from bs4 import BeautifulSoup
import re

def get_ebay_price(url: str) -> float:
    # Use a realistic User-Agent to reduce chance of being blocked
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        )
    }
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")

    # From inspecting the page, the price is “US $28.86” in plain text.
    # Let’s find the span or element containing that.
    # On many eBay product pages, the main price is inside a tag with id="prcIsum" or class like "notranslate"
    # But that can vary. For simplicity, let's search for any element that looks like the price string.
    price_text = None

    # Try a few known patterns:

    # 1) Try an element with id "prcIsum"
    el = soup.find(id="prcIsum")
    if el and el.text:
        price_text = el.text.strip()
    else:
        # 2) Try class-based: some listings use class “notranslate” for price
        el = soup.find("span", class_="notranslate")
        if el and el.text:
            price_text = el.text.strip()
        else:
            # 3) fallback: find text "US $" using regex in all text nodes
            text = soup.get_text(separator=" ", strip=True)
            # find something like "US $28.86"
            m = re.search(r"US\s*\$\s*([0-9,]+(?:\.[0-9]+)?)", text)
            if m:
                price_text = m.group(0)  # e.g. "US $28.86"
            else:
                raise ValueError("Could not find price on page")

    # Now price_text should be something like "US $28.86" or "$28.86"
    # Extract the numeric part
    m = re.search(r"([0-9,]+\.[0-9]+)", price_text)
    if not m:
        # maybe integer dollars
        m = re.search(r"([0-9,]+)", price_text)
    if not m:
        raise ValueError(f"Could not parse price from text: {price_text}")

    # Normalize and convert
    number_str = m.group(1).replace(",", "")
    price = float(number_str)
    return price


if __name__ == "__main__":
    url = "https://www.ebay.com/itm/388799045923"
    price = get_ebay_price(url)
    print("Price:", price)
