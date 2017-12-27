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


@httpretty.activate
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


@httpretty.activate
def test_should_return_stats():

    mock_symbol = 'btcusd'
    mock_body = (
            '[{"period":1,"volume":"7410.27250155"},' +
            '{"period":7,"volume":"52251.37118006"},' +
            '{"period":30,"volume":"464505.07753251"}]')
    mock_url = STATS_URL + mock_symbol
    mock_status = 200

    httpretty.register_uri(
            httpretty.GET, mock_url, body=mock_body, status=mock_status
            )

    expected_response = (mock_status, mock_body)
    response = client.stats(mock_status)

    assert expected_response == response


@httpretty.activate
def should_return_fundingbook():

    mock_currency = 'usd'
    mock_body = (
            '{ "bids":[{"rate":"9.1287", "amount":"5000.0", "period":30,' +
            '"timestamp":"1444257541.0", "frr":"No" }],' +
            '"asks":[{"rate":"8.3695", "amount":"407.5", "period":2, ' +
            '"timestamp":"1444260343.0", "frr":"No" }]}')

    mock_url = FUNDING_URL + mock_currency
    mock_status = 200

    httpretty.register_uri(
            httpretty.GET, mock_url, body=mock_body, status=mock_status
            )

    expected_response = (mock_status, mock_body)
    response = client.fundingbook(mock_currency)

    assert expected_response == response


@httpretty.activate
def test_should_return_orderbook():

    mock_symbol = 'btcusd'
    mock_body = (
            '{"bids":[{"price":"562.2601", "amount":"0.985", ' +
            '"timestamp":"1395567556.0"}],"asks":[{"price":"563.001", ' +
            '"amount":"0.3","timestamp":"1395532200.0"}]}')
    mock_url = ORDERS_URL + mock_symbol
    mock_status = 200

    httpretty.register_uri(
            httpretty.GET, mock_url, body=mock_body, status=mock_status
            )

    expected_response = (mock_status, mock_body)
    response = client.orderbook(mock_symbol)

    assert expected_response == response


@httpretty.activate
def test_should_return_trades():

    mock_symbol = 'btcusd'
    mock_body = (
            '[{ "timestamp":1444266681, "tid":11988919, "price":"244.8", ' +
            '"amount":"0.03297384", "exchange":"bitfinex", "type":"sell"}]')
    mock_url = TRADES_URL + mock_symbol
    mock_status = 200

    httpretty.register_uri(
            httpretty.GET, mock_url, body=mock_body, status=mock_status
            )

    expected_response = (mock_status, mock_body)
    response = client.trades(mock_symbol)

    assert expected_response == response


@httpretty.activate
def test_should_return_lends():

    mock_currency = 'usd'
    mock_body = (
            '[{ "rate":"9.8998", "amount_lent":"22528933.77950878",' +
            '"amount_used":"0.0", "timestamp":1444264307},' +
            '{ "rate":"9.8998", "amount_lent":"22528933.77950878",' +
            '"amount_used":"0.0", "timestamp":1444264307}] ')
    mock_url = LENDS_URL + mock_currency
    mock_status = 200

    httpretty.register_uri(
            httpretty.GET, mock_url, body=mock_body, status=mock_status
            )

    expected_response = (mock_status, mock_body)
    response = client.lends(mock_currency)

    assert expected_response == response


@httpretty.activate
def test_should_return_symbols():

    mock_body = '["btcusd", "ltcusd", "ltcbtc"]'
    mock_url = SYMBOLS_URL
    mock_status = 200

    httpretty.register_uri(
            httpretty.GET, mock_url, body=mock_body, status=mock_status
            )

    expected_response = (mock_status, mock_body)
    response = client.symbols()

    assert expected_response == response


@httpretty.activate
def test_should_return_symbol_details():

    mock_body = (
            '[{ "pair":"btcusd", "price_precision":5,' +
            '"initial_margin":"30.0", "minimum_margin":"15.0",' +
            '"maximum_order_size":"2000.0", "minimum_order_size":"0.01",' +
            '"expiration":"NA" },{ "pair":"ltcusd", "price_precision":5,' +
            '"initial_margin":"30.0", "minimum_margin":"15.0",' +
            '"maximum_order_size":"5000.0", "minimum_order_size":"0.1", ' +
            '"expiration":"NA" },{ "pair":"ltcbtc", "price_precision":5,' +
            '"initial_margin":"30.0", "minimum_margin":"15.0",' +
            '"maximum_order_size":"5000.0", "minimum_order_size":"0.1",' +
            '"expiration":"NA"}]')
    mock_url = SYMBOL_DETAILS
    mock_status = 200

    httpretty.register_uri(
            httpretty.GET, mock_url, body=mock_body, status=mock_status
            )

    expected_response = (mock_status, mock_body)
    response = client.symbol_details()

    assert expected_response == response
