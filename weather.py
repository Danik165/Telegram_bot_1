# http://api.openweathermap.org/data/2.5/find?q=Petersburg&type=like&APPID=6d8e495ca73d5bbc1d6bf8ebd52c4
"http://api.openweathermap.org/data/2.5/find?q=Hyderabad,IN&type=like&APPID=371007bd03f590ec93612b4b95773888"

import requests

s_city = "Petersburg,RU"
city_id = 0
appid = "371007bd03f590ec93612b4b95773888"
try:
    res = requests.get("https://api.openweathermap.org/data/2.5/weather",
                       params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()
    print("conditions:", data['weather'][0]['description'])
    print("temp:", data['main']['temp'])
    print("temp_min:", data['main']['temp_min'])
    print("temp_max:", data['main']['temp_max'])
except Exception as e:
    print("Exception (weather):", e)
    pass
