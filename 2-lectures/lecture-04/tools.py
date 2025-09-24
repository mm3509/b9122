import yfinance as yf


class YahooError(Exception):
    pass


def get_yahoo_value(code):
    """
    >>> a = get_yahoo_value("EURUSD=X")
    >>> a > 1.1
    True
    >>> a < 1.2
    True
    >>> get_yahoo_value(123)
    Traceback (most recent call last):
    ...
    TypeError: argument must be ...
    """

    if not isinstance(code, str):
        raise TypeError("argument must be a string")

    dataframe = yf.download(code, progress=False, auto_adjust=True)
    closing_value_series = dataframe[["Close"]]

    num_obs = closing_value_series.shape[0]
    if num_obs == 0:
        raise YahooError("Yahoo did not return any data")

    latest_date = max(closing_value_series.index)

    latest_value_as_series = closing_value_series.loc[latest_date]
    latest_value_as_float = float(latest_value_as_series.iloc[0])

    return latest_value_as_float
