import requests
import config

s_city = "Petersburg,RU"
city_id = 0
appid = config.OpenWetherAPI

try:
    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                 params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()
    print("conditions:", data['weather'][0]['description'])
    print("temp:", data['main']['temp'])
    print("temp_min:", data['main']['temp_min'])
    print("temp_max:", data['main']['temp_max'])
except Exception as e:
    print("Exception (weather):", e)
    pass