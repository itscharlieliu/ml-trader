import datetime

import matplotlib
import pandas_datareader.data as web

import yfinance
from matplotlib import style, pyplot
from sklearn.model_selection import train_test_split

from iex.cloud import cloud


class Trader:
    def __init__(self, api_key: str, ticker: str, sandbox: bool = True, years: int = 5):
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

        # Calculate rolling mean
        close_price = self._data_points["Adj Close"]
        moving_avg = close_price.rolling(window=100).mean()

        print(moving_avg)

        # matplotlib.rc('figure', figsize=(8, 7))
        #
        # style.use("ggplot")
        #
        # close_price.plot(label="AAPL")
        # moving_avg.plot(label="Moving avg")
        #
        # pyplot.legend()
        #

        returns = close_price / close_price.shift(1) - 1

        returns.plot(label="returns")
        pyplot.show()


        # data_file = web.DataReader("AAPL", "yahoo", start_date, curr_date)
        # print(data_file)

        # x = self._data_points[:, 0:4]
        # y = self._data_points[:, 4]
        # x_train, x_validation, y_train, y_validation = train_test_split(x, y, test_size=0.20, random_state=1)
