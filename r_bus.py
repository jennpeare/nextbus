import requests
from pprint import pprint
import json

url = "http://runextbus.herokuapp.com/config"

data = requests.get(url).json()

with open("businfo.json", "w+") as f:
    json.dump(data, f)

with open("businfo.json", "r") as g:
    data = json.load(g)

#pprint(data)

stops_buses = {}

for stops in data.get("stops").values():
    stops_buses[stops.get("title")] = stops.get("routes")

keylist = stops_buses.keys()
keylist.sort()

for stop in keylist:
    print stop + ": [",
    for bus in stops_buses[stop]:
        print bus.upper(),
    print "]"
