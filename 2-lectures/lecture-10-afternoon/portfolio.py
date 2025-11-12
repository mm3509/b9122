class Transaction():

    def __init__(self, buying_not_selling, ticker, shares, price, date):
        assert isinstance(buying_not_selling, bool)
        assert isinstance(ticker, str)
        for arg in [shares, price]:
            assert isinstance(arg, (int, float)) and shares >= 0
        assert isinstance(date, str)

        self.buying_not_selling = buying_not_selling
        self.ticker = ticker
        self.shares = shares
        self.price = price
        self.date = date

    def compute_total_value(self):
        return self.shares * self.price


class Portfolio():
    
    def __init__(self, amount):
        self.initial_cash = amount
        self.transactions = []

    def count_shares(self, ticker):
        total = 0
        for tx in self.transactions:
            if ticker != tx.ticker:
                continue
            if tx.buying_not_selling:
                total += tx.shares
            else:
                total -= tx.shares

        return total

    def count_cash(self):
        total = self.initial_cash
        for tx in self.transactions:
            amount = tx.compute_total_value()
            if tx.buying_not_selling:
                total -= amount
            else:
                total += amount
                
        return total

    def buy(self, ticker, shares, price, date):

        tx = Transaction(
            buying_not_selling=True,
            ticker=ticker,
            shares=shares,
            price=price,
            date=date
        )

        # No margin: we need to have cash to buy it.
        amount = tx.compute_total_value()
        if self.count_cash() < amount:
            print("Not enough cash")
            return
        
        self.transactions.append(tx)
        print(f"{ticker}: bought {shares:.2f} at {price:.2f} on {date}")

    def sell(self, ticker, shares, price, date):

        # No short-selling: we need to have the shares to sell them.
        if self.count_shares(ticker) < shares:
            print("Not enough shares")
            return

        if 0 == shares:
            return
        
        tx = Transaction(
            buying_not_selling=False,
            ticker=ticker,
            shares=shares,
            price=price,
            date=date
        )
        self.transactions.append(tx)
        print(f"{ticker}: sold {shares:.2f} at {price:.2f} on {date}")

    def profitability(self, total_days):
        current_cash = self.count_cash()
        growth = (current_cash - self.initial_cash) / self.initial_cash
        annualized = (1 + growth) ** (250 / total_days) - 1
        print(f"Annualized growth of portfolio: {annualized * 100:.2f}%")
