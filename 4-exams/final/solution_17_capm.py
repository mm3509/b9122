from sklearn.linear_model import LinearRegression

import pandas as pd

import data_tools


def helper_get_capm_data(tickers):
    rates = data_tools.get_risk_free_and_market_rates()

    stock_data = data_tools.download_and_merge(tickers)

    for ticker in tickers:
        stock_data[ticker] = stock_data[ticker].pct_change()

    merged = pd.merge(stock_data,
                      rates,
                      how="inner",
                      left_index=True,
                      right_index=True)

    merged = merged.dropna()
    for rate in tickers + [data_tools.MARKET_RATE]:
        merged[rate] = merged[rate] - merged[data_tools.RISK_FREE]

    return merged


def find_optimal_stocks(tickers):

    data = helper_get_capm_data(tickers)

    x = data["market_rate"].values.reshape(-1, 1)

    max_alpha = None
    max_beta = None
    min_beta = None

    for ticker in tickers:

        y = data[ticker].values.reshape(-1, 1)

        reg = LinearRegression().fit(x, y)

        alpha = float(reg.intercept_[0])
        beta = float(reg.coef_[0, 0])

        if max_alpha is None or max_alpha < alpha:
            max_alpha = alpha
            argmax_alpha = ticker

        if max_beta is None or max_beta < beta:
            max_beta = beta
            argmax_beta = ticker

        if min_beta is None or min_beta > beta:
            min_beta = beta
            argmin_beta = ticker

    return argmax_alpha, argmax_beta, argmin_beta


if "__main__" == __name__:
    # Students: you can test this function with this code in a shell:

    # python3 exercise_17_capm.py

    sp500_15 = ["MSFT",
                "AAPL",
                "NVDA",
                "AMZN",
                "GOOG",
                "META",
                "BRK-B",
                "AVGO",
                "TSLA",
                "WMT",
                "JPM",
                "LLY",
                "V",
                "MA"]
    print(find_optimal_stocks(sp500_15))
