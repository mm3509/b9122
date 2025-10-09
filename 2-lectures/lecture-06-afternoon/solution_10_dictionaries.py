import tools

portfolio = {'MSFT': 30, 'GTLB': 30, 'GOOG': 20, 'NVDA': 20}

for ticker in portfolio:
    print('Ticker', ticker, 'has', portfolio[ticker], 'shares')


portfolio['GTLB'] = portfolio.get('GTLB', 0) + 10
portfolio['MSFT'] = portfolio.get('MSFT', 0) - 10

value = 0
for ticker in portfolio:
    price = tools.get_yahoo_value(ticker)
    eqv = price * portfolio.get(ticker)
    value += eqv

print(value)
