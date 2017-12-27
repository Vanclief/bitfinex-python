from requester import Requester
import helpers

TICKER_URL = "/pubticker/"
STATS_URL = "/stats/"
FUNDING_URL = "/lendbook/"
ORDERS_URL = "/book/"
TRADES_URL = "/trades/"
LENDS_URL = "/lends/"
SYMBOLS_URL = "/symbols"
SYMBOL_DETAILS = "/symbols_details"


class Market(object):

    def __init__(self, api_base):
        self.r = Requester(api_base)

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

        endpoint = TICKER_URL + symbol
        status, response = self.r.get(endpoint)

        if status != 200:
            return status, response

        return status, helpers.dict_to_float(response)

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

        endpoint = STATS_URL + symbol
        status, response = self.r.get(endpoint)

        if status != 200:
            return status, response

        return status, helpers.list_dict_to_float(response)

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

        endpoint = FUNDING_URL + currency
        status, response = self.r.get(endpoint)

        for fund_type in response.keys():
            for fund in response[fund_type]:
                for key, value in fund.items():
                    if key in ['rate', 'period', 'amount', 'timestamp']:
                        fund[key] = float(value)

        if status != 200:
            return status, response

        return status, response

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

        endpoint = ORDERS_URL + symbol
        status, response = self.r.get(endpoint)

        if status != 200:
            return status, response

        for order_type in response.keys():
            for order in response[order_type]:
                for key, value in order.items():
                    order[key] = float(value)

        return status, response

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

        endpoint = TRADES_URL + symbol
        status, response = self.r.get(endpoint)

        if status != 200:
            return status, response

        return status, helpers.list_dict_to_float(response)

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

        endpoint = LENDS_URL + currency
        status, response = self.r.get(endpoint)

        if status != 200:
            return status, response

        return status, helpers.list_dict_to_float(response)

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

        endpoint = SYMBOLS_URL
        return self.r.get(endpoint)

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

        endpoint = SYMBOL_DETAILS
        status, response = self.r.get(endpoint)

        if status != 200:
            return status, response

        return status, helpers.list_dict_to_float(response)
