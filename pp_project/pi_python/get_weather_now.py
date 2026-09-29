import requests
import time
from datetime import datetime, timedelta
from .new_weather_codes import OPENWEATHER_CODES
import os


def get_weather(unit):
    # San Antonio, Texas
    MY_LAT = 29.602400
    MY_LONG = -98.393089

    api_key = os.environ.get("WEATHER_API_KEY")
    
    url_weather = "https://api.openweathermap.org/data/2.5/forecast"
    if unit == 'C':
        metric_or_imperial = 'metric'
    else:
        metric_or_imperial = 'imperial'
    
    parameters = {
        "lat": MY_LAT,
        "lon": MY_LONG,
        "appid": api_key,
        "cnt": 4,
        "units": metric_or_imperial
        # "units": "imperial"
    }

    response = requests.get(url=url_weather, params=parameters)
    response.raise_for_status()
    data = response.json()

    report = []
    current_time = datetime.now()

    for i in range(3):
        forecast = data["list"][i]
        weather_id = forecast["weather"][0]["id"]
        temp = round(forecast["main"]["temp"])
        
        # Get info from your dict with a safe fallback
        weather_info = OPENWEATHER_CODES.get(weather_id, {"icon": "❓", "description": "unknown"})
        icon = weather_info['icon']
        desc = weather_info['description']

        if i == 0:
            temperature_text = f"{current_time.strftime("%I:%M %p")}  {temp}(°{unit})"
        else:
            hours = i * 2
            new_time = current_time + timedelta(hours=hours)
            temperature_text = f"{new_time.strftime("%I:%M %p")} {temp}(°{unit}) "
        my_dict ={
            "temperature":temperature_text,
            "icon":icon,
            "description":desc
        }
        report.append(my_dict)

    # Print the final report
    for line in report:
        print(line)
    return report 