import requests
import json

# Configuration variables

api_key = None
api_base = 'https://api.bitfinex.com/v1/'


def get_ticker(symbol):
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

    r = requests.request("GET", url)
    status_code = r.status_code
    response = json.loads(r.text)

    return status_code, response


def get_stats(symbol):
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

    r = requests.request("GET", url)
    status_code = r.status_code
    response = json.loads(r.text)

    return status_code, response


s, r = get_stats('btcusd')
print(s, r)
