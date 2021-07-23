import config
import pprint

from weatherbit.api import Api

api_key = config.WeatherAPI
api = Api(api_key)
api.set_granularity('daily')

city = 'Челябинск'

def weather_info(city):
   
    forecast = api.get_forecast(city=f"{city}", country="RU")
    info = forecast.get_series(['temp', 'precip', 'datetime'])
    pprint.pprint(info[1])
   # print(f'''{info['datetime']} в {city}\nвероятность осадков {info['precip']}\nтемпература {info['temp']}C''') 

pprint.pprint(weather_info(city))