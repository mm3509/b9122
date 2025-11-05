import os


import numpy as np
import sklearn.linear_model
import matplotlib.pyplot as plt
import yfinance as yf


import data_tools
import portfolio


# TODO: define the ticker you want to use for back-testing.
TICKER = "GOOG"
INITIAL_CASH = 100


data = data_tools.download_yfinance(TICKER)

total_days = (max(data.index) - min(data.index)).days


reg = sklearn.linear_model.LinearRegression()

p = portfolio.Portfolio(INITIAL_CASH)
prices_as_vector = data.squeeze()

for i in range(10, len(data.index)):
    y = prices_as_vector[:i]

    # For simplicity, use integer indices as the regressor, not dates. This
    # means that we ignore weekends and holidays.
    x = np.arange(i).reshape(-1, 1)
    current_price = y.iloc[-1]

    # TODO: run a linear regression here and define two booleans: below_trend
    # and above_trend.

    if below_trend:
        cash = p.count_cash()
        shares = (0.1 * cash) / current_price
        p.buy(ticker=TICKER,
              shares=shares,
              price=current_price,
              date=str(i))

    if above_trend:
        shares = p.count_shares(TICKER) * 0.1
        p.sell(ticker=TICKER,
               shares=shares,
               price=current_price,
               date=str(i))

shares = p.count_shares(TICKER)
p.sell(ticker=TICKER, shares=shares, price=current_price, date=str(i))
p.profitability(total_days)

# Plot the last linear regression.
plt.figure()
plt.plot(x, y)
y_predicted = reg.predict(x)
plt.plot(x, y_predicted, c="r")
plt.xlabel("time")
plt.ylabel(f"Stock price of {TICKER} (logs)")
plt.savefig("backtesting-linear-regression-log.png")
plt.show()
