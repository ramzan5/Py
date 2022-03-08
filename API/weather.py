import requests
MY_LONG = 19.040236
MY_LAT = 47.497913
parameters = {
    'lat': MY_LAT,
    'lng': MY_LONG,
    'formatted': 0
}
status = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
status.raise_for_status()
data = status.json()
sun_rise = data['results']['sunrise'].split("T")
sun_set = data['results']['sunset'].split("T")
print(sun_rise, sun_set)
