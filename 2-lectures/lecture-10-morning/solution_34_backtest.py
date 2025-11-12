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

for current_date in range(10, len(data.index)):
    y = prices_as_vector[:current_date]

    # For simplicity, use integer indices as the regressor, not dates. This
    # means that we ignore weekends and holidays.
    x = np.arange(current_date).reshape(-1, 1)
    current_price = y.iloc[-1]

    # TODO: run a linear regression here and define two booleans: below_trend
    # and above_trend.
    
    y_log = np.log(y)
    reg_fit = reg.fit(x, y_log)
    y_log_last_predicted = reg.predict(x)[-1]

    above_trend = np.log(current_price) > 1.1 * y_log_last_predicted 
    below_trend = np.log(current_price) < 0.9 * y_log_last_predicted

    if below_trend:
        cash = p.count_cash()
        shares = (0.1 * cash) / current_price
        p.buy(ticker=TICKER,
              shares=shares,
              price=current_price,
              date=str(current_date))

    if above_trend:
        shares = p.count_shares(TICKER) * 0.1
        p.sell(ticker=TICKER,
               shares=shares,
               price=current_price,
               date=str(current_date))

shares = p.count_shares(TICKER)
p.sell(ticker=TICKER, shares=shares, price=current_price, date=str(current_date))
p.profitability(total_days)

# Plot the last linear regression.
plt.figure()
plt.plot(x, y_log)
y_predicted = reg.predict(x)
plt.plot(x, y_predicted, c="r")
plt.xlabel("time")
plt.ylabel(f"Stock price of {TICKER} (logs)")
plt.savefig("backtesting-linear-regression-log.png")
plt.show()
