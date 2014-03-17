import urllib2
import json
from pprint import pprint

url = "http://runextbus.heroku.com/config"

response = urllib2.urlopen(url).read()
data = json.loads(response)

with open("businfo.json", "w+") as f:
    json.dump(data, f)

with open("businfo.json", "r") as g:
    data = json.load(g)
#pprint(data)

stops_buses = {}

for stops in data.get("stops").values():
    stops_buses[stops.get("title")] = stops.get("routes")
g.close()

keylist = stops_buses.keys()
keylist.sort()

for stop in keylist:
    print stop + ": [",
    for bus in stops_buses[stop]:
        print bus.upper(),
    print "]"
