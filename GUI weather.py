import streamlit as st
import requests

# Title
st.title("🌦️ Weather Detection App")
st.subheader("Get real-time weather info using WeatherAPI")

# Input city
city = st.text_input("Enter City Name", value="Chennai")

# Button
if st.button("Get Weather"):
    api_key = "1070554f505b4c499f0112903242608"
    base_url = "http://api.weatherapi.com/v1/current.json"

    params = {
        "key": api_key,
        "q": city,
        "aqi": "no"
    }

    try:
        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            data = response.json()
            st.success(f"✅ Weather in {city.title()}")
            st.write("🌡️ Temperature:", f"{data['current']['temp_c']} °C")
            st.write("💧 Humidity:", f"{data['current']['humidity']} %")
            st.write("🌬️ Pressure:", f"{data['current']['pressure_mb']} hPa")
            st.write("🌤️ Condition:", data['current']['condition']['text'])
        else:
            st.error("❌ Failed to fetch data. Check city name or API key.")
    except Exception as e:
        st.error(f"🚨 Error: {e}")
