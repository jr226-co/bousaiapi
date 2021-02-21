import requests


payload = {
'type': 'pga_alert', 
'time': '1589131441839', 
'max_pga': 0.637, 
'new': True, 
'estimated_intensity': 0, 
'region_list': ['愛媛']
}
requests.post("", data=payload)

