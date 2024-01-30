import requests
import streamlit as st
def get_weather(latitude,longitude):
    """
    
    """
    weather_api_key = st.secrets["OPEN_WEATHER_API_KEY"]
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={weather_api_key}")
    return response

