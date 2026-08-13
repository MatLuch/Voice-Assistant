import requests
from functions.latiudeLongitudeFinder import latlongFinder
def weathe(text):
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