import requests
import json

url = 'http://localhost:8080/'
fk = {"テスト":"強震モニタexの速報api"}
json_data = json.dumps(fk)

result = requests.post(url, json_data, headers={'Content-Type': 'application/json'})

print (result.text)