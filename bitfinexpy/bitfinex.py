from bitfinexpy.markets import Market


class Bitfinex(object):

    def __init__(self, key=None, secret=None):
        self.api_key = key
        self.api_secret = secret
        self.api_base = 'https://api.bitfinex.com/v1/'
        self.market = Market(self.api_base)

    def ticker(self, symbol):
        return self.market.get_ticker(symbol)

    def stats(self, symbol):
        return self.market.get_stats(symbol)

    def fundingbook(self, currency):
        return self.market.get_fundingbook(currency)

    def orderbook(self, symbol):
        return self.market.get_orderbook(symbol)

    def trades(self, symbol):
        return self.market.get_trades(symbol)

    def lends(self, currency):
        return self.market.get_lends(currency)

    def symbols(self):
        return self.market.get_symbols()

    def symbol_details(self):
        return self.market.get_symbol_details()
