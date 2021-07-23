import config
import pprint

from weatherbit.api import Api

api_key = config.WeatherAPI
api = Api(api_key)
api.set_granularity('daily')

city = 'Челябинск'


def weather_info(city):

    forecast = api.get_forecast(city=city, country="RU")
    info = forecast.get_series(['temp', 'precip', 'datetime'])
    otvet = f"""В городе {city} сегодня:\n Температура: {info[1]['temp']}С\n Вероятность осадков: {info[1]['precip']}"""
    return otvet
   # print(f'''{info['datetime']} в {city}\nвероятность осадков {info['precip']}\nтемпература {info['temp']}C''')


pprint.pprint(weather_info(city))
