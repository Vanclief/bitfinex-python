
# Configuration variables


class Bitfinex(object):

    def __init__(self, key=None, secret=None):
        self.api_key = key
        self.api_secret = secret
        self.api_base = 'https://api.bitfinex.com/v1/'

