import os
import requests

class TVDB_Service:
    def __init__(self):
        print("creating tv db service")
        self.api_key = os.getenv('tvdb_api_key')
        self.search_url = "https://api.themoviedb.org/3/search/movie"
        self.headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        self.base_params = {
            "include_adult": False,
            "language": "en-US",
            "page": 1
        }

    def merge_params(self, params):
        return self.base_params | params

    def make_request(self, params):
        return requests.get(self.search_url, headers=self.headers, params=self.merge_params(params))

    def search(self, query):
        print(f"Searching for {query}")
        params = {
            "query": query
        }
        response = self.make_request(params)
        return response.json()
