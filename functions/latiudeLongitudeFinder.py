import requests
import string

def latlongFinder(text):
    words = text.lower().split()

    if "at" in words:
        index = words.index("at")
    elif "in" in words:
        index = words.index("in")
    else:
        return None

    city = " ".join(words[index + 1:])
    city = city.replace("?", "").strip()

    url = "https://geocoding-api.open-meteo.com/v1/search"

    params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    }

    response = requests.get(url, params=params)
    data = response.json()

    if "results" not in data:
        print("City not found")
        return
    latitude = data["results"][0]["latitude"]
    longitude = data["results"][0]["longitude"]

    return latitude, longitude
