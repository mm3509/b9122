import os
import pathlib

import fredapi
import pandas as pd
import yfinance

THIS_DIR = pathlib.Path(__file__).resolve().parent
DATA_FILEPATH = os.path.join(THIS_DIR, "rates.ft")
FED_FUNDS = "DFF"
SP500 = "^SPX"
RISK_FREE = "risk_free"
MARKET_RATE = "market_rate"
START_DATE = "1986-01-02"
END_DATE = "2024-11-01"

USE_CACHE = False


def download_yfinance(ticker):

    # Download financial data from Yahoo Finance. No need for API key.
    data = yfinance.download(ticker,
                             start=START_DATE,
                             end=END_DATE,
                             progress=False,
                             auto_adjust=True,
                             multi_level_index=False,
                             ignore_tz=True)[["Close"]]

    # Use this redundant syntax to avoid a warning from Pandas.
    data = data.rename(columns={"Close": ticker})

    return data


def get_risk_free_and_market_rates():

    return pd.read_feather(DATA_FILEPATH)


def download_and_merge(tickers):

    if USE_CACHE:
        fp = ",".join(tickers) + ".ft"
        if os.path.exists(fp):
            return pd.read_feather(fp)

    first = True
    for ticker in tickers:
        if first:
            merged = download_yfinance(ticker)
            first = False
            continue

        data = download_yfinance(ticker)
        merged = pd.merge(merged,
                          data,
                          how="inner",
                          left_index=True,
                          right_index=True)

    if USE_CACHE:
        merged.to_feather(fp)

    return merged


if "__main__" == __name__:
    print(download_and_merge(["AAPL", "GOOG", "MSFT"]))
