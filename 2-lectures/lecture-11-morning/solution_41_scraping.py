import requests
from bs4 import BeautifulSoup

def get_sp500_tickers(url="https://stockanalysis.com/list/sp-500-stocks/"):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/122.0.0.0 Safari/537.36"
    }
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    tickers = []

    # The tickers appear in table rows.
    # Inspecting the HTML: each row has a number, then a link with the ticker
    # e.g. <tr>…<td><a href="/stocks/NVDA">NVDA</a></td>…
    # So find all those <a> tags in the table
    # We need to locate the correct table first.

    # Let's find the table by looking for header “Symbol” in the first row:
    tables = soup.find_all("table")
    target_table = None
    for table in tables:
        # check if the table has a header with "Symbol"
        header = table.find("th")
        if header and "Symbol" in header.text:
            target_table = table
            break

    if not target_table:
        raise RuntimeError("Could not find the S&P500 table on the page")

    # Now iterate rows in tbody
    for row in target_table.find("tbody").find_all("tr"):
        # The first <td> is the row number, second <td> has the symbol link
        tds = row.find_all("td")
        if len(tds) >= 2:
            symbol_td = tds[1]
            a = symbol_td.find("a")
            if a:
                ticker = a.text.strip()
                tickers.append(ticker)

    return tickers

if __name__ == "__main__":
    tickers = get_sp500_tickers()
    print(f"Found {len(tickers)} tickers")
    print(tickers)
