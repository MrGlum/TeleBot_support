
import config

from weatherbit.api import Api

# Определение APIkey
# set я так и не понял для чего, но в доке прописан
api_key = config.WeatherAPI
api = Api(api_key)
api.set_granularity('daily')

# в функции всё понятно по описанию строки
# форкаст берёт запрос, а гет забирает по инфу по выбраным параметрам
# info[1] выгружает сегодняшний день


def weather_info(city):

    if city[1]: city[1]=city[1]
    else: city[1] = 0
    forecast = api.get_forecast(city=city[0])
    info = forecast.get_series(['temp', 'precip', 'datetime'])
    norm_data = (str(info[int(city[1])]['datetime']).split()[0])
    norm_data = norm_data.split('-')
    otvet = f"""В городе {city[0]} {norm_data[2]}.{norm_data[1]}.{norm_data[0]}:\nТемпература: {info[int(city[1])]['temp']}\u2103\nВероятность осадков: {(info[int(city[1])]['precip']*100)}%"""
    return otvet


if __name__ == "__main__":
    city = ['Челябинск']
    day = 3
    print(weather_info(city))
