import requests
import json

# Configuration variables

api_key = None
api_base = 'https://api.bitfinex.com/v1/'


class Market:
    def _get(self, url):
        """
        Make get http request, return status and response
        """

        r = requests.request("GET", url)
        status_code = r.status_code
        response = json.loads(r.text)

        return status_code, self._to_float(response)

    def _to_float(self, d):
        """
        Strings to Float from response
        """
        if type(d) is dict:
            for key, value in d.items():
                if type(value) is str:
                    d[key] = float(value)

        return d

    def get_ticker(self, symbol):
        """
        METHOD: Get
        PARAMS: symbol
        MODEL:
        {
        "mid":"244.755",
        "bid":"244.75",
        "ask":"244.76",
        "last_price":"244.82",
        "low":"244.2",
        "high":"248.19",
        "volume":"7842.11542563",
        "timestamp":"1444253422.348340958"
        }
        """

        url = api_base + "/pubticker/" + symbol
        return self._get(url)

    def get_stats(self, symbol):
        """
        METHOD: Get
        PARAMS: symbol
        MODEL:
        [{
            "period":1,
            "volume":"7967.96766158"
        },
        {
            "period":7,
            "volume":"55938.67260266"
        },
        {
            "period":30,
            "volume":"275148.09653645"
        }]
        """

        url = api_base + "/stats/" + symbol
        return self._get(url)

    def get_fundingbook(self, currency):
        """
        METHOD: Get
        PARAMS: currency
        MODEL:
        {
            "bids":[{
                "rate":"9.1287",
                "amount":"5000.0",
                "period":30,
                "timestamp":"1444257541.0",
                "frr":"No"
            }],
            "asks":[{
                "rate":"8.3695",
                "amount":"407.5",
                "period":2,
                "timestamp":"1444260343.0",
                "frr":"No"
            }]
         }
        """

        url = api_base + "/lendbook/" + currency
        return self._get(url)

    def get_orderbook(self, symbol):
        """
        METHOD: Get
        PARAMS: symbol
        MODEL:
        {
            "bids":[{
                "price":"574.61",
                "amount":"0.1439327",
                "timestamp":"1472506127.0"
            }],
            "asks":[{
                "price":"574.62",
                "amount":"19.1334",
                "timestamp":"1472506126.0"
            }]
        }
        """

        url = api_base + "/book/" + symbol
        return self._get(url)

    def get_trades(self, symbol):
        """
        METHOD: Get
        PARAMS: symbol
        MODEL:
        [{
            "timestamp":1444266681,
            "tid":11988919,
            "price":"244.8",
            "amount":"0.03297384",
            "exchange":"bitfinex",
            "type":"sell"
         }]
        """

        url = api_base + "/trades/" + symbol
        return self._get(url)

    def get_lends(self, currency):
        """
        METHOD: Get
        PARAMS: currency
        MODEL:
        [{
            "rate":"9.8998",
            "amount_lent":"22528933.77950878",
            "amount_used":"0.0",
            "timestamp":1444264307
        }]
        """

        url = api_base + "/lends/" + currency
        return self._get(url)

    def get_symbols(self):
        """
        METHOD: Get
        MODEL:
        [
            "btcusd",
            "ltcusd",
            "ltcbtc",
            ...
        ]
        """

        url = api_base + "/symbols"
        return self._get(url)

    def get_symbol_details(self):
        """
        METHOD: Get
        PARAMS:
        MODEL:
        [{
            "pair":"btcusd",
            "price_precision":5,
            "initial_margin":"30.0",
            "minimum_margin":"15.0",
            "maximum_order_size":"2000.0",
            "minimum_order_size":"0.01",
            "expiration":"NA"
        },
        ...
        ]
        """

        url = api_base + "/symbols_details"
        return self._get(url)


m = Market()

s, r = m.get_trades("btcusd")
print(s, r)
