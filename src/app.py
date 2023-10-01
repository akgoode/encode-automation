from tvdb import TVDB_Service
from handbrake import Handbrake_Service
from setup import setup

setup()

tvdb = TVDB_Service()
handbrake = Handbrake_Service()

print(tvdb.search("inglourious basterds"))
print(handbrake.convert("ig"))