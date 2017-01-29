#Requires Python3
import json
import os
from json import dumps

gifs = os.listdir( "funnygifs" )
gifs.remove(".DS_Store")

giffile = open("gifs.json","w")

with open("gifs.json", "w") as outfile:
    json.dump({ 'funnygifs' : gifs }, outfile, indent=4)
