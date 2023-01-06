import requests

class Fetch:
    # pass the proxies to be used
    def __init__(self, proxies={}):
        self.proxies = proxies
        self.response = "no response"

    # return json response
    def json(self):
        if type(self.response) != str:
            return str(self.response.json())
        else:
            return self.response
    
    # return text response
    def text(self):
        if type(self.response) != str:
            return str(self.response.text)
        else:
            return self.response

    # make a get request to the following "url" with the proxies
    def get(self, url):
        self.response = requests.get(url, proxies=self.proxies)
        return self.text()

    # make a post request to the following "url", "headers", "body" along with the proxies
    def post(self, url, headers={}, body={}):
        self.response = requests.post(url, proxies=self.proxies, headers=headers, data=body)
        return self.text()


