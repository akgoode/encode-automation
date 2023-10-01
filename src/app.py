from tvdb import TVDB_Service
from handbrake import Handbrake_Service
from setup import setup

setup()

tvdb = TVDB_Service()
handbrake = Handbrake_Service()

first_result = tvdb.search("inglourious basterds")["results"][0]
id = first_result["id"]
title = first_result["original_title"]
release = first_result["release_date"]
print(f"{id}___{title}___{release}")
