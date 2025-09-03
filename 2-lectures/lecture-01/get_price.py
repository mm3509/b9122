# On Colab, uncomment this next line:
#!pip install yfinance

import yfinance

ticker = "MSFT"
data = yfinance.download(ticker, progress=False, auto_adjust=True)[["Close"]]
latest_date = min(data.index)

print(f"Stock prices of {ticker} as of {latest_date}:")
print(data)

