#0925-2026 

import requests
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langgraph.checkpoint.sqlite import SqliteSaver
import uuid
import os
from django.conf import settings
# importing using full app path
from chatbot.documents import load_documents

# 0928-2026 removing 
# GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]



def get_weather(city: str):
    """ Get weather for a given city. """
    api_key = os.environ.get("WEATHER_API_KEY")
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q":city,
        "appid":api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    print(data)
    temperature_celsius = data['main']['temp']
    temperature_fahrenheit = temperature_celsius * 9/5 + 32
    return data, {'temperature_fahrenheit': temperature_fahrenheit, 'temperature_celsius': temperature_celsius}


def get_location(lat,lon):
    """ Get the city and country for a given latitude and longitude. """
    print("lat lon", lat, lon)

        # Reverse geocode to get city name using a free API
    try:
        response = requests.get(
            f'https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json',
            headers={'User-Agent': 'WeatherAssistant/1.0'},
            timeout=3
        )
        data = response.json()
        city = data['address'].get('city', data['address'].get('town', 'Unknown'))
        country = data['address'].get('country', '')
        return f"{city}, {country}"
    except:
        return "Rome, Italy"




llm = ChatGoogleGenerativeAI(
    model="gemini-flash-lite-latest",
    temperature=0.7,
)

data_files = load_documents()
print(data_files)
system_prompt = """
You are a helpful weather assistant. 
YOUR WORKFLOW:
1. If the user asks about weather WITHOUT specifying a location, you MUST:
   - First call get_location() to find their location
   - Then call get_weather(city) with that location

2. If the user provides a city, call get_weather(city) directly.
3. Only mention the temperature in Fahrenheit for US, Liberia, and Burma and only in Celsius for all other regions
4. You also answer questions about these documents: 
"""
system_prompt += data_files

# Simple approach - just use the filename directly
# this approach instead [with] keeps connection to DB open

db_path = os.path.join(settings.BASE_DIR, "checkpoints.db")
connection = SqliteSaver.from_conn_string(db_path)
checkpointer = connection.__enter__()

agent = create_agent(
    model=llm,
    tools=[get_weather, get_location],
    system_prompt=system_prompt,
    checkpointer=checkpointer
)



