import requests
import os
from twilio.rest import Client
account_sid = "Put the account id"
auth_token = os.environ.get("TOKEN")

api_key = os.environ.get("OWN_API_KEY")
LAT = 47.497913
LANG = 19.040236
parameters = {"lat":LAT,
              "lon":LANG,
              "appid": api_key,
              "exclude":"Current,minutely,daily"}
status = requests.get(url="https://api.openweathermap.org/data/2.5/onecall",params=parameters)
status.raise_for_status()
data = status.json()

# first_12hour_data =[data['hourly'][i]['weather'] for i in range(12)]
# Another method by using slicing
weather_slice = data['hourly'][:12]
will_rain = False
for i in weather_slice:
    cond = i['weather'][0]['id']
    if int(cond) < 750:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="It's going to rain please Bring umbrella",
                     from_='+15017122661',
                     to='+32431515345'
                 )
    print(message.status)



