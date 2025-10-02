import tools

import statistics as st
from statistics import mean

portfolio = {'MSFT': 30, 'AAPL': 30, 'GOOG': 20, 'NVDA': 20}

for ticker in portfolio:
    print('Ticker', ticker, 'has', portfolio[ticker], 'shares')

print('Total number of shares:', sum(portfolio.values()))

portfolio['GTLB'] = portfolio.get('GTLB', 0) + 10
portfolio['MSFT'] = portfolio.get('MSFT', 0) - 10

print('Total number of shares:', sum(portfolio.values())

# Computation with an alias.
shares = portfolio.values()
avg = st.mean(shares)
print('Average number of shares:', avg)

print('  Mean:', st.mean(shares))
print('  Mode:', st.mode(shares))
print('Median:', st.median(shares))
print('St-dev:', st.stdev(shares))


# Computation with a `from ... import ...`.
print('  Mean:', mean(shares))



total_value = 0

for key in portfolio:
    total_value += portfolio[key] * tools.get_yahoo_price(key)

print('Total value = ', total_value)
