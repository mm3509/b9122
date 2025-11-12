import yfinance


class YahooError(Exception):
    pass


def download_yfinance(code, start_date=None, end_date=None):

    if not isinstance(code, str):
        raise TypeError("argument must be a string")

    # No need for API key.
    data = yfinance.download(code,
                             start=start_date,
                             end=end_date,
                             progress=False,
                             auto_adjust=True,
                             multi_level_index=False,
                             ignore_tz=True)[["Close"]]

    # Use this redundant syntax to avoid a warning from Pandas.
    data = data.rename(columns={"Close": code})

    return data


def download_yfinance_latest(code):
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

    data_series = download_yfinance(code)[[code]]

    num_obs = data_series.shape[0]
    if num_obs == 0:
        raise YahooError("Yahoo did not return any data")

    latest_date = max(data_series.index)

    latest_value_as_series = data_series.loc[latest_date]
    latest_value_as_float = float(latest_value_as_series.iloc[0])

    return latest_value_as_float


def get_yahoo_value(code):
    return download_yfinance_latest(code)


def get_yahoo_price(code):
    return download_yfinance_latest(code)


