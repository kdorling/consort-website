sensor_index = "122099"
url = f"https://api.purpleair.com/v1/sensors/{sensor_index}?fields=pm2.5,pm2.5_10minute,pm2.5_30minute,pm2.5_60minute,pm2.5_6hour,pm2.5_24hour,pm2.5_1week"
headers = { "X-API-Key" : "407BF525-2B0E-11EE-A77F-42010A800009" }
import requests
import json

response = requests.get(url, headers=headers)

if (response.status_code != 200):
    response.raise_for_status() 

data = json.loads(response.text)
