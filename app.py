import streamlit as st
from get import get_weather_data

st.title("API Calling")

city_name = st.text_input("Enter city name", "nagpur")

if st.button("submit"):
    
    weather_data = get_weather_data(city_name)
    
    
    if weather_data:
        st.subheader("weather desc")
        st.write(weather_data["weather"][0]["description"])  
        st.write(weather_data["main"]["temp"])
    else:
        st.error("Could not fetch weather data.")
