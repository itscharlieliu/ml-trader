from iex.cloud import cloud


class Trader:
    def __init__(self, api_key: str, sandbox: bool = True):
        self._data_points = []
        self._cloud = cloud(api_key, sandbox)

    def get_sentiment(self):
        return self._data_points

    def test(self):
        return self._cloud.get_current_price("aapl")
