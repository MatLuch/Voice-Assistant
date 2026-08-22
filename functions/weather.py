import requests
from functions.latiudeLongitudeFinder import latlongFinder
def tempature(text):
    try:
        lat, lon = latlongFinder(text)
        url = "https://api.open-meteo.com/v1/forecast"

        params = {
            "latitude": lat,
            "longitude": lon,
            "current": "temperature_2m,apparent_temperature"
        }

        response = requests.get(url, params=params)

        data = response.json()

        temp = data["current"]["temperature_2m"]
        feels = data["current"]["apparent_temperature"]
        return f"The temperature is: {temp}"
    except Exception:
        return None
    
def rain(text):
    try: 
        lat, lon = latlongFinder(text)
        url = "https://api.open-meteo.com/v1/forecast"

        params = {
            "latitude": lat,
            "longitude": lon, 
            "daily": "precipitation_probability_max,rain_sum",
            "timezone": "auto"
        }

        response = requests.get(url, params=params)

        data = response.json()

        rainChance = data["daily"]["precipitation_probability_max"][0]
        rainAmm = data["daily"]["rain_sum"][0]
        return f"The chance of rain today is {rainChance}% and expected rain is {rainAmm} mm"
    except Exception:
        return None 