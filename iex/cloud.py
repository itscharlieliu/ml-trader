import requests

IEX_ENDPOINT = "https://{prefix}.iexapis.com/stable/stock/"

class cloud:
    def __init__(self, api_key: str, sandbox: bool = True):
        self.api_key = api_key
        self.sandbox = sandbox

    def get_endpoint(self):
        return IEX_ENDPOINT.format(prefix="sandbox" if self.sandbox else "cloud")

    def get_current_price(self, ticker_symbol: str):
        url = self.get_endpoint() + "{ticker}/quote/latestPrice?token={token}".format(ticker=ticker_symbol, token=self.api_key)
        return requests.get(url).content.decode("utf-8")
