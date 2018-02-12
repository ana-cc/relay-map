import requests
import socket
import json

req  = requests.get("https://anonscm.debian.org/viewvc/webwml/webwml/english/mirror/Mirrors.masterlist?view=co")
mirror_data = req.text.splitlines()
data =[]
dict_inter = {}

for item in mirror_data:
     if item == '':
         if bool(dict_inter) is True:
             data.append(dict_inter)
         dict_inter = {}
     else:
         try:
             pair = item.split(':')
             dict_inter[pair[0].strip()] = pair[1].strip()
         except:
             pass


for item in data:
    fqdn = item['Site']
    try:
        ipaddr = socket.gethostbyname(fqdn)
        print(ipaddr)
        item['ip'] = ipaddr
        geoloc = requests.get('http://freegeoip.net/json/' + ipaddr)
        item['lat'] = geoloc.json()['latitude']
        item ['long'] = geoloc.json()['longitude']
    except:
        print(fqdn)
       
with open ('mirrors.json', 'w') as mirr_file:
    mirr_file.write(json.dumps(data))
