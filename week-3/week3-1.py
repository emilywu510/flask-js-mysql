import urllib.request as request
import json
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data=json.load(response)

clist=data["result"]["results"]
with open("data.csv","w",encoding="utf-8") as file:
    for attractions in clist:
        file.write(attractions["stitle"]+","+attractions["address"][5:8]+","+attractions["longitude"]+","+attractions["latitude"]+","+attractions["file"].split('https',2)[1]+"\n")


