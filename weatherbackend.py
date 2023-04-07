from datetime import datetime
import requests
import json


def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()

def showWeather(city_value):

    api_key = "4451a139823665a3f8fb860cb1ac0ce1"

    city_name = city_value.get()

    weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid=' + api_key + "&units=imperial"

    response = requests.get(weather_url)


    weather_info = response.json()





    if weather_info['cod'] == 200:




        temp = int(weather_info['main']['temp'])
        feels_like_temp = int(weather_info['main']['feels_like'])
        pressure = weather_info['main']['pressure']
        humidity = weather_info['main']['humidity']
        wind_speed = weather_info['wind']['speed']
        sunrise = weather_info['sys']['sunrise']
        sunset = weather_info['sys']['sunset']
        timezone = weather_info['timezone']
        cloudy = weather_info['clouds']['all']
        description = weather_info['weather'][0]['description']

        sunrise_time = time_format_for_location(sunrise + timezone)
        sunset_time = time_format_for_location(sunset + timezone)



        weather = f"\nWeather of: {city_name}\nTemperature (Fahrenheit): {temp}°\nFeels like in (Fahrenheit): {feels_like_temp}°\nWind Speed: {wind_speed}mph\n"f"Pressure: {pressure} hPa\nHumidity: {humidity}%\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\nInfo:{description}"
        return weather

    else:
        error_message = f"\n\tWeather for '{city_name}' not found!\n\tEnter valid City Name"
        return error_message


