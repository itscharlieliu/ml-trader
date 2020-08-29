import datetime

import yfinance

from iex.cloud import cloud


class Trader:
    def __init__(self, api_key: str, ticker: str, sandbox: bool = True, years: int = 1):
        self._data_points = []
        self._cloud = cloud(api_key, sandbox)
        self._years = years
        self._ticker = ticker

    def get_sentiment(self):
        return self._data_points

    def train(self):
        curr_date = datetime.date.today()
        start_date = datetime.date(curr_date.year - self._years, curr_date.month, curr_date.day)

        print(f"{curr_date} {start_date}")
        self._data_points = yfinance.download(self._ticker, start_date, curr_date)
        print(self._data_points)

        x = self._data_points[:, 0:4]
        y = self._data_points[:, 4]
        x_train, x_validation, y_train, y_validation = train_test_split(x, y, test_size=0.20, random_state=1)
