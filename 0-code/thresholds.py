import json
import os
import pathlib
import sys
import time

from datetime import date

import data_tools


DOWN_ARROW = "↓"
UP_ARROW = "↑"

BUY_KEY = "buy"
SELL_KEY = "sell"
PRICE_KEY = "price"
THRESHOLD_KEY = "threshold"

DATE_FORMAT = "%Y-%m-%d"  # Date formatting: year-month-day
TODAY = date.today().strftime(DATE_FORMAT)  # Today's date in that format.

# Look for the thresholds filepath in this directory, if any.
THIS_DIR = pathlib.Path(__file__).resolve().parent
FILEPATH = os.path.join(THIS_DIR, "thresholds.json")


def load_thresholds():
    if not os.path.exists(FILEPATH):
        return {}

    with open(FILEPATH, encoding='utf-8') as f:
        return json.load(f)


def save_thresholds(thresholds):

    with open(FILEPATH, 'w+') as f:
        json.dump(thresholds,
                  f,
                  ensure_ascii=False,
                  indent=2,
                  separators=(',', ':'))
    print("Saved thresholds:")
    print(thresholds)


def record_threshold(ticker, price, threshold):

    assert isinstance(ticker, str)
    assert isinstance(price, (int, float))
    assert isinstance(threshold, (int, float))

    all_thresholds = load_thresholds()
    ticker_thresholds = all_thresholds.get(ticker, {})

    new_threshold = {
        PRICE_KEY: price,
        THRESHOLD_KEY: threshold
    }

    if threshold < price:
        ticker_thresholds[BUY_KEY] = new_threshold
    else:
        ticker_thresholds[SELL_KEY] = new_threshold
    all_thresholds[ticker] = ticker_thresholds

    save_thresholds(all_thresholds)


def compute_growth(latest_value, previous_value):
    
    for arg in [latest_value, previous_value]:
        assert isinstance(arg, (int, float))

    growth = (latest_value - previous_value) / previous_value
    return round(growth, 2)


def notify(notification):
    assert isinstance(notification, str)
    print(notification)

    if "darwin" == sys.platform:
        try:
            msg = ("""osascript  -e 'display notification """
                   """ "%s" with title "Threshold trading"'"""
                   % notification)
            os.system(msg)
        except Exception as e:
            print("Unable to notify on macOS, please contact Miguel")
            print("Exception: ", str(type(e)), str(e))


def should_buy_sell(buy_not_sell, ticker, current_value, threshold_dict):

    assert isinstance(buy_not_sell, bool)
    assert isinstance(ticker, str)
    assert isinstance(current_value, (int, float))
    assert isinstance(threshold_dict, dict)

    if 0 == len(threshold_dict):
        return False

    assert PRICE_KEY in threshold_dict
    assert THRESHOLD_KEY in threshold_dict

    threshold_value = threshold_dict[THRESHOLD_KEY]

    if buy_not_sell:
        if current_value > threshold_value:
            return
        position_relative_to_threshold = "below"
        action = "buying"
    else:
        if current_value < threshold_value:
            return
        position_relative_to_threshold = "above"
        action = "selling"

    price = threshold_dict[PRICE_KEY]
    growth = compute_growth(current_value, price)
    arrow = UP_ARROW if growth > 0 else DOWN_ARROW

    notification = (f"Ticker {ticker} at ${current_value:,.0f},"
                    f" {position_relative_to_threshold} ${threshold_value:,.0f}"
                    f" ({arrow} {abs(growth) * 100:.0f}% compared to ${price:,.0f}),"
                    f" consider {action}")

    notify(notification)


def check_thresholds():
    thresholds = load_thresholds()

    # Students: new syntax: you can iterate through a dictionary's keys and
    # values with this syntax:
    for ticker, ticker_thresholds in thresholds.items():
        current_value = data_tools.download_yfinance_latest(ticker)

        threshold_buy_dict = ticker_thresholds.get(BUY_KEY, {})
        should_buy_sell(buy_not_sell=True,
                        ticker=ticker,
                        current_value=current_value,
                        threshold_dict=threshold_buy_dict)
        
        threshold_sell_dict = ticker_thresholds.get(SELL_KEY, {})
        should_buy_sell(buy_not_sell=False,
                        ticker=ticker,
                        current_value=current_value,
                        threshold_dict=threshold_sell_dict)


def clear_threshold(ticker, threshold_str=None):

    assert isinstance(ticker, str)
    assert threshold_str is None or isinstance(threshold_str, str)

    thresholds = load_thresholds()

    if ticker not in thresholds:
        print(f"Ticker {ticker} not in saved thresholds")
        return

    if None is threshold_str:
        del thresholds[ticker]
        print(f"Thresholds cleared for {ticker}")
        return

    thresholds_for_ticker = thresholds[ticker]
    if threshold_str not in thresholds_for_ticker:
        print(f"Threshold {threshold_str} not in saved thresholds for ticker {ticker}")
        return

    # The subdictionary thresholds_for_ticker is a view, not a copy, of the
    # original dictionary. Therefore, deleting a key in the sub-dictionary also
    # deletes it from the original dictionary.
    del thresholds_for_ticker[threshold_str]
    print(f"Deleted threshold {threshold_str} for ticker {ticker}")

    if not thresholds_for_ticker:
        del thresholds[ticker]

    save_thresholds(thresholds)


def main():
    record_threshold(
        "AAPL",
        price=300,
        threshold=280
    )
    clear_threshold("AAPL", "buy")

    check_thresholds()
    

if '__main__' == __name__:
    main()
