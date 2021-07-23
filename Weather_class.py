import config
import pprint

from weatherbit.api import Api

api_key = config.WeatherAPI
api = Api(api_key)
api.set_granularity('daily')

city = 'Челябинск'

def weather_info(city):
   
    forecast = api.get_forecast(city=f"{city}", country="RU")
    print(forecast.get_series(['temp', 'precip']))

weather_info(city)