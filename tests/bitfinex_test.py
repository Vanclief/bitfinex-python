from bitfinexpy.bitfinex import Bitfinex
# import mock
# import requests
import httpretty

client = Bitfinex()

TICKER_URL = 'https://api.bitfinex.com/v1/pubticker/'
STATS_URL = 'https://api.bitfinex.com/v1/stats/'
FUNDING_URL = 'https://api.bitfinex.com/v1/lendbook/'
ORDERS_URL = 'https://api.bitfinex.com/v1/book'
TRADES_URL = 'https://api.bitfinex.com/v1/trades/'
LENDS_URL = 'https://api.bitfinex.com/v1/lends/'
SYMBOLS_URL = 'https://api.bitfinex.com/v1/symbols'
SYMBOL_DETAILS = 'https://api.bitfinex.com/v1/symbols_details'

# TODO add initialization tests


def test_should_return_ticker():

    mock_symbol = 'btcusd'
    mock_body = (
            '{"mid":"562.56495","bid":"562.15","ask":"562.9799",' +
            '"last_price":"562.25","timestamp":"1395552658.339936691"}')
    mock_url = TICKER_URL + mock_symbol
    mock_status = 200

    httpretty.register_uri(
            httpretty.GET, mock_url, body=mock_body, status=mock_status
            )

    expected_response = (mock_status, mock_body)
    response = client.ticker(mock_symbol)

    assert expected_response == response


def test_should_return_stats():

    mock_body = (
            '[{"period":1,"volume":"7410.27250155"},' +
            '{"period":7,"volume":"52251.37118006"},' +
            '{"period":30,"volume":"464505.07753251"}]')
    mock_url = 'https://api.bitfinex.com/v1/stats/btcusd'
    mock_status = 200

    httpretty.register_uri(
            httpretty.GET, mock_url, body=mock_body, status=mock_status
            )

    expected_response = (mock_status, mock_body)
    response = client.stats('btcusd')

    assert expected_response == response


def should_return_fundingbook():
    mock_body = (
            '{ "bids":[{"rate":"9.1287", "amount":"5000.0", "period":30,' +
            '"timestamp":"1444257541.0", "frr":"No" }],' +
            '"asks":[{"rate":"8.3695", "amount":"407.5", "period":2, ' +
            '"timestamp":"1444260343.0", "frr":"No" }]}')

    mock_url = 'https://api.bitfinex.com/v1/lendbook/'
    mock_status = 200

    httpretty.register_uri(
            httpretty.GET, mock_url, body=mock_body, status=mock_status
            )

    expected_response = (mock_status, mock_body)
    response = b.symbols()

    assert expected_response == response
def test_should_have_symbols():

    mock_body = '["btcusd", "ltcusd", "ltcbtc"]'
    mock_url = 'https://api.bitfinex.com/v1/symbols'
    mock_status = 200

    httpretty.register_uri(
            httpretty.GET, mock_url, body=mock_body, status=mock_status
            )

    expected_response = (mock_status, mock_body)
    response = b.symbols()

    assert expected_response == response
def test_should_have_symbols():

    mock_body = '["btcusd", "ltcusd", "ltcbtc"]'
    mock_url = 'https://api.bitfinex.com/v1/symbols'
    mock_status = 200

    httpretty.register_uri(
            httpretty.GET, mock_url, body=mock_body, status=mock_status
            )

    expected_response = (mock_status, mock_body)
    response = b.symbols()

    assert expected_response == response
def test_should_have_symbols():

    mock_body = '["btcusd", "ltcusd", "ltcbtc"]'
    mock_url = 'https://api.bitfinex.com/v1/symbols'
    mock_status = 200

    httpretty.register_uri(
            httpretty.GET, mock_url, body=mock_body, status=mock_status
            )

    expected_response = (mock_status, mock_body)
    response = b.symbols()

    assert expected_response == response
def test_should_have_symbols():

    mock_body = '["btcusd", "ltcusd", "ltcbtc"]'
    mock_url = 'https://api.bitfinex.com/v1/symbols'
    mock_status = 200

    httpretty.register_uri(
            httpretty.GET, mock_url, body=mock_body, status=mock_status
            )

    expected_response = (mock_status, mock_body)
    response = b.symbols()

    assert expected_response == response

@httpretty.activate
def test_should_have_symbols():

    mock_body = '["btcusd", "ltcusd", "ltcbtc"]'
    mock_url = 'https://api.bitfinex.com/v1/symbols'
    mock_status = 200

    httpretty.register_uri(
            httpretty.GET, mock_url, body=mock_body, status=mock_status
            )

    expected_response = (mock_status, mock_body)
    response = b.symbols()

    assert expected_response == response