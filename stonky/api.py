import gevent.monkey
gevent.monkey.patch_all()
import json
from urllib.parse import urlencode
from urllib.request import urlopen

from stonky.forex import Forex
from stonky.stock import Stock
import sys


class Api:
    def get_quote(self, ticket: tuple) -> Stock:
        url = f"https://query1.finance.yahoo.com/v11/finance/quoteSummary/{ticket[0]}"
        params = {"modules": "summaryDetail,price"}
        try:
            response = self._query(url, params)
        except Exception as e:
            print("Error while calling api.py get_quote()!")
            print(e, type(e))
            sys.exit(1)

        #summary_data = response["quoteSummary"]["result"][0]["summaryDetail"]
        price_data = response["quoteSummary"]["result"][0]["price"]
        #print(ticket[0])
        #print(price_data)
        return Stock(
            ticket=ticket[0],
            name=ticket[1],
            currency_code=price_data["currency"],
            #amount_bid=summary_data["bid"].get("raw", 0.0),
            #amount_ask=summary_data["ask"].get("raw", 0.0),
            amount_now=price_data["regularMarketPrice"].get("raw", 0.0),
            #amount_low=summary_data["dayLow"].get("raw", 0.0),
            #amount_high=summary_data["dayHigh"].get("raw", 0.0),
            #amount_prev_close=summary_data["previousClose"].get("raw", 0.0),
            amount_prev_close=price_data["regularMarketPreviousClose"].get("raw", 0.0),
            delta_amount=price_data["regularMarketChange"].get("raw", 0.0),
            delta_percent=price_data["regularMarketChangePercent"].get(
                "raw", 0.0
            ),
            volume=price_data["regularMarketVolume"]["raw"],
        )

    def get_forex_rates(self, base: str) -> Forex:
        url = "https://api.exchangeratesapi.io/latest"
        params = {"base": base}
        response = self._query(url, params)
        return Forex(**response["rates"])

    @staticmethod
    def _query(url: str, params: dict) -> dict:
        if params:
            url += "?" + urlencode(params)
        response = urlopen(url)
        return json.loads(response.read())
