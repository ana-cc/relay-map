import requests
import socket
import json

req  = requests.get("https://www.debian.org/devel/developers.coords")
dev_data = req.text.splitlines()
data =[]
tup = []
for item in dev_data:
    if bool(tup)!= False:
        data.append(tuple(tup));
    tup =[]
    for t in  item.split():
        try:
            tup.append(float(t))
        except ValueError:
            pass
      
with open ('developers.json', 'w') as dev_file:
    dev_file.write(json.dumps(data))
