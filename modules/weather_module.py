import requests
import datetime


def get_weather(city):
    weather = requests.get('http://api.openweathermap.org/data/2.5/weather', params={
        'lang':'ru',
        'units': 'metric',
        'APPID': 'ef23e5397af13d705cfb244b33d04561',
        'q': city
    }).json()
    if weather["cod"] == "404" or weather["cod"] == 404:
        raise Exception(f"404: Город {city} не найден.")
    elif weather["cod"] != "200" and weather["cod"] != 200:
        raise Exception(f"200: {weather['message']}")
    temp = weather["main"]["temp"]
    utc = weather["timezone"]
    country = weather['sys']['country']
    weather_desc = weather["weather"][0]["description"]
    wind_speed = weather["wind"]["speed"]
    clouds = weather["clouds"]["all"]
    humidity = weather["main"]["humidity"]
    time_update = datetime.datetime.fromtimestamp(weather["dt"]).strftime('%H:%M')
    return city, country, temp, utc, weather_desc, wind_speed, clouds, humidity, time_update


def weather(event):
    if len(event.splited) < 3:
        event.message_send("Ошибка! В команде нужно указывать город.")
    city = event.args
    try:
        city, country, temp, utc, weather_desc, wind_speed, clouds, humidity, time_update = get_weather(city)
    except Exception as error:
                event.message_send(error)
    current_weather = f"""Погода в {country}/{city}:
    •Температура: {temp}°C
    •Состояние: {weather_desc}
    •Скорость ветра: {wind_speed} м/с
    •Облачность: {clouds}%
    •Влажность: {humidity}%
    •Время обновления: {time_update} UTC{f'+{utc / 3600}' if utc >= 0 else utc / 3600}"""
    event.message_send(f"{current_weather}")
    
HandleCmd('погода', 0, weather)
