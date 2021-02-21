import colorama
from termcolor import colored
colorama.init()

import requests
# import weburl

import json
import urllib.request
from datetime import datetime, timezone
import time

def web(ga,gai):
    webhook_url = "https://canary.discord.com/api/webhooks/810069286978715658/rzrLsOWPd-MehatQbFTr7YIaC0bUObRJwpzchyLeA812oq46imqi_I8ECnvV3EfgpVUf"    
    main_content = {

    "username": "強震モニタex速報",
    "embeds": [{
        "title": ga,
        "description": f"```{gai}``` " ,
        "color": 15258703

        }
    ]
}

    
    
    requests.post(webhook_url,json.dumps(main_content),headers={'Content-Type': 'application/json'})



url = 'http://localhost:8000/'
res = urllib.request.urlopen(url)
# json_loads() でPythonオブジェクトに変換S
data = json.loads(res.read(),encoding="utf-8")
ts = data['time']
now_from_ts = datetime.fromtimestamp(int(ts[0:10]))

h = now_from_ts.hour
m =  now_from_ts.minute
s= now_from_ts.second

list = []

if data['type'] == 'None':
    print(data)
    pass
else:
    if now_from_ts.hour <= 9:
        h = f"0{now_from_ts.hour}"
    if now_from_ts.minute <= 9:
        m = f"0{now_from_ts.minute}"
    if now_from_ts.second <= 9:
        s = f"0{now_from_ts.second}"

    if data['type'] == "intensity_report":
        print(f"強震モニタ速報 {h}:{m}:{s}")
        for si in data['intensity_list']:
            maped_list = map(str,si['region_list']) 
            nak = ' '.join(maped_list)
            print(f"震度{si['intensity']}:{nak}")
            list.append(f"震度{si['intensity']}:{nak}\n")
        maped_list = map(str,list) 
        nak = ' '.join(maped_list)
        web(f"強震モニタ速報 {h}:{m}:{s}",nak)
            
