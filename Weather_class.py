import config

from weatherbit.api import Api

#Определение APIkey
#set я так и не понял для чего, но в доке прописан
api_key = config.WeatherAPI
api = Api(api_key)
api.set_granularity('daily')

#в функции всё понятно по описанию строки
#форкаст берёт запрос, а гет забирает по инфу по выбраным параметрам
#info[1] выгружает сегодняшний день
def weather_info(city):

    forecast = api.get_forecast(city=city)
    info = forecast.get_series(['temp', 'precip', 'datetime'])
    otvet = f"""В городе {city} сегодня:\nТемпература: {info[0]['temp']}\u2103\nВероятность осадков: {(info[0]['precip']*100):2}%"""
    return otvet

if __name__ == "__main__":
    city = 'Челябинск'
    print(weather_info(city))
