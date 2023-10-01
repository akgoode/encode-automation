import os

class TVDB_Service:
    def __init__(self):
        print("creating tv db service")
        print(os.getenv('tvdb_api_key'))

    def search(self, title):
        return f"Searching for {title}"
