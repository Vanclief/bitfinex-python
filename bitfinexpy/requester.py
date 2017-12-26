import requests
import json

api_base = 'https://api.bitfinex.com/v1/'


class Requester(object):
    def _construct_url(self, endpoint):
        """
        Construct the url
        """

        return api_base + endpoint

    def get(self, endpoint):
        """
        Make get http request, return status and response
        """

        url = self._construct_url(endpoint)

        r = requests.request("GET", url)
        status_code = r.status_code
        response = json.loads(r.text)

        return status_code, response
