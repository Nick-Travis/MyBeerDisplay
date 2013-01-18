#!/usr/bin/env python
import urllib2
import json
from pprint import pprint

url='http://nicktravis.com/beertemp/tap.php?format=json&tap=2'
req = urllib2.Request(url)
req.add_header('Accept', 'application/json')
req.add_header("Content-type", "application/x-www-form-urlencoded")
res = urllib2.urlopen(req)

data = json.loads(res.read())

name=data["posts"][0]["name"]
brewed=data["posts"][0]["Brewed"]
remains=data["posts"][0]["Remains"]
print(name)
print(brewed)
print(remains)

pprint(data)
